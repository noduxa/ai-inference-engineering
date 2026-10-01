# Benchmark-design assessment

Status: Not started. Time budget: 25 minutes.

[Assessment index](README.md) · [Rubric](rubric.md)

Attempt independently first. Record assistance and uncertainty. Answers and
review criteria belong in [facilitator guidance](facilitator-guidance.md), not
beside these questions.

A colleague reports “System B is twice as fast” using different GPUs, models,
output lengths, sampling settings and warm-up policies. No raw data is
available.

1. Separate the unsupported claim from what the stated evidence can establish.
2. Design a fair comparison: hardware/software profiles, model/tokenizer
   revision, representation, prompt distribution, output counts,
   batch/concurrency, arrival process, cache policy, warm-up, repeats, timing
   boundaries and failure accounting.
3. Define primary and secondary metrics and the precise tokens/s denominator.
4. Explain what sample count and quantile convention you would use for P95 and
   why a tiny P99 should not be treated as an SLO measurement.
5. Use one actual E02–E07 result set to show the raw record, calculation and
   limits. If none exists, the evidence requirement is Not started; artificial
   examples cannot substitute.
6. Explain why normalized cost or theoretical compute alone does not make unlike
   hardware directly comparable across all workloads.

## Evidence

Retain the original attempt, calculation/code trace, cited corrections and score
by criterion. Link actual experiment records where requested. Missing evidence
stays Not started rather than becoming a hypothetical completed experiment.
