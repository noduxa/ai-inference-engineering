# Module 2 exercise specifications

Status: Not started. These are specifications, not completed experiments.

[Module guide](../modules/02-numpy-and-tensors.md) ·
[Source pack](../notebooklm/source-packs/02-numpy-and-tensors.md) ·
[Evidence template](EVIDENCE_TEMPLATE.md)

## Execution contract

Use public or synthetic inputs, an isolated environment and bounded resources.
Write your prediction before execution. Record exact versions, configuration,
checks, observations, failures and cleanup. Expected effects are **hypotheses**;
no timings, memory results or successful runs are asserted here. Each exercise
must include a correctness check before any performance claim.

## NP-01: Loop versus vectorized operation

Status: Not started.

Apply the same arithmetic transformation to a bounded numeric list and ndarray.
Check outputs before timing. Separate conversion from operation timing, repeat
measurements and record shape, dtype and environment. Treat any speed difference
as a hypothesis until measured.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

## NP-02: Broadcasting

Status: Not started.

Predict success and result shape for (3,1)+(1,4), (2,3)+(3,), and (2,3)+(2,).
Draw aligned axes before running. Add a shape assertion and explain why an
invalid pair fails.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

## NP-03: Copy versus view

Status: Not started.

Slice and transpose an array, mutate one element, and inspect the original.
Compare with copy() and advanced indexing. Record strides, flags, base/sharing
checks and the difference between shared bytes and equal values.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

## NP-04: Dtype memory comparison

Status: Not started.

Construct the same bounded shape using float64, float32, float16 and int8.
Predict nbytes from shape and itemsize; compare observed payload bytes. Include
a representability/overflow example and explain why smaller storage does not
prove numerical suitability.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

## NP-05: Matrix shapes

Status: Not started.

Predict outputs for (2,3)@(3,4) and batched (5,2,3)@(5,3,4). Explain a failing
(2,3)@(2,4). Compare @ with element-wise \* and include a reduction with and
without keepdims.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.
