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

### NP-01 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** conversion and operation times separately, dtype,
  shape, equality.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## NP-02: Broadcasting

Status: Not started.

Predict success and result shape for (3,1)+(1,4), (2,3)+(3,), and (2,3)+(2,).
Draw aligned axes before running. Add a shape assertion and explain why an
invalid pair fails.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### NP-02 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** predicted/actual shapes and captured ValueError for
  invalid case.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## NP-03: Copy versus view

Status: Not started.

Slice and transpose an array, mutate one element, and inspect the original.
Compare with copy() and advanced indexing. Record strides, flags, base/sharing
checks and the difference between shared bytes and equal values.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### NP-03 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** strides, contiguity, memory-sharing, mutation
  results and copy cost.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## NP-04: Dtype memory comparison

Status: Not started.

Construct the same bounded shape using float64, float32, float16 and int8.
Predict nbytes from shape and itemsize; compare observed payload bytes. Include
a representability/overflow example and explain why smaller storage does not
prove numerical suitability.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### NP-04 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** shape, itemsize, nbytes and representability error.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## NP-05: Matrix shapes

Status: Not started.

Predict outputs for (2,3)@(3,4) and batched (5,2,3)@(5,3,4). Explain a failing
(2,3)@(2,4). Compare @ with element-wise \* and include a reduction with and
without keepdims.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### NP-05 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** input/output shapes, axis reductions and
  correctness.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.
