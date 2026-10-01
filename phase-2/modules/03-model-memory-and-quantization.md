# Module 3: Model memory and quantization

Status: Not started. Last verified: 2026-09-30. Estimated time: **13 hours**,
including selected reading, experiments, code reading, review and catch-up.
Shared experiments are charged once in the schedule.

[Curriculum](../CURRICULUM.md) ·
[Source pack](../notebooklm/source-packs/03-model-memory-and-quantization.md) ·
[Evidence](../EVIDENCE.md) · [Schedule](../SCHEDULE.md)

## Purpose and relevance to inference engineering

Build a memory budget including weights, activations, KV state, workspace and
overhead. This connects an observable request behavior to the implementation
boundary responsible for it, so an optimization can be tested.

## Prerequisites

Complete the preceding module’s evidence and exit test; retain its assumptions
for comparisons.

## Learning objectives

- Build a memory budget including weights, activations, KV state, workspace and
  overhead.
- Compare two supported precisions and interpret memory, timing and output
  differences.
- Diagnose an OOM without treating reserved memory as a leak.

## Required concepts

- Parameter count
- weights
- activations
- KV cache
- temporary workspace
- runtime and allocator overhead
- FP32
- FP16
- BF16
- INT8
- INT4
- weight-only and activation quantization
- calibration
- accuracy
- dequantization
- hardware support
- fragmentation
- allocated and reserved memory
- OOM

## Detailed explanations and worked examples

### A model file size is not a runtime memory budget

Use `weight_bytes ≈ parameter_count × bits_per_weight / 8` for an ideal uniform
representation. State whether tied/shared parameters are counted once. Add scale
and zero-point metadata, packing/alignment and unquantized modules. Then budget
activations, KV state, temporary workspaces, runtime contexts and allocator
slack. Peak overlap matters: two buffers can coexist during conversion or
loading.

**Worked example:** an assumed 100 million unique parameters occupy 400 MB at
FP32, 200 MB at FP16/BF16, 100 MB at INT8 and an ideal 50 MB at packed INT4.
These are decimal MB, before all overhead. A 200 MB weight estimate does not
prove a model fits in 200 MB of device memory. Add the cache estimate from
Module 2 for the actual batch/length, then leave measured headroom.

FP16 and BF16 both use two bytes, but trade exponent range against significand
precision differently. Quantization maps values to a smaller code set, commonly
using a scale (and possibly a zero point). Weight-only quantization compresses
weights while activations may remain floating-point. Activation quantization
also constrains intermediate values. Calibration estimates suitable ranges from
representative data; a mismatched calibration set can hide important outliers.

A simple symmetric toy mapping is `q=clip(round(x/scale),-127,127)` and
`x_hat=scale*q`. At scale 0.1, 0.26 maps to 3 and reconstructs as 0.3. The error
0.04 illustrates rounding, not the behavior of every quantization library.
Dequantization, unsupported kernels, layout conversions and small problem sizes
can cancel storage benefits. Check the current backend support table before
choosing E05; precision comparison is sufficient when quantized execution is
unsupported. Do not install an unrelated accelerator toolchain for this phase.

Allocated CUDA memory measures live allocator-managed allocations; reserved
memory includes reusable blocks. A gap can be normal caching, not a leak.
Fragmentation means free capacity may not be available in the required layout.
Diagnose OOM by recording request sizes, peaks and live references, then
reducing one driver of demand. Do not "fix" it solely by clearing unused cache
while live tensors still occupy the device. The CUDA semantics reading supplies
the API measurement contract; E09 uses a safe software budget when physical OOM
is risky.

## Required and optional sources

- `p2-m3-optimization` :
  [Optimizing LLMs for Speed and Memory](https://huggingface.co/docs/transformers/llm_tutorial_optimization)
  — primary, required; 0.75 h. Study: Memory requirements; lower precision;
  key-value cache; MQA/GQA discussion. Skip: Unlisted APIs,
  training/fine-tuning, distributed deployment and backend installation beyond
  the local lab.
- `p2-m3-quant` :
  [Quantization overview](https://huggingface.co/docs/transformers/quantization/overview)
  — supporting, required; 0.5 h. Study: Quantization introduction;
  hardware/method compatibility table. Skip: Unlisted APIs,
  training/fine-tuning, distributed deployment and backend installation beyond
  the local lab.
- `p2-m3-bnb` :
  [Bitsandbytes](https://huggingface.co/docs/transformers/quantization/bitsandbytes)
  — supporting, required; 0.5 h. Study: Hardware compatibility; 8-bit and 4-bit
  loading; memory footprint. Skip: Unlisted APIs, training/fine-tuning,
  distributed deployment and backend installation beyond the local lab.
- `p2-m3-cuda` :
  [CUDA semantics](https://docs.pytorch.org/docs/2.14/notes/cuda.html) —
  supporting, required; 0.5 h. Study: Asynchronous execution; memory management;
  memory statistics. Skip: Unlisted APIs, training/fine-tuning, distributed
  deployment and backend installation beyond the local lab.

The source pack records publisher, access, terms, exact sections and import
order. Prefer the official contract over overlapping generic tutorials. Reused
sources are targeted lookups, not a requirement to reread the full document.
Optional visual study: redraw the architecture/cache diagrams in these same
sources and explain every arrow; no extra repetitive source is needed.

## Study order

1. Read the primary source’s listed sections and define the module’s terms.
2. Work through the example above by hand, checking shapes, units and
   assumptions.
3. Read supporting sources in the listed order; record one clarification or
   conflict.
4. Execute the linked practical work and retain raw observations before
   analysis.
5. Read code, give a closed-source teach-back, then correct it against sources.

## Practical exercises

- [E05](../exercises/05-precision.md)
- [E09](../exercises/09-resource-limits.md)

## Code-reading task

Read the relevant path in [the local lab](../scripts/inference_lab.py): dtype
selection and allocated/reserved accounting. Annotate inputs, outputs, ownership
and one error path. Then locate the related symbol using the source link in the
official documentation at a recorded version.

## Reflection and misconceptions

- Which statement here depends on a model, backend or workload assumption?
- What observation would falsify your current explanation?
- Which result cannot be generalized to a larger model or different hardware?
- Challenge: a smaller memory footprint always means lower latency.
- Challenge: a successful run or Audio Overview proves this module is mastered.

## Common implementation mistakes

Reusing unrecorded defaults; changing multiple workload variables; confusing
logical tokens with padded positions; measuring asynchronous enqueue time;
retaining previous request state; and treating simulated results as device data.
Identify which mistakes are relevant to your experiment and show how you
checked.

## Required evidence and exit test

- Original explanation and annotated code trace
- Reproducible experiment with raw measurements or explicit hardware limitation
- Reviewed exit assessment with corrections

Without NotebookLM, demonstrate each learning objective on a fresh example.
Explain one failed hypothesis or plausible failure and what measurement would
resolve it. Apply the [rubric](../assessments/rubric.md); explicitly admit where
supplied evidence is insufficient. Reading time alone cannot pass this gate.

## Completion checklist

- [ ] Explain each required concept at application level where exercised.
- [ ] Complete a fresh calculation/trace with stated assumptions.
- [ ] Link raw observations, environment and interpretation.
- [ ] Review the exit test; correct critical misconceptions.
- [ ] Mark hardware-dependent work pending where it was not executed.

## Connection to the next module

Continue to
[Batching, scheduling and serving](04-batching-scheduling-and-serving.md) after
recording the exit evidence.
