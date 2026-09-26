---
source: https://code.claude.com/docs/en/code-review
source_date: undated
researched: 2026-09-26
---

# Claude Code docs: Code Review (what it checks and does not)

First-party vendor documentation, read as the raw Markdown of the page (the page carries no date; it is marked a research preview for Team and Enterprise plans). Records what the vendor claims, not measured performance.

- Design: "multiple agents analyze the diff and surrounding code in parallel"; each looks for a different class of issue, "then a verification step checks candidates against actual code behavior to filter out false positives." Results are deduplicated, ranked by severity and posted as inline comments.
- Scope: "By default, Code Review focuses on correctness: bugs that would break production, not formatting preferences or missing test coverage." Checks can be expanded with `CLAUDE.md` or `REVIEW.md`. So by default the tool is not pointed at whether tests were weakened; a team has to ask for it.
- `REVIEW.md` (review-only instructions) is given to the agents that find and verify findings. The docs' examples of repo-specific rules include "New API routes have an integration test", and the example file also tells the reviewer to skip "Test-only code that intentionally violates production rules". A rule such as "flag deleted or loosened assertions" is not given in the docs; it would be our own addition.
- Findings are tagged by severity (Important, Nit, pre-existing) and "don't approve or block your PR"; the review is advisory, not a gate.
- Cost and time: "completing in 20 minutes on average"; "Each review averages $15-25 in cost", scaling with PR size. Reviewing on every push multiplies cost.
- Local `/code-review` command reviews a diff in the terminal; at `low`/`medium` effort it reports only its most confident findings ("fewer false positives"), and `high` to `max` "may include findings the review is less sure about". Vendor's own statement of a precision/coverage trade-off, with no numbers.
- The page gives no detection rate, no false-positive rate, and no mention of test tampering or reward hacking.
- Classification: an inferential control (LLM judgement, non-deterministic, slow, paid per run) in Böckeler's vocabulary.
