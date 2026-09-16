# Module 7 NotebookLM source pack

Status: Planned. Source inspection: Verified. NotebookLM import: To be
validated. Last verified: 2026-09-16.

[NotebookLM workflow](../README.md) ·
[Module](../../modules/07-gpu-architecture-and-memory.md) ·
[Source registry](../../sources.yaml)

## Module purpose

Hardware limits determine which experiments are possible. Memory estimates and
honest timing are prerequisites to interpreting serving performance.

## Learning objectives

- Draw a conceptual execution and memory map for a CPU/GPU system.
- Estimate tensor payload memory across precision formats and state overhead
  limits.
- Interpret utilization, allocated memory and reserved memory without conflating
  them.
- Design a bounded resource experiment and diagnose likely memory or compute
  limits.

## Prerequisites

Preceding curriculum modules; review unresolved prerequisite exit tests.

## Ordered source table

Four curated source collections: one primary and three supporting. A collection
can contain several individual pages. Import **4–8 relevant pages at a time**,
not every page below at once. An index URL does not import linked chapters. Use
the session batches below and add missing sections only when needed.

| Order | Registry ID        | Source collection                                                                                                                            | Role       | Selected reading |
| ----- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------- |
| 1     | `gpu-architecture` | [CUDA programming guide: architecture concepts](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)  | primary    | 0.75 h           |
| 2     | `gpu-performance`  | [GPU performance background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html)                      | supporting | 0.5 h            |
| 3     | `gpu-precision`    | [Numerical formats and quantization concepts](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/mathematical-functions.html) | supporting | 0.5 h            |
| 4     | `gpu-memory`       | [PyTorch CUDA memory and NVIDIA monitoring](https://docs.pytorch.org/docs/2.14/notes/cuda.html)                                              | supporting | 0.5 h            |

## Exact sections, selection reasons and access

### gpu-architecture: CUDA programming guide: architecture concepts

Expected knowledge: Distinguish execution hierarchy, physical memories and
CUDA’s role without writing kernels.

- Author/institution: NVIDIA documentation team; NVIDIA.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Sep 09, 2026; see
  section-level dates in the registry where available.
- Selected study time: 0.75 h; included in this module’s budget.
- Authority and phase fit: Vendor architecture explanation identifies execution
  and memory concepts; kernel programming is explicitly excluded.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                                           | Study these sections                                                   | Skip for Phase 1                                            |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| [Programming model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)      | CPU/GPU, kernels, thread hierarchy, warps, blocks and memory hierarchy | All kernel implementation and advanced programming sections |
| [CUDA platform](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/cuda-platform.html)              | Toolkit and driver relationship                                        | All kernel implementation and advanced programming sections |
| [Unified and system memory](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/understanding-memory.html) | Opening explanation of host/device physical memory and placement only  | All kernel implementation and advanced programming sections |

### gpu-performance: GPU performance background

Expected knowledge: Explain compute throughput versus memory bandwidth and avoid
diagnosing from utilization alone.

- Author/institution: NVIDIA documentation team; NVIDIA.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Feb 1, 2023; see
  section-level dates in the registry where available.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Introduces bandwidth, throughput and
  math-versus-memory limits; hardware-specific numbers are not transferred to
  Joshua’s machine.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                                              | Study these sections                                                | Skip for Phase 1                |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------- |
| [GPU performance background](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html) | GPU architecture; performance; math and memory bounds; Tensor Cores | Product performance comparisons |

### gpu-precision: Numerical formats and quantization concepts

Expected knowledge: Distinguish floating-point range/precision from integer
quantization and storage assumptions.

- Author/institution: NVIDIA documentation team; NVIDIA.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Sep 09, 2026; see
  section-level dates in the registry where available.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Distinguishes numeric formats from hardware support
  and conceptual low-bit compression; no quantization toolchain is required.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                                                          | Study these sections                      | Skip for Phase 1                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------- |
| [Floating-point computation](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/mathematical-functions.html)         | Floating-point types and accuracy caveats | Intrinsics and kernel code                                           |
| [Quantization concepts](https://raw.githubusercontent.com/NVIDIA/Model-Optimizer/main/docs/source/guides/_pytorch_quantization.rst) | INT8 and INT4 concept and formats only    | All optimization commands, serving integrations and model conversion |

### gpu-memory: PyTorch CUDA memory and NVIDIA monitoring

Expected knowledge: Interpret allocator accounting and device-monitoring
measurements without equating them.

- Author/institution: PyTorch contributors, NVIDIA documentation team; PyTorch /
  NVIDIA.
- Format: documentation. Access: free.
- Publication/update: Primary linked page last updated Jul 17, 2026; see
  section-level dates in the registry where available.
- Selected study time: 0.5 h; included in this module’s budget.
- Authority and phase fit: Pairs framework allocation accounting with device
  monitoring; the two measurements need not match.
- Terms: Publisher terms apply; link only, no redistribution assumed.
- Import compatibility: To be validated: import individual text pages; verify
  equations, code and source coverage manually.

| Exact page                                                                                 | Study these sections                                              | Skip for Phase 1                                                                 |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| [CUDA memory semantics](https://docs.pytorch.org/docs/2.14/notes/cuda.html)                | Memory management; memory_allocated; memory_reserved; empty_cache | Distributed and graph sections                                                   |
| [NVIDIA System Management Interface](https://docs.nvidia.com/deploy/nvidia-smi/index.html) | GPU name, memory usage and utilization reporting                  | Device resets, administrative controls and process identifiers in published logs |

## Optional visual lane and overlap decisions

Use NVIDIA’s programming-model and performance diagrams. The current programming
guide defines hardware concepts; older performance examples are context, not
expected performance on a modern GPU.

No additional secondary blog is selected: the first-party diagrams and textbook
explanations cover the visual need without another overlapping source.

## Notebook name and adding sources

Suggested name: **Joshua — Phase 1 — 07 GPU architecture, precision and
memory**.

Add pages in the source-table order within the current session batch. Name each
import with its registry ID and section title. Check that the actual page text,
code and equations appear before asking questions. Retain at most eight active
pages; rotate earlier pages out after saving your own cited notes. Re-add an
omitted page if a prompt needs it. Do not use an index as a substitute for
content.

## Session import batches

- **Hardware and memory:** Programming model; CUDA platform; Unified and system
  memory; GPU performance background; Floating-point computation; Quantization
  concepts; CUDA memory semantics; NVIDIA System Management Interface.

## Initial NotebookLM questions

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

- Where do model tensors live during a host-to-device copy?
- How would you distinguish allocator caching from live memory growth?
- What can a utilization sample tell you, and what can it not tell you?

## Audio Overview customization prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Give a short spoken orientation to gpu architecture, precision and memory for a
backend engineer. Use one concrete example from the selected pages, explain why
it matters to later inference study, and challenge one misconception below. Name
sources aloud and end with three questions to answer without replaying the
overview. Avoid advanced serving topics and performance promises. Listening is
preparation, not completion.

## Study-guide generation prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Organize this module around its learning objectives. For each, show the exact
source section, a prerequisite, a small application question and an evidence
check. Mark recognition-only topics and exclude the listed skip sections. Flag
objectives that the currently imported batch cannot support before attempting to
explain them.

## Flashcard-generation prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Make ten cards: four concept distinctions, three shape or code predictions and
three error-diagnosis prompts. Put questions first and source-backed answers in
a separate section. Include assumptions and one counterexample per tricky
concept. Do not reduce the deck to vocabulary definitions.

## Quiz-generation prompt

Use only supplied sources. Identify the source title and section for important
claims; include citations where supported. If coverage is missing or sources
disagree, say so explicitly. Do not invent facts, citations, measurements or
completed learning. Treat my notes as learner claims to verify, not
authoritative evidence.

Ask six questions progressing from recognition through explanation to
application and early diagnosis. Use fresh tiny inputs, not copied worked
examples. Withhold answers until I submit mine. Then score reasoning, identify
the source for each correction and give one targeted retry. Do not infer
practical completion from a correct multiple-choice answer.

## Common misconceptions to test

These are deliberately questionable claims to correct, not facts to memorize.

- A GPU is always faster for every tensor operation.
- FP16 and BF16 have identical range and precision.
- INT4 storage costs exactly half a byte per value with no metadata or packing
  constraints.
- empty_cache() frees live tensors.
- High utilization proves a workload is compute-bound.

## Practical exercise

Start with `GPU-01` in the
[module exercise specifications](../../exercises/07-gpu-architecture-and-memory.md),
then complete the remaining exercises. Ask for a plan critique before executing;
never ask the model to fabricate an observation or to silently fill in missing
measurements.

## Required learning evidence

- Own-word explanation with inspected source citations.
- Exercise code/calculations and explicit correctness checks.
- Environment record, actual observations, failed attempts and limitations.
- Prediction-versus-result comparison and a reviewed teach-back.

## Exit criteria

- Complete the 4 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

Use the [assessment rubric](../../assessments/rubric.md); neither imported
sources nor generated study artifacts establish mastery.

## What to study next

Complete the [final assessments](../../ASSESSMENT.md), then consult
[Phase 2 of the roadmap](../../../ROADMAP.md). No Phase 2 work is required to
pass this phase.
