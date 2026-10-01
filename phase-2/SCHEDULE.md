# Four-week schedule

Status: Planned. Last verified: 2026-09-30. Total: **60 hours**, 15 per week.

[Curriculum](CURRICULUM.md) ·
[Weekly review](assessments/weekly-review-template.md)

November 1–28 is the original proposed target calendar, conditional on a passed
Phase 1 gate by October 31. No such completion is recorded. If starting Phase 1
on the forward six-week calendar (October 4–November 14), use November 15–
December 12 for Phase 2 instead. Preserve the order and workload; do not
compress 150 hours into the remaining original calendar or silently assume past
study. The November milestone in the root roadmap remains a target, not an
achievement.

Each session asks: what assumption controls the result, and what observation
would change the explanation? Retain an original trace/calculation or raw
results, then corrected reasoning. Time spent alone is not evidence. Reserve the
explicit review/catch-up slots; unresolved gaps move proposed dates.

## Week 1

Target: 2026-11-01 to 2026-11-07. Forward fallback: 2026-11-15 to 2026-11-21.

| Session | Hours | Objective                            | Required source IDs                                                              | Activity/evidence                                                               |
| ------- | ----- | ------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 1       | 3     | Loading and lifecycle                | p2-m1-generate, p2-m1-api, p2-m1-format, p2-m1-padding, p2-m1-model              | E01 trace and public model metadata; original record and interpretation         |
| 2       | 3     | Generation and streaming boundaries  | p2-m1-generate, p2-m1-api, p2-m1-format, p2-m1-padding, p2-m1-model              | E01 code trace and E07 cold boundary; original record and interpretation        |
| 3       | 3     | Lifecycle exit; prefill introduction | p2-m1-generate, p2-m1-api, p2-m1-format, p2-m1-padding, p2-m1-model, p2-m2-cache | 1 h M1 exit; 2 h M2 prefill prediction; original record and interpretation      |
| 4       | 3     | Prefill versus decode                | p2-m2-cache, p2-m2-strategies, p2-m2-paged, p2-m2-prefix                         | E02 length sweep; original record and interpretation                            |
| 5       | 3     | Output scaling and review            | p2-m2-cache, p2-m2-strategies, p2-m2-paged, p2-m2-prefix                         | E03, 0.5 h catch-up and 0.5 h weekly review; original record and interpretation |

Sources resolve to exact readings in [sources.yaml](sources.yaml).

## Week 2

Target: 2026-11-08 to 2026-11-14. Forward fallback: 2026-11-22 to 2026-11-28.

| Session | Hours | Objective                   | Required source IDs                                                          | Activity/evidence                                                                     |
| ------- | ----- | --------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1       | 3     | KV estimate; memory budget  | p2-m2-cache, p2-m2-strategies, p2-m2-paged, p2-m2-prefix, p2-m3-optimization | 2 h M2 E04; 1 h M3 weights/workspace; original record and interpretation              |
| 2       | 3     | Representations and support | p2-m3-optimization, p2-m3-quant, p2-m3-bnb, p2-m3-cuda                       | E05 backend and dtype plan; original record and interpretation                        |
| 3       | 3     | Precision comparison        | p2-m3-optimization, p2-m3-quant, p2-m3-bnb, p2-m3-cuda                       | E05 repeated comparison; original record and interpretation                           |
| 4       | 3     | OOM and accounting          | p2-m3-optimization, p2-m3-quant, p2-m3-bnb, p2-m3-cuda                       | E09 simulation and allocator explanation; original record and interpretation          |
| 5       | 3     | Memory consolidation        | p2-m3-optimization, p2-m3-quant, p2-m3-bnb, p2-m3-cuda                       | E04/E05 analysis, 0.5 h catch-up and 0.5 h review; original record and interpretation |

Sources resolve to exact readings in [sources.yaml](sources.yaml).

## Week 3

Target: 2026-11-15 to 2026-11-21. Forward fallback: 2026-11-29 to 2026-12-05.

| Session | Hours | Objective                         | Required source IDs                                                  | Activity/evidence                                                                      |
| ------- | ----- | --------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| 1       | 3     | Batch policies and queue timeline | p2-m4-continuous, p2-m4-orca, p2-m4-arch, p2-m4-padding              | E06 analytic scheduler timeline; original record and interpretation                    |
| 2       | 3     | Batch and concurrency sweeps      | p2-m4-continuous, p2-m4-orca, p2-m4-arch, p2-m4-padding              | E06 measurements; original record and interpretation                                   |
| 3       | 3     | Scheduling exit; metrics          | p2-m4-continuous, p2-m4-orca, p2-m4-arch, p2-m4-padding, p2-m5-bench | 1 h M4 exit; 2 h M5 timestamp definitions; original record and interpretation          |
| 4       | 3     | Fair benchmark design             | p2-m5-bench, p2-m5-metrics, p2-m5-gpu, p2-m5-cuda                    | E06/E07 controlled comparison analysis; original record and interpretation             |
| 5       | 3     | Metric consolidation              | p2-m5-bench, p2-m5-metrics, p2-m5-gpu, p2-m5-cuda                    | Raw record review, 0.5 h catch-up and 0.5 h review; original record and interpretation |

Sources resolve to exact readings in [sources.yaml](sources.yaml).

## Week 4

Target: 2026-11-22 to 2026-11-28. Forward fallback: 2026-12-06 to 2026-12-12.

| Session | Hours | Objective                | Required source IDs                                  | Activity/evidence                                                                  |
| ------- | ----- | ------------------------ | ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1       | 3     | Profiler and baseline    | p2-m6-profiler, p2-m6-cuda, p2-m6-smi, p2-m6-python  | E08 trace and competing hypotheses; original record and interpretation             |
| 2       | 3     | One-variable diagnosis   | p2-m6-profiler, p2-m6-cuda, p2-m6-smi, p2-m6-python  | E08/E09 analysis; 0.5 h catch-up; original record and interpretation               |
| 3       | 3     | Serving responsibilities | p2-m7-arch, p2-m7-online, p2-m7-metrics, p2-m7-paged | API/scheduler/worker annotated request map; original record and interpretation     |
| 4       | 3     | vLLM code bridge         | p2-m7-arch, p2-m7-online, p2-m7-metrics, p2-m7-paged | Readiness map, 0.5 h catch-up and 0.5 h review; original record and interpretation |
| 5       | 3     | Final assessment         | p2-m7-arch, p2-m7-online, p2-m7-metrics, p2-m7-paged | 3 h final gate, not charged to M7; original record and interpretation              |

Sources resolve to exact readings in [sources.yaml](sources.yaml).

## Hour accounting

Week 1: M1 7 + M2 8. Week 2: M2 2 + M3 13. Week 3: M4 7 + M5 8. Week 4: M6 6 +
M7 6 + final assessment 3. These are 60 hours; weekly reviews/catch-up are
inside the module allocations. The final session covers all final assessments
and the readiness decision.
