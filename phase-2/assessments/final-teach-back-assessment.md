# Teach-back assessment

Status: Not started. Time budget: 25 minutes.

[Assessment index](README.md) · [Rubric](rubric.md)

Attempt independently first. Record assistance and uncertainty. Answers and
review criteria belong in [facilitator guidance](facilitator-guidance.md), not
beside these questions.

Explain one request from public text to final streamed output in your own words.
Use a drawing and an assumed small model configuration. Include:

- First-token versus later-token work, cache state and mask changes.
- Weight and KV memory calculations with explicit architecture/dtype
  assumptions.
- A scheduler decision involving a long and short request.
- A fair timing boundary and why buffering complicates streaming metrics.
- One measured result, its limits and a plausible alternative explanation.
- How API, scheduler, cache and worker responsibilities connect to vLLM reading.
- Three things you do not yet know and a practical next question for each.

First attempt without NotebookLM. Then use the source-grounded teach-back
prompt; retain original wording, feedback, cited corrections and a second
attempt. Do not count the generated replacement explanation as your unaided
answer.

## Evidence

Retain the original attempt, calculation/code trace, cited corrections and score
by criterion. Link actual experiment records where requested. Missing evidence
stays Not started rather than becoming a hypothetical completed experiment.
