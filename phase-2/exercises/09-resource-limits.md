# E09: How can resource exhaustion be diagnosed without destabilizing the machine?

Status: Not started. Last verified: 2026-09-30.

[Experiment index](README.md) · [Benchmark contract](../BENCHMARKING.md) ·
[Plan template](../templates/experiment-plan.md)

## Question and hypothesis

How can resource exhaustion be diagnosed without destabilizing the machine?

Hypothesis to test: A predeclared budget refuses a request before physical
exhaustion; this is a simulation, not a GPU OOM. This is an expected conceptual
pattern, not an observed result.

## Prerequisites and variables

Complete the corresponding module and the [lab setup](../scripts/README.md).

- Controlled variables: Float32 square tensor arithmetic; software cap 16 MiB;
  no physical allocations in default path.
- Independent variable: Square side length doubled from 64 until the first
  budget refusal.
- Dependent measurements: Requested bytes, configured limit, accepted/refused
  decision, stop reason and recovery explanation.
- Hardware/software metadata: complete the
  [profile](../templates/hardware-software-profile.md), including Python
  version and the lab commit. Mark model, model revision and accelerator fields
  not applicable for the arithmetic simulation; record them for any hardware
  extension.

## Commands and code

From the repository root after setup, use a new output name for each condition:

```bash
.venv/bin/python phase-2/scripts/inference_lab.py \
  --budget-only \
  --out outputs/phase-2/E09/baseline.json
```

The complete runnable code is [inference_lab.py](../scripts/inference_lab.py).
Inspect `budget_study` before running. This path loads no model and its JSON
contains no model revision. Record the repository commit, byte budget and
requested shapes instead; `--revision` is not applicable. Use a new output file
for each run. The default byte budget is fixed in the function; any changed
budget must be recorded as a code/configuration change.

## Procedure

1. Record your prediction and the variables above in the experiment plan.
2. Run the arithmetic simulation and verify each requested byte count by hand.
   Confirm it stops after the first budget refusal without allocating tensors.
3. Explain allocation versus reservation and why release of live references
   matters. For optional hardware observation, cap new tensor payload at the
   lesser of 256 MiB and 10% currently free memory, stop on pressure or the
   first failure, and never intentionally exhaust shared/unified memory. Capture
   an incidental OOM only if safe; otherwise keep physical-OOM status Not
   started.
4. Preserve all measured runs and failures, then apply the analysis template.
5. Give an unaided explanation of the result and one alternative explanation.

## Raw results and analysis

Raw-results location: `outputs/phase-2/E09/` (ignored until reviewed). Use
[benchmark-results](../templates/benchmark-results.md) and, for a causal claim,
[performance-investigation](../templates/performance-investigation.md). Record
units, counts, measurement boundaries, hypotheses versus observations,
uncertainty and a source-backed interpretation. Do not insert worked-example
numbers into measured-result columns.

## Common mistakes and limitations

A software-budget refusal is not a caught allocator exception. The simulation
reports tensor payload only; it does not measure process RSS, allocator
reservation, fragmentation or device pressure. Do not treat its acceptance
decisions as proof that a real allocation will succeed. Keep optional hardware
observations separate from the arithmetic rows.

## Required evidence and interpretation questions

- Prediction, exact commands, repository commit and configured byte budget.
- Raw results, metadata and correctness checks, or a precise execution blocker.
- Analysis: what changed, what stayed fixed and what could confound the result?
- What measurement would distinguish your explanation from its alternative?
- What cannot be generalized to another backend or larger model?
- A corrected teach-back and links to supporting source sections.

## Cleanup and hardware fallback

The default path allocates no trial tensors, needs only standard-library Python
and requires no device cleanup. Preserve the JSON and your calculations. For an
optional hardware extension, exit only your own process and release its tensor
references; do not change drivers or delete global caches. Label the default
result an arithmetic simulation. Physical OOM recovery remains Not started
unless it was safely observed and documented.
