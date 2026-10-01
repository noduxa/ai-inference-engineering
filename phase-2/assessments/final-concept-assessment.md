# Concept assessment

Status: Not started. Time budget: 25 minutes.

[Assessment index](README.md) · [Rubric](rubric.md)

Attempt independently first. Record assistance and uncertainty. Answers and
review criteria belong in [facilitator guidance](facilitator-guidance.md), not
beside these questions.

1. Trace a public text request from model configuration and weights through
   tokenizer, masks, device, logits, selection, cache, detokenization and
   stream. Identify a stage that can fail before the GPU runs.
2. Explain why prefill and decode perform different work. Give a counterexample
   to a universal claim that one is always compute-bound and the other
   memory-bound.
3. What is stored in a KV cache, per layer? Distinguish query heads from KV
   heads, logical context from allocated capacity, and prefix reuse from new
   decoding.
4. Contrast static, dynamic and continuous batching. Where do admission control,
   backpressure, cancellation and fairness enter the request lifecycle?
5. Explain why INT4 weight storage might not improve latency. What do
   calibration, activation quantization, metadata and hardware support change?
6. Define TTFT, TPOT, ITL and throughput with explicit boundaries. Explain why
   GPU activity, memory occupancy and memory bandwidth are different
   measurements.
7. Map API server, scheduler, worker, cache manager, metrics and health checks.
   Which vLLM details remain introduced rather than mastered?

## Evidence

Retain the original attempt, calculation/code trace, cited corrections and score
by criterion. Link actual experiment records where requested. Missing evidence
stays Not started rather than becoming a hypothetical completed experiment.
