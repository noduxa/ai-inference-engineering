# Module 7: GPU architecture, precision and memory

Status: Not started. Estimated time: **5 hours**, including practice, review and
catch-up. Last verified: 2026-09-16.

[Curriculum](../CURRICULUM.md) · [Schedule](../SCHEDULE.md) ·
[Source pack](../notebooklm/source-packs/07-gpu-architecture-and-memory.md)

## Why this matters

Hardware limits determine which experiments are possible. Memory estimates and
honest timing are prerequisites to interpreting serving performance.

## Learning objectives

- Draw a conceptual execution and memory map for a CPU/GPU system.
- Estimate tensor payload memory across precision formats and state overhead
  limits.
- Interpret utilization, allocated memory and reserved memory without conflating
  them.
- Design a bounded resource experiment and diagnose likely memory or compute
  limits.

## Prerequisites

Complete the preceding module’s core shape, calculation or programming checks;
revisit any unresolved prerequisite before continuing.

## Required concepts

- CPU versus GPU and parallel computation
- GPU cores and streaming multiprocessors
- Warps and thread blocks: conceptual
- CUDA’s role and kernels: conceptual
- Tensor cores
- Host memory, device memory and VRAM
- Registers, shared memory and global memory
- Memory hierarchy and memory bandwidth
- Compute throughput and host-to-device transfers
- Data types: FP32, FP16, BF16, INT8 and INT4
- Quantization: conceptual
- Compute-bound versus memory-bound workloads
- GPU utilization
- Out-of-memory errors
- PyTorch allocated and reserved CUDA memory
- Estimating tensor memory from shape and data type

## Recommended sources

- `gpu-architecture` —
  [CUDA programming guide: architecture concepts](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)
  (primary; selected reading 0.75 h).
- `gpu-performance` —
  [GPU performance background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html)
  (supporting; selected reading 0.5 h).
- `gpu-precision` —
  [Numerical formats and quantization concepts](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/mathematical-functions.html)
  (supporting; selected reading 0.5 h).
- `gpu-memory` —
  [PyTorch CUDA memory and NVIDIA monitoring](https://docs.pytorch.org/docs/2.14/notes/cuda.html)
  (supporting; selected reading 0.5 h).

Exact page links, selected sections, exclusions, access terms and import order
are in the source pack. Reading times are selective budgets, not estimates for
completing entire documentation collections.

## Study order

1. Draw the CPU/GPU execution and memory hierarchy from NVIDIA’s conceptual
   sections.
2. Relate bandwidth and throughput to bounded operations without assuming a
   bottleneck from utilization.
3. Identify the available device in GPU-01, then predict format-dependent
   payloads before GPU-02.
4. Apply GPU-03’s pre-allocation budget and use GPU-04’s simulated refusal for
   safe diagnostic practice.
5. Explain allocated/reserved memory, cleanup and missing hardware evidence
   before the final assessment.

## Exercises and deliverables

[Open the exercise specifications](../exercises/07-gpu-architecture-and-memory.md).

- `GPU-01` — Inspect and monitor the available GPU.
- `GPU-02` — Estimate and compare tensor memory.
- `GPU-03` — Approach a bounded resource limit.
- `GPU-04` — Explain an out-of-memory condition safely.

Deliver a short concept note, original calculations/code, environment record,
actual measurements where applicable, and a teach-back. Use the
[evidence template](../exercises/EVIDENCE_TEMPLATE.md). No outputs are supplied
as completed work.

## Reflection questions

- Where do model tensors live during a host-to-device copy?
- How would you distinguish allocator caching from live memory growth?
- What can a utilization sample tell you, and what can it not tell you?

## Common mistakes to challenge

The following statements are deliberately questionable; correct them with
sources:

- A GPU is always faster for every tensor operation.
- FP16 and BF16 have identical range and precision.
- INT4 storage costs exactly half a byte per value with no metadata or packing
  constraints.
- empty_cache() frees live tensors.
- High utilization proves a workload is compute-bound.

## Exit test

Without NotebookLM, answer the reflection questions and explain a fresh variant
of one exercise. Then use sources to check your answer. Demonstrate a working
application, predict its outcome and diagnose one plausible failure. Record
assistance, corrections and evidence using the
[rubric](../assessments/rubric.md).

- Complete the 4 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

## Completion checklist

- [ ] Selected reading completed and source coverage checked.
- [ ] Each required concept can be recognized and explained at its stated depth.
- [ ] Exercises attempted with reproducible evidence and honest limitations.
- [ ] Exit test and teach-back reviewed; critical misconceptions corrected.
- [ ] Hardware-dependent work still pending is explicitly identified.
- [ ] Weekly review links the evidence; status changes have supporting records.
