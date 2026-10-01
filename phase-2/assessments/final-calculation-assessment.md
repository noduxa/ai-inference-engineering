# Calculation assessment

Status: Not started. Time budget: 30 minutes.

[Assessment index](README.md) · [Rubric](rubric.md)

Attempt independently first. Record assistance and uncertainty. Answers and
review criteria belong in [facilitator guidance](facilitator-guidance.md), not
beside these questions.

State assumptions and units beside every answer. Show working before using code.

1. Estimate ideal weight bytes for 750 million unique parameters in FP32, BF16
   and packed INT4. Convert to GiB. List four omitted runtime costs.
2. For a hypothetical full-attention decoder with 12 layers, 8 query heads, 2 KV
   heads, head width 64, batch 3, cached length 512 and 2-byte cache elements,
   estimate K/V payload. What changes when length doubles? When only query heads
   double? What if one sequence is length 256 instead of 512?
3. An additive causal mask is applied to scores shaped `(2,4,8,8)`. Annotate
   batch/head/query/key axes. During cached one-token decoding after 8
   positions, what score and mask lengths should you expect?
4. Artificial token times after request start are 0.4, 0.5, 0.7 and 1.0 seconds;
   the response completes at 1.1 seconds. Calculate TTFT, ITLs, TPOT and E2E.
   Which metrics become undefined for a one-token response?
5. Six requests complete 12 tokens each over one 3-second shared window.
   Calculate completion throughput and request throughput. Why is averaging six
   separately calculated token rates a different statistic?
6. An allocator reports 600 MiB allocated, 900 MiB reserved, and device
   monitoring reports 1,100 MiB. Explain what can and cannot be inferred about
   leaks and whether a new 350 MiB request will succeed.

## Evidence

Retain the original attempt, calculation/code trace, cited corrections and score
by criterion. Link actual experiment records where requested. Missing evidence
stays Not started rather than becoming a hypothetical completed experiment.
