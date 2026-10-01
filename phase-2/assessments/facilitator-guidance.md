# Facilitator guidance — separate from learner questions

[Assessment index](README.md) · [Rubric](rubric.md)

Status: Planned. Use after the first independent attempt.

## Calculation checks

For question 1, ideal weight payloads are 3,000,000,000; 1,500,000,000; and
375,000,000 bytes. Divide by 2^30 for GiB; require runtime-overhead caveats. For
question 2, the homogeneous K/V payload is 9,437,184 bytes (9 MiB). Doubling
length doubles it; doubling only query heads does not change this formula when
KV heads/head width remain fixed. Unequal lengths use their sum. For question 3,
one new query after eight cached positions attends over nine keys; head
dimensions and mask broadcasting depend on the API contract. Question 4: TTFT
0.4 s, ITLs 0.1/0.2/0.3 s, TPOT 0.2 s, E2E 1.1 s. Question 5: 24 output tokens/s
and 2 requests/s over the common window. These are answer guidance for
artificial questions, not benchmark observations.

## Reasoning checks

A correct cached loop passes only unprocessed tokens and maintains the combined
attention-mask/position contract. It does not repeatedly append an
already-cached prefix. Eval mode, gradient mode, EOS/length behavior and
buffering are distinct. Require a distinction between model-side and client-side
latency.

Reserved-minus-allocated memory is not proof of a leak or guaranteed capacity
for a new allocation. Inspect live state, overhead and fragmentation. A smaller
representation needs supported efficient kernels to improve speed; accuracy is
not established by similar-looking text. Higher concurrency can improve
aggregate work rate while increasing queueing and tail latency.

For diagnostics, reward a falsifiable intervention and controlled comparison,
not selecting a familiar bottleneck name. Check that the actual raw record
supports the conclusion and includes failures. Ask for one alternative mechanism
and an observation that would distinguish it. Never certify GPU evidence from
CPU-only tests, or learner mastery from repository implementation checks.
