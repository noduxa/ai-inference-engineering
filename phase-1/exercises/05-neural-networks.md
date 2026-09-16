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

## NN-02: Generalization and learning settings

Status: Not started.

Use a fixed train/validation split and seed. Change only learning rate or weight
decay, keeping batch size, epochs and initialization documented. Cap each run at
50 epochs on a tiny dataset. Record train and validation loss without claiming
that any specific curve must appear. Explain overfitting if observed, otherwise
state why the experiment may not show it.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

## NN-03: Training versus inference teach-back

Status: Not started.

Draw the graph for one batch and mark work needed for prediction, gradient
computation and parameter updates. Explain batch size versus epoch,
initialization, regularization and why normal inference omits backward. Run the
trained module in evaluation mode without gradient tracking and verify finite
outputs.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.
