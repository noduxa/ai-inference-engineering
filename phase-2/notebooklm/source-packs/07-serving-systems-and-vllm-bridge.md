# Module 7 NotebookLM source pack

Status: Planned. NotebookLM import: To be validated. Last verified: 2026-09-30.

[Module](../../modules/07-serving-systems-and-vllm-bridge.md) ·
[Workflow](../README.md) · [Registry](../../sources.yaml)

## Notebook name

Joshua — Phase 2 — 07 Serving systems and the vLLM bridge

## Module purpose and learning objectives

- Map API, scheduling, execution, cache and streaming responsibilities.
- Explain PagedAttention conceptually without claiming kernel expertise.
- Prepare a code-reading and development plan for Phase 3 with evidence gaps.

## Prerequisites

Previous module exit evidence; retain earlier calculation assumptions.

## Ordered source table and import order

Import the exact pages below in order. Do not assume linked child pages were
imported. Keep about 4–8 active documents; remove overlapping material when it
adds no distinct explanation. Original papers are historical evidence, not
current API manuals. Check extracted equations and code manually.

| Order | Exact source URL                                                                                                        | Role                 | Selected time |
| ----- | ----------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------- |
| 1     | [vLLM Architecture Overview](https://docs.vllm.ai/en/latest/design/arch_overview/)                                      | primary; required    | 0.75 h        |
| 2     | [vLLM Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/)                                           | supporting; required | 0.5 h         |
| 3     | [vLLM Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/)                                                | supporting; required | 0.5 h         |
| 4     | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/html/2309.06180v1) | supporting; optional | 0.5 h         |

## Exact sections, credibility and selection

### p2-m7-arch

- Institution/authors: vLLM project; vLLM project contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Process architecture; API server; engine core; workers and model
  execution.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Map request handling to scheduler and worker
  responsibilities. Maintainer documentation defines the contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m7-online

- Institution/authors: vLLM project; vLLM project contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: OpenAI-compatible server; supported APIs; basic and metrics APIs.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Distinguish API compatibility from identical
  model behavior and operational readiness. Maintainer documentation defines the
  contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m7-metrics

- Institution/authors: vLLM project; vLLM project contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Metrics endpoint; request latency, queue, token and cache metric
  examples.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Relate aggregate operational counters to
  individual request observations. Maintainer documentation defines the
  contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m7-paged

- Institution/authors: ACM SOSP / arXiv; Woosuk Kwon et al..
- Format: paper; access: free.
- Date: 2023-09-12 (v1).
- Study: Sections 2–4; 6.1 experiment setup; Figures 2–4.
- Skip: Distributed deployment, custom kernels and full evaluation reproduction;
  follow only the listed sections.
- Selection and expected knowledge: Understand block-based KV allocation and
  inspect historical workload assumptions. Original peer-reviewed systems
  research, with historical results kept separate from current behavior.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

## Initial grounding questions

- Map API, scheduling, execution, cache and streaming responsibilities.
- Explain PagedAttention conceptually without claiming kernel expertise.
- Prepare a code-reading and development plan for Phase 3 with evidence gaps.

Turn each objective into a question. Ask NotebookLM which imported section
supports the answer and which missing source would prevent a confident answer.

## Audio Overview prompt

Explain serving systems and the vllm bridge using one request and one failure
scenario. Pause to ask me to predict a shape, memory change or timing boundary.
Use only supplied sources. Identify the source and section for important claims;
separate source statements from your inference. State when material is
insufficient and identify disagreements or version differences. Do not invent
measurements or certify learning from listening.

## Study-guide prompt

Build a study guide around these objectives: Map API, scheduling, execution,
cache and streaming responsibilities. Explain PagedAttention conceptually
without claiming kernel expertise. Prepare a code-reading and development plan
for Phase 3 with evidence gaps. Include one worked example, then a different
unanswered practice problem. Use only supplied sources. Identify the source and
section for important claims; separate source statements from your inference.
State when material is insufficient and identify disagreements or version
differences. Do not invent measurements or certify learning from listening.

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
[module exercises](../../modules/07-serving-systems-and-vllm-bridge.md) with a
prediction, raw results, configuration, interpretation and limitations. Give an
unaided teach-back and pass the module exit test. Save source-cited corrections.
NotebookLM output is study assistance, not evidence that Joshua performed an
experiment.

## What to study next

Return to the module’s next-step link after the evidence review.
