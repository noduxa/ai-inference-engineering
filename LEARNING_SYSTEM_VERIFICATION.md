# Learning-system verification

Verified: 2026-10-01. Implementation verified; learner study and Phase 3
readiness remain **Not started**. Branch: `docs/phase-1-2-learning-system`.

## Audit and changes

The [initial audit](LEARNING_SYSTEM_AUDIT.md) found a useful, merged Phase 1
harness and no Phase 2 programme. Existing source collections, exercise
procedures, assessment questions, public-learning narrative and milestone dates
were preserved. No unrelated user changes were present or included.

Phase 1 now adds worked reasoning, code-reading tasks, precise concurrency and
memory explanations, MPS guidance, evidence requirements, facilitator guidance
and stronger NotebookLM prompts. Phase 2 adds seven connected modules, nine
experiment specifications, a bounded runnable inference lab, benchmark
templates, assessments and a Phase 3 readiness review. Shared validation reuses
the existing YAML loader and HTTP checker. The complete inventory below
identifies new and updated files; other repository areas remain outside this
change.

## Sources and learning budget

| Module number | Phase 1 source records | Phase 2 source records  |
| ------------- | ---------------------- | ----------------------- |
| 1             | 4 required             | 5 required              |
| 2             | 4 required             | 4 required              |
| 3             | 4 required             | 4 required              |
| 4             | 4 required             | 4 required              |
| 5             | 4 required             | 4 required              |
| 6             | 4 required             | 4 required              |
| 7             | 4 required             | 3 required + 1 optional |

There are **14 modules, 14 source packs, 57 source records: 56 required and one
optional**. A Phase 1 record can be a scoped collection of official sections,
not a single import URL. Its pack tells the learner what to import and skip.
Phase 1 has 81 distinct assigned URLs; Phase 2 has 23; six overlap, producing
**98 distinct selected URLs**. Optional visual explanations sometimes reuse a
selected source rather than add another record. All selected readings are free;
none requires paid access or registration. NotebookLM itself requires an account
and manual import, which was not attempted.

Research combined web search with opening and selectively inspecting the
assigned publisher pages or PDFs on September 30–October 1. The
[inspection ledger](scripts/source-review.json) records all 98 URLs, source IDs,
selected sections and content hashes without copying source bodies. Inspection
does not mean every upstream example was executed. Two documentation redirect
notices were replaced with substantive destinations. A misleading compact mask
notation in an upstream cache explanation is explicitly qualified in Module 2.

Phase 1 totals **90 hours over six weeks** (88 module hours plus two final
assessment hours). Phase 2 totals **60 hours over four weeks** (57 plus three).
Both schedules budget 15 hours per week and include review/consolidation.
Original October/November targets are preserved. With no evidence of earlier
study, proposed forward dates are October 4–November 14 and November
15–December 12. These are planning assumptions, not attendance or completion
records.

## Verification results

- All seven YAML documents parse; both registries, references, source-pack URLs,
  prerequisites, assessment/exercise paths and hour budgets pass shared checks.
- All selected URLs have matching inspection-ledger entries and content hashes.
- 25 existing/extended source-validator tests pass.
- 26 shared validation and measurement-calculation tests pass.
- Three model integration tests pass: cache/no-cache token equivalence,
  batch/concurrency accounting, timing order and dtype payload size.
- All 652 repository internal Markdown links and checked headings resolve. The
  command below prints the exact count for the checked revision.
- Final HTTP checks: **98/98 selected URLs reachable**. HTTP reachability is
  separate from content inspection. Additional repository/community links were
  checked; the GitHub new-issue form requires login, as expected. No selected
  reading remained inaccessible or unverifiable during this run.
- Markdown lint passes across 136 Markdown files with the existing configuration. `git diff --check`
  passes. No TODO/FIXME/TBD or unfinished implementation placeholders remain;
  blank learner report fields are intentional templates.
- Credential/private-address pattern checks across 156 repository files found no
  matches. Content review found no employer/client material, patient data,
  credentials or private configuration. Automated scans are heuristic.
- Status review found no claimed learner completion. Source verification,
  implementation tests and worked examples are explicitly separated from
  experimental observations. No duplicate module directories were introduced.

The last validation pass caught YAML aliases that shared session and module
source lists. The lists were separated and the structural checks rerun. The HTTP
checker also gained a regression test for a documentation-version notice that
returns HTTP 200 without the intended content.

### Reproduce checks

Use an isolated environment with the pinned PyYAML dependency described in the
[shared tools](scripts/README.md). Model integration tests additionally require
the isolated [lab dependencies](phase-2/scripts/README.md).

```bash
python -m unittest discover -s phase-1/scripts/tests -v
python -m unittest discover -s scripts/tests -v
python -m unittest discover -s phase-2/scripts/tests -v
python scripts/validate_learning.py
python scripts/validate_learning.py --http --json /tmp/learning-links.json
python phase-1/scripts/validate_harness.py
npx --yes markdownlint-cli2@0.18.1 '**/*.md'
git diff --check
```

