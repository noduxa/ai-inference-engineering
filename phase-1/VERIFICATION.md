# Harness implementation verification

Last verified: 2026-09-16. This records implementation checks, not learner
progress. Learning status: Not started. NotebookLM imports: To be validated.

## Scope reviewed

- Seven ordered modules, seven source packs, nine reusable study prompts.
- Seven exercise-specification files containing 32 individually identified
  tasks.
- Five final assessments, weekly review and four-dimension rubric.
- Root README and roadmap integration; existing milestone dates preserved.
- Machine-readable source and curriculum registries plus validation tooling.
- 88 module hours and two final-assessment hours, scheduled as six 15-hour weeks
  from 20 September through 31 October 2026.

## Research and source choices

Web searches preceded selection. Exact source pages were opened and inspected
for content and section names. The registry contains **28 source collections**,
four per module: one primary and three supporting. Collections contain **79
unique URLs** in total, including exact API pages and MIT transcript PDFs.
NotebookLM batches use four to eight pages at once, rather than treating a
documentation index as a whole book. Optional visual work reuses authoritative
figures or MIT segments rather than adding another overlapping tutorial.

Python/NumPy/PyTorch documentation supplies API semantics; D2L and MIT supply
selected theory; Hugging Face supplies tokenization and generation references;
NVIDIA supplies GPU concepts. The original transformer paper is paired with D2L.
All selected learning resources are free to read; no paid or
registration-required source is assigned. Optional hosted execution and
NotebookLM have separate account and resource requirements.

## Link repairs made during research

- Replaced PyTorch rolling documentation redirect stubs with inspected versioned
  content URLs and corrected the save/load tutorial filename.
- Replaced stale D2L generalization and weight-decay paths that reached the book
  landing page with the actual chapter pages.
- Replaced an MIT lecture-index redirect loop with individual lecture resources
  and inspected official transcript PDFs for import.
- Replaced unavailable rendered NVIDIA quantization-guide paths with the
  official repository’s documentation source. Only the format concepts are
  assigned; optimization commands and advanced serving integrations are
  excluded.

No inaccessible candidate remains in the selected registry. Repository-wide
external checks also found one existing GitHub issue-creation link that requires
sign-in, plus five existing redirects outside the new source packs. The sign-in
link is a contribution action, not a required learning source; it was left
intact. The validator reports HTTP reachability separately from content
relevance and NotebookLM compatibility.

## Reproducible checks

See [scripts/README.md](scripts/README.md) for commands. Verification uses an
isolated environment with PyYAML 6.0.3; no model or GPU dependencies were
installed.

- Source registry: required fields, duplicate IDs/keys, URL formats and dates.
- Curriculum: prerequisite/source/exercise/assessment references and hour
  totals.
- All five YAML files parse; source-pack exact URLs match the registry.
- All 24 source-validator unit tests pass using mock HTTP responses.
- Live bounded GET checks: all 79 registered URLs reachable without redirects.
- All 308 internal Markdown links resolve; Markdown lint passes across 80 files.
- Changes reviewed for accidental credentials and private content; synthetic
  examples and test fixtures are not actual experiment results.

The pull request records final command outcomes and counts after all edits.

## Limitations and manual actions

- No NotebookLM account was accessed, authenticated or automated. Joshua must
  import and inspect each active batch manually, including formulas and code.
- No curriculum exercise, CUDA run, benchmark or learner assessment was
  performed.
- CUDA-specific evidence needs compatible NVIDIA hardware. CPU/conceptual work
  may proceed, but does not establish CUDA execution proficiency.
- A simulated allocation-budget refusal is explicitly distinct from a real OOM.
- Full books and full MIT lectures are not assigned. The 90-hour estimate
  assumes existing software-engineering fluency and selective reading, not
  exhaustive study.
- Documentation versions and APIs may change. Published/update dates are
  recorded only when stated; an HTTP check date does not certify API
  compatibility.
- No learning completion or specialist credential is claimed.
