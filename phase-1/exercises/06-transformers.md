# Module 6 exercise specifications

Status: Not started. These are specifications, not completed experiments.

[Module guide](../modules/06-transformers.md) ·
[Source pack](../notebooklm/source-packs/06-transformers.md) ·
[Evidence template](EVIDENCE_TEMPLATE.md)

## Execution contract

Use public or synthetic inputs, an isolated environment and bounded resources.
Write your prediction before execution. Record exact versions, configuration,
checks, observations, failures and cleanup. Expected effects are **hypotheses**;
no timings, memory results or successful runs are asserted here. Each exercise
must include a correctness check before any performance claim.

## TR-01: Manual scaled dot-product attention

Status: Not started.

Use Q=K=[[1,0],[0,1]] and V=[[1,2],[3,4]]. Calculate QKᵀ/sqrt(2), row-wise
softmax and the weighted result. Repeat with a causal mask. Label every shape
and identify the softmax axis; calculate before checking with NumPy or PyTorch.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### TR-01 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** score and mask matrices, softmax rows, weighted
  outputs.
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

## TR-02: Tokenizer and mask inspection

Status: Not started.

Use two publicly accessible, ungated tokenizer revisions selected from the
course examples; download only tokenizers initially. Compare the same synthetic
sentence, vocabulary IDs, special tokens and decoded text. Batch a short and a
long sentence; inspect padding, truncation and attention masks. Record revisions
and do not treat differing token counts as model quality evidence.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### TR-02 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** IDs, vocabulary/revision, padded lengths and masks.
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

## TR-03: Decoder-only generation walkthrough

Status: Not started.

On paper, trace two generation steps: token IDs, embeddings, positional
information, attention/block output, last-position logits, selection and
appended token. Include batch, sequence, hidden and vocabulary dimensions. A
small locally initialized causal model may verify shapes; no pretrained model
download is required.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### TR-03 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** two-step shapes, selected IDs and stop reason.
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

## TR-04: Sampling parameters

Status: Not started.

Use fixed synthetic logits and a seed to compare greedy selection with sampling
at two temperatures, top-k and top-p. Record selected candidates and frequencies
over a bounded sample count. Explain that these are synthetic sampling results,
not model quality benchmarks. Compare to the framework GenerationConfig
definitions.

Evidence: prediction, exact method, actual output or limitation, interpretation
and a link to the relevant selected source section.

### TR-04 evidence and execution fields

- **Purpose:** test the specific mechanism in the procedure above; connect it to
  a request-processing, tensor or memory failure in the linked module.
- **Prerequisites:** finish the module's preceding study steps; use synthetic
  inputs and record installed versions before running.
- **Prediction:** write a direction/shape/value prediction and one condition
  under which it could fail, before seeing output.
- **Required measurements:** probability vectors, fixed seeds and sample
  frequencies.
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
