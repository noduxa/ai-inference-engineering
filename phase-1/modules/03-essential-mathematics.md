# Module 3: Essential mathematics

Status: Not started. Estimated time: **15 hours**, including practice, review
and catch-up. Last verified: 2026-09-16.

[Curriculum](../CURRICULUM.md) · [Schedule](../SCHEDULE.md) ·
[Source pack](../notebooklm/source-packs/03-essential-mathematics.md)

## Why this matters

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

Complete the preceding module’s core shape, calculation or programming checks;
revisit any unresolved prerequisite before continuing.

## Required concepts

- Scalars, vectors, matrices and tensors
- Dimensions and shapes
- Dot products and matrix multiplication
- Transposes and linear transformations
- Vector norms
- Rank, basis and orthogonality
- Eigenvalues and eigenvectors: introductory recognition
- Singular value decomposition (SVD): introductory recognition
- Functions, exponentials and logarithms
- Derivatives, partial derivatives and gradients
- Chain rule
- Softmax
- Basic probability, random variables and probability distributions
- Expected value and variance
- Basic numerical stability

## Recommended sources

- `math-prelim` —
  [Dive into Deep Learning: mathematical preliminaries](https://d2l.ai/chapter_preliminaries/linear-algebra.html)
  (primary; selected reading 3 h).
- `math-mit` —
  [MIT 18.06 selected linear algebra lectures](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/)
  (supporting; selected reading 1.5 h).
- `math-softmax` —
  [Softmax regression: mathematical setup and stability](https://d2l.ai/chapter_linear-classification/softmax-regression.html)
  (supporting; selected reading 0.75 h).
- `math-float` —
  [Floating-point arithmetic: issues and limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
  (supporting; selected reading 0.5 h).

Exact page links, selected sections, exclusions, access terms and import order
are in the source pack. Reading times are selective budgets, not estimates for
completing entire documentation collections.

## Study order

1. Calculate scalar/vector/matrix operations and annotate tensor dimensions in
   MA-01/MA-02.
2. Use selected MIT transcript segments to recognize geometric vocabulary; do
   not work through the full course.
3. Connect functions and local derivatives to the chain-rule calculation in
   MA-04.
4. Study finite probability, exponentials and logarithms before softmax and
   stability in MA-03/MA-05.
5. Take a fresh calculation check; use the curriculum depth contract to avoid
   unnecessary proofs.

## Exercises and deliverables

[Open the exercise specifications](../exercises/03-essential-mathematics.md).

- `MA-01` — Matrix multiplication.
- `MA-02` — Tensor shapes.
- `MA-03` — Softmax.
- `MA-04` — Gradient and chain rule.
- `MA-05` — Numerical stability and probability.

Deliver a short concept note, original calculations/code, environment record,
actual measurements where applicable, and a teach-back. Use the
[evidence template](../exercises/EVIDENCE_TEMPLATE.md). No outputs are supplied
as completed work.

## Reflection questions

- Which dimension is contracted in a matrix product?
- How does the chain rule connect a loss to a weight?
- Why can shifting logits help compute softmax?

## Common mistakes to challenge

The following statements are deliberately questionable; correct them with
sources:

- A matrix product is commutative.
- A gradient is a scalar for every function.
- A large logit is already a probability.
- Floating-point addition is exactly associative.
- Knowing the definition of SVD means being able to derive it.

## Exit test

Without NotebookLM, answer the reflection questions and explain a fresh variant
of one exercise. Then use sources to check your answer. Demonstrate a working
application, predict its outcome and diagnose one plausible failure. Record
assistance, corrections and evidence using the
[rubric](../assessments/rubric.md).

- Complete the 5 exercise specifications or explicitly record hardware-limited
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
