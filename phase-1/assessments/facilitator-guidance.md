# Facilitator guidance — separate from learner questions

[Assessment index](README.md) · [Rubric](rubric.md) ·
[Evidence gate](../EVIDENCE.md)

Status: Planned. Read after the learner attempts the assessments.

Use fresh variants rather than grading memorized worked examples. Ask for shape,
unit and ownership reasoning before execution. Recognition alone is
insufficient.

- Python: require the distinction between I/O waits, pure-Python CPU execution,
  native GIL-releasing work and process overhead. A generator retains
  references; shallow copying does not recursively isolate nested objects.
- NumPy/math: right-aligned broadcasting and contracted matrix dimensions must
  agree. Check stable softmax, local gradient reasoning and GB/GiB conversion.
- PyTorch: eval mode and disabled gradient recording solve different problems.
  Verify parameter updates, cleared gradients, device alignment and output
  checks.
- Attention: require Q/K/V shapes, causal versus padding masks, normalization
  axis and the use of last-position logits for next-token prediction.
- Memory/timing: payload is not total process/device memory; CUDA dispatch is
  asynchronous. Reserved memory is not automatically a leak.

Ask Joshua to interpret one real exercise record: what was predicted, measured,
controlled and left uncertain? Do not award hardware evidence for a simulation.
Record criterion scores, exact evidence paths, unresolved misconceptions and a
reassessment question. The facilitator may be Joshua performing a delayed
self-review, but assistance must be disclosed and an unseen variant used.
