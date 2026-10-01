# Phase 1 evidence and exit gate

Status: Not started. No learner completion is certified by repository tooling.

[Assessment](ASSESSMENT.md) · [Rubric](assessments/rubric.md) ·
[Evidence template](exercises/EVIDENCE_TEMPLATE.md) ·
[Phase 2](../phase-2/README.md)

For each exercise retain the prediction, original code/calculation, environment,
raw observations, interpretation, corrected mistakes and source sections. Use
public/synthetic data. Stage only reviewed small artifacts; outputs and model
files remain ignored by default. A code smoke test proves a tool runs, not that
Joshua can independently explain its behavior.

## Exit decision

Require an unaided explanation, fresh shape and memory calculations, a short
Python/NumPy/PyTorch code trace, diagnosis of a basic error, interpretation of
measurements and a transformer inference walkthrough. Record uncertainty rather
than fill missing evidence with plausible numbers. Apply all rubric thresholds;
no averaging away a critical misconception about masks, autograd or memory.

| Evidence group                             | Status      | Evidence/reviewer                |
| ------------------------------------------ | ----------- | -------------------------------- |
| Seven module exit tests                    | Not started | No learner submissions           |
| Calculations and code reading              | Not started | No learner submissions           |
| Experiments and measurement interpretation | Not started | No learner submissions           |
| Final assessment and corrected teach-back  | Not started | No learner submissions           |
| Phase 2 entry decision                     | Not started | Requires reviewed evidence above |

Hardware fallbacks can establish conceptual/application evidence on CPU. They
cannot establish CUDA timing or physical GPU memory behavior. Keep that gap
explicit in the review and plan a later bounded accelerator check.
