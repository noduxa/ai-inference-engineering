# Module 6 NotebookLM source pack

Status: Planned. Source inspection: Verified. NotebookLM import: To be
validated. Last verified: 2026-09-30.

[NotebookLM workflow](../README.md) · [Module](../../modules/06-transformers.md)
· [Source registry](../../sources.yaml)

## Module purpose

A model-serving request is easier to reason about when tokens, masks, attention
and generation are concrete operations rather than labels.

## Learning objectives

- Trace text through tokens, embeddings, transformer blocks and output logits.
- Calculate tiny masked attention and annotate every intermediate shape.
- Distinguish encoder, decoder, encoder-decoder and decoder-only models.
- Explain and inspect one-token-at-a-time generation and sampling controls.

## Prerequisites

Preceding curriculum modules; review unresolved prerequisite exit tests.

## Ordered source table

Four curated source collections: one primary and three supporting. A collection
can contain several individual pages. Import **4–8 relevant pages at a time**,
not every page below at once. An index URL does not import linked chapters. Use
the session batches below and add missing sections only when needed.

| Order | Registry ID     | Source collection                                                                                                       | Role       | Selected reading |
| ----- | --------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 1     | `tr-d2l`        | [Attention and transformer architecture](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html) | primary    | 1.25 h           |
| 2     | `tr-hf`         | [Hugging Face LLM course: models and tokenization](https://huggingface.co/learn/llm-course/chapter1/4)                  | supporting | 1 h              |
| 3     | `tr-generation` | [Transformers generation strategies](https://huggingface.co/docs/transformers/generation_strategies)                    | supporting | 0.5 h            |
| 4     | `tr-paper`      | [Attention Is All You Need](https://arxiv.org/abs/1706.03762)                                                           | supporting | 0.5 h            |

## Exact sections, selection reasons and access

### tr-d2l: Attention and transformer architecture

Expected knowledge: Draw transformer blocks and calculate tiny attention with
explicit shapes and masks.

- Author/institution: Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola;
  Dive into Deep Learning.
- Format: textbook. Access: free.
- Publication/update: Online edition 1.0.3; exact page update not stated.
- Selected study time: 1.25 h; included in this module’s budget.
- Authority and phase fit: Accessible diagrams and tensor-level explanations
  accompany the original paper.
- Terms: CC BY-SA 4.0 text; separate code terms.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                                                                         | Study these sections                                                                               | Skip for Phase 1                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [Attention scoring](https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html)                                 | Scaled dot-product attention and masked softmax                                                    | Full training loops and machine-translation experiments |
| [Multi-head attention](https://d2l.ai/chapter_attention-mechanisms-and-transformers/multihead-attention.html)                                      | Parallel heads and shape transformations                                                           | Full training loops and machine-translation experiments |
| [Self-attention and positional encoding](https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html) | Self-attention; positional information                                                             | Full training loops and machine-translation experiments |
| [Transformer](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html)                                                       | Architecture; feed-forward network; residual connections; layer normalization; encoder and decoder | Full training loops and machine-translation experiments |

### tr-hf: Hugging Face LLM course: models and tokenization

Expected knowledge: Trace tokens and batching inputs and distinguish practical
transformer model families.

- Author/institution: Hugging Face course contributors; Hugging Face.
- Format: course. Access: free.
- Publication/update: Not stated; rolling documentation.
- Selected study time: 1 h; included in this module’s budget.
- Authority and phase fit: Official course connects architecture to tokenizers
  and decoder-only use without assigning fine-tuning.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                        | Study these sections                              | Skip for Phase 1                                    |
| --------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------- |
| [How transformers work](https://huggingface.co/learn/llm-course/chapter1/4)       | Encoder, decoder and encoder-decoder overview     | Hosted demos, model training and optional exercises |
| [Transformer architectures](https://huggingface.co/learn/llm-course/chapter1/6)   | Causal next-token prediction                      | Hosted demos, model training and optional exercises |
| [Tokenizers](https://huggingface.co/learn/llm-course/chapter2/4)                  | Vocabulary; tokenization; encoding and decoding   | Hosted demos, model training and optional exercises |
| [Handling multiple sequences](https://huggingface.co/learn/llm-course/chapter2/5) | Batching, padding, attention masks and truncation | Hosted demos, model training and optional exercises |

### tr-generation: Transformers generation strategies

Expected knowledge: Explain the effects and assumptions of greedy decoding,
temperature, top-k and top-p.

- Author/institution: Transformers contributors; Hugging Face.
- Format: documentation. Access: free.
- Publication/update: Not stated; rolling documentation.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Current framework reference grounds sampling
  vocabulary and avoids unsupported decoding folklore.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                        | Study these sections                                    | Skip for Phase 1                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------ |
| [Generation strategies](https://huggingface.co/docs/transformers/generation_strategies)           | Greedy decoding and multinomial sampling                | Beam search, assisted decoding and advanced generation |
| [Generation configuration](https://huggingface.co/docs/transformers/main_classes/text_generation) | do_sample, temperature, top_k, top_p and max_new_tokens | Cache implementations and advanced generation controls |

### tr-paper: Attention Is All You Need

Expected knowledge: Identify the original encoder-decoder design and relate its
attention equation to a toy calculation.

- Author/institution: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
  Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin; arXiv
  / NeurIPS.
- Format: paper. Access: free.
- Publication/update: 2017-06-12 first submission.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Original transformer architecture paper establishes
  provenance; read only after the accessible explanation.
- Terms: arXiv distribution terms; do not redistribute the paper.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                             | Study these sections                                                         | Skip for Phase 1                                                |
| ------------------------------------------------------ | ---------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [Original paper](https://arxiv.org/abs/1706.03762)     | Figure 1; Sections 3.1–3.5; equation (1); use the PDF linked by the abstract | Training settings, benchmark tables and performance comparisons |
| [Full paper HTML](https://arxiv.org/html/1706.03762v7) | Figure 1; Sections 3.1–3.5 and equation (1)                                  | Training and benchmark results                                  |

## Optional visual lane and overlap decisions

Use D2L’s transformer diagram as the intuitive companion to the original paper.
The paper establishes the original architecture; Hugging Face explains practical
model families and generation.

No additional secondary blog is selected: the first-party diagrams and textbook
explanations cover the visual need without another overlapping source.

## Notebook name and adding sources

Suggested name: **Joshua — Phase 1 — 06 Transformer architecture**.

Add pages in the source-table order within the current session batch. Name each
import with its registry ID and section title. Check that the actual page text,
code and equations appear before asking questions. Retain at most eight active
pages; rotate earlier pages out after saving your own cited notes. Re-add an
omitted page if a prompt needs it. Do not use an index as a substitute for
content.

## Session import batches

- **Text and architecture:** Tokenizers; Handling multiple sequences; Attention
  scoring; Multi-head attention; Self-attention and positional encoding;
  Transformer; Transformer architectures; Full paper HTML.
- **Generation:** How transformers work; Transformer architectures; Tokenizers;
  Handling multiple sequences; Generation strategies; Generation configuration.

## Initial NotebookLM questions

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

- Which tensors are mixed by attention, and along which dimension?
- How do causal and padding masks differ?
- What changes between two consecutive generation steps?

## Audio Overview customization prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Give a short spoken orientation to transformer architecture for a backend
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

- One token is always one word.
- An attention mask and token padding are the same thing.
- The original transformer paper describes only a decoder-only model.
- Attention weights are output vocabulary probabilities.
- Changing temperature changes learned weights.

## Practical exercise

Start with `TR-01` in the
[module exercise specifications](../../exercises/06-transformers.md), then
complete the remaining exercises. Ask for a plan critique before executing;
never ask the model to fabricate an observation or to silently fill in missing
measurements.

## Required learning evidence

- Own-word explanation with inspected source citations.
- Exercise code/calculations and explicit correctness checks.
- Environment record, actual observations, failed attempts and limitations.
- Prediction-versus-result comparison and a reviewed teach-back.

## Exit criteria

- Complete the 4 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

Use the [assessment rubric](../../assessments/rubric.md); neither imported
sources nor generated study artifacts establish mastery.

## What to study next

Continue to [Module 7](../../modules/07-gpu-architecture-and-memory.md) after
the exit check.

## Comparison prompt

Using only the imported sources, compare their scope, definitions and
assumptions. Cite the section behind each important claim, distinguish inference
from source statements, identify real disagreements and say when coverage is
insufficient. Do not invent a conflict between complementary sources.

## Teach-back prompt

Evaluate my explanation before rewriting it: correct statements, incomplete
statements, misconceptions, unsupported claims, missing connections and
questions I should answer next. Cite source sections and ask me to revise first.
An Audio Overview is preparation, not evidence of understanding.

## Experiment-preparation prompt

Check my linked exercise plan against the supplied sources. Identify controls,
changed variable, observations, resource bounds and missing prerequisites.
Require my prediction before execution; never invent an observed result.

## Measurement-interpretation prompt

Use the [shared measurement-review prompt](../prompts/measurement-review.md).
Check the exercise's actual shapes, units, timing/memory boundaries and
correctness. State what the supplied observations cannot establish and ask for
one next test.
