# Module 4 exercise specifications

Status: Not started. These are specifications, not completed experiments.

[Module guide](../modules/04-pytorch-fundamentals.md) ·
[Source pack](../notebooklm/source-packs/04-pytorch-fundamentals.md) ·
[Evidence template](EVIDENCE_TEMPLATE.md)

## Execution contract

Use public or synthetic inputs, an isolated environment and bounded resources.
Write your prediction before execution. Record exact versions, configuration,
checks, observations, failures and cleanup. Expected effects are **hypotheses**;
no timings, memory results or successful runs are asserted here. Each exercise
must include a correctness check before any performance claim.

## PT-01: Tensor device and dtype

Status: Not started.

Install using the current official selector for your OS; record exact installed
versions. Verify a CPU tensor, shape, stride, dtype and element size. Check CUDA
availability before any move. Compare supported dtypes and CPU/CUDA transfers;
if CUDA is absent record Not started for device-specific work.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PT-01 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** availability, device, dtype, shape and transfer
  boundaries.
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

## PT-02: Small module and one training step

Status: Not started.

Use synthetic features with shape (4,3) and two output classes. Build nn.Module
with Linear(3,2), list named parameters, run forward, calculate a loss, zero
gradients, backpropagate and take one optimizer step. Record tensor shapes and
verify at least one parameter update; check Dataset/DataLoader with the same
synthetic samples.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PT-02 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** parameter count, loss, gradients and weight delta.
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

## PT-03: Inference and state round-trip

Status: Not started.

Compare training/evaluation mode and gradient-enabled/no_grad/inference_mode
execution. Check requires_grad and grad_fn where appropriate. Save your own
state_dict and reload into a fresh matching module on CPU; compare outputs in
evaluation mode with tolerances. Never load an untrusted pickle or require
remote custom code.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PT-03 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** requires_grad, mode, file size and output
  tolerance.
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

## PT-04: Profiler, compile and mixed precision

Status: Not started.

Profile the tiny module with CPU activity and memory recording. Explain the
hottest operator from the report. Attempt basic torch.compile after checking
platform support; separate first compilation from warmed calls. Compare
supported autocast with FP32 and record numerical differences. Mark unsupported
features To be validated rather than inventing results.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PT-04 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** operator table, graph/compile warm-up, unsupported
  operations.
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

## PT-05: CPU versus GPU timing and memory

Status: Not started.

Reuse the same small workload, dtype and shapes. Capture CPU perf_counter
timings; for CUDA, use synchronization or CUDA events and include completion
before reading results. Report transfers separately and include warmup. Record
memory_allocated and memory_reserved before/after. No GPU means the CUDA
comparison remains Not started; complete the written measurement design.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### PT-05 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** synchronized repeated times, peak
  allocated/reserved bytes.
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
