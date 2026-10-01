# Code-reading assessment

Status: Not started. Time budget: 25 minutes.

[Assessment index](README.md) · [Rubric](rubric.md)

Attempt independently first. Record assistance and uncertainty. Answers and
review criteria belong in [facilitator guidance](facilitator-guidance.md), not
beside these questions.

Read this deliberately incomplete pseudocode without executing it:

```python
cache = None
for step in range(limit):
    result = model(input_ids=ids, past_key_values=cache, use_cache=True)
    next_id = result.logits[:, -1].argmax(-1, keepdim=True)
    cache = result.past_key_values
    ids = concatenate([ids, next_id], axis=1)
    print(decode(next_id))
```

1. Explain the intended lifecycle and the difference between logits and token
   IDs.
2. Identify a cache/input mismatch after the first iteration. Describe the mask
   and position information a correct version may need at the chosen API
   version.
3. Explain why printing decoded single IDs does not prove correct streamed text
   assembly or provide reliable client-visible ITL.
4. Identify missing mode/gradient, stop-condition and timing controls.
5. Read the repository lab's `request` function and annotate where it addresses
   these issues and where its behavior is still deliberately simplified.
6. Locate one related production symbol through official source links. Record
   revision, input/output contract and one test you would inspect in Phase 3.

## Evidence

Retain the original attempt, calculation/code trace, cited corrections and score
by criterion. Link actual experiment records where requested. Missing evidence
stays Not started rather than becoming a hypothetical completed experiment.
