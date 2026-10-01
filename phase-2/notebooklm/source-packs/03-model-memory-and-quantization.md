# Module 3 NotebookLM source pack

Status: Planned. NotebookLM import: To be validated. Last verified: 2026-09-30.

[Module](../../modules/03-model-memory-and-quantization.md) ·
[Workflow](../README.md) · [Registry](../../sources.yaml)

## Notebook name

Joshua — Phase 2 — 03 Model memory and quantization

## Module purpose and learning objectives

- Build a memory budget including weights, activations, KV state, workspace and
  overhead.
- Compare two supported precisions and interpret memory, timing and output
  differences.
- Diagnose an OOM without treating reserved memory as a leak.

## Prerequisites

Previous module exit evidence; retain earlier calculation assumptions.

## Ordered source table and import order

Import the exact pages below in order. Do not assume linked child pages were
imported. Keep about 4–8 active documents; remove overlapping material when it
adds no distinct explanation. Original papers are historical evidence, not
current API manuals. Check extracted equations and code manually.

| Order | Exact source URL                                                                                           | Role                 | Selected time |
| ----- | ---------------------------------------------------------------------------------------------------------- | -------------------- | ------------- |
| 1     | [Optimizing LLMs for Speed and Memory](https://huggingface.co/docs/transformers/llm_tutorial_optimization) | primary; required    | 0.75 h        |
| 2     | [Quantization overview](https://huggingface.co/docs/transformers/quantization/overview)                    | supporting; required | 0.5 h         |
| 3     | [Bitsandbytes](https://huggingface.co/docs/transformers/quantization/bitsandbytes)                         | supporting; required | 0.5 h         |
| 4     | [CUDA semantics](https://docs.pytorch.org/docs/2.14/notes/cuda.html)                                       | supporting; required | 0.5 h         |

## Exact sections, credibility and selection

### p2-m3-optimization

- Institution/authors: Hugging Face; Hugging Face contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Memory requirements; lower precision; key-value cache; MQA/GQA
  discussion.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Account separately for weights and cache and
  state architecture assumptions. Maintainer documentation defines the contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m3-quant

- Institution/authors: Hugging Face; Hugging Face contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Quantization introduction; hardware/method compatibility table.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Choose a supported representation and
  distinguish calibration requirements. Maintainer documentation defines the
  contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m3-bnb

- Institution/authors: Hugging Face; Hugging Face contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Hardware compatibility; 8-bit and 4-bit loading; memory footprint.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Check backend support and avoid assuming
  reduced storage guarantees acceleration. Maintainer documentation defines the
  contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m3-cuda

- Institution/authors: PyTorch project; PyTorch project contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Asynchronous execution; memory management; memory statistics.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Measure completed work and separate live
  tensor memory from allocator reservation. Maintainer documentation defines the
  contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

## Initial grounding questions

- Build a memory budget including weights, activations, KV state, workspace and
  overhead.
- Compare two supported precisions and interpret memory, timing and output
  differences.
- Diagnose an OOM without treating reserved memory as a leak.

Turn each objective into a question. Ask NotebookLM which imported section
supports the answer and which missing source would prevent a confident answer.

## Audio Overview prompt

Explain model memory and quantization using one request and one failure
scenario. Pause to ask me to predict a shape, memory change or timing boundary.
Use only supplied sources. Identify the source and section for important claims;
separate source statements from your inference. State when material is
insufficient and identify disagreements or version differences. Do not invent
measurements or certify learning from listening.

## Study-guide prompt

Build a study guide around these objectives: Build a memory budget including
weights, activations, KV state, workspace and overhead. Compare two supported
precisions and interpret memory, timing and output differences. Diagnose an OOM
without treating reserved memory as a leak. Include one worked example, then a
different unanswered practice problem. Use only supplied sources. Identify the
source and section for important claims; separate source statements from your
inference. State when material is insufficient and identify disagreements or
version differences. Do not invent measurements or certify learning from
listening.

## Comparison prompt

Compare the primary source with each supporting source. Identify differences in
scope, definitions, versions and assumptions; do not invent a disagreement when
they are complementary. Use only supplied sources. Identify the source and
section for important claims; separate source statements from your inference.
State when material is insufficient and identify disagreements or version
differences. Do not invent measurements or certify learning from listening.

## Flashcard prompt

Create eight question cards: two definitions, two calculations, two
implementation mistakes and two limits of measurement. Put answers in a separate
section and cite each. Use only supplied sources. Identify the source and
section for important claims; separate source statements from your inference.
State when material is insufficient and identify disagreements or version
differences. Do not invent measurements or certify learning from listening.

## Quiz prompt

Ask one application question at a time about this module. Wait for my reasoning
before grading; introduce a changed assumption after a correct answer. Use only
supplied sources. Identify the source and section for important claims; separate
source statements from your inference. State when material is insufficient and
identify disagreements or version differences. Do not invent measurements or
certify learning from listening.

## Teach-back prompt

Evaluate my explanation before rewriting it. List correct statements, incomplete
statements, misconceptions, unsupported claims, missing connections and
follow-up questions. Ask me to revise first. Use only supplied sources. Identify
the source and section for important claims; separate source statements from
your inference. State when material is insufficient and identify disagreements
or version differences. Do not invent measurements or certify learning from
listening.

## Experiment-preparation prompt

Review the linked experiment plan: identify the hypothesis, controls,
independent variable, observations, resource bound and possible confounders. Ask
for missing metadata before suggesting interpretation. Use only supplied
sources. Identify the source and section for important claims; separate source
statements from your inference. State when material is insufficient and identify
disagreements or version differences. Do not invent measurements or certify
learning from listening.

## Measurement-interpretation prompt

Review my raw results and measurement boundary. Recalculate units and
denominators, inspect failures and sample count, and distinguish correlation
from causal evidence. Suggest one discriminating next experiment. Use only
supplied sources. Identify the source and section for important claims; separate
source statements from your inference. State when material is insufficient and
identify disagreements or version differences. Do not invent measurements or
certify learning from listening.

## Misconceptions to test

Challenge the module’s misconception statements and identify a counterexample.
Test especially whether the measurement boundary is being confused with a model
property, and whether a toy example is being generalized without evidence.

## Required learning evidence and exit criteria

Complete the
[module exercises](../../modules/03-model-memory-and-quantization.md) with a
prediction, raw results, configuration, interpretation and limitations. Give an
unaided teach-back and pass the module exit test. Save source-cited corrections.
NotebookLM output is study assistance, not evidence that Joshua performed an
experiment.

## What to study next

Return to the module’s next-step link after the evidence review.
