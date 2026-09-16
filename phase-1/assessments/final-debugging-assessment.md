# Final debugging assessment

Assessment ID: final-debugging. Status: Not started. Budget: 25 minutes.

[Rubric](rubric.md) · [Plan](../ASSESSMENT.md)

All scenarios are hypothetical. For each, rank two plausible causes, propose a
minimal discriminating check and describe a safe corrective action. Do not
diagnose from one metric alone or report invented measurements.

1. An async service stops responding while a task performs a long Python
   arithmetic loop. A thread-pool rewrite fails to improve CPU throughput. What
   assumptions about waiting, the GIL, native code and process overhead must be
   checked?
2. A NumPy “memory optimization” introduces incorrect values after a slice is
   modified. A broadcasted intermediate is much larger than either input. How do
   you investigate aliasing and shape expansion separately?
3. A PyTorch run reports mixed devices and later accumulates gradients across
   iterations. A colleague says eval() should fix both. Diagnose the claims and
   propose independent tests for devices and gradient handling.
4. A tiny CUDA operation appears much faster when measured without
   synchronization; the full request is slower than CPU. What timing boundaries,
   transfers, warmup and sample counts are missing? What does the profiler add?
5. GPU reserved memory stays high after tensors are released, then a larger
   request fails. Explain live references, cache reservation, workspace/headroom
   and why empty_cache() is not a universal fix. Describe bounded cleanup and
   retry.
6. Batched generation changes when padding is added; a sampling comparison
   changes several settings and a seed at once. Which masks, positions,
   tokenization and sampling controls need inspection? Avoid asserting a
   specific root cause.
