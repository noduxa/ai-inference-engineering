# Module 1: Advanced Python for AI systems

Status: Not started. Estimated time: **20 hours**, including practice, review
and catch-up. Last verified: 2026-09-30.

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

## Detailed explanation and worked example

### Ownership is a graph, not a variable-sized box

A Python name refers to an object. Assignment adds a reference; it does not copy
that object. A shallow copy creates an outer container but retains references to
nested objects. A deep copy recursively copies supported objects and keeps a
memo to handle cycles. This matters when requests share mutable configuration.
See the [data model](https://docs.python.org/3/reference/datamodel.html) and
[copy semantics](https://docs.python.org/3/library/copy.html).

```python
import copy
original = [[1], [2]]
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)
shallow[0].append(9)
assert alias is original
assert original[0] == [1, 9]
assert deep[0] == [1]
```

The assertions illustrate semantics, not recorded learner evidence. Draw objects
and arrows before executing. Deleting `original` removes that name, not every
reference. CPython reference counting and cyclic garbage collection are
implementation details; finalization timing is not a portable resource-lifetime
contract. Use context managers for files, locks and cleanup, including
exceptions. A generator retains its suspended frame and referenced inputs. Its
small object size does not prove the entire computation uses little memory.

### Concurrency follows the waiting and execution boundaries

AsyncIO overlaps cooperative waits in one event-loop thread. A blocking function
inside a coroutine prevents other tasks on that loop from progressing. Threads
can overlap blocking I/O, but a GIL-enabled CPython process normally runs only
one thread's Python bytecode at a time. Native numerical code can release the
GIL; free-threaded builds differ. Record the interpreter/build and native thread
count before interpreting an experiment. Neither the GIL nor AsyncIO makes
compound shared-state updates automatically safe. See
[threading](https://docs.python.org/3/library/threading.html).

Processes can execute pure-Python CPU work in parallel, but startup,
serialization and duplicated memory can outweigh useful work.
`concurrent.futures` provides a shared interface, not equivalent execution
costs. Four independent simulated 100 ms waits have an ideal overlap floor near
100 ms, not a promised measurement; four CPU tasks each taking 100 ms cannot get
that benefit from cooperative waits. Measure total wall time, per-task latency
and overhead at several bounded sizes.

### Boundaries that make infrastructure understandable

Closures capture bindings; decorators wrap callables and can obscure signatures.
Context managers express paired acquisition/release. Iterators implement a pull
interface, while generators make incremental production convenient. A Protocol
specifies a structural interface for type checking; annotations do not validate
incoming requests at runtime. A dataclass organizes fields; use a factory for
per-instance mutable defaults. Catch errors where you can add context or
recover, and preserve the original exception when re-raising.

A package should declare build requirements and project dependencies in
`pyproject.toml`; a virtual environment isolates installation, while a recorded
resolved dependency set makes reruns reproducible. Use pytest fixtures for setup
and teardown. Log durations and safe request IDs, never private prompts or
tokens. Profile before optimizing: `cProfile` attributes execution time, whereas
`tracemalloc` tracks Python allocations and does not account for all native/GPU
memory. A hot function is a hypothesis target, not proof of root cause.

## Code-reading task and implementation mistakes

For PY-06, choose the installed public pytest package. Record its version,
locate one public fixture-related entry point, follow two calls, and identify an
error path and its test. Explain how you found them using symbol search. Do not
claim a complete repository understanding from one trace. Watch for late-bound
closures, mutable defaults, swallowed cancellation, nested executor deadlocks
and logging inside a timed loop.

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

## Connection to the next module

Continue to [numpy and tensors](02-numpy-and-tensors.md) after the exit test.
