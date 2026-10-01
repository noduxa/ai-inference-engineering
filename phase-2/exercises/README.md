# Phase 2 experiments

Status: Not started. These specifications supply no completed learner results.

- [E01: Where does each request stage begin and end?](01-request-lifecycle.md)
- [E02: How does prompt length affect first-token work?](02-prefill-decode.md)
- [E03: How does output length change total latency?](03-output-length.md)
- [E04: Does a formula explain observed request memory growth?](04-kv-cache.md)
- [E05: Does a smaller supported floating representation reduce memory and
  latency?][nav-1]
- [E06: When does more outstanding work improve throughput and harm
  latency?][nav-2]
- [E07: Which first-run costs disappear in later requests?](07-warm-cold.md)
- [E08: Which measured component explains one reproducible performance
  symptom?][nav-3]
- [E09: How can resource exhaustion be diagnosed without destabilizing the
  machine?][nav-4]

Use the [benchmark standard](../BENCHMARKING.md),
[lab setup](../scripts/README.md) and [evidence gate](../EVIDENCE.md).
E06/E07/E08/E09 support multiple modules; the schedule charges each execution
once, with later interpretation in context.

[nav-1]: 05-precision.md
[nav-2]: 06-batching-concurrency.md
[nav-3]: 08-bottleneck.md
[nav-4]: 09-resource-limits.md