### Exercise execution and limits

Implementation smoke tests ran in isolated Python 3.12.14 with PyTorch 2.14.1
and Transformers 5.18.0 on an Apple M3 Pro with 36 GiB RAM. Random tiny-model
checks covered CPU FP32/FP64, cache disabled/enabled, batching, concurrency,
profiling and MPS. The public SmolLM2-135M model ran on CPU FP32 and MPS FP16 at
revision `93efa2f097d58c2a74874c7e644dbc9b0cee75a2`. A resource-budget
simulation allocates no trial tensors. These checks verified mechanics; no
performance rankings or benchmark results are claimed.

The 32 Phase 1 exercise specifications and nine Phase 2 experiments are learner
assignments, not completed studies. Full controlled experiments, statistical
benchmark campaigns and final assessments were not executed for Joshua. CUDA was
unavailable; CUDA timing/memory execution, integer quantization, physical OOM
recovery and production server behavior remain unverified. Safe CPU and
arithmetic fallbacks are documented. No vLLM server was installed, no public
endpoint was started and no NotebookLM authentication or automation occurred.
Temporary smoke outputs and profiler traces stayed outside the repository; no
machine-specific paths or traces are published. Tests reproduce core checks.

The local lab measures model-side token availability and local worker queues,
not HTTP streaming latency. It deliberately bounds input sizes and concurrency;
its worker pool is not continuous batching. Supported dtype failures must be
recorded, and instrumentation overhead limits generalization. A reviewer must
check raw results, source extraction and scientific interpretations.

## Exit gates and Joshua's next actions

**Phase 1 gate:** produce original explanations, tensor/shape/memory
calculations, code-reading and debugging attempts, interpreted experiment
evidence and a transformer-pass teach-back. Meet the
[Phase 1 rubric](phase-1/assessments/rubric.md), correct critical misconceptions
and identify uncertainty. Hours or Audio Overviews alone do not pass the gate.

**Phase 2 gate:** trace a request, distinguish prefill/decode, estimate weights
and KV memory with assumptions, design a fair benchmark, interpret measurements,
diagnose a reproducible symptom and state limits of generalization. Meet the
[Phase 2 rubric](phase-2/assessments/rubric.md) and document remaining gaps.

**Phase 3 readiness: Not started.** Complete the
[readiness review](phase-2/assessments/phase-3-readiness-review.md) before
beginning the upstream code-study/development plan. Readiness permits further
study; it is not specialist status or proof of an upstream contribution.

Joshua must select the proposed schedule, manually import the scoped sources
into NotebookLM, verify extraction of formulas/code, perform and record the
exercises, arrange assessment review and record hardware-dependent gaps. Recheck
evolving documentation before study. No merge is authorized by this
implementation; the branch is prepared for pull-request review.

## Complete relevant file inventory

`A` means created, `M` updated, and `=` preserved. Paths form the complete
relevant tree, including preserved Phase 1 files. Root scaffolding and unrelated
learning stubs are omitted because they were unchanged.

This change creates **64 files** and updates **34 files**.

