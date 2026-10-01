# E01: Where does each request stage begin and end?

Status: Not started. Last verified: 2026-09-30.

[Experiment index](README.md) · [Benchmark contract](../BENCHMARKING.md) ·
[Plan template](../templates/experiment-plan.md)

## Question and hypothesis

Where does each request stage begin and end?

Hypothesis to test: The final prompt position predicts the first continuation
token; decoding IDs into text is separate from model execution. This is an
expected conceptual pattern, not an observed result.

## Prerequisites and variables

Complete the corresponding module and the [lab setup](../scripts/README.md).

- Controlled variables: One public prompt, model revision, CPU FP32,
  batch/concurrency 1.
- Independent variable: Stage being inspected.
- Dependent measurements: Input IDs/masks/shapes, preparation time, forward
  durations, selected IDs, text snapshots and stop reason.
- Hardware/software metadata: complete the
  [profile](../templates/hardware-software-profile.md), including model
  revision, backend, RAM/VRAM, versions and competing workloads.

## Commands and code

From the repository root after setup, use a new output name for each condition:

```bash
.venv/bin/python phase-2/scripts/inference_lab.py \
  --prompt-tokens 16 --output-tokens 4 --runs 1 --warmup 0 \
  --out outputs/phase-2/E01/baseline.json
```

The complete runnable code is [inference_lab.py](../scripts/inference_lab.py).
Inspect its request and main functions before running. For comparisons copy the
immutable model revision from the first result into `--revision`, change only
the intended argument, and select a new output file. Use only synthetic/public
prompts. Never publish an unreviewed profiler trace.

## Procedure

1. Record your prediction and the variables above in the experiment plan.
2. Run a bounded smoke test and check counts, shapes and finite values.
3. Annotate configuration → weights → tokenizer → mask/device → forward → logits
   → argmax → append → EOS/length → decoded text. Compare the logged first
   forward with subsequent steps; explain why this local token stream is not an
   HTTP stream.
4. Preserve all measured runs and failures, then apply the analysis template.
5. Give an unaided explanation of the result and one alternative explanation.

## Raw results and analysis

Raw-results location: `outputs/phase-2/E01/` (ignored until reviewed). Use
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
