# Module 5 exercise specifications

Status: Not started. These are specifications, not completed experiments.

[Module guide](../modules/05-neural-networks.md) ·
[Source pack](../notebooklm/source-packs/05-neural-networks.md) ·
[Evidence template](EVIDENCE_TEMPLATE.md)

## Execution contract

Use public or synthetic inputs, an isolated environment and bounded resources.
Write your prediction before execution. Record exact versions, configuration,
checks, observations, failures and cleanup. Expected effects are **hypotheses**;
no timings, memory results or successful runs are asserted here. Each exercise
must include a correctness check before any performance claim.

## NN-01: Regression and classification

Status: Not started.

Reuse a synthetic Dataset. Fit a tiny linear regression model, then a two-class
MLP with one hidden layer. Annotate weights, biases, activation, forward pass,
loss, backward pass and optimizer step. Compare a single perceptron-style
threshold unit conceptually with the smooth trainable model; no vision dataset
is required.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### NN-01 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** train/validation losses, split, seed and parameter
  count.
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

## NN-02: Generalization and learning settings

Status: Not started.

Use a fixed train/validation split and seed. Change only learning rate or weight
decay, keeping batch size, epochs and initialization documented. Cap each run at
50 epochs on a tiny dataset. Record train and validation loss without claiming
that any specific curve must appear. Explain overfitting if observed, otherwise
state why the experiment may not show it.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### NN-02 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** one-variable learning curves and update counts.
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

## NN-03: Training versus inference teach-back

Status: Not started.

Draw the graph for one batch and mark work needed for prediction, gradient
computation and parameter updates. Explain batch size versus epoch,
initialization, regularization and why normal inference omits backward. Run the
trained module in evaluation mode without gradient tracking and verify finite
outputs.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### NN-03 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** retained state inventory and unchanged inference
  weights.
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
