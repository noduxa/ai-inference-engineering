# Module 6: Transformer architecture

Status: Not started. Estimated time: **8 hours**, including practice, review and
catch-up. Last verified: 2026-09-16.

[Curriculum](../CURRICULUM.md) · [Schedule](../SCHEDULE.md) ·
[Source pack](../notebooklm/source-packs/06-transformers.md)

## Why this matters

A model-serving request is easier to reason about when tokens, masks, attention
and generation are concrete operations rather than labels.

## Learning objectives

- Trace text through tokens, embeddings, transformer blocks and output logits.
- Calculate tiny masked attention and annotate every intermediate shape.
- Distinguish encoder, decoder, encoder-decoder and decoder-only models.
- Explain and inspect one-token-at-a-time generation and sampling controls.

## Prerequisites

Complete the preceding module’s core shape, calculation or programming checks;
revisit any unresolved prerequisite before continuing.

## Required concepts

- Tokenization and vocabulary
- Embeddings and sequence representation
- Queries, keys and values
- Scaled dot-product attention
- Attention masks and self-attention
- Multi-head attention
- Positional information
- Feed-forward layers
- Residual connections and normalization
- Encoder architecture
- Decoder architecture
- Encoder-decoder architecture
- Decoder-only transformers
- Autoregressive generation
- Logits and softmax
- Sampling, temperature, top-k and top-p
- Padding, truncation and batching
- Model parameters
- Inference one token at a time: conceptual request walkthrough

## Recommended sources

- `tr-d2l` —
  [Attention and transformer architecture](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html)
  (primary; selected reading 1.25 h).
- `tr-hf` —
  [Hugging Face LLM course: models and tokenization](https://huggingface.co/learn/llm-course/chapter1/4)
  (supporting; selected reading 1 h).
- `tr-generation` —
  [Transformers generation strategies](https://huggingface.co/docs/transformers/generation_strategies)
  (supporting; selected reading 0.5 h).
- `tr-paper` — [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
  (supporting; selected reading 0.5 h).

Exact page links, selected sections, exclusions, access terms and import order
are in the source pack. Reading times are selective budgets, not estimates for
completing entire documentation collections.

## Study order

1. Inspect tokenization, vocabulary and batched masks in TR-02.
2. Calculate TR-01 attention and annotate Q/K/V, normalization axis and mask
   effects.
3. Build a diagram of attention heads, positional information, residuals,
   normalization and feed-forward layers.
4. Read the original paper’s selected architecture sections after D2L;
   distinguish its architecture from decoder-only generation in TR-03.
5. Compare synthetic sampling controls in TR-04 and finish with a two-token
   generation teach-back.

## Exercises and deliverables

[Open the exercise specifications](../exercises/06-transformers.md).

- `TR-01` — Manual scaled dot-product attention.
- `TR-02` — Tokenizer and mask inspection.
- `TR-03` — Decoder-only generation walkthrough.
- `TR-04` — Sampling parameters.

Deliver a short concept note, original calculations/code, environment record,
actual measurements where applicable, and a teach-back. Use the
[evidence template](../exercises/EVIDENCE_TEMPLATE.md). No outputs are supplied
as completed work.

## Reflection questions

- Which tensors are mixed by attention, and along which dimension?
- How do causal and padding masks differ?
- What changes between two consecutive generation steps?

## Common mistakes to challenge

The following statements are deliberately questionable; correct them with
sources:

- One token is always one word.
- An attention mask and token padding are the same thing.
- The original transformer paper describes only a decoder-only model.
- Attention weights are output vocabulary probabilities.
- Changing temperature changes learned weights.

## Exit test

Without NotebookLM, answer the reflection questions and explain a fresh variant
of one exercise. Then use sources to check your answer. Demonstrate a working
application, predict its outcome and diagnose one plausible failure. Record
assistance, corrections and evidence using the
[rubric](../assessments/rubric.md).

- Complete the 4 exercise specifications or explicitly record hardware-limited
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
