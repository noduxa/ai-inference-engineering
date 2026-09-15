# Benchmarks

**Status: Not started.** No benchmark numbers or system rankings are published.

## Planned methodology

1. State the question and select a reproducible baseline.
2. Record CPU, RAM, GPU count/model/VRAM, software versions, model revision,
   tokenizer, precision, server settings and load-generator placement.
3. Control prompt/output lengths, concurrency, arrival pattern, caching state,
   seeds, warmup and repetitions. Use synthetic data.
4. Explain unavoidable differences between Transformers, Ollama and vLLM.
5. Preserve reviewed raw data and the script that calculates summaries.
6. Include errors, timeouts, variability, sample counts and measurement
   overhead.
7. Re-run surprising outcomes before drawing conclusions.

## Metrics and definitions to record

- TTFT: specify when request timing starts and the first token is observed.
- TPOT and inter-token latency: specify averaging and per-token interval
  methods.
- Requests per second and tokens per second: specify successful requests and
  input/output token accounting over the measurement window.
- P50, P95 and P99 latency: specify the latency type and percentile method.
- GPU utilization and VRAM consumption: specify sampling interval and
  peak/average.
- Error rate: include the total attempted request denominator.
- Cost per million tokens: record currency, pricing source/date, billed
  duration, included resources and whether the denominator counts input or
  output tokens.

## Publication gate

Publish only validated results with reproduction instructions, raw evidence,
limitations and source links. Do not generalize beyond the tested conditions.
Keep unvalidated procedures marked **To be validated** and report failed runs.

See the [benchmark runbook](../runbooks/benchmark-inference-server.md) and
[contribution standards](../CONTRIBUTING.md).
