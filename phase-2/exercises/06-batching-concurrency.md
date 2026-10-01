# E06: When does more outstanding work improve throughput and harm latency?

Status: Not started. Last verified: 2026-09-30.

[Experiment index](README.md) · [Benchmark contract](../BENCHMARKING.md) ·
[Plan template](../templates/experiment-plan.md)

## Question and hypothesis

When does more outstanding work improve throughput and harm latency?

Hypothesis to test: A larger batch or worker count may increase throughput while
contention or waiting increases per-job latency. This is an expected conceptual
pattern, not an observed result.

## Prerequisites and variables

Complete the corresponding module and the [lab setup](../scripts/README.md).

- Controlled variables: Same model/revision, prompt length 16, output cap 8,
  dtype and CPU thread count.
- Independent variable: Batch 1/2/4, then concurrency 1/2/4 in a separate sweep.
- Dependent measurements: Shared-window tokens/s, batch jobs/s, sequences/s,
  per-job E2E/TTFT and actual counts.
- Hardware/software metadata: complete the
  [profile](../templates/hardware-software-profile.md), including model
  revision, backend, RAM/VRAM, versions and competing workloads.

## Commands and code

From the repository root after setup, use a new output name for each condition:

```bash
.venv/bin/python phase-2/scripts/inference_lab.py \
  --batch 1 --concurrency 1 --prompt-tokens 16 \
  --output-tokens 8 --fixed-output --runs 8 \
  --out outputs/phase-2/E06/baseline.json
```

The complete runnable code is [inference_lab.py](../scripts/inference_lab.py).
Inspect its request and main functions before running. For comparisons copy the
immutable model revision from the first result into `--revision`, change only
the intended argument, and select a new output file. Use only synthetic/public
prompts. Never publish an unreviewed profiler trace.

## Procedure

1. Record your prediction and the variables above in the experiment plan.
2. Run a bounded smoke test and check counts, shapes and finite values.
3. First sweep batch with concurrency 1. Then sweep CPU concurrency with batch 1
   and enough jobs to occupy workers. Use queue_s and submitted_e2e_s for local
   queue-inclusive latency; model-side TTFT starts inside the worker. Neither
   measures HTTP transport. Draw an iteration-level schedule for lengths 4,1,3
   and explain how it differs from this worker pool.
4. Preserve all measured runs and failures, then apply the analysis template.
5. Give an unaided explanation of the result and one alternative explanation.

## Raw results and analysis

Raw-results location: `outputs/phase-2/E06/` (ignored until reviewed). Use
[benchmark-results](../templates/benchmark-results.md) and, for a causal claim,
[performance-investigation](../templates/performance-investigation.md). Record
units, counts, measurement boundaries, hypotheses versus observations,
uncertainty and a source-backed interpretation. Do not insert worked-example
numbers into measured-result columns.

## Common mistakes and limitations

Do not compare different model revisions, include download time in only one arm,
average incompatible token rates, hide failed requests or infer large-model
behavior from a tiny model. Per-token synchronization and text decoding in this
lab affect timing. It does not measure production HTTP service latency,
implement continuous batching or provide a benchmark of model quality.

## Required evidence and interpretation questions

- Prediction, exact commands and immutable model revision.
- Raw results, metadata and correctness checks, or a precise execution blocker.
- Analysis: what changed, what stayed fixed and what could confound the result?
- What measurement would distinguish your explanation from its alternative?
- What cannot be generalized to another backend or larger model?
- A corrected teach-back and links to supporting source sections.

## Cleanup and hardware fallback

Exit only the process you started; release model/tensor references. Keep raw
results and discard temporary traces only after preserving reviewed evidence. Do
not delete global caches or change GPU driver settings. Default to CPU. Add
`--toy` for a tiny random model without downloads (except E09, which needs no
model packages). Label this a mechanics smoke test, with no language-quality
claim. Where accelerator evidence is absent, record Not started rather than
claiming CPU measurements establish CUDA behavior.
