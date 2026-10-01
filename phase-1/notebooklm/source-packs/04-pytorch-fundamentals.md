# Module 4 NotebookLM source pack

Status: Planned. Source inspection: Verified. NotebookLM import: To be
validated. Last verified: 2026-09-30.

[NotebookLM workflow](../README.md) ·
[Module](../../modules/04-pytorch-fundamentals.md) ·
[Source registry](../../sources.yaml)

## Module purpose

Framework literacy makes it possible to inspect a model, distinguish its state
from its computation and measure forward-only execution.

## Learning objectives

- Build and inspect a small module with named parameters and a reproducible
  forward pass.
- Perform one training step and distinguish parameter updates from forward-only
  inference.
- Save/reload a state dictionary and verify equivalent outputs.
- Measure timing and memory using correct device-specific boundaries.

## Prerequisites

Preceding curriculum modules; review unresolved prerequisite exit tests.

## Ordered source table

Four curated source collections: one primary and three supporting. A collection
can contain several individual pages. Import **4–8 relevant pages at a time**,
not every page below at once. An index URL does not import linked chapters. Use
the session batches below and add missing sections only when needed.

| Order | Registry ID      | Source collection                                                                                                             | Role       | Selected reading |
| ----- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 1     | `pt-basics`      | [PyTorch Learn the Basics and installation](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)                    | primary    | 2.5 h            |
| 2     | `pt-autograd`    | [Autograd mechanics and inference mode](https://docs.pytorch.org/docs/2.14/notes/autograd.html)                               | supporting | 0.75 h           |
| 3     | `pt-performance` | [PyTorch profiling, compilation and mixed precision](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) | supporting | 1.25 h           |
| 4     | `pt-cuda`        | [CUDA semantics: timing and memory](https://docs.pytorch.org/docs/2.14/notes/cuda.html)                                       | supporting | 0.75 h           |

## Exact sections, selection reasons and access

### pt-basics: PyTorch Learn the Basics and installation

Expected knowledge: Construct a tensor/module workflow, perform an update and
preserve model state.

- Author/institution: Suraj Subramanian, Seth Juarez, Cassie Breviu, Dmitry
  Soshnikov, Ari Bornstein; PyTorch.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Jan 20, 2026; see
  section-level dates in the registry where available.
- Selected study time: 2.5 h; included in this module’s budget.
- Authority and phase fit: Official workflow teaches modules, autograd and state
  dictionaries; substitute synthetic tabular data for image-course expansion.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                        | Study these sections                                                                  | Skip for Phase 1                                    |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [Install locally](https://pytorch.org/get-started/locally/)                                       | Choose supported build and verify installation                                        | Building from source                                |
| [Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)              | Tensor attributes, operations, device moves and NumPy sharing                         | FashionMNIST download and computer-vision expansion |
| [Datasets and DataLoaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html) | Dataset and DataLoader basics                                                         | FashionMNIST download and computer-vision expansion |
| [Build model](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html)        | nn.Module, layers and parameters                                                      | FashionMNIST download and computer-vision expansion |
| [Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)           | Computational graph, gradients and disabling tracking                                 | FashionMNIST download and computer-vision expansion |
| [Optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)     | Loss, learning rate, zero_grad, backward and step                                     | FashionMNIST download and computer-vision expansion |
| [Save and load](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)     | state_dict saving, loading and model.eval                                             | FashionMNIST download and computer-vision expansion |
| [Tensor strides](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.stride.html)           | Tensor.stride definition and example; compare element strides with NumPy byte strides | None in this short API page                         |

### pt-autograd: Autograd mechanics and inference mode

Expected knowledge: Select evaluation and gradient modes correctly and explain
their different restrictions.

- Author/institution: PyTorch contributors; PyTorch.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Aug 03, 2026; see
  section-level dates in the registry where available.
- Selected study time: 0.75 h; included in this module’s budget.
- Authority and phase fit: Distinguishes evaluation mode from gradient modes,
  preventing a common inference correctness error.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                                  | Study these sections                                                             | Skip for Phase 1                                     |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [Autograd mechanics](https://docs.pytorch.org/docs/2.14/notes/autograd.html)                                | Locally disabling gradient computation; no-grad; inference mode; evaluation mode | Multithreaded autograd and custom saved tensor hooks |
| [Inference mode](https://docs.pytorch.org/docs/2.14/generated/torch.autograd.grad_mode.inference_mode.html) | Restrictions and example                                                         | Internal implementation                              |

### pt-performance: PyTorch profiling, compilation and mixed precision

Expected knowledge: Collect a minimal profile and distinguish
compilation/autocast setup from measured execution.

- Author/institution: PyTorch contributors; PyTorch.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Jul 19, 2026; see
  section-level dates in the registry where available.
- Selected study time: 1.25 h; included in this module’s budget.
- Authority and phase fit: Provides first-party measurement and compilation
  APIs; no acceleration is assumed.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                 | Study these sections                                               | Skip for Phase 1                              |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | --------------------------------------------- |
| [Profiler recipe](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) | CPU activity, CUDA activity and memory profiling                   | Distributed traces and long-running schedules |
| [torch.compile](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)           | Basic callable wrapping; compilation overhead and modes            | Custom backends and compiler internals        |
| [Automatic mixed precision](https://docs.pytorch.org/docs/2.14/amp.html)                   | autocast; gradient scaling purpose; supported device/dtype caveats | Operator lists beyond the exercise            |

### pt-cuda: CUDA semantics: timing and memory

Expected knowledge: Use completed-work timing boundaries and distinguish live
versus reserved device memory.

- Author/institution: PyTorch contributors; PyTorch.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Jul 17, 2026; see
  section-level dates in the registry where available.
- Selected study time: 0.75 h; included in this module’s budget.
- Authority and phase fit: Framework semantics explain asynchronous timing and
  the caching allocator before GPU comparisons.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                           | Study these sections                                                                  | Skip for Phase 1                                            |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [CUDA semantics](https://docs.pytorch.org/docs/2.14/notes/cuda.html) | Asynchronous execution; CUDA events; memory management; allocated and reserved memory | Multi-device operations, CUDA graphs and distributed topics |

## Optional visual lane and overlap decisions

Use the official autograd tutorial’s graph diagram. The autograd mechanics
reference takes precedence over simplified tutorial wording about evaluation and
gradient modes.

No additional secondary blog is selected: the first-party diagrams and textbook
explanations cover the visual need without another overlapping source.

## Notebook name and adding sources

Suggested name: **Joshua — Phase 1 — 04 PyTorch fundamentals**.

Add pages in the source-table order within the current session batch. Name each
import with its registry ID and section title. Check that the actual page text,
code and equations appear before asking questions. Retain at most eight active
pages; rotate earlier pages out after saving your own cited notes. Re-add an
omitted page if a prompt needs it. Do not use an index as a substitute for
content.

## Session import batches

- **Basic workflow:** Install locally; Tensors; Datasets and DataLoaders; Build
  model; Autograd; Optimization; Save and load; Tensor strides.
- **Modes and measurements:** Autograd mechanics; Inference mode; Profiler
  recipe; torch.compile; Automatic mixed precision; CUDA semantics.

## Initial NotebookLM questions

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

- What state does a state_dict contain, and what code is still needed?
- How would you verify that a forward pass did not build a gradient graph?
- Why separate transfer, warmup, compile and steady-state timing?

## Audio Overview customization prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Give a short spoken orientation to pytorch fundamentals for a backend engineer.
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

- model.eval() disables autograd.
- no_grad() and inference_mode() have identical restrictions.
- Moving inputs also moves model parameters.
- Host wall-clock timing alone always measures completed CUDA work.
- Reserved memory is the same as live tensor memory.

## Practical exercise

Start with `PT-01` in the
[module exercise specifications](../../exercises/04-pytorch-fundamentals.md),
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

Continue to [Module 5](../../modules/05-neural-networks.md) after the exit
check.

### Device reference: MPS backend

[MPS backend](https://docs.pytorch.org/docs/2.14/notes/mps.html): study
Availability and moving tensors/modules to MPS. Skip shader compilation and
unrelated APIs. Official PyTorch reference; free; 2.14 documentation. Selected
lookup included in pt-cuda time. NotebookLM extraction remains To be validated.

### Device reference: MPS APIs

[MPS APIs](https://docs.pytorch.org/docs/2.14/mps.html): study synchronize;
current_allocated_memory; driver_allocated_memory. Skip shader compilation and
unrelated APIs. Official PyTorch reference; free; 2.14 documentation. Selected
lookup included in pt-cuda time. NotebookLM extraction remains To be validated.

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
