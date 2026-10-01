# Six-week schedule

Status: Planned. Target: 31 October 2026. Last verified: 2026-09-16.

[Curriculum](CURRICULUM.md) · [Source packs](notebooklm/README.md) ·
[Weekly review](assessments/weekly-review-template.md)

The original September 20–October 31 calendar below is a **proposed target**,
not a record of completed study. As of September 30, no learner completion is
recorded. A forward alternative is October 4–November 14 at the same 15 hours
per week. Keep the existing session order and use the date mapping below; do not
compress missed weeks. This makes the November Phase 2 target conditional.

| Week | Original proposed dates | Forward proposed dates |
| ---- | ----------------------- | ---------------------- |
| 1    | Sep 20–26               | Oct 4–10               |
| 2    | Sep 27–Oct 3            | Oct 11–17              |
| 3    | Oct 4–10                | Oct 18–24              |
| 4    | Oct 11–17               | Oct 25–31              |
| 5    | Oct 18–24               | Nov 1–7                |
| 6    | Oct 25–31               | Nov 8–14               |

Each session includes reading and practice. At its end answer: which assumption
mattered, what differed from the prediction, and what evidence remains missing?
The existing catch-up and weekly-review slots remain inside the 90-hour budget.
Week 6 is a compact foundation, not advanced architecture mastery.

Source IDs resolve to exact links and sections in each module’s source pack and
[sources.yaml](sources.yaml). Exercise IDs resolve in
[exercises](exercises/README.md).

## Week 1: 20–26 September 2026

| Session | Hours | Objective                                           | Sources                                                     | Practical work                                 | Expected evidence, not completed                |
| ------- | ----- | --------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------- |
| 1       | 3     | Object identity, mutability and copying             | py-runtime: data model/copy                                 | PY-01 prediction and ownership sketches        | Object graph and initial memory prediction      |
| 2       | 3     | Functions, closures, decorators, context managers   | py-tutorial; py-runtime: function definitions/contextlib    | PY-06 cleanup and decorator tests              | Small implementation with failed-path test      |
| 3       | 3     | Types, protocols, dataclasses, errors and logging   | py-runtime: typing/dataclasses/logging; py-tutorial: errors | PY-06 typed boundary and fixture               | Typed package interface and exception record    |
| 4       | 3     | Modules, virtual environments, packaging and pytest | py-packaging; py-pytest; py-tutorial: modules/venv          | PY-06 package and repository trace             | Reproduction instructions and source call path  |
| 5       | 3     | Iterators, generators; catch-up and review          | py-tutorial: classes; py-runtime: data model                | Finish PY-01; 1 h catch-up + 1 h weekly review | Observed memory record and corrected teach-back |

**Weekly total: 15 hours.**

## Week 2: 27 September–3 October 2026

| Session | Hours | Objective                                  | Sources                                               | Practical work                              | Expected evidence, not completed              |
| ------- | ----- | ------------------------------------------ | ----------------------------------------------------- | ------------------------------------------- | --------------------------------------------- |
| 1       | 3     | AsyncIO, threads, GIL and process pools    | py-runtime: asyncio/threading/multiprocessing/futures | PY-02 and PY-03 bounded comparisons         | Workload-choice table with real observations  |
| 2       | 2     | CPU and allocation profiling               | py-runtime: profile/tracemalloc                       | PY-04 and PY-05                             | Hotspot and allocation trace with limitations |
| 3       | 3     | Arrays, shapes, dtype and storage          | np-quickstart; np-types                               | NP-04 and NP-05                             | Shape calculations and payload estimate       |
| 4       | 4     | Broadcasting, vectorization and aliasing   | np-broadcast; np-views; np-quickstart                 | NP-01, NP-02 and NP-03                      | Correctness checks and controlled timing      |
| 5       | 3     | Strides and precision; catch-up and review | np-quickstart: ndarray layout; np-types               | Array exit check; 1 h catch-up + 1 h review | Memory-layout explanation and weekly review   |

**Weekly total: 15 hours.**

## Week 3: 4–10 October 2026

| Session | Hours | Objective                                              | Sources                                            | Practical work                                    | Expected evidence, not completed                     |
| ------- | ----- | ------------------------------------------------------ | -------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| 1       | 3     | Vectors, matrices and tensor products                  | math-prelim: linear algebra                        | MA-01 and MA-02                                   | Hand calculations before NumPy checks                |
| 2       | 3     | Linear transformations, norms and geometric vocabulary | math-mit: selected transcript segments             | Rank/basis/orthogonality sketches                 | Eigenvector/SVD recognition note                     |
| 3       | 3     | Functions, derivatives and chain rule                  | math-prelim: calculus                              | MA-04                                             | Local derivatives and finite-difference check        |
| 4       | 3     | Probability, logits, softmax and stability             | math-prelim: probability; math-softmax; math-float | MA-03 and MA-05                                   | Stable calculation and discrete expectation/variance |
| 5       | 3     | Calculation retry; catch-up and review                 | Revisit only sections supporting identified gaps   | 1 h fresh calculation + 1 h catch-up + 1 h review | Corrected reasoning and weekly review                |