```text
A LEARNING_SYSTEM_AUDIT.md
A LEARNING_SYSTEM_VERIFICATION.md
M README.md
M ROADMAP.md
= phase-1/ASSESSMENT.md
= phase-1/CURRICULUM.md
A phase-1/EVIDENCE.md
M phase-1/README.md
M phase-1/SCHEDULE.md
M phase-1/SOURCE_POLICY.md
= phase-1/VERIFICATION.md
M phase-1/assessments/README.md
A phase-1/assessments/facilitator-guidance.md
= phase-1/assessments/final-calculation-assessment.md
= phase-1/assessments/final-code-reading-assessment.md
= phase-1/assessments/final-concept-assessment.md
= phase-1/assessments/final-debugging-assessment.md
= phase-1/assessments/final-teach-back-assessment.md
= phase-1/assessments/rubric.md
= phase-1/assessments/weekly-review-template.md
M phase-1/curriculum.yaml
M phase-1/exercises/01-advanced-python.md
M phase-1/exercises/02-numpy-and-tensors.md
M phase-1/exercises/03-essential-mathematics.md
M phase-1/exercises/04-pytorch-fundamentals.md
M phase-1/exercises/05-neural-networks.md
M phase-1/exercises/06-transformers.md
M phase-1/exercises/07-gpu-architecture-and-memory.md
= phase-1/exercises/EVIDENCE_TEMPLATE.md
= phase-1/exercises/README.md
M phase-1/modules/01-advanced-python.md
M phase-1/modules/02-numpy-and-tensors.md
M phase-1/modules/03-essential-mathematics.md
M phase-1/modules/04-pytorch-fundamentals.md
M phase-1/modules/05-neural-networks.md
M phase-1/modules/06-transformers.md
M phase-1/modules/07-gpu-architecture-and-memory.md
= phase-1/notebooklm/README.md
M phase-1/notebooklm/prompts/README.md
= phase-1/notebooklm/prompts/audio-overview.md
= phase-1/notebooklm/prompts/compare-sources.md
= phase-1/notebooklm/prompts/concept-explanation.md
= phase-1/notebooklm/prompts/flashcards.md
A phase-1/notebooklm/prompts/measurement-review.md
= phase-1/notebooklm/prompts/misconception-check.md
= phase-1/notebooklm/prompts/practical-exercise.md
= phase-1/notebooklm/prompts/self-assessment.md
= phase-1/notebooklm/prompts/study-guide.md
M phase-1/notebooklm/prompts/teach-back-review.md
M phase-1/notebooklm/source-packs/01-advanced-python.md
M phase-1/notebooklm/source-packs/02-numpy-and-tensors.md
M phase-1/notebooklm/source-packs/03-essential-mathematics.md
M phase-1/notebooklm/source-packs/04-pytorch-fundamentals.md
M phase-1/notebooklm/source-packs/05-neural-networks.md
M phase-1/notebooklm/source-packs/06-transformers.md
M phase-1/notebooklm/source-packs/07-gpu-architecture-and-memory.md
M phase-1/scripts/README.md
= phase-1/scripts/requirements.txt
M phase-1/scripts/tests/test_validate_sources.py
= phase-1/scripts/validate_harness.py
M phase-1/scripts/validate_sources.py
M phase-1/sources.yaml
A phase-2/ASSESSMENT.md
A phase-2/BENCHMARKING.md
A phase-2/CURRICULUM.md
A phase-2/EVIDENCE.md
A phase-2/GLOSSARY.md
A phase-2/README.md
A phase-2/SCHEDULE.md
A phase-2/SOURCE_POLICY.md
A phase-2/assessments/README.md
A phase-2/assessments/facilitator-guidance.md
A phase-2/assessments/final-benchmarking-assessment.md
A phase-2/assessments/final-calculation-assessment.md
A phase-2/assessments/final-code-reading-assessment.md
A phase-2/assessments/final-concept-assessment.md
A phase-2/assessments/final-diagnostic-assessment.md
A phase-2/assessments/final-teach-back-assessment.md
A phase-2/assessments/phase-3-readiness-review.md
A phase-2/assessments/rubric.md
A phase-2/assessments/weekly-review-template.md
A phase-2/curriculum.yaml
A phase-2/exercises/01-request-lifecycle.md
A phase-2/exercises/02-prefill-decode.md
A phase-2/exercises/03-output-length.md
A phase-2/exercises/04-kv-cache.md
A phase-2/exercises/05-precision.md
A phase-2/exercises/06-batching-concurrency.md
A phase-2/exercises/07-warm-cold.md
A phase-2/exercises/08-bottleneck.md
A phase-2/exercises/09-resource-limits.md
A phase-2/exercises/README.md
A phase-2/modules/01-inference-request-lifecycle.md
A phase-2/modules/02-prefill-decode-and-kv-cache.md
A phase-2/modules/03-model-memory-and-quantization.md
A phase-2/modules/04-batching-scheduling-and-serving.md
A phase-2/modules/05-performance-metrics-and-benchmarking.md
A phase-2/modules/06-profiling-and-bottleneck-diagnosis.md
A phase-2/modules/07-serving-systems-and-vllm-bridge.md
A phase-2/notebooklm/README.md
A phase-2/notebooklm/prompts/README.md
A phase-2/notebooklm/source-packs/01-inference-request-lifecycle.md
A phase-2/notebooklm/source-packs/02-prefill-decode-and-kv-cache.md
A phase-2/notebooklm/source-packs/03-model-memory-and-quantization.md
A phase-2/notebooklm/source-packs/04-batching-scheduling-and-serving.md
A phase-2/notebooklm/source-packs/05-performance-metrics-and-benchmarking.md
A phase-2/notebooklm/source-packs/06-profiling-and-bottleneck-diagnosis.md
A phase-2/notebooklm/source-packs/07-serving-systems-and-vllm-bridge.md
A phase-2/scripts/README.md
A phase-2/scripts/inference_lab.py
A phase-2/scripts/requirements-lab.txt
A phase-2/scripts/tests/test_lab_integration.py
A phase-2/sources.yaml
A phase-2/templates/benchmark-results.md
A phase-2/templates/experiment-plan.md
A phase-2/templates/hardware-software-profile.md
A phase-2/templates/performance-investigation.md
A scripts/README.md
A scripts/source-review.json
A scripts/tests/test_learning.py
A scripts/validate_learning.py
```
