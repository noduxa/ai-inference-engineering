# Final calculation assessment

Assessment ID: final-calculation. Status: Not started. Budget: 25 minutes.

[Rubric](rubric.md) · [Plan](../ASSESSMENT.md)

Show intermediate steps and units. Use a calculator for exponentials, then
verify with code only after preserving the independent attempt.

1. Calculate `[[2,1],[0,3]] @ [[1,2],[4,0]]`. Explain the contracted dimension
   and why reversing operands need not preserve the result.
2. Give the result shape of `(4,1,3) + (1,5,1)` and explain whether `(4,3)+(4,)`
   broadcasts. Give the shape of `(2,6,4) @ (4,3)` and its FP32 payload bytes.
3. Calculate softmax of `[1,2,3]`. Explain how to evaluate `[1001,1002,1003]`
   safely without changing the mathematical distribution.
4. For `L=(w*x+b-y)^2`, evaluate partial derivatives at `x=3, y=2, w=1, b=0`.
   Show the chain rule and one gradient-descent update with learning rate 0.1.
5. For Q=K=`[[1,1],[1,0]]` and V=`[[2,0],[0,2]]`, calculate the first causal
   attention row and describe the second row’s calculation. Label shapes before
   multiplying and identify the normalization axis.
6. Estimate payload memory for shape `(2,128,64)` in FP32, FP16, BF16, INT8 and
   tightly packed INT4. Explain which assumptions make the INT4 figure
   theoretical. For a random variable taking 1 and 3 with equal probability,
   calculate its expectation and variance.
