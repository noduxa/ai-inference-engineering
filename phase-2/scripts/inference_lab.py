#!/usr/bin/env python3
"""Bounded local inference measurements; never a production serving benchmark.

Use --toy for random-weight CPU smoke tests without downloads. See README.md.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import importlib.metadata
import json
import math
from pathlib import Path
import platform
import statistics
import time


def kv_bytes(layers, batch, length, kv_heads, head_dim, element_bytes):
    values = (layers, batch, length, kv_heads, head_dim, element_bytes)
    if any(type(v) is not int or v <= 0 for v in values):
        raise ValueError('Cache dimensions and element bytes must be positive integers')
    return 2 * math.prod(values)


def token_metrics(start, stamps, end):
    if not stamps or any(not math.isfinite(v) for v in [start, *stamps, end]):
        raise ValueError('Require finite timestamps and at least one output token')
    if any(b < a for a, b in zip([start, *stamps], [*stamps, end])):
        raise ValueError('Timestamps must be monotonic')
    return {'ttft_s': stamps[0] - start, 'e2e_s': end - start,
            'tpot_s': (stamps[-1] - stamps[0]) / (len(stamps)-1) if len(stamps)>1 else None,
            'itl_s': [b-a for a,b in zip(stamps, stamps[1:])]}


def summarize(samples):
    if not samples or any(not math.isfinite(x) or x < 0 for x in samples):
        raise ValueError('Require nonnegative finite samples')
    ordered = sorted(samples)
    return {'n':len(samples), 'mean':statistics.mean(samples),
            'median':statistics.median(samples),
            'p95_nearest_rank':ordered[math.ceil(.95*len(samples))-1] if len(samples)>=20 else None,
            'tail_note':'P95 omitted below 20 samples; even 20 is exploratory, not a reliable tail SLO.'}


def budget_study(limit=16*1024*1024):
    """Pure arithmetic simulation: allocates no trial tensors."""
    rows=[]
    for side in (64,128,256,512,1024,2048,4096):
        requested=side*side*4
        accepted=requested<=limit
        rows.append({'shape':[side,side], 'dtype':'float32', 'requested_bytes':requested,
                     'budget_bytes':limit,'accepted':accepted})
        if not accepted:break
    return {'kind':'simulation', 'physical_oom':False, 'rows':rows,
            'explanation':'Software budget refusal; not physical allocation or accelerator evidence.'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--toy',action='store_true',help='Random tiny GPT-2; no tokenizer/download/quality claim')
    parser.add_argument('--budget-only',action='store_true',help='Arithmetic resource simulation; no torch needed')
    parser.add_argument('--model',default='HuggingFaceTB/SmolLM2-135M',choices=['HuggingFaceTB/SmolLM2-135M'])
    parser.add_argument('--revision',help='Immutable 40-character model commit; resolves public main once if omitted')
    parser.add_argument('--device',choices=['cpu','cuda','mps'],default='cpu')
    parser.add_argument('--dtype',choices=['float32','float16','bfloat16','float64'],default='float32')
    parser.add_argument('--prompt',default='A small computer can')
    parser.add_argument('--prompt-tokens',type=int,default=16,help='Controlled exact token length using repeated public prompt IDs')
    parser.add_argument('--output-tokens',type=int,default=8)
    parser.add_argument('--batch',type=int,default=1)
    parser.add_argument('--concurrency',type=int,default=1,help='CPU worker-pool requests; not continuous batching')
    parser.add_argument('--runs',type=int,default=3)
    parser.add_argument('--warmup',type=int,default=1)
    parser.add_argument('--threads',type=int,default=1)
    parser.add_argument('--fixed-output',action='store_true',help='Ignore EOS for controlled synthetic-length studies')
    parser.add_argument('--no-cache',action='store_true')
    parser.add_argument('--profile',action='store_true',help='Separate profile run after measured runs')
    parser.add_argument('--out',type=Path,required=True,help='New JSON result path; existing files are not overwritten')
    a=parser.parse_args(argv)
    if a.out.exists():parser.error('Result file already exists; select a new run path')
    for name,low,high in [('prompt_tokens',1,256),('output_tokens',1,32),('batch',1,4),('concurrency',1,4),('runs',1,100),('warmup',0,5),('threads',1,4)]:
        if not low<=getattr(a,name)<=high:parser.error(f'{name} must be in [{low}, {high}]')
    if a.concurrency>1 and a.device!='cpu':parser.error('Concurrent lab requests are CPU-only to bound accelerator pressure')
    if a.profile and a.concurrency>1:parser.error('Profile one CPU request at a time')
    a.out.parent.mkdir(parents=True,exist_ok=True)
    if a.budget_only:
        a.out.write_text(json.dumps(budget_study(),indent=2)+'\n');return 0
    if a.revision and (len(a.revision)!=40 or any(c not in '0123456789abcdef' for c in a.revision)):
        parser.error('revision must be a full lowercase commit SHA')
    import torch
    from transformers import AutoModelForCausalLM,AutoTokenizer,GPT2Config,GPT2LMHeadModel
    from huggingface_hub import HfApi
    torch.set_num_threads(a.threads)
    torch.manual_seed(7)
    if a.device=='cuda' and not torch.cuda.is_available():parser.error('CUDA unavailable; use CPU fallback')
    if a.device=='mps' and not torch.backends.mps.is_available():parser.error('MPS unavailable; use CPU fallback')
    dtype=getattr(torch,a.dtype)
    def sync():
        if a.device=='cuda':torch.cuda.synchronize()
        elif a.device=='mps':torch.mps.synchronize()
    def memory():
        if a.device=='cuda':return {'allocated_bytes':torch.cuda.memory_allocated(),'reserved_bytes':torch.cuda.memory_reserved(),'peak_allocated_bytes':torch.cuda.max_memory_allocated()}
        if a.device=='mps':return {'mps_tensor_bytes':torch.mps.current_allocated_memory(),'mps_driver_bytes':torch.mps.driver_allocated_memory()}
        return {'allocator_bytes':None,'note':'CPU tensor payload is not process RSS; record RSS separately.'}
    loading=time.perf_counter()
    tokenizer=None
    if a.toy:
        model=GPT2LMHeadModel(GPT2Config(n_layer=2,n_head=2,n_embd=32,n_positions=512,vocab_size=64,bos_token_id=0,eos_token_id=0))
        revision='seed-7-random-initialization'
    else:
        revision=a.revision or HfApi(token=False).model_info(a.model,token=False).sha
        tokenizer=AutoTokenizer.from_pretrained(a.model,revision=revision,token=False,trust_remote_code=False)
        model=AutoModelForCausalLM.from_pretrained(a.model,revision=revision,token=False,
            trust_remote_code=False,use_safetensors=True,dtype=dtype)
    model=model.to(device=a.device,dtype=dtype).eval();sync()
    load_s=time.perf_counter()-loading
    config=model.config
    layers=getattr(config,'num_hidden_layers',None) or config.n_layer
    heads=getattr(config,'num_attention_heads',None) or config.n_head
    hidden=getattr(config,'hidden_size',None) or config.n_embd
    kv_heads=getattr(config,'num_key_value_heads',heads)
    dim=getattr(config,'head_dim',None) or hidden//heads
    parameter_bytes=sum(p.numel()*p.element_size() for p in model.parameters())
    before=memory()
    def request(index, submitted=None):
        sync();start=time.perf_counter()
        ids=tokenizer.encode(a.prompt,add_special_tokens=False) if tokenizer else list(range(1,17))
        if not ids:raise ValueError('Prompt tokenizes to an empty sequence')
        ids=(ids*math.ceil(a.prompt_tokens/len(ids)))[:a.prompt_tokens]
        inputs=torch.tensor([ids]*a.batch,dtype=torch.long,device=a.device)
        mask=torch.ones_like(inputs);sync();prepared=time.perf_counter()
        generated=inputs;cache=None;stamps=[];forwards=[];selected=[];snapshots=[];cache_memory=[]
        with torch.inference_mode():
            for step in range(a.output_tokens):
                current=generated if cache is None else generated[:,-1:]
                sync();f0=time.perf_counter()
                result=model(input_ids=current,attention_mask=mask,past_key_values=cache,use_cache=not a.no_cache)
                sync();f1=time.perf_counter();forwards.append(f1-f0)
                cache=result.past_key_values if not a.no_cache else None
                if not torch.isfinite(result.logits[:, -1, :]).all():
                    raise ValueError('Non-finite next-token logits; do not publish timings as successful')
                token=result.logits[:,-1,:].argmax(-1,keepdim=True)
                generated=torch.cat([generated,token],dim=-1)
                # Host materialization establishes token availability, before text decoding.
                chosen=token.squeeze(-1).tolist();stamps.append(time.perf_counter());selected.append(chosen)
                snapshots.append(tokenizer.decode(generated[0,a.prompt_tokens:].tolist()) if tokenizer else '')
                cache_memory.append(memory())
                mask=torch.cat([mask,torch.ones((a.batch,1),device=a.device,dtype=mask.dtype)],dim=-1)
                eos=getattr(config,'eos_token_id',None);eos_ids=eos if isinstance(eos,list) else [eos]
                if not a.fixed_output and all(t in eos_ids for t in chosen):break
        sync();end=time.perf_counter()
        n=len(stamps)
        return {'request':index,'queue_s':start-submitted if submitted is not None else 0.0,
                'submitted_e2e_s':end-submitted if submitted is not None else end-start,
                'prompt_tokens_per_sequence':len(ids),'completion_tokens_per_sequence':n,
                'batch':a.batch,'selected_ids':selected,'prompt_ids':ids,'input_shape':[a.batch,len(ids)],
                'attention_mask_shape':[a.batch,len(ids)],'logits_shape_last':list(result.logits.shape),
                'text_snapshots_first_sequence':snapshots,'preparation_s':prepared-start,
                'forward_s':forwards,'token_offsets_s':[t-start for t in stamps],
                'memory_per_step':cache_memory,'metrics':token_metrics(start,stamps,end),
                'stop_reason':'requested_length' if n==a.output_tokens else 'all_sequences_eos',
                'estimated_cache_bytes':kv_bytes(layers,a.batch,len(ids)+n-1,kv_heads,dim,torch.empty((),dtype=dtype).element_size()) if not a.no_cache else 0}
    warm=[request(-i-1) for i in range(a.warmup)]
    if a.device=='cuda':torch.cuda.reset_peak_memory_stats()
    sync();window_start=time.perf_counter()
    with ThreadPoolExecutor(max_workers=a.concurrency) as pool:
        futures = [pool.submit(request, index, time.perf_counter()) for index in range(a.runs)]
        rows = [future.result() for future in futures]
    sync();window=time.perf_counter()-window_start
    profile_path=None
    if a.profile:
        activities=[torch.profiler.ProfilerActivity.CPU]
        if a.device=='cuda':activities.append(torch.profiler.ProfilerActivity.CUDA)
        profile_path=a.out.with_suffix('.trace.json')
        if profile_path.exists():raise FileExistsError(profile_path)
        with torch.profiler.profile(activities=activities,record_shapes=True,profile_memory=True) as prof:request(-999)
        prof.export_chrome_trace(str(profile_path))
    result={'kind':'random_model_smoke' if a.toy else 'local_model_measurement','date':datetime.now(timezone.utc).isoformat(),
            'metadata':{'os':platform.system()+' '+platform.release(),'cpu_arch':platform.machine(),
             'python':platform.python_version(),'torch':torch.__version__,'transformers':importlib.metadata.version('transformers'),
             'device':a.device,'cuda_runtime':torch.version.cuda,'accelerator':torch.cuda.get_device_name() if a.device=='cuda' else a.device,
             'model':'random-tiny-gpt2' if a.toy else a.model,'revision':revision,'dtype':a.dtype,'quantization':'none',
             'layers':layers,'query_heads':heads,'kv_heads':kv_heads,'head_dim':dim,'parameter_payload_bytes':parameter_bytes,
             'threads':a.threads,'batch':a.batch,'concurrency':a.concurrency,'requested_output_tokens':a.output_tokens,
             'fixed_output':a.fixed_output,'cache':not a.no_cache,'warmup_runs':a.warmup,'measured_runs':a.runs},
            'load_s':load_s,'memory_before':before,'memory_after':memory(),'warmup':warm,'requests':rows,
            'summary':{'e2e_s':summarize([r['metrics']['e2e_s'] for r in rows]),
             'submitted_e2e_s':summarize([r['submitted_e2e_s'] for r in rows]),
             'queue_s':summarize([r['queue_s'] for r in rows]),'ttft_s':summarize([r['metrics']['ttft_s'] for r in rows]),
             'window_s':window,'batch_jobs_per_s':len(rows)/window,'sequences_per_s':len(rows)*a.batch/window,
             'output_tokens_per_s':sum(r['completion_tokens_per_sequence']*a.batch for r in rows)/window},
            'profile_trace':str(profile_path) if profile_path else None,
            'limitations':['Local model-side token timestamps; queue_s/submitted_e2e_s include the local worker-pool queue, not HTTP transport.',
             'Per-token synchronization, finite-logit checks, memory sampling and text decoding add instrumentation overhead.',
             'Homogeneous repeated prompts; batch stops only when all sequences emit EOS together or cap reached.',
             'Worker pool is not an inference scheduler; no continuous batching or cancellation implementation.',
             'RAM, driver, power state and competing workloads require the manual profile.',
             'Cache formula assumes homogeneous full attention and no sharing or page rounding.']}
    with a.out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(f'Wrote {a.out}; {len(rows)} measured batch jobs. This is implementation evidence, not learner completion.')
    return 0

if __name__=='__main__':raise SystemExit(main())
