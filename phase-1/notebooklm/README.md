# Manual NotebookLM study workflow

Harness status: Planned. Manual import status: To be validated. Last verified:
2026-09-16.

[Phase 1 home](../README.md) · [Prompt templates](prompts/README.md) ·
[Source policy](../SOURCE_POLICY.md)

## Source packs

- [Advanced Python for AI systems](source-packs/01-advanced-python.md)
- [NumPy, tensors and numerical computing](source-packs/02-numpy-and-tensors.md)
- [Essential mathematics](source-packs/03-essential-mathematics.md)
- [PyTorch fundamentals](source-packs/04-pytorch-fundamentals.md)
- [Neural-network fundamentals](source-packs/05-neural-networks.md)
- [Transformer architecture](source-packs/06-transformers.md)
- [GPU architecture, precision and memory](source-packs/07-gpu-architecture-and-memory.md)

## A study session

1. Create the named notebook manually using your own account. This repository
   contains no authentication or automation for NotebookLM.
2. Add the exact pages in the current import batch; keep four to eight active
   pages. Four source collections can contain more than four pages. Do not
   bulk-import every linked API page, an entire website or an entire textbook.
3. Check each source’s actual text. Web imports do not bring nested pages,
   images or embedded videos. MIT lecture landing pages are not lecture
   transcripts; use the linked official transcript PDF when allowed. Confirm
   formulas and code survived import. See
   [Google’s guidance](https://support.google.com/gemininotebook/answer/16215270?hl=en).
4. Ask the initial questions. Ask for missing coverage before relying on an
   answer.
5. Generate a short Audio Overview or guide within the reading time budget.
6. Close the generated explanation and perform the exercise yourself.
7. Submit your own teach-back for critique, check citations, then take the exit
   test.

## Grounding and provenance

Keep source IDs in imported names. Distinguish authoritative sources, your notes
and generated material. Important claims need source/section references; missing
coverage must be acknowledged. Cross-check citations manually. Generated quizzes
and flashcards are study aids, not an authoritative answer key or proof of
completion.

A feature’s availability can depend on your account or current product
interface. If an Audio Overview or quiz control differs, use the prompt as a
manual study instruction. No account tier, quota or successful import is
assumed.

## Import log template

For each notebook record date, source ID, exact page, successful/failed import,
formula/code checks, source restrictions and missing topics in your own study
log. If a source fails, read the original and write your own cited notes; do not
bypass access controls or copy protected material without permission. Revalidate
imports when source versions change.
