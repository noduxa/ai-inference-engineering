# Phase 2: Language-model inference fundamentals

Status: Not started. Target month: November 2026. Planned workload: **60
hours**. Last verified: 2026-09-30.

Joshua’s next step is practical inference understanding, not a claim of
specialist status. Begin only after the
[Phase 1 evidence gate](../phase-1/EVIDENCE.md). Use a small public model,
measured experiments and explicit uncertainty to bridge from tensor/attention
foundations into reading vLLM in Phase 3.

## Navigate the programme

- [Curriculum](CURRICULUM.md) and [four-week schedule](SCHEDULE.md).
- [NotebookLM source packs](notebooklm/README.md) and
  [source policy](SOURCE_POLICY.md).
- [Experiments](exercises/README.md) and [local lab](scripts/README.md).
- [Benchmark standard](BENCHMARKING.md) and [glossary](GLOSSARY.md).
- [Assessment](ASSESSMENT.md), [evidence](EVIDENCE.md) and
  [Phase 3 readiness gate](assessments/phase-3-readiness-review.md).
- [Machine-readable curriculum](curriculum.yaml), [sources](sources.yaml) and
  [shared validation](../scripts/README.md).

| Order | Module                                                                                     | Hours | Status      |
| ----- | ------------------------------------------------------------------------------------------ | ----- | ----------- |
| 1     | [Inference request lifecycle](modules/01-inference-request-lifecycle.md)                   | 7     | Not started |
| 2     | [Prefill, decode and KV cache](modules/02-prefill-decode-and-kv-cache.md)                  | 10    | Not started |
| 3     | [Model memory and quantization](modules/03-model-memory-and-quantization.md)               | 13    | Not started |
| 4     | [Batching, scheduling and serving](modules/04-batching-scheduling-and-serving.md)          | 7     | Not started |
| 5     | [Performance metrics and benchmarking](modules/05-performance-metrics-and-benchmarking.md) | 8     | Not started |
| 6     | [Profiling and bottleneck diagnosis](modules/06-profiling-and-bottleneck-diagnosis.md)     | 6     | Not started |
| 7     | [Serving systems and the vLLM bridge](modules/07-serving-systems-and-vllm-bridge.md)       | 6     | Not started |

Modules total 57 hours plus 3 hours of final assessment. Reading, practice,
weekly review and catch-up are included. No production distributed serving,
custom kernels, RDMA or multi-node deployment is required. CPU fallbacks
establish mechanics; absent GPU observations remain an explicit evidence gap.
