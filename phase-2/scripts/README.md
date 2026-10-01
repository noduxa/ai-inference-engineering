# Local lab and shared validation

Last verified: 2026-09-30. Learner experiment status: Not started.

[Experiments](../exercises/README.md) ·
[Shared validation](../../scripts/README.md)

## Setup

Use Python 3.12+ in an isolated environment. From the repository root:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r phase-2/scripts/requirements-lab.txt
.venv/bin/python phase-2/scripts/inference_lab.py --help
```

The pinned environment is for the small local lab. For CUDA, use the official
[PyTorch selector](https://pytorch.org/get-started/locally/) and record the
exact resolved wheel/runtime versions. CPU is sufficient for the core exercises.
A GPU comparison remains pending if no supported accelerator is available.

## Start small

```bash
.venv/bin/python phase-2/scripts/inference_lab.py --toy --fixed-output \
  --out outputs/phase-2/smoke.json
.venv/bin/python phase-2/scripts/inference_lab.py --budget-only \
  --out outputs/phase-2/budget.json
```

The toy path initializes random tiny GPT-2 weights and synthetic token IDs. It
checks instrumentation, not language quality. The default model path downloads
[SmolLM2-135M](https://huggingface.co/HuggingFaceTB/SmolLM2-135M), an ungated
public Apache-2.0 model, using safetensors and no remote code or implicit
account token. Allow roughly 1 GB of local disk/RAM headroom; check actual
availability first. The resolved revision is stored; pass its full SHA on
subsequent comparisons. No cloud service or public endpoint is started.

## Measurement contract

The lab timestamps local token availability after host materialization. It
records preparation, forward calls, token gaps, text snapshots and a shared
completion window. It synchronizes CUDA/MPS and explicitly records
instrumentation limitations. It does not claim client-visible streaming latency.
Homogeneous batches and a CPU worker pool are deliberately limited; neither is a
continuous batching engine. Decode is greedy; fixed-output mode ignores EOS for
controlled length studies and must be labeled artificial.

`--profile` runs an additional, separate request after the timing samples and
writes a local trace. `--no-cache` recomputes the prefix for diagnosis. The
budget simulation allocates no tensors and cannot prove physical OOM recovery.
Output files are not overwritten. Remove personal paths from traces before
publication.

Run dependency-free lab tests through the
[shared tools](../../scripts/README.md).

## Integration tests

```bash
.venv/bin/python -m unittest discover -s phase-2/scripts/tests -v
```

These use random tiny models without downloads. They check cache/no-cache token
equivalence, batch/concurrency accounting, timing ordering and dtype payload.
`queue_s` and `submitted_e2e_s` include local worker-pool waiting; token
timestamps and `metrics.e2e_s` start inside the worker. No field measures HTTP
transport. Finite-logit checks and text snapshots add instrumentation overhead.

Unsupported device/dtype combinations and runtime failures can abort before a
results file is written. Record the command, exit status and sanitized error in
the experiment report; a missing JSON file is not a successful trial. Include
failed attempts in error-rate accounting.
