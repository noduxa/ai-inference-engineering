# Curriculum and depth boundaries

Status: Not started. Last verified: 2026-09-16.

[Home](README.md) · [Schedule](SCHEDULE.md) · [Assessment](ASSESSMENT.md)

## Ordered path

| Order | Module                                                                              | Hours | Learning status |
| ----- | ----------------------------------------------------------------------------------- | ----- | --------------- |
| 1     | [Advanced Python for AI systems](modules/01-advanced-python.md)                     | 20    | Not started     |
| 2     | [NumPy, tensors and numerical computing](modules/02-numpy-and-tensors.md)           | 10    | Not started     |
| 3     | [Essential mathematics](modules/03-essential-mathematics.md)                        | 15    | Not started     |
| 4     | [PyTorch fundamentals](modules/04-pytorch-fundamentals.md)                          | 15    | Not started     |
| 5     | [Neural-network fundamentals](modules/05-neural-networks.md)                        | 15    | Not started     |
| 6     | [Transformer architecture](modules/06-transformers.md)                              | 8     | Not started     |
| 7     | [GPU architecture, precision and memory](modules/07-gpu-architecture-and-memory.md) | 5     | Not started     |

Follow the order. Module 1 spans Week 1 and the beginning of Week 2. Module 2
finishes Week 2. Modules 3–5 occupy Weeks 3–5. Week 6 assigns eight hours to
transformers, five to GPU foundations and two to synthesis assessment.

This is an intensive foundation for an experienced software engineer, not
mastery of every referenced book or framework. 29.5 hours are selected reading;
the balance is practice, retrieval, review and catch-up. If prerequisites take
longer, log the gap and continue with the same evidence standard. The deadline
is a target, not a reason to silently drop failed checks.

## Mathematical depth contract

| Depth                        | Required topics                                                                                                                                                                                     | Evidence                                                                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Conceptual recognition       | Rank, basis, orthogonality, eigenvalues/eigenvectors and SVD                                                                                                                                        | Identify a dependent pair, explain geometric meaning and recognize a factorization; no decomposition algorithm or proof required |
| Calculation ability          | Scalars, vectors, matrices, tensors, dimensions, shapes, dot products, matrix multiplication, transposes, norms, functions, exponentials, logarithms, basic probabilities, expectation and variance | Work small examples by hand and check them numerically                                                                           |
| Deeper working understanding | Linear transformations, gradients, partial derivatives, chain rule, softmax and numerical stability                                                                                                 | Connect equations to code, calculate local derivatives and diagnose an unstable expression                                       |

Probability distributions and random variables require recognition plus simple
finite discrete calculations; measure-theoretic probability is outside scope.
SVD and eigenvalues are vocabulary for later systems reading, not prerequisites
for writing an inference kernel.

## Other depth boundaries

- Python, array shapes, module execution and measurements target application.
- Neural networks use tiny regression/classification models, not a vision
  course.
- Transformer components require explanation and tiny attention calculations; no
  pretrained model training or production model server is required.
- GPU blocks, warps, kernels, Tensor Cores and quantization require conceptual
  recognition. Tensor byte estimates and memory accounting require application.
- Basic compiler and mixed-precision experiments may remain To be validated if
  unsupported locally. Neither compiler internals nor quantization
  implementation is required.

## Evidence and dependency gates

Each [module guide](modules/01-advanced-python.md) links objectives to exercises
and a source pack. The [machine-readable curriculum](curriculum.yaml) maps IDs
and prerequisites. Use [weekly reviews](assessments/weekly-review-template.md)
to record assisted versus independent performance. Reading and NotebookLM
outputs are inputs to assessment; they are not evidence of applied ability by
themselves.

The initial roadmap mentions distributed-system fundamentals. In this harness,
that means only Python concurrency and host/device boundaries. Distributed
training, vLLM, distributed inference, CUDA kernel programming, TensorRT-LLM,
Triton kernels, RDMA and multi-node serving remain later-phase subjects.
