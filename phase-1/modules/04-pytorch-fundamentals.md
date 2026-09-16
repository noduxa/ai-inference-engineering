# Module 4: PyTorch fundamentals

Status: Not started. Estimated time: **15 hours**, including practice, review
and catch-up. Last verified: 2026-09-16.

[Curriculum](../CURRICULUM.md) · [Schedule](../SCHEDULE.md) ·
[Source pack](../notebooklm/source-packs/04-pytorch-fundamentals.md)

## Why this matters

Framework literacy makes it possible to inspect a model, distinguish its state
from its computation and measure forward-only execution.

## Learning objectives

- Build and inspect a small module with named parameters and a reproducible
  forward pass.
- Perform one training step and distinguish parameter updates from forward-only
  inference.
- Save/reload a state dictionary and verify equivalent outputs.
- Measure timing and memory using correct device-specific boundaries.

## Prerequisites

Complete the preceding module’s core shape, calculation or programming checks;
revisit any unresolved prerequisite before continuing.

## Required concepts

- Installing and verifying PyTorch
- Tensors, shapes and strides
- Data types
- CPU and CUDA devices
- Moving tensors between devices
- nn.Module and parameters
- Forward passes
- Computational graphs
- Automatic differentiation and gradients
- Loss functions and optimization loops
- Dataset and DataLoader basics
- Training mode versus evaluation mode
- torch.no_grad() and torch.inference_mode()
- Saving and loading state dictionaries
- Mixed precision
- Basic torch.compile
- PyTorch profiler
- Measuring CPU time and CUDA time
- Measuring allocated and reserved GPU memory

## Recommended sources

- `pt-basics` —
  [PyTorch Learn the Basics and installation](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)
  (primary; selected reading 2.5 h).
- `pt-autograd` —
  [Autograd mechanics and inference mode](https://docs.pytorch.org/docs/2.14/notes/autograd.html)
  (supporting; selected reading 0.75 h).
- `pt-performance` —
  [PyTorch profiling, compilation and mixed precision](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)
  (supporting; selected reading 1.25 h).
- `pt-cuda` —
  [CUDA semantics: timing and memory](https://docs.pytorch.org/docs/2.14/notes/cuda.html)
  (supporting; selected reading 0.75 h).

Exact page links, selected sections, exclusions, access terms and import order
are in the source pack. Reading times are selective budgets, not estimates for
completing entire documentation collections.

## Study order

1. Install a supported build and inspect tensor devices, dtypes, shapes and
   strides in PT-01.
2. Build the tiny module and DataLoader, then trace a forward pass before adding
   autograd and one update in PT-02.
3. Compare execution/gradient modes and validate a state-dictionary round-trip
   in PT-03.
4. Collect a CPU profile; attempt only supported compile and autocast cases in
   PT-04.
5. Design correct timing and memory boundaries for PT-05; retain explicit CUDA
   limitations where necessary.

## Exercises and deliverables

[Open the exercise specifications](../exercises/04-pytorch-fundamentals.md).

- `PT-01` — Tensor device and dtype.
- `PT-02` — Small module and one training step.
- `PT-03` — Inference and state round-trip.
- `PT-04` — Profiler, compile and mixed precision.
- `PT-05` — CPU versus GPU timing and memory.

Deliver a short concept note, original calculations/code, environment record,
actual measurements where applicable, and a teach-back. Use the
[evidence template](../exercises/EVIDENCE_TEMPLATE.md). No outputs are supplied
as completed work.

## Reflection questions

- What state does a state_dict contain, and what code is still needed?
- How would you verify that a forward pass did not build a gradient graph?
- Why separate transfer, warmup, compile and steady-state timing?

## Common mistakes to challenge

The following statements are deliberately questionable; correct them with
sources:

- model.eval() disables autograd.
- no_grad() and inference_mode() have identical restrictions.
- Moving inputs also moves model parameters.
- Host wall-clock timing alone always measures completed CUDA work.
- Reserved memory is the same as live tensor memory.

## Exit test

Without NotebookLM, answer the reflection questions and explain a fresh variant
of one exercise. Then use sources to check your answer. Demonstrate a working
application, predict its outcome and diagnose one plausible failure. Record
assistance, corrections and evidence using the
[rubric](../assessments/rubric.md).

- Complete the 5 exercise specifications or explicitly record hardware-limited
  steps.
- Demonstrate application on the module exit test with evidence and corrected
  reasoning.
- Resolve critical misconceptions in teach-back before claiming completion.

## Completion checklist

- [ ] Selected reading completed and source coverage checked.
- [ ] Each required concept can be recognized and explained at its stated depth.
- [ ] Exercises attempted with reproducible evidence and honest limitations.
- [ ] Exit test and teach-back reviewed; critical misconceptions corrected.
- [ ] Hardware-dependent work still pending is explicitly identified.
- [ ] Weekly review links the evidence; status changes have supporting records.
