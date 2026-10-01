# Phase 2 rubric

[Assessment index](README.md) · [Readiness gate](phase-3-readiness-review.md)

Status: Planned. Score the evidence, not confidence or hours spent.

| Level       | 0                  | 1                                | 2                                           | 3                                         |
| ----------- | ------------------ | -------------------------------- | ------------------------------------------- | ----------------------------------------- |
| Recognition | Incorrect/absent   | Recognizes with prompts          | Identifies independently                    | Distinguishes close alternatives          |
| Explanation | Unsupported        | Repeats a definition             | Explains mechanism and assumptions          | Connects mechanisms and limits            |
| Application | No usable evidence | Works only with substantial help | Solves a fresh calculation/trace/experiment | Transfers to a changed workload           |
| Diagnosis   | Guesses            | Names a plausible cause          | Designs a controlled discriminating test    | Interprets competing evidence and revises |

Assess lifecycle, prefill/decode, cache/memory, representation, batching,
metrics, benchmarking, profiling and server architecture separately. Require
recognition, explanation and application at least 2 in every core domain.
Require diagnosis at least 2 for timing validity, OOM/cache growth and one real
performance symptom; at least 1 elsewhere. Require source-backed corrections and
disclosure of help.

Critical errors block progression: claiming physical GPU evidence from a
simulation; using the wrong KV-head count without recognizing the assumption;
conflating enqueue time with completed device execution; presenting unmatched
system comparisons as causal; or inventing observations. Do not average these
away. Hardware-limited areas remain pending, with a specific follow-up plan.

A reviewer records evidence paths, scores, unresolved questions and one unseen
reassessment variant. A delayed self-review is acceptable if declared. This gate
permits beginning vLLM study; it does not certify professional expertise.
