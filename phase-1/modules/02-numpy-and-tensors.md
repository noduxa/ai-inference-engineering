# Module 2: NumPy, tensors and numerical computing

Status: Not started. Estimated time: **10 hours**, including practice, review
and catch-up. Last verified: 2026-09-30.

[Curriculum](../CURRICULUM.md) · [Schedule](../SCHEDULE.md) ·
[Source pack](../notebooklm/source-packs/02-numpy-and-tensors.md)

## Why this matters

Inference tensors have shape and storage constraints. A numerically correct
expression can still create an unexpectedly large temporary array.

## Learning objectives

- Predict result shapes before executing array operations.
- Explain aliasing and layout using strides, views and contiguous storage.
- Estimate payload bytes and compare dtypes without assuming equal numerical
  behaviour.
- Measure a controlled loop/vectorized comparison and discuss temporary
  allocations.

## Prerequisites

Complete the preceding module’s core shape, calculation or programming checks;
revisit any unresolved prerequisite before continuing.

## Required concepts

- NumPy arrays
- Dimensions, axes and shapes
- Shape transformations
- Data types and data-type size
- Indexing and slicing
- Copies versus views
- Broadcasting
- Vectorization
- Element-wise operations
- Dot products and matrix multiplication
- Reductions
- Strides
- Contiguous and non-contiguous data
- CPU memory consumption
- Numerical precision and floating-point limitations
- Comparing Python loops with vectorized operations

## Recommended sources

- `np-quickstart` —
  [NumPy quickstart and ndarray storage](https://numpy.org/doc/stable/user/quickstart.html)
  (primary; selected reading 1.25 h).
- `np-broadcast` —
  [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
  (supporting; selected reading 0.5 h).
- `np-views` —
  [Copies and views](https://numpy.org/doc/stable/user/basics.copies.html)
  (supporting; selected reading 0.5 h).
- `np-types` — [Data types](https://numpy.org/doc/stable/user/basics.types.html)
  (supporting; selected reading 0.5 h).

Exact page links, selected sections, exclusions, access terms and import order
are in the source pack. Reading times are selective budgets, not estimates for
completing entire documentation collections.

## Detailed explanation and worked example

An ndarray combines storage with metadata: dtype, shape, byte strides and an
offset. Shape describes logical axes; strides tell how far to move in storage.
For a contiguous float32 array shaped `(2, 3)`, ordinary C-order strides are
`(12, 4)` bytes. Its transpose has shape `(3, 2)` and strides `(4, 12)` without
necessarily copying storage. A downstream operation may still need a contiguous
copy. See [ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html).

```python
import numpy as np
x = np.arange(6, dtype=np.float32).reshape(2, 3)
y = x.T
assert np.shares_memory(x, y)
z = y.copy()
assert not np.shares_memory(x, z)
```

This is a worked prediction to verify. Basic slicing usually produces views;
advanced indexing produces copies. Reshape may copy if the layout cannot express
the requested view. `nbytes` counts logical element payload, not process RSS or
unique ownership. A tiny slice can keep a large backing allocation alive.

Broadcasting aligns axes from the right. Two dimensions are compatible when
equal or one is 1. Thus `(3,1)+(1,4)` yields `(3,4)`, but `(2,3)+(2,)` fails.
Broadcasting avoids physically tiling the inputs; the output and intermediates
can still be large. See the
[broadcasting rules](https://numpy.org/doc/stable/user/basics.broadcasting.html)
.

Matrix multiplication contracts the inner dimension: `(m,k)@(k,n)` yields
`(m,n)`. Batched leading dimensions broadcast. Element-wise multiplication does
not contract an axis. A reduction removes an axis unless `keepdims=True`, which
can make the intended subsequent broadcast explicit.

For `(1024,1024)` float32, payload is `1024*1024*4 = 4 MiB`; float64 doubles it.
This calculation excludes container metadata and temporary results. Smaller
dtypes change range and precision. Integer overflow and floating-point rounding
are different failure modes. Use tolerances justified by dtype and scale, not
exact equality for every floating-point computation.

Vectorization moves repeated operations from Python dispatch into array kernels.
It is not a guarantee of lower latency: small arrays, temporary allocations,
layout conversion and native-library thread startup can dominate. In NP-01,
compare an identical formula and report conversion separately. In NP-03, time a
transpose-consuming operation with and without an explicit contiguous copy;
include the copy in an end-to-end comparison and verify equal results.

## Code-reading task and implementation mistakes

Trace `x.mean(axis=1, keepdims=True)` into its shape contract, then explain
`x - x.mean(axis=1, keepdims=True)` before execution. Inspect the installed
NumPy wrapper source when available and identify where native execution begins;
do not infer Python-level loop counts from a native call. Watch for wrong axes,
accidental float64 promotion, hidden copies and measuring allocation in only one
comparison arm. Connect these errors to the tensor layouts in Module 3.

## Study order

1. Create arrays and annotate dimensions, axes, dtype and payload bytes.
2. Predict reshape, indexing and matrix-product results before executing
   NP-04/NP-05.
3. Apply broadcasting rules in NP-02, then inspect copies, views, strides and
   contiguity in NP-03.
4. Compare a loop with a vectorized operation in NP-01 under controlled timing
   boundaries.
5. Explain a numerical limitation and diagnose one shape or aliasing error
   without generated help.

## Exercises and deliverables

[Open the exercise specifications](../exercises/02-numpy-and-tensors.md).

- `NP-01` — Loop versus vectorized operation.
- `NP-02` — Broadcasting.
- `NP-03` — Copy versus view.
- `NP-04` — Dtype memory comparison.
- `NP-05` — Matrix shapes.

Deliver a short concept note, original calculations/code, environment record,
actual measurements where applicable, and a teach-back. Use the
[evidence template](../exercises/EVIDENCE_TEMPLATE.md). No outputs are supplied
as completed work.

## Reflection questions

- Which dimensions align during broadcasting?
- How can a transposed array share storage but have different strides?
- What memory does your estimate deliberately omit?

## Common mistakes to challenge

The following statements are deliberately questionable; correct them with
sources:

- A reshape always copies.
- Broadcasting always materializes expanded inputs.
- Element-wise multiplication and matrix multiplication are equivalent.
- A view owns independent data.
- nbytes includes every allocation and object overhead.

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

## Connection to the next module

Continue to [essential mathematics](03-essential-mathematics.md) after the exit
test.
