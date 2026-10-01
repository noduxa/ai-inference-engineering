# Module 4: Batching, scheduling and serving

Status: Not started. Last verified: 2026-09-30. Estimated time: **7 hours**,
including selected reading, experiments, code reading, review and catch-up.
Shared experiments are charged once in the schedule.

[Curriculum](../CURRICULUM.md) ·
[Source pack](../notebooklm/source-packs/04-batching-scheduling-and-serving.md)
· [Evidence](../EVIDENCE.md) · [Schedule](../SCHEDULE.md)

## Purpose and relevance to inference engineering

Explain static, dynamic and continuous batching with a request timeline. This
connects an observable request behavior to the implementation boundary
responsible for it, so an optimization can be tested.

## Prerequisites

Complete the preceding module’s evidence and exit test; retain its assumptions
for comparisons.

## Learning objectives

- Explain static, dynamic and continuous batching with a request timeline.
- Measure concurrency and batch-size effects on throughput and individual
  latency.
- Specify bounded admission, cancellation and backpressure behavior.

## Required concepts

- Static batching
- dynamic batching
- continuous batching
- queues
- schedulers
- prefill/decode scheduling
- head-of-line blocking
- padding
- sequence variation
- throughput/latency
- concurrency
- backpressure
- admission control
- cancellation
- streaming
- fairness
- capacity
- SLOs

## Detailed explanations and worked examples

### Batching exchanges waiting time for shared work

Static batching fixes a group for one execution/generation job. Dynamic batching
waits briefly to combine arriving requests, often using a maximum batch size and
queue-delay budget. Continuous batching can admit or retire requests between
generation iterations. These policies solve different problems; concurrency is
the number of outstanding requests, not the batch size actually executed.

A scheduler decides which requests get token/compute and cache capacity next.
Long prompts can occupy work that delays decode; long outputs retain cache and
slots. Padding a length-4 and length-20 input to 20 creates 16 padded positions
for the short input in a dense padded representation. Padding masks preserve
semantics but do not guarantee every backend skips padded computation.

**Worked timeline:** request A needs 4 decode iterations, B needs 1, and C
arrives after iteration 1. A static group `[A,B]` can leave B's slot unused
during the remaining three iterations. A continuous scheduler could admit C at
iteration 2 if its prefill and cache budget fit. This is a scheduling
illustration, not a vLLM benchmark. Prefill work, block availability and
fairness can prevent the idealized schedule. Orca supplies the original
iteration-scheduling motivation.

Queue delay contributes to latency. Raising concurrency may increase aggregate
tokens/s by improving utilization while increasing each request's wait. At
saturation the queue can grow without improving useful throughput. A service
level objective (SLO) might bound P95 TTFT for a specified workload and error
rate; it must specify the population and observation window.

Admission control refuses or delays work exceeding capacity. Backpressure slows
upstream producers instead of permitting an unbounded queue. Cancellation must
release request state, avoid emitting further output and account for partial
work. Fairness may trade maximum throughput for bounded waiting across request
sizes. Streaming improves visibility of progress but does not by itself reduce
compute cost. In E06 distinguish a worker-pool simulation from a real continuous
batching engine; client threads alone do not implement a GPU scheduler.

## Required and optional sources

- `p2-m4-continuous` :
  [Continuous batching](https://huggingface.co/docs/transformers/continuous_batching)
  — primary, required; 0.75 h. Study: Introduction; generate_batch;
  ContinuousBatchingManager; streaming and cancellation. Skip: Unlisted APIs,
  training/fine-tuning, distributed deployment and backend installation beyond
  the local lab.
- `p2-m4-orca` :
  [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/system/files/osdi22-yu.pdf)
  — supporting, required; 0.5 h. Study: Sections 2–4: generative workload,
  iteration scheduling and selective batching. Skip: Distributed deployment,
  custom kernels and full evaluation reproduction; follow only the listed
  sections.
- `p2-m4-arch` :
  [vLLM Architecture Overview](https://docs.vllm.ai/en/latest/design/arch_overview/)
  — supporting, required; 0.5 h. Study: Process architecture; API server; engine
  core; workers and model execution. Skip: Unlisted APIs, training/fine-tuning,
  distributed deployment and backend installation beyond the local lab.
- `p2-m4-padding` :
  [Padding and truncation](https://huggingface.co/docs/transformers/main/en/pad_truncation)
  — supporting, required; 0.5 h. Study: Padding; truncation; max_length
  combinations. Skip: Unlisted APIs, training/fine-tuning, distributed
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

## Code-reading task

Read the relevant path in [the local lab](../scripts/inference_lab.py): batch
and worker-pool boundaries; explain what is not continuous batching. Annotate
inputs, outputs, ownership and one error path. Then locate the related symbol
using the source link in the official documentation at a recorded version.

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
[Performance metrics and benchmarking](05-performance-metrics-and-benchmarking.md)
after recording the exit evidence.
