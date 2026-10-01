# Module 3 NotebookLM source pack

Status: Planned. Source inspection: Verified. NotebookLM import: To be
validated. Last verified: 2026-09-30.

[NotebookLM workflow](../README.md) ·
[Module](../../modules/03-essential-mathematics.md) ·
[Source registry](../../sources.yaml)

## Module purpose

Attention and model layers are compositions of matrix operations. Basic calculus
explains training, while probability and stability explain logits and sampling.

## Learning objectives

- Calculate small matrix products, tensor shapes, gradients and stable softmax
  values.
- Connect linear transformations and probability notation to tensor programs.
- Recognize rank, basis, orthogonality, eigenvectors and SVD without proof-heavy
  derivations.
- Explain numerical failure modes using finite-precision reasoning.

## Prerequisites

Preceding curriculum modules; review unresolved prerequisite exit tests.

## Ordered source table

Four curated source collections: one primary and three supporting. A collection
can contain several individual pages. Import **4–8 relevant pages at a time**,
not every page below at once. An index URL does not import linked chapters. Use
the session batches below and add missing sections only when needed.

| Order | Registry ID    | Source collection                                                                                                                                                | Role       | Selected reading |
| ----- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 1     | `math-prelim`  | [Dive into Deep Learning: mathematical preliminaries](https://d2l.ai/chapter_preliminaries/linear-algebra.html)                                                  | primary    | 3 h              |
| 2     | `math-mit`     | [MIT 18.06 selected linear algebra lectures](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/) | supporting | 1.5 h            |
| 3     | `math-softmax` | [Softmax regression: mathematical setup and stability](https://d2l.ai/chapter_linear-classification/softmax-regression.html)                                     | supporting | 0.75 h           |
| 4     | `math-float`   | [Floating-point arithmetic: issues and limitations](https://docs.python.org/3/tutorial/floatingpoint.html)                                                       | supporting | 0.5 h            |

## Exact sections, selection reasons and access

### math-prelim: Dive into Deep Learning: mathematical preliminaries

Expected knowledge: Calculate small tensor operations, local derivatives,
expectations and variances.

- Author/institution: Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola;
  Dive into Deep Learning.
- Format: textbook. Access: free.
- Publication/update: Online edition 1.0.3; exact page update not stated.
- Selected study time: 3 h; included in this module’s budget.
- Authority and phase fit: Researcher-authored open textbook ties notation
  directly to tensors without requiring a proof-heavy course.
- Terms: CC BY-SA 4.0 text; code under separate upstream terms.
- Import compatibility: To be validated: import individual text pages or the
  official MIT transcript PDFs; verify equations, code and source coverage
  manually.

| Exact page                                                                          | Study these sections                                       | Skip for Phase 1                                                |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- |
| [Linear algebra](https://d2l.ai/chapter_preliminaries/linear-algebra.html)          | Scalars through norms; matrix products and transposes      | Library setup and optional exercises outside the selected scope |
| [Calculus](https://d2l.ai/chapter_preliminaries/calculus.html)                      | Derivatives; partial derivatives; gradients; chain rule    | Library setup and optional exercises outside the selected scope |
| [Probability and statistics](https://d2l.ai/chapter_preliminaries/probability.html) | Random variables; distributions; expectations and variance | Library setup and optional exercises outside the selected scope |

### math-mit: MIT 18.06 selected linear algebra lectures

Expected knowledge: Recognize basis, rank, orthogonality, eigenvectors and the
purpose of SVD geometrically.

- Author/institution: Gilbert Strang; MIT OpenCourseWare.
- Format: course. Access: free.
- Publication/update: Spring 2010 course; lectures recorded Fall 1999.
- Selected study time: 1.5 h; included in this module’s budget.
- Authority and phase fit: University explanations give geometric recognition of
  basis, rank, orthogonality and decompositions; a full course is not assigned.
- Terms: MIT OCW terms; generally CC BY-NC-SA, check individual assets.
- Import compatibility: To be validated: import individual text pages or the
  official MIT transcript PDFs; verify equations, code and source coverage
  manually.

| Exact page                                                                                                                             | Study these sections                                    | Skip for Phase 1                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| [Lecture 9 transcript](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/36ad03fa0fce88a4b97f846156c11b8b_yjBerM5jWsc.pdf)  | PDF pp. 1–8: independence, basis, dimension and rank    | Full lectures and proofs; use first explanatory segment or transcript only |
| [Lecture 15 transcript](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/96a31504ec5d489d84113320b593eb0d_Y_Ac6KiQ1t0.pdf) | PDF pp. 1–3: orthogonality and projection geometry      | Full lectures and proofs; use first explanatory segment or transcript only |
| [Lecture 21 transcript](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/8d0f7baefcedee6596eaab43c55122fe_cdZnhQjJu4I.pdf) | PDF pp. 1–3: eigenvector direction and eigenvalue scale | Full lectures and proofs; use first explanatory segment or transcript only |
| [Lecture 29 transcript](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/0f4d618b79d74403afcbaef310117f03_TX_vooSnhm8.pdf) | PDF pp. 1–3: SVD factors and geometric interpretation   | Full lectures and proofs; use first explanatory segment or transcript only |

### math-softmax: Softmax regression: mathematical setup and stability

Expected knowledge: Connect logits, exponentials and log-likelihood and explain
stable softmax evaluation.

- Author/institution: Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola;
  Dive into Deep Learning.
- Format: textbook. Access: free.
- Publication/update: Online edition 1.0.3; exact page update not stated.
- Selected study time: 0.75 h; included in this module’s budget.
- Authority and phase fit: Connects exponentials, logarithms and normalized
  class scores to later attention and generation.
- Terms: CC BY-SA 4.0 text; separate code terms.
- Import compatibility: To be validated: import individual text pages or the
  official MIT transcript PDFs; verify equations, code and source coverage
  manually.

| Exact page                                                                                      | Study these sections                       | Skip for Phase 1                    |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------- |
| [Softmax regression](https://d2l.ai/chapter_linear-classification/softmax-regression.html)      | Classification, softmax and log-likelihood | Dataset and training implementation |
| [Concise softmax](https://d2l.ai/chapter_linear-classification/softmax-regression-concise.html) | Softmax numerical stability                | Framework training exercise         |

### math-float: Floating-point arithmetic: issues and limitations

Expected knowledge: Explain representation error and use tolerance-based
numerical comparisons.

- Author/institution: Python documentation contributors; Python Software
  Foundation.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Sep 30, 2026 (17:37 UTC);
  see section-level dates in the registry where available.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Provides practical numerical limits and comparison
  tools without additional mathematical machinery.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages or the
  official MIT transcript PDFs; verify equations, code and source coverage
  manually.

| Exact page                                                              | Study these sections                                  | Skip for Phase 1                                        |
| ----------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------- |
| [Floating point](https://docs.python.org/3/tutorial/floatingpoint.html) | Representation error; comparisons; accurate summation | Detailed binary derivation after the practical examples |

## Optional visual lane and overlap decisions

Optionally watch the selected MIT lecture segments instead of reading their
transcripts within the same time budget. D2L carries the calculations; MIT
supplies geometric recognition, not a second full mathematics course.

No additional secondary blog is selected: the first-party diagrams and textbook
explanations cover the visual need without another overlapping source.

## Notebook name and adding sources

Suggested name: **Joshua — Phase 1 — 03 Essential mathematics**.

Add pages in the source-table order within the current session batch. Name each
import with its registry ID and section title. Check that the actual page text,
code and equations appear before asking questions. Retain at most eight active
pages; rotate earlier pages out after saving your own cited notes. Re-add an
omitted page if a prompt needs it. Do not use an index as a substitute for
content.

## Session import batches

- **Calculation foundation:** Linear algebra; Calculus; Probability and
  statistics; Softmax regression; Concise softmax; Floating point.
- **Geometric recognition:** The four MIT transcript PDFs; Linear algebra.
  Rotate out unrelated calculus pages..

## Initial NotebookLM questions

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

- Which dimension is contracted in a matrix product?
- How does the chain rule connect a loss to a weight?
- Why can shifting logits help compute softmax?

## Audio Overview customization prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Give a short spoken orientation to essential mathematics for a backend engineer.
Use one concrete example from the selected pages, explain why it matters to
later inference study, and challenge one misconception below. Name sources aloud
and end with three questions to answer without replaying the overview. Avoid
advanced serving topics and performance promises. Listening is preparation, not
completion.

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

- A matrix product is commutative.
- A gradient is a scalar for every function.
- A large logit is already a probability.
- Floating-point addition is exactly associative.
- Knowing the definition of SVD means being able to derive it.

## Practical exercise

Start with `MA-01` in the
[module exercise specifications](../../exercises/03-essential-mathematics.md),
then complete the remaining exercises. Ask for a plan critique before executing;
never ask the model to fabricate an observation or to silently fill in missing
measurements.

## Required learning evidence

- Own-word explanation with inspected source citations.
- Exercise code/calculations and explicit correctness checks.
- Environment record, actual observations, failed attempts and limitations.
- Prediction-versus-result comparison and a reviewed teach-back.

## Exit criteria

- Complete the 5 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

Use the [assessment rubric](../../assessments/rubric.md); neither imported
sources nor generated study artifacts establish mastery.

## What to study next

Continue to [Module 4](../../modules/04-pytorch-fundamentals.md) after the exit
check.

## Comparison prompt

Using only the imported sources, compare their scope, definitions and
assumptions. Cite the section behind each important claim, distinguish inference
from source statements, identify real disagreements and say when coverage is
insufficient. Do not invent a conflict between complementary sources.

## Teach-back prompt

Evaluate my explanation before rewriting it: correct statements, incomplete
statements, misconceptions, unsupported claims, missing connections and
questions I should answer next. Cite source sections and ask me to revise first.
An Audio Overview is preparation, not evidence of understanding.

## Experiment-preparation prompt

Check my linked exercise plan against the supplied sources. Identify controls,
changed variable, observations, resource bounds and missing prerequisites.
Require my prediction before execution; never invent an observed result.

## Measurement-interpretation prompt

Use the [shared measurement-review prompt](../prompts/measurement-review.md).
Check the exercise's actual shapes, units, timing/memory boundaries and
correctness. State what the supplied observations cannot establish and ask for
one next test.
