---
source: https://learn.chatgpt.com/docs/third-party/github
source_date: undated
researched: 2026-09-26
---

# OpenAI Codex docs: code review on GitHub pull requests

First-party vendor documentation. How it was read this time: fetched with curl (final URL after redirect) and converted to text, read in full for the review sections. Undated. The earlier note's quoted wording was not exact (see below).

- Default focus: "Codex flags only P0 and P1 issues so review comments stay focused on high-priority risks." (Page also says Codex posts "a standard GitHub code review focused on serious issues".) A weakened test may fall below that bar unless the team's rules say otherwise; that is our inference.
- Customisation: a `## Code Review Rules` section in `AGENTS.md`, nearest file to the code, nested files allowed. Advice on rules includes: "Leave mechanical checks in CI. Keep formatting, lint, and other deterministic checks out of review rules." The earlier note's quote ("Leave formatting, lint, and other deterministic checks in CI") was a paraphrase and is replaced by this wording.
- "Code review rules guide Codex; they don't replace tests, branch protections, or required approvals."
- Triggered with `@codex review` in a PR comment, or automatically per repository; needs Codex cloud set up on the repository.
- The search-snippet claim that Codex "surfaces regressions, missing tests, and documentation issues" is not on the page and is dropped.
- No detection rates, no mention of test tampering.
- Classification: an inferential control, advisory.
