# Phase 2 curriculum

Status: Not started. Last verified: 2026-09-30.

[Overview](README.md) · [Schedule](SCHEDULE.md) · [Registry](curriculum.yaml)

## Entry and progression

Phase 1 supplies object ownership, concurrency, shapes, gradients, attention,
devices and memory arithmetic. Phase 2 uses them to explain complete requests,
measure performance and investigate failures. It does not repeat a general
Python or neural-network course. If a prerequisite cannot be explained unaided,
repair that specific Phase 1 evidence before advancing.

| Order | Module                                                                                     | Hours | Status      |
| ----- | ------------------------------------------------------------------------------------------ | ----- | ----------- |
| 1     | [Inference request lifecycle](modules/01-inference-request-lifecycle.md)                   | 7     | Not started |
| 2     | [Prefill, decode and KV cache](modules/02-prefill-decode-and-kv-cache.md)                  | 10    | Not started |
| 3     | [Model memory and quantization](modules/03-model-memory-and-quantization.md)               | 13    | Not started |
| 4     | [Batching, scheduling and serving](modules/04-batching-scheduling-and-serving.md)          | 7     | Not started |
| 5     | [Performance metrics and benchmarking](modules/05-performance-metrics-and-benchmarking.md) | 8     | Not started |
| 6     | [Profiling and bottleneck diagnosis](modules/06-profiling-and-bottleneck-diagnosis.md)     | 6     | Not started |
| 7     | [Serving systems and the vLLM bridge](modules/07-serving-systems-and-vllm-bridge.md)       | 6     | Not started |

## Depth contract

Application is required for request tracing, cache/weight calculations, timing,
controlled comparisons and diagnostic experiments. Early diagnosis means
choosing a useful next measurement and ruling out a plausible alternative
explanation. PagedAttention, continuous scheduling, cache eviction and server
decomposition require conceptual explanation and code navigation, not
implementation mastery. Quantization requires trade-off reasoning; a supported
precision comparison is acceptable when integer-quantized execution is
unavailable.

Use the module study order, four or five source collections, original
calculations and nine experiments. The same experiment can support several
learning claims, but its hours are counted once. Later modules reinterpret its
evidence rather than manufacture new runs. Finish with the
[assessment system](ASSESSMENT.md) and
[readiness review](assessments/phase-3-readiness-review.md).
