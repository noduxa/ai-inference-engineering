# Phase 1 learning harness

Status: Not started. Target: **31 October 2026**. Planned budget: **90 hours**.
Last verified: 2026-09-16.

This is Joshua Nsereko’s foundational learning path into AI systems and
inference infrastructure. It supplies study boundaries, credible sources and
evidence checks; it does not claim prior AI expertise or completed learning.

## Start here

1. Read the [curriculum](CURRICULUM.md) and its depth boundaries.
2. Reserve the [six-week schedule](SCHEDULE.md), starting 20 September 2026.
3. Open the first module and its [NotebookLM source pack](notebooklm/README.md).
4. Complete the small [exercise specifications](exercises/README.md), using the
   [evidence template](exercises/EVIDENCE_TEMPLATE.md).
5. Review your own explanation with the [assessment system](ASSESSMENT.md).

| Order | Module                                                                              | Hours | Learning status |
| ----- | ----------------------------------------------------------------------------------- | ----- | --------------- |
| 1     | [Advanced Python for AI systems](modules/01-advanced-python.md)                     | 20    | Not started     |
| 2     | [NumPy, tensors and numerical computing](modules/02-numpy-and-tensors.md)           | 10    | Not started     |
| 3     | [Essential mathematics](modules/03-essential-mathematics.md)                        | 15    | Not started     |
| 4     | [PyTorch fundamentals](modules/04-pytorch-fundamentals.md)                          | 15    | Not started     |
| 5     | [Neural-network fundamentals](modules/05-neural-networks.md)                        | 15    | Not started     |
| 6     | [Transformer architecture](modules/06-transformers.md)                              | 8     | Not started     |
| 7     | [GPU architecture, precision and memory](modules/07-gpu-architecture-and-memory.md) | 5     | Not started     |

The modules total 88 hours; the final synthesis assessment uses another two. All
study, exercises, weekly reviews and catch-up are included in that budget.
Optional full lectures and extended experiments are excluded.

## How the harness is maintained

- [Source policy](SOURCE_POLICY.md): authority, currency and replacement rules.
- [Source registry](sources.yaml): source collections and exact inspected pages.
- [Curriculum registry](curriculum.yaml): objectives, dependencies and evidence
  IDs.
- [Validation tooling](scripts/README.md): reproducible offline checks and
  optional HTTP checks.
- [Verification record](VERIFICATION.md): implementation checks and known
  limitations.

One source collection can contain several pages. Each module selects four
collections, while each NotebookLM study session uses only four to eight
relevant pages. Collections are not claimed to be single imported documents.

## Environment and scope

Start on CPU with synthetic data. Use an isolated environment and choose a
Python version supported by the installed PyTorch build. Record versions;
documentation version numbers are not evidence of locally tested compatibility.
CUDA exercises require a compatible NVIDIA GPU. Apple MPS is a different backend
and is not a substitute for claiming CUDA measurements. No cloud purchase is
assumed.

No kernel programming, advanced serving system, distributed inference or
multi-node deployment is required. When hardware is unavailable, complete the
conceptual design and keep the CUDA-specific evidence marked Not started. Do not
mark full practical completion until the missing evidence exists.

This remains personal public learning under the repository’s
[independence and privacy rules](../CONTRIBUTING.md).
