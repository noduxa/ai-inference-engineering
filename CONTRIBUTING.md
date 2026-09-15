# Contributing

This is Joshua Nsereko’s public learning and contribution journey. Corrections,
focused learning suggestions and reproducible technical investigations are
welcome. Read the [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## Evidence standards

- Evidence must be reproducible, with methods and artifacts available for
  review.
- Planned work must not be presented as completed. Use **Planned**, **Not
  started** or **To be validated** until supporting evidence exists.
- Link technical sources and record the relevant version or revision.
- Experiments must state hardware, software versions and configuration,
  including model revision, tokenizer, precision, workload, seeds and relevant
  constraints.
- Benchmark comparisons must use controlled conditions. State warmup,
  repetitions, concurrency, input/output lengths, measurement boundaries and
  confounding factors.
- Publish failures and uncertainty. Never invent measurements or contribution
  history.
- Review generated material for accuracy before submitting it.

## Workflow

1. Open a focused learning, experiment or documentation issue where useful.
2. Work on a branch and keep pull requests focused on one understandable change.
3. Follow the relevant [experiment](experiments/README.md),
   [benchmark](benchmarks/README.md) or [runbook](runbooks/README.md) format.
4. Check relative Markdown links and run Markdown linting where available.
5. Record tests actually run, their outcomes and anything not tested.
6. Complete the pull-request template with reproducible evidence and
   limitations.

## Markdown validation

Run `npx --yes markdownlint-cli2@0.18.1 '**/*.md'` from the repository root.
The lint configuration keeps the default rules and permits long table rows so
that the milestone table remains readable in Markdown source.

## Privacy and independence

Never include sensitive employer, client or patient information, protected
health information, credentials, private repository content,
employer-confidential information, client configuration, or internal hostnames
or IP addresses. Use synthetic data and publicly shareable infrastructure
descriptions. Inspect logs, screenshots, notebook outputs and commit metadata
before publication.

Do not make claims on behalf of Noduxa, Madiro, MSF, OpenMRS or any other
organization. Hosting under Noduxa does not make these experiments employer or
client work. Publish no unverified benchmark results.

## Licensing

Submit only material you have the right to share under the
[Apache License 2.0](LICENSE). Preserve attribution and applicable licenses for
third-party material, including the Contributor Covenant.
