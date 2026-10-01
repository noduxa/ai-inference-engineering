# Source policy

Last verified: 2026-09-30. Policy status: Active; learning status remains Not
started.

[Registry](sources.yaml) · [Validator](scripts/README.md) ·
[NotebookLM](notebooklm/README.md)

## Authority hierarchy

1. Official language, framework and vendor documentation for current API
   behaviour.
2. Original peer-reviewed research or original papers on arXiv with venue
   context.
3. Globally recognized university courses for established theory.
4. Official researcher-authored books and open textbooks.
5. Recognized technical organizations.
6. Established practitioners only when they add exceptional explanatory value.

A primary source establishes the module’s main definitions and sequence. A
supporting source fills a specific gap. An original paper establishes
provenance; it does not automatically provide a beginner-friendly lesson. A
visual explanation supports understanding and does not override authoritative
semantics.

## Compact selection and overlap

Use one primary collection and two to four supporting collections per module.
Prefer four to eight individual pages per active NotebookLM session. Large
collections are divided into explicit import batches; an index is never counted
as having supplied its linked chapters. Reuse the same source across modules
when the objective changes, but budget only targeted rereading. Optional visual
study uses already selected diagrams or lecture segments rather than redundant
blogs.

## Currency and verification

Search before selection, open each exact assigned page and inspect substantive
content and section names. Check that successful HTTP responses contain the
intended resource, not a redirect stub, login page or unrelated landing page.
Record the verification date separately from publication/update dates. Use “Not
stated” when a page supplies no trustworthy update date; do not substitute a
search crawl date.

Prefer current official API guidance and record the locally installed versions.
Versioned PyTorch references avoid inspected rolling-path redirect stubs;
recheck before installation. Older MIT mathematics and the original transformer
paper remain appropriate for stable theory. Older NVIDIA performance examples
are not current hardware specifications or expected experiment results.

## Stale-source replacement

1. Run offline validation and optional HTTP checks before a source update.
2. Inspect flagged content manually. A 403, 429, timeout or bot challenge is an
   access limitation, not proof the underlying source is academically invalid.
3. Find the canonical publisher page and check title, sections and intended
   scope.
4. Replace the URL and section selections in the registry and source pack
   together.
5. Record the reason and new verification date in the change/PR; rerun checks.
6. Never silently substitute an aggregator, mirror or paywalled copy.

## Access, licensing and copyright

Selected learning pages are free to read without required registration. Optional
hosted execution, NotebookLM itself or model downloads may have account, region,
quota or hardware conditions. These are distinct from source access.

Store links, original study instructions, small necessary compliant quotations
and Joshua’s own notes. Do not copy books, papers, course transcripts or
protected code into this repository. Source text keeps its own license; the
repository’s Apache license does not relicense it. Inspect publisher terms
before uploading a copy to any third-party service. A public URL is not
permission to redistribute content.

## Citations and NotebookLM compatibility

Cite source title, URL, section and version where available. Attach claims to
the source that actually supports them. Distinguish observations from
predictions and AI-generated explanations from checked facts.

Compatibility is recorded as To be validated until Joshua manually verifies
imports. Website ingestion may omit images, embedded videos and child pages;
mathematical symbols and code may be distorted. Use the exact text page or an
official PDF when permitted, check its contents, and state missing coverage. See
[Google’s source-import guidance](https://support.google.com/gemininotebook/answer/16215270?hl=en)
.

Do not automate NotebookLM authentication or import. Do not upload private,
employer, client or patient material. Never bypass an access restriction; record
it and select a legitimate alternative if needed.
