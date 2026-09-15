# Roadmap

**Status: Planned.** All phases are learning and contribution targets. Dates do
not certify completion. Upstream acceptance and external recognition depend on
others; record evidence and adjust scope honestly in
[weekly logs](weekly-logs/README.md).

## Phase 1: Foundations — September to October 2026

Learning order:

1. Advanced Python
2. NumPy and tensors
3. Essential linear algebra
4. PyTorch fundamentals
5. Neural-network fundamentals
6. Transformer architecture
7. GPU architecture and memory

### Python study

- Memory and object behaviour, references, mutability and allocation
- Iterators and generators
- Decorators and context managers
- Type hints and protocols
- AsyncIO and cancellation
- Multiprocessing and process communication
- Packaging and dependency isolation
- Testing with pytest
- CPU and memory profiling
- Reading large Python repositories and tracing execution paths

### Numerical and model foundations

Study array shapes, broadcasting, vectorization, matrix multiplication, norms,
probability basics and numerical precision. Connect these to neural-network
layers, activations, losses and the distinction between training and inference.

### PyTorch study

- Tensors and shapes
- CPU and GPU devices
- `nn.Module`
- Model loading
- Data types and precision
- Memory measurement
- PyTorch profiler
- `torch.compile`
- Distributed-system fundamentals

### Phase 1 evidence and exit criteria — Planned

By 31 October, target small tested Python examples, explained tensor operations,
a minimal model-loading exercise, and a CPU/GPU memory investigation where
hardware permits. Record hardware limits explicitly. Produce notes explaining
GPU execution, memory hierarchy and data movement. Link runnable artifacts and
observations before marking foundations established.

## Phase 2: Inference fundamentals — November 2026

Study tokenization, autoregressive generation, prefill and decode, attention, KV
cache, context length, quantization, static and continuous batching, prefix
caching and speculative decoding. Investigate throughput versus latency and CPU,
GPU, memory and network bottlenecks.

### Metrics

- Time to first token (TTFT)
- Time per output token (TPOT)
- Inter-token latency (ITL)
- Requests per second
- Tokens per second
- P50, P95 and P99 latency
- GPU utilization
- VRAM consumption
- Error rate
- Cost per million tokens

Define measurement boundaries, token counting, percentile methods and whether
cost includes input tokens, output tokens, idle time or infrastructure overhead.
Do not treat TPOT averages and individual inter-token intervals as
interchangeable.

### Initial systems to compare

1. Hugging Face Transformers
2. Ollama
3. vLLM

Use compatible model artifacts and controlled workloads where possible. Record
any differences in model conversion, precision, tokenizer, hardware or serving
configuration that limit comparability. No performance ranking is assumed.

### Phase 2 evidence and exit criteria — Planned

Target an explained inference request lifecycle and one reproducible comparison
with raw measurements, failures and limitations by 30 November. Validate the
[runbook templates](runbooks/README.md) before calling any deployment
successful.

## Phase 3: Join open source — December 2026

Initial community: **vLLM**. December is for community entry and preparation,
not a claim of major contributions.

- Read the contribution guide.
- Study the architecture.
- Join appropriate community channels.
- Attend or review community meetings.
- Build vLLM locally or on suitable GPU infrastructure.
- Run its tests and official benchmarks.
- Trace an inference request through the codebase.
- Study recently merged pull requests.
- Identify maintainers and subsystem owners.
- Reproduce at least one real issue.
- Write a technically useful issue comment.
- Prepare the first contribution for January 2027.

Recommended entry areas: documentation, testing, CI reliability, benchmark
reliability, observability, Docker, Kubernetes, API serving and error handling.
Check current upstream guidance before selecting an issue or contacting anyone.

### Phase 3 evidence and exit criteria — Planned

By 31 December, target a local build/test record, a request trace, a
reproducible issue investigation, a useful public interaction and a focused
contribution proposal. Follow the
[community entry plan](open-source/community-entry-plan.md).

## Phase 4: Begin contributions — January to March 2027

- First contribution submitted by 15 January 2027.
- Three to five accepted contributions targeted by 31 March 2027.
- At least one code contribution.
- At least one test or benchmark contribution.
- Consistent participation in the community.
- Selection of one inference subsystem for deeper specialization.

Recommended starting specialization:

> Observability, benchmark reliability and Kubernetes-based model serving.

Maintain a contribution record with upstream links, tests, review feedback and
actual status. Submission is distinct from acceptance. Choose subsystem depth
based on investigated problems, feedback and available infrastructure.

## Phase 5: Serious contribution — April to August 2027

Study and investigate:

- Continuous batching and paged attention
- Prefix caching and chunked prefill
- Speculative decoding
- Tensor parallelism and data parallelism
- Multi-GPU communication and NCCL fundamentals
- Autoscaling and admission control
- Backpressure and failure recovery

### Expected evidence — Planned

- Performance investigation
- Benchmark improvement
- Memory, concurrency or scheduling fix
- Distributed test improvement
- Ownership of a contained feature
- International mentorship or community-program applications

Target a meaningful subsystem-level contribution by 31 August. Scope work with
maintainers, establish a baseline and include regression evidence. Applications
are intentions, not selections or awards.

## Phase 6: Public authority — September to December 2027

Expected outputs, all planned:

- Rigorous performance investigation
- Reproducible benchmark methodology
- Public benchmark results
- Technical article
- Community presentation
- Kubernetes inference deployment
- Monitoring dashboard
- Meaningful upstream contribution

By 31 December, aim for public technical authority to begin emerging from
useful, reviewable work. Publish methods, raw evidence and limitations;
recognition is an aspiration, not a self-awarded credential.

## Phase 7: Specialist depth — 2028 onward

Long-term topics:

- C++ and CUDA
- Triton
- PyTorch internals and GPU profiling
- NCCL and RDMA
- Multi-node serving
- Compiler optimization and memory allocators
- Kernel fusion and FlashAttention
- Mixture-of-experts inference

Pursue sustained technical ownership of a subsystem. Select advanced topics in
response to measured bottlenecks and upstream needs. Recognized specialist
status is a long-term target supported by external review and sustained
contributions.

## Review cadence

Use the [weekly template](weekly-logs/TEMPLATE.md) to compare intentions with
actual evidence. Review phase scope monthly. Keep missed targets visible and
explain rescheduling without rewriting planned work as achievement.
