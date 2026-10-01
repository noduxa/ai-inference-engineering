# Module 4: PyTorch fundamentals

Status: Not started. Estimated time: **15 hours**, including practice, review
and catch-up. Last verified: 2026-09-30.

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

## Detailed explanation and worked example

A tensor's values, layout, dtype and device are separate properties. Moving a
module does not automatically move unrelated inputs. Verify installation with
CPU first, then query CUDA or `torch.backends.mps.is_available()` before
selecting an accelerator. Apple MPS uses a different backend and memory model;
CUDA memory APIs do not measure MPS. See the
[MPS backend](https://docs.pytorch.org/docs/2.14/notes/mps.html).

An `nn.Module` registers parameter tensors and child modules. Its `forward`
describes computation; it does not perform an optimizer update. For a linear
layer with 3 inputs and 2 outputs, weight shape is `(2,3)`, bias shape `(2,)`,
and an input `(4,3)` yields `(4,2)`. There are `3*2+2=8` parameters.

```python
import torch
layer = torch.nn.Linear(3, 2)
x = torch.ones(4, 3)
optimizer = torch.optim.SGD(layer.parameters(), lr=0.01)
optimizer.zero_grad()
loss = layer(x).square().mean()
loss.backward()
optimizer.step()
layer.eval()
with torch.inference_mode():
    prediction = layer(x)
```

Identify which lines build a graph, compute gradients and change weights.
Autograd constructs a graph of recorded operations; gradients normally
accumulate until cleared. `Dataset` supplies examples and `DataLoader`
groups/loads them; worker processes can cost more than they save for tiny
synthetic inputs.

`eval()` changes behavior of mode-sensitive layers such as dropout; it does not
disable autograd. `no_grad()` disables gradient recording in its scope.
`inference_mode()` removes additional tracking but restricts later autograd use
of tensors created there. See
[autograd modes](https://docs.pytorch.org/docs/2.14/notes/autograd.html). Save a
state dictionary, reconstruct the same architecture, reload it, set eval mode
and compare outputs with a stated tolerance. State dictionaries do not encode
the entire preprocessing contract.

Mixed precision chooses operation-specific representations; it is not equivalent
to blindly converting every operation to FP16. `torch.compile` can introduce a
large first-call cost and specialization/recompilation. Report compilation and
steady-state timings separately. A profiler adds overhead, so use it to localize
work and then confirm timings without profiling.

CUDA dispatch is asynchronous. A wall-clock interval must synchronize before and
after the measured region, or use CUDA events on the relevant stream and wait
for completion. MPS timing needs `torch.mps.synchronize()`; CPU timing does not.
Allocated CUDA memory describes live tensor allocation; reserved memory includes
the caching allocator's pool. These differ from all-process device usage. See
[CUDA semantics](https://docs.pytorch.org/docs/2.14/notes/cuda.html).

## Code-reading task and implementation mistakes

Annotate the example line by line, then inspect the installed
`nn.Linear.forward` implementation and the official optimization tutorial's
training loop. Explain how broadcasting could let a wrong target shape silently
change a loss. Common failures include uncleared gradients, train mode during
evaluation, retained graph-bearing losses in a list, device mismatch and timing
only enqueue work. Carry the forward/backward distinction into Module 5.

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

## Connection to the next module

Continue to [neural networks](05-neural-networks.md) after the exit test.
