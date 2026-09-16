# Final code-reading assessment

Assessment ID: final-code-reading. Status: Not started. Budget: 25 minutes.

[Rubric](rubric.md) · [Plan](../ASSESSMENT.md)

The snippets are assessment inputs, not validated examples or recommended
patterns. Predict behaviour before running. Explain each important line and
propose tests.

## A: References and lazy evaluation

```python
rows = [[0]] * 3
copied = rows.copy()
values = (row[0] for row in rows)
rows[0][0] = 7
```

What do `rows`, `copied` and a subsequent `list(values)` represent? Draw
references. What remains after consuming the generator once? Which tests expose
the aliasing?

## B: Array shapes and views

```python
import numpy as np

x = np.arange(12, dtype=np.float32).reshape(3, 4)
y = x[:, ::2]
z = y + np.array([10, 20], dtype=np.float32)
```

Predict shapes, strides, payload byte counts and whether mutation of `y` or `z`
changes `x`. What observation would verify sharing without relying only on
`base`?

## C: Forward, backward and inference

```python
import torch
from torch import nn

model = nn.Linear(3, 2)
x = torch.ones(4, 3)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
model.eval()
out = model(x)
loss = out.square().mean()
loss.backward()
optimizer.step()
```

Identify parameters and all shapes. Is a graph built despite eval()? What
changes after step()? What is missing if this block is repeated? Rewrite only
after explaining how an ordinary inference-only version should differ.

## D: Public repository navigation

Using your PY-06 evidence, trace a public Python API to its implementation and a
relevant test or documented test gap. Name the revision, entry point, helper and
one failure path. Distinguish what you inspected from what you inferred.
