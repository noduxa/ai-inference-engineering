# Phase 1 rubric

Status: Planned; no learner scores have been recorded.

[Assessment plan](../ASSESSMENT.md) · [Weekly review](weekly-review-template.md)

## Four dimensions, scored separately

| Dimension   | 0                                 | 1                                        | 2                                                | 3                                                     |
| ----------- | --------------------------------- | ---------------------------------------- | ------------------------------------------------ | ----------------------------------------------------- |
| Recognition | Cannot identify the concept       | Recognizes a term with cues              | Distinguishes it from a nearby concept           | Recognizes it in an unfamiliar example                |
| Explanation | Missing or incorrect              | Repeats a definition without mechanism   | Explains mechanism and assumptions               | Explains limits and a valid counterexample            |
| Application | No working evidence               | Follows an example with substantial help | Solves a fresh small task and checks correctness | Transfers the skill and justifies measurement choices |
| Diagnosis   | Guesses or proposes unsafe action | Suggests a plausible cause               | Uses a discriminating check and safe correction  | Tests competing causes and records uncertainty        |

## Decision rules

Record scores for each module objective, not only a single average. Application
objectives require at least 2 in recognition, explanation and application.
Recognition-only topics follow the [curriculum depth contract](../CURRICULUM.md)
and require recognition/explanation of 2, not advanced implementation.

Early diagnosis requires at least 2 on three distinct final debugging scenarios,
including the memory/resource scenario, and at least 1 on the others. No
critical misconception may remain unresolved: examples include equating eval()
with disabled autograd, confusing matrix multiplication with element-wise
multiplication, using unsynchronized timing as completed CUDA latency, or
calling simulated OOM an observed device failure.

Evidence must be linked, reproducible and correctly labeled. Correct answers
obtained after help are assisted corrections until a fresh independent retry.
Missing practical CUDA evidence remains a limitation; it cannot be averaged
away. A conceptual/CPU pass can be recorded separately from full practical
completion.

## Reviewer record

For each objective: initial score, independent evidence, assistance used,
source-backed correction, retry result and unresolved limitations. Reviews may
be self-reviews if clearly labeled. This rubric is a learning tool, not a
credential or a claim of externally recognized expertise.
