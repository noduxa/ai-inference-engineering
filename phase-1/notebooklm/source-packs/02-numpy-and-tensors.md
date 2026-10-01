# Module 2 NotebookLM source pack

Status: Planned. Source inspection: Verified. NotebookLM import: To be
validated. Last verified: 2026-09-30.

[NotebookLM workflow](../README.md) ·
[Module](../../modules/02-numpy-and-tensors.md) ·
[Source registry](../../sources.yaml)

## Module purpose

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

Preceding curriculum modules; review unresolved prerequisite exit tests.

## Ordered source table

Four curated source collections: one primary and three supporting. A collection
can contain several individual pages. Import **4–8 relevant pages at a time**,
not every page below at once. An index URL does not import linked chapters. Use
the session batches below and add missing sections only when needed.

| Order | Registry ID     | Source collection                                                                         | Role       | Selected reading |
| ----- | --------------- | ----------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 1     | `np-quickstart` | [NumPy quickstart and ndarray storage](https://numpy.org/doc/stable/user/quickstart.html) | primary    | 1.25 h           |
| 2     | `np-broadcast`  | [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)                | supporting | 0.5 h            |
| 3     | `np-views`      | [Copies and views](https://numpy.org/doc/stable/user/basics.copies.html)                  | supporting | 0.5 h            |
| 4     | `np-types`      | [Data types](https://numpy.org/doc/stable/user/basics.types.html)                         | supporting | 0.5 h            |

## Exact sections, selection reasons and access

### np-quickstart: NumPy quickstart and ndarray storage

Expected knowledge: Predict shapes and storage layout and use reductions,
products and transformations deliberately.

- Author/institution: NumPy developers; NumPy.
- Format: documentation. Access: free.
- Publication/update: Not stated; rolling documentation.
- Selected study time: 1.25 h; included in this module’s budget.
- Authority and phase fit: Official array operations plus storage reference
  connect shapes to actual bytes.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                        | Study these sections                                                        | Skip for Phase 1                      |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------- |
| [Quickstart](https://numpy.org/doc/stable/user/quickstart.html)                   | Basics; basic operations; universal functions; indexing; shape manipulation | Stacking helpers beyond the exercises |
| [N-dimensional array](https://numpy.org/doc/stable/reference/arrays.ndarray.html) | Constructing arrays; internal memory layout; attributes; array methods      | C API and subclassing                 |

### np-broadcast: Broadcasting

Expected knowledge: Align trailing axes, detect incompatible shapes and
anticipate large intermediates.

- Author/institution: NumPy developers; NumPy.
- Format: documentation. Access: free.
- Publication/update: Not stated; rolling documentation.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Authoritative broadcasting rules and memory cautions
  support shape prediction.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                 | Study these sections                                    | Skip for Phase 1               |
| -------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------ |
| [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) | General broadcasting rules and memory-inefficient cases | Large domain-specific examples |

### np-views: Copies and views

Expected knowledge: Distinguish shared storage from copied storage and diagnose
mutation through aliases.

- Author/institution: NumPy developers; NumPy.
- Format: documentation. Access: free.
- Publication/update: Not stated; rolling documentation.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Explains aliasing and reshape behaviour needed to
  diagnose accidental mutation.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                               | Study these sections                      | Skip for Phase 1        |
| ------------------------------------------------------------------------ | ----------------------------------------- | ----------------------- |
| [Copies and views](https://numpy.org/doc/stable/user/basics.copies.html) | View, copy, indexing and other operations | None in this short page |

### np-types: Data types

Expected knowledge: Calculate payload bytes and explain overflow and precision
limits of fixed-width types.

- Author/institution: NumPy developers; NumPy.
- Format: documentation. Access: free.
- Publication/update: Not stated; rolling documentation.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Explains fixed-width numeric storage and overflow
  rather than treating Python numbers and arrays as interchangeable.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                        | Study these sections                                        | Skip for Phase 1                   |
| ----------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------- |
| [Data types](https://numpy.org/doc/stable/user/basics.types.html) | Array types; fixed-size types; overflow; extended precision | String and structured data details |

## Optional visual lane and overlap decisions

Use the official broadcasting diagrams as the optional visual explanation. The
quickstart introduces arrays; the dedicated broadcasting and views pages take
precedence for edge cases.

No additional secondary blog is selected: the first-party diagrams and textbook
explanations cover the visual need without another overlapping source.

## Notebook name and adding sources

Suggested name: **Joshua — Phase 1 — 02 NumPy, tensors and numerical
computing**.

Add pages in the source-table order within the current session batch. Name each
import with its registry ID and section title. Check that the actual page text,
code and equations appear before asking questions. Retain at most eight active
pages; rotate earlier pages out after saving your own cited notes. Re-add an
omitted page if a prompt needs it. Do not use an index as a substitute for
content.

## Session import batches

- **Array operations and storage:** Quickstart; N-dimensional array;
  Broadcasting; Copies and views; Data types.

## Initial NotebookLM questions

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

- Which dimensions align during broadcasting?
- How can a transposed array share storage but have different strides?
- What memory does your estimate deliberately omit?

## Audio Overview customization prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Give a short spoken orientation to numpy, tensors and numerical computing for a
backend engineer. Use one concrete example from the selected pages, explain why
it matters to later inference study, and challenge one misconception below. Name
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

- A reshape always copies.
- Broadcasting always materializes expanded inputs.
- Element-wise multiplication and matrix multiplication are equivalent.
- A view owns independent data.
- nbytes includes every allocation and object overhead.

## Practical exercise

Start with `NP-01` in the
[module exercise specifications](../../exercises/02-numpy-and-tensors.md), then
complete the remaining exercises. Ask for a plan critique before executing;
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

Continue to [Module 3](../../modules/03-essential-mathematics.md) after the exit
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
