# Diagnostic assessment

Status: Not started. Time budget: 30 minutes.

[Assessment index](README.md) · [Rubric](rubric.md)

Attempt independently first. Record assistance and uncertainty. Answers and
review criteria belong in [facilitator guidance](facilitator-guidance.md), not
beside these questions.

For each scenario: define the symptom, request missing metadata, establish a
reproducible baseline, propose two explanations and select one-variable tests.

1. GPU activity is low and TTFT is high for short prompts. What would
   distinguish CPU tokenization, insufficient work, device transfers and
   measurement mistakes?
2. Requests succeed individually but OOM with concurrent long outputs. Explain
   weight, cache, activation/workspace, live-reference and allocator
   possibilities.
3. INT4 weights occupy less memory, yet E2E latency increases. How would you
   check kernel support, conversion/dequantization, warm-up and workload parity?
4. Aggregate tokens/s rises as concurrency increases, but P95 TTFT worsens.
   Explain a plausible queueing mechanism and a bounded admission/SLO
   experiment.
5. A profiler timeline shows host gaps before kernels. Why is correlation
   insufficient? What repeatable intervention would strengthen the explanation?
6. Present E08's actual baseline and changed-variable evidence. State whether
   the hypothesis is supported, rejected or unresolved, and why it may not
   generalize.

## Evidence

Retain the original attempt, calculation/code trace, cited corrections and score
by criterion. Link actual experiment records where requested. Missing evidence
stays Not started rather than becoming a hypothetical completed experiment.
