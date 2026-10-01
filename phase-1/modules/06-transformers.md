# Module 6: Transformer architecture

Status: Not started. Estimated time: **8 hours**, including practice, review and
catch-up. Last verified: 2026-09-30.

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

## Detailed explanation and worked example

Tokenization converts text into vocabulary IDs; an embedding lookup maps each ID
to a learned vector. Token count is not character count. The tokenizer and model
revision form one contract. Padding aligns batches; truncation discards context.
Padding masks identify non-content positions, while causal masks prevent a
position from reading future positions. Mask conventions differ by API: verify
whether True means allowed or blocked.

For one attention head, `Q=XWq`, `K=XWk`, `V=XWv`, and
`A=softmax(QKᵀ/sqrt(dk)+M)` ; output is `AV` . An additive mask uses zero for
allowed scores and negative infinity for blocked scores before softmax.
Multiplying a blocked score by zero is not equivalent. The
[original paper](https://arxiv.org/html/1706.03762v7) defines scaled attention;
[D2L](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html)
provides the accessible architecture walkthrough.

Worked example: let `Q=K=[[1,0],[0,1]]`, `V=[[2,0],[0,4]]`, `dk=2`. For the
first causally masked row, attention weights are `[1,0]` and output `[2,0]`. For
the second row, scores are `[0,1/sqrt(2)]`; calculate its softmax and weighted
value sum. This is an analytic example, not experimental evidence. An
all-blocked row needs explicit handling; naive softmax can produce NaNs.

Multi-head attention learns different projections, concatenates their results
and projects again. Positional information distinguishes order; a feed-forward
layer transforms each position. Residual connections add a sublayer's input to
its output, and normalization controls scale. Exact norm placement and
positional schemes depend on architecture; do not assume every modern model
reproduces the 2017 design.

Encoders build contextual representations, usually with bidirectional attention.
Decoders use causal self-attention; an encoder-decoder adds cross-attention to
encoder outputs. A decoder-only language model projects its final hidden state
to vocabulary logits. The last prompt position predicts the first continuation
token. Append the selected token and repeat until EOS or a length/stop
condition. Sampling uses a distribution rather than always choosing argmax.
Temperature rescales logits, top-k keeps a fixed count, and top-p keeps a
probability mass; none establishes factual correctness. See the selected HF
generation reference.

## Code-reading task and implementation mistakes

Trace shapes
`[B,T] → [B,T,D] → [B,H,T,D/H] → [B,H,T,T] → [B,T,D] → [B,T,Vocab]`. Inspect
D2L's decoder block and identify its causal behavior. Explain which positions a
second generated token can attend to. Common mistakes include treating an
attention matrix as embeddings, using the wrong softmax axis, dropping padding
masks, confusing model parameters with request tokens and reporting sampling
differences as quality improvements without evaluation. Module 7 accounts for
the memory required by these tensors.

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

## Connection to the next module

Continue to [gpu architecture and memory](07-gpu-architecture-and-memory.md)
after the exit test.
