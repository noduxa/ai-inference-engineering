# Shared learning-system validation

The shared entry point validates both phases. It reuses the existing Phase 1
YAML loader and safe HTTP checker rather than maintaining duplicate network
code. Python 3.10+ and the existing pinned PyYAML dependency are sufficient;
model packages are not needed for structural checks or unit tests.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r phase-1/scripts/requirements.txt
.venv/bin/python -m unittest discover -s phase-1/scripts/tests -v
.venv/bin/python -m unittest discover -s scripts/tests -v
.venv/bin/python scripts/validate_learning.py
.venv/bin/python scripts/validate_learning.py --http --json /tmp/learning-links.json
npx --yes markdownlint-cli2@0.18.1 '**/*.md'
```

Structural errors exit 2. Checks cover duplicate YAML keys and IDs, required
source metadata, URL syntax, cross-phase IDs, missing/unused source references,
prerequisites, assessments, source-pack URLs, exercise paths, evidence/status
fields, schedule totals and local Markdown links/headings. The link parser
covers the repository's ordinary Markdown, not every renderer extension.
Completion status requires evidence files; a human still evaluates their
quality.

HTTP checks use the existing bounded public GET implementation, following safe
redirects and distinguishing blocked, inaccessible and unverified responses.
Access restrictions are reports, not malformed-data failures or evidence that a
source lacks authority. HTTP 200 alone never certifies relevant content. Review
the JSON report and inspect source sections manually. The older Phase 1 commands
remain available for backwards compatibility and targeted checks.

## Source inspection record

[source-review.json](source-review.json) records each exact inspected URL,
selected sections and an extracted-content hash. It contains no copied source
bodies. This is an inspection record, not an HTTP status cache or proof that all
upstream examples run. Update it when source selections change. New lab
integration tests and their isolated dependencies are documented in the
[lab guide](../phase-2/scripts/README.md).
