# Inference glossary

Last verified: 2026-09-30.

[Modules and sources](CURRICULUM.md) · [Benchmark definitions](BENCHMARKING.md)

## Prefill

Processing prompt tokens to form model state and first-token logits.

## Decode

Repeated next-token computation using available history/cache.

## KV cache

Per-layer stored attention keys and values for processed positions.

## TTFT

Elapsed time from declared request start to first output token at a declared
boundary.

## TPOT

Mean interval after the first token: (last-first)/(N-1), for N≥2.

## ITL

An individual interval between successive output tokens at the same boundary.

## Throughput

Completed work per shared wall-clock interval; name the work unit.

## Concurrency

Outstanding requests; not necessarily the executed batch size.

## Dynamic batching

Combining arriving requests using a batching policy and queue-delay budget.

## Continuous batching

Changing active requests at generation iteration boundaries.

## SLO

A service level objective with a metric, population, threshold and time window.

## Head-of-line blocking

Work at the front prevents later work from progressing.

## Backpressure

Slowing producers when consumers lack capacity.

## Admission control

Deciding whether to accept work given bounded capacity.

## Allocated memory

Live allocations tracked by a particular allocator; not all device usage.

## Reserved memory

Capacity held by an allocator, including reusable unused blocks.

## Quantization

Representing values with a restricted code set and mapping/scaling rules.

## Calibration

Using representative data to choose quantization parameters.

## Arithmetic intensity

Operations per byte transferred at the chosen memory boundary.

## Cold execution

A first execution whose initialization/cache boundary must be specified.

## Paged KV storage

Mapping logical token blocks to physical cache blocks.

## Prefix caching

Reusing compatible previously computed prefix state.

## Evidence gap

A required observation or demonstration that has not been supplied.
