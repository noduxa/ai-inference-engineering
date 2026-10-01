# Module 1 exercise specifications

Status: Not started. These are specifications, not completed experiments.

[Module guide](../modules/01-advanced-python.md) ·
[Source pack](../notebooklm/source-packs/01-advanced-python.md) ·
[Evidence template](EVIDENCE_TEMPLATE.md)

## Execution contract

Use public or synthetic inputs, an isolated environment and bounded resources.
Write your prediction before execution. Record exact versions, configuration,
checks, observations, failures and cleanup. Expected effects are **hypotheses**;
no timings, memory results or successful runs are asserted here. Each exercise
must include a correctness check before any performance claim.

## PY-01: Generator versus list memory

Status: Not started.

Predict relative peak allocation for summing a bounded range from a list and a
generator. Use the same values and verify equal sums. Measure tracemalloc
current/peak separately from shallow object size. Repeat in fresh processes with
a fixed maximum of 100,000 values; record time as well as memory.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PY-01 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** peak traced bytes and total consumption time, equal
  sums.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## PY-02: AsyncIO versus threads for I/O

Status: Not started.

Compare a fixed number of simulated waits using asyncio.sleep and time.sleep in
a thread pool. Add a sequential baseline, equal task count and bounded
concurrency. Label this simulated I/O, not a network benchmark. Test
timeout/cancellation and exception handling; do not contact external services.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PY-02 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** wall time, task latency, worker count and
  successful task count.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## PY-03: Multiprocessing for CPU-bound work

Status: Not started.

Use a small pure-Python checksum or arithmetic workload. Compare sequential,
ThreadPoolExecutor and ProcessPoolExecutor. Guard the entry point, select and
record the start method, include startup/serialization costs and validate equal
output. Cap workers at two and total runtime at 30 seconds. Record Python
version and GIL/build assumptions.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PY-03 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** startup-inclusive wall time, result equality, task
  size and process count.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## PY-04: Profile a slow function

Status: Not started.

Write a deliberately repetitive string-counting function with a correctness
test. Use cProfile and sorted cumulative statistics to choose one change.
Compare repeated perf_counter timings outside the profiler; report an
inconclusive result if noise dominates.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PY-04 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** cumulative/self time and call count before and
  after one change.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## PY-05: Trace memory allocations

Status: Not started.

Take tracemalloc snapshots before and after a bounded cache population, inspect
allocation tracebacks, clear the cache and inspect again. Explain why traced
Python allocations, process resident memory and GPU memory are different
measurements.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PY-05 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** snapshot byte/count deltas and allocation
  tracebacks.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.

## PY-06: Package and read code

Status: Not started.

Create a tiny local package with pyproject.toml, a virtual environment, a typed
Protocol, a dataclass using default_factory, a closure-based decorator and a
context manager. Test cleanup after an exception with pytest and use logging
without sensitive data. Inspect the public source linked from one
standard-library API page: trace a function to a helper and a test or test
search plan, record revision and file paths. Do not publish a package or clone
private code.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PY-06 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** package version, file/symbol call trace, passing
  and failing test cases.
- **Expected conceptual pattern:** use the module's worked example as a
  hypothesis, not a supplied observation. Explain departures from it.
- **Interpretation questions:** did correctness hold? What changed besides the
  intended variable? What does this measurement fail to measure?
- **Common mistakes:** timing setup in only one arm, omitting units or shapes,
  selecting only a favorable run, or interpreting a simulation as hardware data.
- **Required evidence:** original code/calculation, raw output, prediction,
  environment, interpretation and a source section; use EVIDENCE_TEMPLATE.md.
- **Cleanup:** close executors/files, release temporary arrays/models, terminate
  only processes started by this exercise, and retain reviewed raw measurements.
- **Hardware-independent fallback:** do calculations and use bounded CPU arrays
  or simulated waits; explicitly mark accelerator-only observations Not started.
