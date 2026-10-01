# Module 6: Profiling and bottleneck diagnosis

Status: Not started. Last verified: 2026-09-30. Estimated time: **6 hours**,
including selected reading, experiments, code reading, review and catch-up.
Shared experiments are charged once in the schedule.

[Curriculum](../CURRICULUM.md) ·
[Source pack](../notebooklm/source-packs/06-profiling-and-bottleneck-diagnosis.md)
· [Evidence](../EVIDENCE.md) · [Schedule](../SCHEDULE.md)

## Purpose and relevance to inference engineering

Use CPU and device observations to form a falsifiable performance hypothesis.
This connects an observable request behavior to the implementation boundary
responsible for it, so an optimization can be tested.

## Prerequisites

Complete the preceding module’s evidence and exit test; retain its assumptions
for comparisons.

## Learning objectives

- Use CPU and device observations to form a falsifiable performance hypothesis.
- Read a profiler timeline and distinguish activity from causal evidence.
- Change one variable and report uncertainty and failed hypotheses.

## Required concepts

- CPU
- tokenization
- GPU
- transfers
- synchronization
- kernel launch overhead
- memory-bound and compute-bound execution
- underutilization
- small batches
- long prompts
- long outputs
- allocation pressure
- OOM
- PyTorch Profiler
- NVIDIA monitoring
- CPU/RAM monitoring
- timelines
- controlled hypotheses
- correlation and causation

## Detailed explanations and worked examples

### Diagnose a reproducible symptom

1. Define the symptom in observable terms: for example, higher model-side TTFT
   at the same prompt length, not simply "the GPU is slow".
2. Fix model revision, token IDs, precision, backend, batch/concurrency and
   clocks.
3. Measure repeated baseline runs and verify correct outputs.
4. Form a hypothesis with a prediction that could be wrong.
5. Change one variable and record exactly what changed.
6. Measure again under the same boundary, separately from profiler overhead.
7. Compare distributions and competing explanations, not only the best run.
8. Record uncertainty, limitations and the next discriminating experiment.

CPU tokenization, Python dispatch, serialization and host-to-device copies can
leave the accelerator idle. Small batches may not expose enough parallel work;
launch overhead can dominate small kernels. Long prompts enlarge prefill work;
long outputs repeat decode and grow cache. Memory bandwidth and compute limits
can shift with shape and batch, so one utilization percentage cannot classify
all workloads. See NVIDIA's monitoring reference and the PyTorch profiler
recipe.

A timeline relates host events, copies, device kernels and synchronization. An
idle gap before a kernel suggests an investigation of its producer, but not
proof of a CPU bottleneck. A `.item()` or host read can synchronize
unexpectedly. An allocation spike can reflect a temporary buffer, retained
reference or cache capacity; examine its lifetime and dimensions. Monitor
process RAM separately from CUDA allocated/reserved memory. CPU-only systems can
still expose scheduling, allocation and tokenization costs.

**Worked investigation design:** suppose short requests have poor throughput.
Hypothesis: per-request tokenization dominates. Compare tokenization-included
and pretokenized model boundaries using identical IDs. If only the model-only
measurement improves, the model kernel did not get faster. Next test bounded
batching without changing text or precision. A synthetic injected delay can test
the instrumentation, but cannot establish the bottleneck of a real model.

For OOM, first capture the failing workload and configured limits. Estimate
weights plus KV state, inspect live references and peak allocations, then reduce
one of batch, length or representation. Avoid repeatedly retrying the same
allocation. Use E09's simulated budget refusal when physical exhaustion is
unsafe.

## Required and optional sources

- `p2-m6-profiler` :
  [PyTorch Profiler recipe](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)
  — primary, required; 0.75 h. Study: Execution time; memory consumption;
  tracing; profiler schedules. Skip: Unlisted APIs, training/fine-tuning,
  distributed deployment and backend installation beyond the local lab.
- `p2-m6-cuda` :
  [CUDA semantics](https://docs.pytorch.org/docs/2.14/notes/cuda.html) —
  supporting, required; 0.5 h. Study: Asynchronous execution; memory management;
  memory statistics. Skip: Unlisted APIs, training/fine-tuning, distributed
  deployment and backend installation beyond the local lab.
- `p2-m6-smi` :
  [NVIDIA System Management Interface](https://docs.nvidia.com/deploy/nvidia-smi/index.html)
  — supporting, required; 0.5 h. Study: Query options; utilization; memory;
  sampling limitations. Skip: Unlisted APIs, training/fine-tuning, distributed
  deployment and backend installation beyond the local lab.
- `p2-m6-python` :
  [The Python Profilers](https://docs.python.org/3/library/profile.html) —
  supporting, required; 0.5 h. Study: Introduction; cProfile; pstats cumulative
  and internal time. Skip: Unlisted APIs, training/fine-tuning, distributed
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

- [E08](../exercises/08-bottleneck.md)
- [E09](../exercises/09-resource-limits.md)

## Code-reading task

Read the relevant path in [the local lab](../scripts/inference_lab.py): profiler
scope and controlled experiment inputs. Annotate inputs, outputs, ownership and
one error path. Then locate the related symbol using the source link in the
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
[Serving systems and the vLLM bridge](07-serving-systems-and-vllm-bridge.md)
after recording the exit evidence.
