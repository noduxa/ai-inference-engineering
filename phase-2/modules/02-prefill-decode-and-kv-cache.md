# Module 2: Prefill, decode and KV cache

Status: Not started. Last verified: 2026-09-30. Estimated time: **10 hours**,
including selected reading, experiments, code reading, review and catch-up.
Shared experiments are charged once in the schedule.

[Curriculum](../CURRICULUM.md) ·
[Source pack](../notebooklm/source-packs/02-prefill-decode-and-kv-cache.md) ·
[Evidence](../EVIDENCE.md) · [Schedule](../SCHEDULE.md)

## Purpose and relevance to inference engineering

Explain the different work done during prefill and decode. This connects an
observable request behavior to the implementation boundary responsible for it,
so an optimization can be tested.

## Prerequisites

Complete the preceding module’s evidence and exit test; retain its assumptions
for comparisons.

## Learning objectives

- Explain the different work done during prefill and decode.
- Estimate cache growth using layer, KV-head, sequence, batch and dtype
  assumptions.
- Distinguish logical context, allocated cache capacity, prefix reuse and
  eviction.

## Required concepts

- Autoregression
- prefill
- decode
- TTFT
- TPOT
- per-layer keys and values
- sequence and batch growth
- prompt and output length
- capacity
- context windows
- cache reuse
- paged allocation
- prefix caching
- eviction

## Detailed explanations and worked examples

### Reuse changes the work, not the causal dependency

Prefill processes the prompt and initializes per-layer cache state. Dense
attention considers prompt-position pairs; projections and feed-forward work
operate across many tokens. Decode processes a new token against cached history.
Its smaller query batch may offer less weight reuse and parallel work. Long
history still increases attention reads. These are workload hypotheses, not a
universal claim that every prefill is compute-bound and every decode is
memory-bound. The cache explanation and performance experiment separate them.

Past keys and values can be reused because causal positions do not depend on
future tokens. Each layer keeps its own state. This avoids re-projecting old
tokens, but spends memory and requires correct positions/masks. Cached attention
still reads the relevant history. A context-window limit is an architectural or
configured bound, not a promise that available memory can serve it at any batch.

For a homogeneous full-attention decoder, assume no sharing, no offload, no
quantization metadata, no padding, equal length `T` for all `B` sequences:

`KV bytes = 2 × L × B × T × Hkv × Dhead × s`

`L` is layers, `Hkv` KV heads, `Dhead` head width, `s` bytes per cache element.
The factor 2 counts K and V. With grouped-query attention use KV heads, not
query heads. With unequal lengths replace `B*T` by the sum of cached lengths.
Sliding windows, hybrid layers, page rounding, beam duplication and cache
compression require different accounting.

**Worked example:** `L=4,B=2,T=128,Hkv=2,Dhead=16,s=2` gives 131,072 bytes (128
KiB). One extra cached token per sequence adds 1,024 bytes. This is a toy
calculation, not a model measurement. The last selected output token may not yet
have been forwarded into the cache at the instant a generation loop ends.

Dynamic storage grows with use; static caches reserve capacity ahead of time.
Paged storage maps logical token blocks to separately allocated physical blocks,
reducing contiguous-allocation waste while introducing mapping/block overhead.
Prefix caching reuses matching already-computed prefixes under a compatible
model/tokenization/configuration contract. It can reduce repeated prefill work;
it does not eliminate generation of new output. Cache eviction frees reusable
capacity but can require recomputation. Do not equate evicting reusable prefixes
with arbitrarily removing active context without changing model behavior.

## Required and optional sources

- `p2-m2-cache` :
  [How caching works](https://huggingface.co/docs/transformers/cache_explanation)
  — primary, required; 0.75 h. Study: Attention matrices; Cache class; cache
  storage implementation. Skip: Unlisted APIs, training/fine-tuning, distributed
  deployment and backend installation beyond the local lab.
- `p2-m2-strategies` :
  [Cache strategies](https://huggingface.co/docs/transformers/kv_cache) —
  supporting, required; 0.5 h. Study: Comparison table; default, fixed-size and
  quantized caches. Skip: Unlisted APIs, training/fine-tuning, distributed
  deployment and backend installation beyond the local lab.
- `p2-m2-paged` :
  [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/html/2309.06180v1)
  — supporting, required; 0.5 h. Study: Sections 2–4; 6.1 experiment setup;
  Figures 2–4. Skip: Distributed deployment, custom kernels and full evaluation
  reproduction; follow only the listed sections.
- `p2-m2-prefix` :
  [Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)
  — supporting, required; 0.5 h. Study: Introduction; example workloads; limits.
  Skip: Unlisted APIs, training/fine-tuning, distributed deployment and backend
  installation beyond the local lab.

The source pack records publisher, access, terms, exact sections and import
order. Prefer the official contract over overlapping generic tutorials. Reused
sources are targeted lookups, not a requirement to reread the full document.
Optional visual study: redraw the architecture/cache diagrams in these same
sources and explain every arrow; no extra repetitive source is needed.

## Study order

1. Read the primary source’s listed sections and define the module’s terms.
2. Work through the example above by hand, checking shapes, units and
   assumptions.
3. Read supporting sources in the listed order; record one clarification or
   conflict.
4. Execute the linked practical work and retain raw observations before
   analysis.
5. Read code, give a closed-source teach-back, then correct it against sources.

## Practical exercises

- [E02](../exercises/02-prefill-decode.md)
- [E03](../exercises/03-output-length.md)
- [E04](../exercises/04-kv-cache.md)

## Code-reading task

Read the relevant path in [the local lab](../scripts/inference_lab.py): cached
forward calls, attention-mask growth and cache estimates. Annotate inputs,
outputs, ownership and one error path. Then locate the related symbol using the
source link in the official documentation at a recorded version.

## Reflection and misconceptions

- Which statement here depends on a model, backend or workload assumption?
- What observation would falsify your current explanation?
- Which result cannot be generalized to a larger model or different hardware?
- Challenge: a smaller memory footprint always means lower latency.
- Challenge: a successful run or Audio Overview proves this module is mastered.

## Common implementation mistakes

Reusing unrecorded defaults; changing multiple workload variables; confusing
logical tokens with padded positions; measuring asynchronous enqueue time;
retaining previous request state; and treating simulated results as device data.
Identify which mistakes are relevant to your experiment and show how you
checked.

## Required evidence and exit test

- Original explanation and annotated code trace
- Reproducible experiment with raw measurements or explicit hardware limitation
- Reviewed exit assessment with corrections

Without NotebookLM, demonstrate each learning objective on a fresh example.
Explain one failed hypothesis or plausible failure and what measurement would
resolve it. Apply the [rubric](../assessments/rubric.md); explicitly admit where
supplied evidence is insufficient. Reading time alone cannot pass this gate.

## Completion checklist

- [ ] Explain each required concept at application level where exercised.
- [ ] Complete a fresh calculation/trace with stated assumptions.
- [ ] Link raw observations, environment and interpretation.
- [ ] Review the exit test; correct critical misconceptions.
- [ ] Mark hardware-dependent work pending where it was not executed.

## Connection to the next module

Continue to [Model memory and quantization](03-model-memory-and-quantization.md)
after recording the exit evidence.

## Source-reading caution: mask notation

The selected HF cache explanation uses a compact multiplicative mask notation.
Do not translate a zero/one mask into multiplication of pre-softmax logits:
zeroing a blocked logit can still give it nonzero probability. The additive
negative-infinity example in Phase 1 describes the intended blocked-score
effect. Always verify the concrete framework API's boolean/additive mask
convention.
