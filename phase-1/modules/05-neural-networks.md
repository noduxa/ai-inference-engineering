# Module 5: Neural-network fundamentals

Status: Not started. Estimated time: **15 hours**, including practice, review
and catch-up. Last verified: 2026-09-30.

[Curriculum](../CURRICULUM.md) · [Schedule](../SCHEDULE.md) ·
[Source pack](../notebooklm/source-packs/05-neural-networks.md)

## Why this matters

Understanding what training produces clarifies what inference must preserve and
which work it can omit.

## Learning objectives

- Explain what parameters learn in regression, classification and an MLP.
- Trace forward propagation, loss, backward propagation and an update.
- Investigate one learning-rate or regularization change under controlled
  conditions.
- Explain generalization and the work omitted during inference.

## Prerequisites

Complete the preceding module’s core shape, calculation or programming checks;
revisit any unresolved prerequisite before continuing.

## Required concepts

- Linear regression and classification
- Perceptrons and multilayer perceptrons
- Weights and biases
- Activation functions
- Forward propagation
- Loss and backpropagation
- Gradient descent and learning rate
- Batch size and epochs
- Overfitting and generalization
- Regularization
- Numerical stability
- Parameter initialization
- Training versus inference
- Why inference does not require backpropagation

## Recommended sources

- `nn-linear` —
  [Linear regression](https://d2l.ai/chapter_linear-regression/linear-regression.html)
  (primary; selected reading 1.25 h).
- `nn-classification` —
  [Softmax classification](https://d2l.ai/chapter_linear-classification/softmax-regression.html)
  (supporting; selected reading 0.5 h).
- `nn-mlp` —
  [MLPs, generalization and stable training](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html)
  (supporting; selected reading 2 h).
- `nn-loop` —
  [PyTorch optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
  (supporting; selected reading 0.5 h).

Exact page links, selected sections, exclusions, access terms and import order
are in the source pack. Reading times are selective budgets, not estimates for
completing entire documentation collections.

## Detailed explanation and worked example

Linear regression predicts a numeric target using a weighted sum and bias.
Classification predicts class scores; a perceptron applies a threshold to a
linear score, while an MLP composes affine layers with nonlinear activations.
Without nonlinearities, composing affine layers remains affine. The distinction
matters when reading a transformer's feed-forward block. See
[D2L MLPs](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html).

Consider `h=ReLU(W1 x+b1)` and `z=W2 h+b2`. With input width 3, hidden width 4,
and output width 2, parameter count is `(3*4+4)+(4*2+2)=26`. A batch of 5
produces hidden shape `(5,4)` and logits `(5,2)`. Parameter count does not grow
with batch size, but intermediate activation storage does.

The forward pass computes predictions; loss measures mismatch to targets.
Backpropagation applies the chain rule through recorded operations. Gradient
descent changes parameters using those derivatives. Learning rate sets update
scale. Batch size determines examples per update, whereas an epoch is a pass
through the training set. Equal epoch counts with different batch sizes need not
mean equal numbers of updates.

Train and validation sets serve different purposes. Falling training loss alone
does not establish generalization. In NN-02, keep a fixed split and seed and
change one factor: learning rate or weight decay. Record both losses, update
count and configuration. Weight decay discourages large weights but does not
repair data leakage. Parameter initialization breaks symmetry and controls
signal scale; unstable activations/gradients can make learning fail before a
model becomes useful. See the selected D2L generalization and initialization
readings in the source pack.

A deployed model normally holds learned parameters fixed. Prediction requires a
forward pass, but not target labels, backpropagation or an optimizer step.
Dropping saved training activations and gradient/optimizer state can reduce
memory; it does not remove model weights or every temporary buffer. Explain this
using NN-03 rather than assuming a universal training-to-inference memory ratio.

## Code-reading task and implementation mistakes

Read the official optimization loop and label parameters, activations, loss,
gradients and optimizer state. Replace its data mentally with a synthetic
numeric classification task. Explain why applying softmax before a loss that
expects logits can be wrong. Diagnose identical hidden-unit behavior after
all-zero initialization, exploding loss after an excessive learning rate, and
validation leakage. The next module reuses affine maps, nonlinearities and
normalization inside a transformer; no computer-vision survey is required.

## Study order

1. Explain linear regression and classification parameters and loss before
   training anything.
2. Build the small NN-01 models and annotate every forward and backward
   operation.
3. Study the learning-rate, batch and epoch distinctions, then change one
   setting in NN-02.
4. Interpret generalization, regularization and initialization using observed
   evidence or explicitly unresolved results.
5. Explain the forward-only path in NN-03 and defend one claim about
   generalization with appropriate limits.

## Exercises and deliverables

[Open the exercise specifications](../exercises/05-neural-networks.md).

- `NN-01` — Regression and classification.
- `NN-02` — Generalization and learning settings.
- `NN-03` — Training versus inference teach-back.

Deliver a short concept note, original calculations/code, environment record,
actual measurements where applicable, and a teach-back. Use the
[evidence template](../exercises/EVIDENCE_TEMPLATE.md). No outputs are supplied
as completed work.

## Reflection questions

- Which quantities change during a training step?
- How could a validation split expose overfitting?
- Which forward operations still behave differently in evaluation mode?

## Common mistakes to challenge

The following statements are deliberately questionable; correct them with
sources:

- Lower training loss guarantees better generalization.
- Backpropagation itself updates parameters.
- An epoch and a batch are the same unit.
- A stack of linear layers without nonlinearities adds nonlinear expressive
  power.
- Ordinary prediction requires computing parameter gradients.

## Exit test

Without NotebookLM, answer the reflection questions and explain a fresh variant
of one exercise. Then use sources to check your answer. Demonstrate a working
application, predict its outcome and diagnose one plausible failure. Record
assistance, corrections and evidence using the
[rubric](../assessments/rubric.md).

- Complete the 3 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

## Completion checklist

- [ ] Selected reading completed and source coverage checked.
- [ ] Each required concept can be recognized and explained at its stated depth.
- [ ] Exercises attempted with reproducible evidence and honest limitations.
- [ ] Exit test and teach-back reviewed; critical misconceptions corrected.
- [ ] Hardware-dependent work still pending is explicitly identified.
- [ ] Weekly review links the evidence; status changes have supporting records.

## Connection to the next module

Continue to [transformers](06-transformers.md) after the exit test.
