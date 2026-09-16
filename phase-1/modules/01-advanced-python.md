# Module 1: Advanced Python for AI systems

Status: Not started. Estimated time: **20 hours**, including practice, review
and catch-up. Last verified: 2026-09-16.

[Curriculum](../CURRICULUM.md) · [Schedule](../SCHEDULE.md) ·
[Source pack](../notebooklm/source-packs/01-advanced-python.md)

## Why this matters

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

Existing programming experience, basic Python syntax and command-line use. No AI
specialization is assumed.

## Required concepts

- Python’s object and memory model
- References, identity, mutability and copying
- Functions and closures
- Decorators
- Context managers
- Iterators and generators
- Type hints and protocols
- Dataclasses
- Error handling
- Modules and packages
- Virtual environments
- Modern project packaging with pyproject.toml
- Testing with pytest
- Logging
- AsyncIO
- Threads
- Multiprocessing
- concurrent.futures
- The Global Interpreter Lock (GIL), including version/build differences
- CPU-bound versus I/O-bound workloads
- Performance profiling
- Memory profiling
- Reading and navigating a large Python repository

## Recommended sources

- `py-runtime` —
  [Python data model and standard-library references](https://docs.python.org/3/reference/datamodel.html)
  (primary; selected reading 3 h).
- `py-tutorial` —
  [Python tutorial: functions, modules, classes and environments](https://docs.python.org/3/tutorial/index.html)
  (supporting; selected reading 1.5 h).
- `py-pytest` —
  [pytest: getting started and fixtures](https://docs.pytest.org/en/stable/getting-started.html)
  (supporting; selected reading 0.75 h).
- `py-packaging` —
  [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
  (supporting; selected reading 0.75 h).

Exact page links, selected sections, exclusions, access terms and import order
are in the source pack. Reading times are selective budgets, not estimates for
completing entire documentation collections.

## Study order

1. Start with data-model ownership, copying and PY-01 predictions before memory
   measurements.
2. Study functions, closures, decorators and context-manager cleanup; build
   those pieces in PY-06.
3. Add protocols, dataclasses, exceptions and logging, then package and test the
   small interface.
4. Compare concurrency choices in PY-02/PY-03 before profiling CPU and
   allocation behaviour in PY-04/PY-05.
5. Trace a public implementation and take a fresh ownership/concurrency exit
   check.

## Exercises and deliverables

[Open the exercise specifications](../exercises/01-advanced-python.md).

- `PY-01` — Generator versus list memory.
- `PY-02` — AsyncIO versus threads for I/O.
- `PY-03` — Multiprocessing for CPU-bound work.
- `PY-04` — Profile a slow function.
- `PY-05` — Trace memory allocations.
- `PY-06` — Package and read code.

Deliver a short concept note, original calculations/code, environment record,
actual measurements where applicable, and a teach-back. Use the
[evidence template](../exercises/EVIDENCE_TEMPLATE.md). No outputs are supplied
as completed work.

## Reflection questions

- Why can a shallow copy still share nested objects?
- Which measurement would distinguish waiting from Python CPU work?
- What evidence would justify replacing a loop with processes?

## Common mistakes to challenge

The following statements are deliberately questionable; correct them with
sources:

- Assignment copies an object.
- A generator stores all produced values.
- AsyncIO speeds up arbitrary CPU work.
- Threads are always unable to run in parallel, regardless of interpreter build
  or native code.
- tracemalloc measures all process and GPU memory.

## Exit test

Without NotebookLM, answer the reflection questions and explain a fresh variant
of one exercise. Then use sources to check your answer. Demonstrate a working
application, predict its outcome and diagnose one plausible failure. Record
assistance, corrections and evidence using the
[rubric](../assessments/rubric.md).

- Complete the 6 exercise specifications or explicitly record hardware-limited
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
