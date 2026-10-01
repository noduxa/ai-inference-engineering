# Module 5: Performance metrics and benchmarking

Status: Not started. Last verified: 2026-09-30. Estimated time: **8 hours**,
including selected reading, experiments, code reading, review and catch-up.
Shared experiments are charged once in the schedule.

[Curriculum](../CURRICULUM.md) ·
[Source pack](../notebooklm/source-packs/05-performance-metrics-and-benchmarking.md)
· [Evidence](../EVIDENCE.md) · [Schedule](../SCHEDULE.md)

## Purpose and relevance to inference engineering

Define TTFT, TPOT, ITL and throughput with explicit clocks and token counts.
This connects an observable request behavior to the implementation boundary
responsible for it, so an optimization can be tested.

## Prerequisites

Complete the preceding module’s evidence and exit test; retain its assumptions
for comparisons.

## Learning objectives

- Define TTFT, TPOT, ITL and throughput with explicit clocks and token counts.
- Design a repeated, controlled comparison with raw per-request records.
- Explain when tail percentiles and cross-hardware comparisons are misleading.

## Required concepts

- End-to-end latency
- TTFT
- TPOT
- ITL
- tokens/s
- requests/s
- throughput
- concurrency
- prompt/completion tokens
- P50/P95/P99
- GPU activity and memory
- bandwidth and compute
- warm-up
- repetition
- synchronization
- fixed and variable workloads
- measurement error
- versions
- fair comparison

## Detailed explanations and worked examples

### A metric is a numerator, denominator and measurement boundary

For request start `t0`, first output-token availability `t1`, last token `tN`
and response completion `te`: TTFT is `t1-t0`, end-to-end latency is `te-t0`,
and per-request mean TPOT is `(tN-t1)/(N-1)` for `N>=2` . ITL samples are
successive token timestamp differences. Report TPOT as unavailable for one-token
outputs. Client chunk gaps are not necessarily token gaps: buffering can
coalesce tokens. Define whether timestamps are model-side or client-side.

Aggregate output throughput is total successful completion tokens divided by a
shared wall-clock window. Requests/s uses completed requests over that window.
Mean per-request token rates are not the same estimator. Report prompt tokens,
actual completion tokens, requested maximum, failures and partial/cancelled
work. A system producing shorter answers can look faster without doing
equivalent work. The vLLM benchmark reference makes load-generator settings
inspectable.

**Worked arithmetic:** artificial token timestamps `[0.2,0.3,0.5]` seconds after
start imply TTFT 0.2 s, ITLs 0.1 and 0.2 s, and TPOT 0.15 s. If two requests
produce 3 and 5 tokens over a shared 1-second interval, aggregate throughput is
8 tokens/s, regardless of their individual rates. These numbers are assessment
examples and must never enter raw benchmark results.

P50 is a median; P95/P99 describe tails under a specified quantile convention.
Ten runs cannot establish a reliable P99. Preserve raw samples, report sample
count and variability, and label a tiny-sample percentile exploratory. A closed
loop at fixed concurrency sends the next request after completion; an open-loop
arrival process controls offered load. They answer different questions and can
hide queueing differently. Always record the load model.

Warm up using the measured shape/configuration, repeat, control competing work,
and alternate comparison arms when drift matters. Synchronize device work at
measurement boundaries. Profiling overhead and explicit per-token
synchronization can alter the workload. GPU activity, memory occupancy, achieved
compute and memory bandwidth are distinct quantities. A high utilization sample
is not proof of a compute bottleneck. Use the benchmarking contract before
publishing any system comparison, especially across hardware.

## Required and optional sources

- `p2-m5-bench` :
  [vLLM bench serve reference](https://docs.vllm.ai/en/latest/cli/bench/serve/)
  — primary, required; 0.75 h. Study: Dataset, request-rate, max-concurrency,
  warm-up, metric and result-saving arguments. Skip: Unlisted APIs,
  training/fine-tuning, distributed deployment and backend installation beyond
  the local lab.
- `p2-m5-metrics` :
  [vLLM Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/) —
  supporting, required; 0.5 h. Study: Metrics endpoint; request latency, queue,
  token and cache metric examples. Skip: Unlisted APIs, training/fine-tuning,
  distributed deployment and backend installation beyond the local lab.
- `p2-m5-gpu` :
  [GPU Performance Background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html)
  — supporting, required; 0.5 h. Study: Sections 2–5: architecture, execution,
  arithmetic intensity and operation categories. Skip: Unlisted APIs,
  training/fine-tuning, distributed deployment and backend installation beyond
  the local lab.
- `p2-m5-cuda` :
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

- [E06](../exercises/06-batching-concurrency.md)
- [E07](../exercises/07-warm-cold.md)

## Code-reading task

Read the relevant path in [the local lab](../scripts/inference_lab.py):
timestamp collection, token counts and summary denominators. Annotate inputs,
outputs, ownership and one error path. Then locate the related symbol using the
source link in the official documentation at a recorded version.

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
[Profiling and bottleneck diagnosis](06-profiling-and-bottleneck-diagnosis.md)
after recording the exit evidence.
