# Final concept assessment

Assessment ID: final-concept. Status: Not started. Budget: 20 minutes.

[Rubric](rubric.md) · [Plan](../ASSESSMENT.md)

Answer briefly without sources first. Give reasoning, not just definitions.

1. **Python concurrency:** Compare AsyncIO, threads and processes for simulated
   waiting, pure-Python arithmetic and native-library work. State
   interpreter/GIL assumptions and one overhead for each choice.
2. **Memory and profiling:** Distinguish object identity, shallow copying,
   generator state, traced allocations and process memory. Which profiling tool
   would you use for a CPU hotspot versus a growing Python cache?
3. **Arrays:** Explain axes, broadcasting, strides, views and contiguous
   storage. Why can a view report many bytes while sharing its backing
   allocation?
4. **Math:** Explain a gradient, linear transformation, expectation and
   variance. Recognize rank, basis, orthogonality, eigenvalues and SVD in plain
   language; no proof is required.
5. **PyTorch:** Distinguish nn.Module, parameters, autograd graph, loss and
   optimizer. Explain eval(), no_grad() and inference_mode() separately.
6. **Networks:** Compare training and inference. What do initialization,
   learning rate, batch size, epochs and regularization influence? Why can
   training loss and generalization disagree?
7. **Transformers:** Explain Q/K/V, multi-head attention, positions, residuals,
   normalization and feed-forward layers. Contrast encoder, decoder-only and
   encoder-decoder models. Where do logits and sampling enter generation?
8. **GPU:** Distinguish device memory, registers, shared memory and global
   memory; FP32, FP16, BF16 and low-bit integer representations; allocated and
   reserved memory. What would count as evidence of a bottleneck?