**Weekly total: 15 hours.**

## Week 4: 11–17 October 2026

| Session | Hours | Objective                                         | Sources                                 | Practical work                             | Expected evidence, not completed                  |
| ------- | ----- | ------------------------------------------------- | --------------------------------------- | ------------------------------------------ | ------------------------------------------------- |
| 1       | 3     | Install, tensors, dtype and device checks         | pt-basics: installation/tensors         | PT-01                                      | Environment manifest and device limitations       |
| 2       | 3     | Module, parameters, datasets and autograd         | pt-basics: build/data/autograd          | PT-02                                      | One training-step trace                           |
| 3       | 3     | Evaluation, gradient modes and state dictionaries | pt-autograd; pt-basics: save/load       | PT-03                                      | Output equivalence and graph inspection           |
| 4       | 3     | Profiler, timing, memory, compile and autocast    | pt-performance; pt-cuda                 | PT-04 and PT-05: smallest supported cases  | Profiler record; CUDA work or explicit limitation |
| 5       | 3     | Fresh forward-pass check; catch-up and review     | Targeted pt-basics/pt-autograd sections | 1 h exit check + 1 h catch-up + 1 h review | Mode comparison and weekly review                 |

**Weekly total: 15 hours.**

## Week 5: 18–24 October 2026

| Session | Hours | Objective                                            | Sources                                    | Practical work                             | Expected evidence, not completed            |
| ------- | ----- | ---------------------------------------------------- | ------------------------------------------ | ------------------------------------------ | ------------------------------------------- |
| 1       | 3     | Regression, classification and perceptrons           | nn-linear; nn-classification               | NN-01 small regression                     | Annotated model and loss                    |
| 2       | 3     | MLP, activation, graph and backward pass             | nn-mlp: MLP/backprop; nn-loop              | NN-01 small classifier                     | Shape and parameter-update trace            |
| 3       | 3     | Learning rate, batch size, epochs and generalization | nn-mlp: generalization; nn-loop            | NN-02 controlled change                    | Train/validation record, no assumed outcome |
| 4       | 3     | Initialization, regularization and inference         | nn-mlp: weight decay/stability             | NN-03                                      | Forward-only explanation and finite outputs |
| 5       | 3     | Network exit check; catch-up and review              | Revisit the specific misconception sources | 1 h exit check + 1 h catch-up + 1 h review | Generalization teach-back and weekly review |

**Weekly total: 15 hours.**

## Week 6: 25–31 October 2026

| Session | Hours | Objective                                         | Sources                                                      | Practical work                                             | Expected evidence, not completed                    |
| ------- | ----- | ------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- | --------------------------------------------------- |
| 1       | 3     | Tokens, embeddings, sequence shapes and attention | tr-hf; tr-d2l: attention                                     | TR-01 and TR-02                                            | Tiny attention calculation and mask inspection      |
| 2       | 3     | Blocks, model families and generation             | tr-d2l: transformer; tr-paper: §3; tr-generation             | TR-03 and TR-04                                            | Two-step generation trace and synthetic sampling    |
| 3       | 2     | Transformer consolidation and catch-up            | Targeted tr-hf/tr-d2l pages                                  | 1 h exit test + 1 h catch-up                               | Corrected architecture map                          |
| 4       | 3     | GPU execution, precision and memory               | gpu-architecture; gpu-performance; gpu-precision; gpu-memory | GPU-01 and GPU-02                                          | Device map, monitoring plan and byte estimates      |
| 5       | 4     | Bounded resource study and synthesis              | gpu-memory; assessment files                                 | GPU-03/GPU-04 and GPU review (2 h); final assessment (2 h) | Safe limit/OOM analysis and final assessment record |

**Weekly total: 15 hours.**

## When the schedule slips

Use the reserved catch-up before adding optional material. Week 6 reserves one
hour of transformer catch-up; GPU review is included in its final two-hour
block. Keep hardware-blocked work visible and log revised dates rather than
reporting success. If the final check uncovers a prerequisite gap, schedule
remediation after 31 October and retain the original target in the roadmap.
