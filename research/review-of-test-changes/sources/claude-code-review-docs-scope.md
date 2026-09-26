---
source: https://code.claude.com/docs/en/code-review
source_date: undated
researched: 2026-09-26
---

# Claude Code docs: Code Review (what it checks and does not)

First-party vendor documentation. How it was read this time: fetched with curl and converted to text (html parser), read for every claim below; verified against the page text. The page carries no date; it is marked a research preview for Team and Enterprise plans. Records what the vendor claims, not measured performance.

- Design: "multiple agents analyze the diff and surrounding code in parallel"; each looks for a different class of issue, "then a verification step checks candidates against actual code behavior to filter out false positives." Results are deduplicated, ranked by severity and posted as inline comments.
- Scope: "By default, Code Review focuses on correctness: bugs that would break production, not formatting preferences or missing test coverage." Checks can be expanded with `CLAUDE.md` or `REVIEW.md`. By default the tool is not pointed at whether tests were weakened; a team has to ask for it.
- `REVIEW.md` (review-only instructions) goes to the agents that find and verify findings. The docs' examples of repo-specific rules include "New API routes have an integration test" (under "Always check"); the example file's "Do not report" list includes "Test-only code that intentionally violates production rules". A rule such as "flag deleted or loosened assertions" is not given in the docs; it would be our own addition.
- The local `/code-review` command "doesn't read REVIEW.md" (it follows CLAUDE.md).
- Findings are tagged by severity (Important, Nit, Pre-existing) and "don't approve or block your PR"; the review is advisory, not a gate.
- Cost and time: "completing in 20 minutes on average"; "Each review averages $15-25 in cost", scaling with PR size, codebase complexity and issues needing verification.
- Local `/code-review` effort levels: at low and medium it reports only the findings it is most confident in ("fewer false positives"); high through max "broaden coverage and may include findings the review is less sure about". A stated precision/coverage trade-off with no numbers.
- The page gives no detection rate, no false-positive rate, and no mention of test tampering or reward hacking.
- Classification: an inferential control (LLM judgement, non-deterministic, slow, paid per run) in Böckeler's vocabulary.
