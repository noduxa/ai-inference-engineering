# Module 1 NotebookLM source pack

Status: Planned. Source inspection: Verified. NotebookLM import: To be
validated. Last verified: 2026-09-16.

[NotebookLM workflow](../README.md) ·
[Module](../../modules/01-advanced-python.md) ·
[Source registry](../../sources.yaml)

## Module purpose

Serving code is still Python software: ownership mistakes, blocking work and
hidden allocations can affect reliability before any model optimization begins.

## Learning objectives

- Predict aliasing, lifetime and lazy-evaluation behaviour in short Python
  programs.
- Build a tested package with typed boundaries and reliable cleanup.
- Choose a concurrency mechanism from a workload description and measure its
  overhead.
- Locate an allocation or CPU hotspot and trace a public repository call path.

## Prerequisites

Working Python familiarity and command-line use.

## Ordered source table

Four curated source collections: one primary and three supporting. A collection
can contain several individual pages. Import **4–8 relevant pages at a time**,
not every page below at once. An index URL does not import linked chapters. Use
the session batches below and add missing sections only when needed.

| Order | Registry ID    | Source collection                                                                                              | Role       | Selected reading |
| ----- | -------------- | -------------------------------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 1     | `py-runtime`   | [Python data model and standard-library references](https://docs.python.org/3/reference/datamodel.html)        | primary    | 3 h              |
| 2     | `py-tutorial`  | [Python tutorial: functions, modules, classes and environments](https://docs.python.org/3/tutorial/index.html) | supporting | 1.5 h            |
| 3     | `py-pytest`    | [pytest: getting started and fixtures](https://docs.pytest.org/en/stable/getting-started.html)                 | supporting | 0.75 h           |
| 4     | `py-packaging` | [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)           | supporting | 0.75 h           |

## Exact sections, selection reasons and access

### py-runtime: Python data model and standard-library references

Expected knowledge: Predict ownership and memory behaviour; choose and inspect
runtime concurrency and profiling APIs.

- Author/institution: Python documentation contributors; Python Software
  Foundation.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Sep 15, 2026 (23:57 UTC);
  see section-level dates in the registry where available.
- Selected study time: 3 h; included in this module’s budget.
- Authority and phase fit: Defines language semantics and runtime APIs directly;
  selected lookups connect memory, concurrency and profiling to small systems
  experiments.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                      | Study these sections                                                                 | Skip for Phase 1                                          |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| [Data model](https://docs.python.org/3/reference/datamodel.html)                | Objects, values and types; standard type hierarchy; callable types; context managers | Metaclasses, descriptors in depth and C internals         |
| [copy](https://docs.python.org/3/library/copy.html)                             | Shallow and deep copy                                                                | Unrelated APIs and advanced implementation details        |
| [typing](https://docs.python.org/3/library/typing.html)                         | Type aliases, callable annotations and Protocol                                      | Unrelated APIs and advanced implementation details        |
| [dataclasses](https://docs.python.org/3/library/dataclasses.html)               | dataclass and default_factory                                                        | Unrelated APIs and advanced implementation details        |
| [contextlib](https://docs.python.org/3/library/contextlib.html)                 | contextmanager and cleanup                                                           | Unrelated APIs and advanced implementation details        |
| [asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)            | Coroutines, tasks, TaskGroup, cancellation and blocking calls                        | Unrelated APIs and advanced implementation details        |
| [threading](https://docs.python.org/3/library/threading.html)                   | Thread objects, locks and GIL/free-threaded notes                                    | Unrelated APIs and advanced implementation details        |
| [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)       | Process, Pool, start methods and programming guidelines                              | Unrelated APIs and advanced implementation details        |
| [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) | ThreadPoolExecutor, ProcessPoolExecutor, exceptions and deadlocks                    | Unrelated APIs and advanced implementation details        |
| [Profilers](https://docs.python.org/3/library/profile.html)                     | cProfile and interpreting statistics                                                 | Unrelated APIs and advanced implementation details        |
| [tracemalloc](https://docs.python.org/3/library/tracemalloc.html)               | Snapshots, statistics and traceback comparison                                       | Unrelated APIs and advanced implementation details        |
| [logging](https://docs.python.org/3/library/logging.html)                       | Logger, levels and handlers                                                          | Unrelated APIs and advanced implementation details        |
| [Function definitions](https://docs.python.org/3/reference/compound_stmts.html) | Function definitions: decorators and closure behaviour                               | Other compound statements already covered by the tutorial |
| [Timing clocks](https://docs.python.org/3/library/time.html)                    | perf_counter, process_time and clock measurement boundaries                          | Calendar and timezone APIs                                |

### py-tutorial: Python tutorial: functions, modules, classes and environments

Expected knowledge: Write scoped functions and lazy iterators; understand
imports, exceptions and isolated environments.

- Author/institution: Python documentation contributors; Python Software
  Foundation.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Sep 15, 2026 (23:57 UTC);
  see section-level dates in the registry where available.
- Selected study time: 1.5 h; included in this module’s budget.
- Authority and phase fit: A concise bridge from existing Java/Python experience
  to Python-specific control flow and packaging boundaries.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                               | Study these sections                                                            | Skip for Phase 1                                         |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [More control flow](https://docs.python.org/3/tutorial/controlflow.html) | Defining functions; default arguments; lambda expressions; function annotations | Beginner syntax already demonstrated; unrelated examples |
| [Modules](https://docs.python.org/3/tutorial/modules.html)               | Modules, packages and import paths                                              | Beginner syntax already demonstrated; unrelated examples |
| [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)  | Handling exceptions, raising and cleanup                                        | Beginner syntax already demonstrated; unrelated examples |
| [Classes](https://docs.python.org/3/tutorial/classes.html)               | Scopes and namespaces; iterators; generators; generator expressions             | Beginner syntax already demonstrated; unrelated examples |
| [Virtual environments](https://docs.python.org/3/tutorial/venv.html)     | Creating virtual environments and managing packages                             | Beginner syntax already demonstrated; unrelated examples |

### py-pytest: pytest: getting started and fixtures

Expected knowledge: Write discoverable assertions and fixtures that clean up
resources even after failure.

- Author/institution: pytest development team; pytest.
- Format: documentation. Access: free.
- Publication/update: Not stated; rolling documentation.
- Selected study time: 0.75 h; included in this module’s budget.
- Authority and phase fit: The testing tool’s own instructions establish
  collection, assertions and isolated fixtures.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                            | Study these sections                       | Skip for Phase 1           |
| --------------------------------------------------------------------- | ------------------------------------------ | -------------------------- |
| [Get started](https://docs.pytest.org/en/stable/getting-started.html) | First test, assertions and test discovery  | Installation alternatives  |
| [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)    | Requesting fixtures; scope; yield teardown | Advanced fixture factories |

### py-packaging: Writing your pyproject.toml

Expected knowledge: Describe the build-system and project tables and package a
small local project.

- Author/institution: PyPA contributors; Python Packaging Authority.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Sep 09, 2026; see
  section-level dates in the registry where available.
- Selected study time: 0.75 h; included in this module’s budget.
- Authority and phase fit: Current packaging guidance avoids legacy setup-only
  tutorials; the exercise stops before publication.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                      | Study these sections                                      | Skip for Phase 1                                          |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) | Build backend, project metadata, dependencies and scripts | Publishing and optional metadata not used by the exercise |

## Optional visual lane and overlap decisions

Sketch the object graph from the Python data model, then compare it with the
generator and class examples. No extra video is necessary.

No additional secondary blog is selected: the first-party diagrams and textbook
explanations cover the visual need without another overlapping source.

## Notebook name and adding sources

Suggested name: **Joshua — Phase 1 — 01 Advanced Python for AI systems**.

Add pages in the source-table order within the current session batch. Name each
import with its registry ID and section title. Check that the actual page text,
code and equations appear before asking questions. Retain at most eight active
pages; rotate earlier pages out after saving your own cited notes. Re-add an
omitted page if a prompt needs it. Do not use an index as a substitute for
content.

## Session import batches

- **Object model and language:** Data model; copy; Function definitions;
  Classes; contextlib; typing; dataclasses; Errors and exceptions.
- **Package and test:** Modules; Virtual environments; Writing pyproject.toml;
  Get started; Fixtures; logging.
- **Concurrency and profiling:** asyncio tasks; threading; multiprocessing;
  concurrent.futures; Profilers; tracemalloc; Timing clocks.

## Initial NotebookLM questions

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

- Why can a shallow copy still share nested objects?
- Which measurement would distinguish waiting from Python CPU work?
- What evidence would justify replacing a loop with processes?

## Audio Overview customization prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Give a short spoken orientation to advanced python for ai systems for a backend
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

- Assignment copies an object.
- A generator stores all produced values.
- AsyncIO speeds up arbitrary CPU work.
- Threads are always unable to run in parallel, regardless of interpreter build
  or native code.
- tracemalloc measures all process and GPU memory.

## Practical exercise

Start with `PY-01` in the
[module exercise specifications](../../exercises/01-advanced-python.md), then
complete the remaining exercises. Ask for a plan critique before executing;
never ask the model to fabricate an observation or to silently fill in missing
measurements.

## Required learning evidence

- Own-word explanation with inspected source citations.
- Exercise code/calculations and explicit correctness checks.
- Environment record, actual observations, failed attempts and limitations.
- Prediction-versus-result comparison and a reviewed teach-back.

## Exit criteria

- Complete the 6 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

Use the [assessment rubric](../../assessments/rubric.md); neither imported
sources nor generated study artifacts establish mastery.

## What to study next

Continue to [Module 2](../../modules/02-numpy-and-tensors.md) after the exit
check.
