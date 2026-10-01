# NotebookLM workflow for Phase 2

Status: Planned. Last verified: 2026-09-30. Imports remain To be validated.

This repository prepares manual source packs. It does not authenticate with or
automate NotebookLM. Use only public permitted content and your own learning
notes.

1. Create the notebook named in a pack.
2. Import exact selected pages/PDFs in order; inspect extracted code/equations.
3. Ask grounding questions and verify that answers cite the intended section.
4. Use the Audio Overview to orient study, then calculate and experiment
   yourself.
5. Give an unaided teach-back before requesting feedback; keep original
   attempts.
6. Record missing coverage, source disagreements, corrections and evidence.

## Source packs

- [Inference request lifecycle](source-packs/01-inference-request-lifecycle.md)
- [Prefill, decode and KV cache](source-packs/02-prefill-decode-and-kv-cache.md)
- [Model memory and quantization][nav-1]
- [Batching, scheduling and serving][nav-2]
- [Performance metrics and benchmarking][nav-3]
- [Profiling and bottleneck diagnosis][nav-4]
- [Serving systems and the vLLM bridge][nav-5]

## Reusable prompts

[Prompt index](prompts/README.md). The existing Phase 1 prompt files are shared;
there is one maintained copy. Each Phase 2 pack supplies module-specific
prompts. NotebookLM citations and generated audio must be checked against the
imported material. They do not certify experiment execution, accuracy or
learning.

[nav-1]: source-packs/03-model-memory-and-quantization.md
[nav-2]: source-packs/04-batching-scheduling-and-serving.md
[nav-3]: source-packs/05-performance-metrics-and-benchmarking.md
[nav-4]: source-packs/06-profiling-and-bottleneck-diagnosis.md
[nav-5]: source-packs/07-serving-systems-and-vllm-bridge.md
