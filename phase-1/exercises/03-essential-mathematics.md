# Module 3 exercise specifications

Status: Not started. These are specifications, not completed experiments.

[Module guide](../modules/03-essential-mathematics.md) ·
[Source pack](../notebooklm/source-packs/03-essential-mathematics.md) ·
[Evidence template](EVIDENCE_TEMPLATE.md)

## Execution contract

Use public or synthetic inputs, an isolated environment and bounded resources.
Write your prediction before execution. Record exact versions, configuration,
checks, observations, failures and cleanup. Expected effects are **hypotheses**;
no timings, memory results or successful runs are asserted here. Each exercise
must include a correctness check before any performance claim.

## MA-01: Matrix multiplication

Status: Not started.

Calculate [[1,2],[3,4]] @ [[2,0],[1,2]] by hand. Annotate rows, columns and
contracted dimension. Calculate a transpose and a vector norm; only then verify
with NumPy.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### MA-01 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** hand products and checked outputs.
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

## MA-02: Tensor shapes

Status: Not started.

Trace a batch (2,3,4) multiplied by a feature projection (4,5). State output
shape, element count and FP32 payload estimate. Draw a basis and identify a
dependent pair of vectors.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### MA-02 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** axis labels and contracted dimensions.
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

## MA-03: Softmax

Status: Not started.

Calculate softmax([0,1,2]) with intermediate exponentials and denominator, then
repeat after adding a common constant. Explain what remains invariant and why
outputs sum to one.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### MA-03 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** logits, shifted exponentials and probability sum.
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

## MA-04: Gradient and chain rule

Status: Not started.

For L=(w\*x+b-y)^2 with x=2, y=1, w=0.5, b=1, calculate partial derivatives with
respect to w and b. Show the chain of local derivatives, then check with a small
finite difference.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### MA-04 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** analytic derivative and finite-difference error at
  two step sizes.
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

## MA-05: Numerical stability and probability

Status: Not started.

Compare naive and shifted softmax for [1000,1001,1002] using a controlled
floating-point type. Predict overflow before execution. For a random variable
taking values 0 and 2 with equal probability, calculate expectation and
variance. Explain the distinction between a mathematical formula and its
numerical implementation.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### MA-05 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** finite/non-finite outputs, expectation and
  variance.
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
