# Module 5 NotebookLM source pack

Status: Planned. Source inspection: Verified. NotebookLM import: To be
validated. Last verified: 2026-09-16.

[NotebookLM workflow](../README.md) ·
[Module](../../modules/05-neural-networks.md) ·
[Source registry](../../sources.yaml)

## Module purpose

Understanding what training produces clarifies what inference must preserve and
which work it can omit.

## Learning objectives

- Explain what parameters learn in regression, classification and an MLP.
- Trace forward propagation, loss, backward propagation and an update.
- Investigate one learning-rate or regularization change under controlled
  conditions.
- Explain generalization and the work omitted during inference.

## Prerequisites

Preceding curriculum modules; review unresolved prerequisite exit tests.

## Ordered source table

Four curated source collections: one primary and three supporting. A collection
can contain several individual pages. Import **4–8 relevant pages at a time**,
not every page below at once. An index URL does not import linked chapters. Use
the session batches below and add missing sections only when needed.

| Order | Registry ID         | Source collection                                                                                          | Role       | Selected reading |
| ----- | ------------------- | ---------------------------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 1     | `nn-linear`         | [Linear regression](https://d2l.ai/chapter_linear-regression/linear-regression.html)                       | primary    | 1.25 h           |
| 2     | `nn-classification` | [Softmax classification](https://d2l.ai/chapter_linear-classification/softmax-regression.html)             | supporting | 0.5 h            |
| 3     | `nn-mlp`            | [MLPs, generalization and stable training](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html)         | supporting | 2 h              |
| 4     | `nn-loop`           | [PyTorch optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | supporting | 0.5 h            |

## Exact sections, selection reasons and access

### nn-linear: Linear regression

Expected knowledge: Explain regression parameters, squared loss and a minibatch
parameter update.

- Author/institution: Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola;
  Dive into Deep Learning.
- Format: textbook. Access: free.
- Publication/update: Online edition 1.0.3; exact page update not stated.
- Selected study time: 1.25 h; included in this module’s budget.
- Authority and phase fit: A small model makes the relationship between
  parameters, loss and gradient updates explicit.
- Terms: CC BY-SA 4.0 text; separate code terms.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                           | Study these sections                                               | Skip for Phase 1                                    |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | --------------------------------------------------- |
| [Linear regression](https://d2l.ai/chapter_linear-regression/linear-regression.html) | Model, loss, minibatch stochastic gradient descent and predictions | Historical notes and full framework implementations |

### nn-classification: Softmax classification

Expected knowledge: Explain classification scores, probabilities and
cross-entropy loss.

- Author/institution: Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola;
  Dive into Deep Learning.
- Format: textbook. Access: free.
- Publication/update: Online edition 1.0.3; exact page update not stated.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Reuses the mathematical source for the new purpose of
  classification and cross-entropy; prior reading is not repeated.
- Terms: CC BY-SA 4.0 text; separate code terms.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                 | Study these sections                        | Skip for Phase 1                              |
| ------------------------------------------------------------------------------------------ | ------------------------------------------- | --------------------------------------------- |
| [Softmax regression](https://d2l.ai/chapter_linear-classification/softmax-regression.html) | Classification and cross-entropy connection | Repeat derivation already studied in Module 3 |

### nn-mlp: MLPs, generalization and stable training

Expected knowledge: Trace an MLP graph and explain activation, generalization,
regularization and initialization.

- Author/institution: Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola;
  Dive into Deep Learning.
- Format: textbook. Access: free.
- Publication/update: Online edition 1.0.3; exact page update not stated.
- Selected study time: 2 h; included in this module’s budget.
- Authority and phase fit: Explains the minimum network concepts needed to
  understand inference inputs and learned parameters.
- Terms: CC BY-SA 4.0 text; separate code terms.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                                                | Study these sections                                             | Skip for Phase 1                                             |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ |
| [Multilayer perceptrons](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html)                                          | Hidden layers; activation functions; linear and nonlinear models | Proofs, broad architecture surveys and lengthy training runs |
| [Generalization](https://d2l.ai/chapter_linear-regression/generalization.html)                                            | Overfitting; model complexity; train/validation separation       | Proofs, broad architecture surveys and lengthy training runs |
| [Weight decay](https://d2l.ai/chapter_linear-regression/weight-decay.html)                                                | L2 regularization concept                                        | Proofs, broad architecture surveys and lengthy training runs |
| [Forward and backward propagation](https://d2l.ai/chapter_multilayer-perceptrons/backprop.html)                           | Forward graph; backward chain rule; intermediate storage         | Proofs, broad architecture surveys and lengthy training runs |
| [Numerical stability and initialization](https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html) | Vanishing/exploding gradients and initialization                 | Proofs, broad architecture surveys and lengthy training runs |

### nn-loop: PyTorch optimization loop

Expected knowledge: Identify each training-loop operation and distinguish it
from forward-only evaluation.

- Author/institution: PyTorch tutorial contributors; PyTorch.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Jul 31, 2026; see
  section-level dates in the registry where available.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Connects the textbook training concepts to a short
  inspectable loop; only the loop is revisited.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                         | Study these sections                                   | Skip for Phase 1                           |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------ |
| [Optimization loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | Hyperparameters; loss; optimizer; train and test loops | FashionMNIST and computer-vision expansion |

## Optional visual lane and overlap decisions

Use the MLP and forward/backward graph figures from D2L. Reuse the Module 3
softmax and Module 4 loop sources; do not repeat the entire lessons.

No additional secondary blog is selected: the first-party diagrams and textbook
explanations cover the visual need without another overlapping source.

## Notebook name and adding sources

Suggested name: **Joshua — Phase 1 — 05 Neural-network fundamentals**.

Add pages in the source-table order within the current session batch. Name each
import with its registry ID and section title. Check that the actual page text,
code and equations appear before asking questions. Retain at most eight active
pages; rotate earlier pages out after saving your own cited notes. Re-add an
omitted page if a prompt needs it. Do not use an index as a substitute for
content.

## Session import batches

- **Small models and generalization:** Linear regression; Softmax regression;
  Multilayer perceptrons; Generalization; Weight decay; Forward and backward
  propagation; Numerical stability and initialization; Optimization loop.

## Initial NotebookLM questions

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

- Which quantities change during a training step?
- How could a validation split expose overfitting?
- Which forward operations still behave differently in evaluation mode?

## Audio Overview customization prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Give a short spoken orientation to neural-network fundamentals for a backend
engineer. Use one concrete example from the selected pages, explain why it
matters to later inference study, and challenge one misconception below. Name
sources aloud and end with three questions to answer without replaying the
overview. Avoid advanced serving topics and performance promises. Listening is
preparation, not completion.

## Study-guide generation prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Organize this module around its learning objectives. For each, show the exact
source section, a prerequisite, a small application question and an evidence
check. Mark recognition-only topics and exclude the listed skip sections. Flag
objectives that the currently imported batch cannot support before attempting to
explain them.

## Flashcard-generation prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Make ten cards: four concept distinctions, three shape or code predictions and
three error-diagnosis prompts. Put questions first and source-backed answers in
a separate section. Include assumptions and one counterexample per tricky
concept. Do not reduce the deck to vocabulary definitions.

## Quiz-generation prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Ask six questions progressing from recognition through explanation to
application and early diagnosis. Use fresh tiny inputs, not copied worked
examples. Withhold answers until I submit mine. Then score reasoning, identify
the source for each correction and give one targeted retry. Do not infer
practical completion from a correct multiple-choice answer.

## Common misconceptions to test

These are deliberately questionable claims to correct, not facts to memorize.

- Lower training loss guarantees better generalization.
- Backpropagation itself updates parameters.
- An epoch and a batch are the same unit.
- A stack of linear layers without nonlinearities adds nonlinear expressive
  power.
- Ordinary prediction requires computing parameter gradients.

## Practical exercise

Start with `NN-01` in the
[module exercise specifications](../../exercises/05-neural-networks.md), then
complete the remaining exercises. Ask for a plan critique before executing;
never ask the model to fabricate an observation or to silently fill in missing
measurements.

## Required learning evidence

- Own-word explanation with inspected source citations.
- Exercise code/calculations and explicit correctness checks.
- Environment record, actual observations, failed attempts and limitations.
- Prediction-versus-result comparison and a reviewed teach-back.

## Exit criteria

- Complete the 3 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

Use the [assessment rubric](../../assessments/rubric.md); neither imported
sources nor generated study artifacts establish mastery.

## What to study next

Continue to [Module 6](../../modules/06-transformers.md) after the exit check.
