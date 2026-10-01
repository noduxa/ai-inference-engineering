# Validation tooling

[Phase 1 home](../README.md) · [Source policy](../SOURCE_POLICY.md)

The tools validate the harness, not Joshua’s learning. Python 3.10+ is required.
PyYAML is the only added dependency; HTTP, CLI and test code use the standard
library. No model packages, GPU, NotebookLM login or cloud resources are
required.

## Setup

From the repository root, use a disposable virtual environment:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r phase-1/scripts/requirements.txt
```

## Offline checks

```bash
.venv/bin/python -m unittest discover -s phase-1/scripts/tests -v
.venv/bin/python phase-1/scripts/validate_sources.py
.venv/bin/python phase-1/scripts/validate_harness.py
npx --yes markdownlint-cli2@0.18.1 '**/*.md'
```

`validate_sources.py` checks required fields and types, dates, source IDs, exact
sections and URL syntax. Duplicate YAML mapping keys are rejected. A malformed
registry exits 2. Offline validation does not make a network request.

`validate_harness.py` checks YAML, module prerequisites,
source/assessment/exercise references, source-pack URL consistency, learning
statuses, the six-week/90-hour budget and local Markdown file/heading links. It
exits 1 for inconsistencies. If a module is later marked Completed, add an
`evidence` list of existing file paths relative to `phase-1`; a human still
needs to assess their quality. The simple heading checker covers the current
documents, not every possible GitHub Markdown extension.

## Optional HTTP checks

```bash
.venv/bin/python phase-1/scripts/validate_sources.py --http --timeout 15
.venv/bin/python phase-1/scripts/validate_sources.py --strict-http
```

Use `--json /tmp/phase-1-links.json` to save a machine-readable HTTP report
outside the repository. A bounded GET reads at most 32 KiB per response, follows
public HTTP redirects and recognizes static HTML refresh stubs. It does not
execute JavaScript, authenticate, store cookies or persist page bodies.
Non-public network destinations and HTTPS downgrades are rejected. Checks are
sequential to avoid a burst of requests to documentation sites; timeouts are per
request.

Results distinguish reachable, redirected, blocked, inaccessible and unverified.
The default HTTP mode reports all findings without turning access restrictions
into malformed-data errors. `--strict-http` exits 1 for inaccessible links;
403/429 blocks and transport failures still require manual review. Neither mode
treats a successful response as proof of correct page content. Inspect redirects
and update the registry to the final content URL when appropriate.

The tests are offline and mock network responses. They cover missing fields,
duplicate IDs/keys, invalid types/dates/URLs, redirect handling, challenge
pages, HTTP errors, timeouts and non-public destinations. Use these tools only
with reviewed registry URLs; they are not a general-purpose crawling service.

## Both phases

Use the [shared entry point](../../scripts/README.md) for both-phase checks, new
metadata fields and cross-phase reference validation.
