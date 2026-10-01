# Benchmarking contract

Status: Planned. Last verified: 2026-09-30.

[Experiments](exercises/README.md) ·
[Results template](templates/benchmark-results.md)

## State the question before choosing the metric

A local forward-call microbenchmark, a generation-loop experiment and a loaded
HTTP service benchmark have different clocks and queues. Label yours. Record
what is inside the timed region, where timestamps originate, and whether stream
events are tokens or text chunks. The local lab measures model-side
availability; its synchronized token loop is intentionally observable and is not
an optimized server. See
[vLLM benchmark options](https://docs.vllm.ai/en/latest/cli/bench/serve/) and
[CUDA timing](https://docs.pytorch.org/docs/2.14/notes/cuda.html).

## Required environment and workload record

Report date; OS; CPU; RAM; GPU/accelerator; VRAM or unified-memory distinction;
driver; CUDA or relevant backend; Python and framework versions; model and
immutable revision; quantization/precision; tokenizer revision; prompt token
counts; requested and actual output lengths; batch size; concurrency; arrival
model; warm-up count; measured-run count; seeds; thread counts; cache policy;
stop rules; and competing workloads. Use the
[hardware/software profile](templates/hardware-software-profile.md).

## Measurement and analysis rules

1. Check correctness first. Retain failures, timeouts, rejected requests and
   partial output counts. Report error rate and the denominator.
2. Fix public/synthetic prompts. For a length sweep, vary only that dimension.
   Repeated tokens are an artificial workload; a mixed-length corpus is a
   separate experiment with its distribution recorded.
3. Separate download, loading, first execution, warm-up and measured runs. Warm
   up the measured shapes/configuration. Record cache reuse explicitly.
4. Synchronize device timing boundaries. Record instrumentation/profiling cost;
   run the profiler separately from headline timing samples.
5. Repeat and, where feasible, alternate comparison arms to expose thermal or
   background-load drift. Keep every raw measurement.
6. Report count, mean and median. P95 is exploratory at 20 samples; collect a
   larger representative sample before tail/SLO claims. State the quantile rule.
   Do not infer P99 reliability from a handful of runs.
7. Define output tokens/s as successful output tokens over a shared measured
   window; distinguish it from input+output throughput and per-request rates.
   State whether failures and warm-up are excluded from numerator/window.
8. TTFT includes everything between the declared request start and first token.
   TPOT=(last-first token time)/(actual output tokens-1), unavailable below two
   tokens. ITL is each successive token gap. Chunk gaps need a different label.
9. Compare systems under matched artifacts, dtype, prompts, outputs, load,
   resource bounds and timing scope. API compatibility does not ensure parity.
   Different hardware is a different experiment: contextualize compute/memory,
   cost and workload; no universal normalization makes all systems equivalent.
10. Record limitations and plausible alternative explanations. High sampled GPU
    activity is not measured FLOPs; occupied VRAM is not memory bandwidth.

## Publication gate

Keep raw files under ignored `outputs/phase-2/E##/`. Review them for prompts,
local paths, private environment values and copyrighted/model artifacts before
copying selected small evidence into the public experiments/benchmarks area.
Link the exact command and commit, not an unsupported performance claim. No
benchmark numbers are supplied as Joshua’s results in this curriculum.
