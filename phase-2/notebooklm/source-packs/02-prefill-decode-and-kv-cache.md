# Module 2 NotebookLM source pack

Status: Planned. NotebookLM import: To be validated. Last verified: 2026-09-30.

[Module](../../modules/02-prefill-decode-and-kv-cache.md) ·
[Workflow](../README.md) · [Registry](../../sources.yaml)

## Notebook name

Joshua — Phase 2 — 02 Prefill, decode and KV cache

## Module purpose and learning objectives

- Explain the different work done during prefill and decode.
- Estimate cache growth using layer, KV-head, sequence, batch and dtype
  assumptions.
- Distinguish logical context, allocated cache capacity, prefix reuse and
  eviction.

## Prerequisites

Previous module exit evidence; retain earlier calculation assumptions.

## Ordered source table and import order

Import the exact pages below in order. Do not assume linked child pages were
imported. Keep about 4–8 active documents; remove overlapping material when it
adds no distinct explanation. Original papers are historical evidence, not
current API manuals. Check extracted equations and code manually.

| Order | Exact source URL                                                                                                        | Role                 | Selected time |
| ----- | ----------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------- |
| 1     | [How caching works](https://huggingface.co/docs/transformers/cache_explanation)                                         | primary; required    | 0.75 h        |
| 2     | [Cache strategies](https://huggingface.co/docs/transformers/kv_cache)                                                   | supporting; required | 0.5 h         |
| 3     | [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/html/2309.06180v1) | supporting; required | 0.5 h         |
| 4     | [Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)                           | supporting; required | 0.5 h         |

## Exact sections, credibility and selection

### p2-m2-cache

- Institution/authors: Hugging Face; Hugging Face contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Attention matrices; Cache class; cache storage implementation.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Trace per-layer K/V reuse and growing masks
  in a decode loop. Maintainer documentation defines the contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m2-strategies

- Institution/authors: Hugging Face; Hugging Face contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Comparison table; default, fixed-size and quantized caches.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Distinguish allocated capacity from logical
  cache length. Maintainer documentation defines the contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

### p2-m2-paged

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

### p2-m2-prefix

- Institution/authors: vLLM project; vLLM project contributors.
- Format: documentation; access: free.
- Date: Continuously maintained; page-specific date not stated; inspected
  2026-09-30.
- Study: Introduction; example workloads; limits.
- Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.
- Selection and expected knowledge: Explain when matching prefixes save prefill
  work and when they do not. Maintainer documentation defines the contract.
- Terms: Link only; publisher/author terms apply; no redistribution assumed.
- NotebookLM compatibility: To be validated manually: import this exact text
  page or publisher PDF; inspect equations/code extraction.

## Initial grounding questions

- Explain the different work done during prefill and decode.
- Estimate cache growth using layer, KV-head, sequence, batch and dtype
  assumptions.
- Distinguish logical context, allocated cache capacity, prefix reuse and
  eviction.

Turn each objective into a question. Ask NotebookLM which imported section
supports the answer and which missing source would prevent a confident answer.

## Audio Overview prompt

Explain prefill, decode and kv cache using one request and one failure scenario.
Pause to ask me to predict a shape, memory change or timing boundary. Use only
supplied sources. Identify the source and section for important claims; separate
source statements from your inference. State when material is insufficient and
identify disagreements or version differences. Do not invent measurements or
certify learning from listening.

## Study-guide prompt

Build a study guide around these objectives: Explain the different work done
during prefill and decode. Estimate cache growth using layer, KV-head, sequence,
batch and dtype assumptions. Distinguish logical context, allocated cache
capacity, prefix reuse and eviction. Include one worked example, then a
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

Complete the [module exercises](../../modules/02-prefill-decode-and-kv-cache.md)
with a prediction, raw results, configuration, interpretation and limitations.
Give an unaided teach-back and pass the module exit test. Save source-cited
corrections. NotebookLM output is study assistance, not evidence that Joshua
performed an experiment.

## What to study next

Return to the module’s next-step link after the evidence review.
