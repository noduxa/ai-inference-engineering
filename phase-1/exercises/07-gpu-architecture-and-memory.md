# Module 7 exercise specifications

Status: Not started. These are specifications, not completed experiments.

[Module guide](../modules/07-gpu-architecture-and-memory.md) ·
[Source pack](../notebooklm/source-packs/07-gpu-architecture-and-memory.md) ·
[Evidence template](EVIDENCE_TEMPLATE.md)

## Execution contract

Use public or synthetic inputs, an isolated environment and bounded resources.
Write your prediction before execution. Record exact versions, configuration,
checks, observations, failures and cleanup. Expected effects are **hypotheses**;
no timings, memory results or successful runs are asserted here. Each exercise
must include a correctness check before any performance claim.

## GPU-01: Inspect and monitor the available GPU

Status: Not started.

Check CUDA availability and device name using PyTorch. On NVIDIA systems inspect
nvidia-smi help before querying only device name, memory and utilization. Avoid
publishing UUIDs, process lists or host identifiers. Observe utilization during
one bounded operation; if no NVIDIA GPU is available record that limitation and
create a measurement plan.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### GPU-01 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** device/backend, available memory and bounded
  utilization samples.
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

## GPU-02: Estimate and compare tensor memory

Status: Not started.

Predict bytes for a (1024,1024) tensor in FP32 and FP16 before allocating.
Compare payload estimates with allocated/reserved deltas on available hardware.
Explain BF16 range versus precision and theoretical INT8/packed INT4 payloads
plus scale/packing overhead; no quantization implementation is required.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### GPU-02 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** predicted payload and observed allocator deltas.
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

## GPU-03: Approach a bounded resource limit

Status: Not started.

Run only in a disposable single-process context on hardware you control. Start
with small matrices, calculate input/output plus safety allowance, and stop
before the next size exceeds the lesser of 256 MiB or 10% of currently free
device memory. Limit to five sizes; release each before the next. Do not exhaust
host RAM or a shared GPU. Record the stopping rule even if no failure occurs.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### GPU-03 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** planned cap, accepted sizes and stop reason.
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

## GPU-04: Explain an out-of-memory condition safely

Status: Not started.

Default: simulate a budget refusal by requesting more than your experiment’s
declared allocation budget, without allocating it. Label it simulated, not a
real CUDA OOM. If an actual torch.OutOfMemoryError occurs incidentally inside
GPU-03’s bounded subprocess, preserve only a sanitized error, terminate the
child, and verify cleanup before any retry. Explain requested bytes, live
tensors, reserved memory and headroom. Never deliberately fill the physical GPU
just to obtain an error message.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### GPU-04 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** simulated budget error or safely observed OOM,
  recovery check.
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
