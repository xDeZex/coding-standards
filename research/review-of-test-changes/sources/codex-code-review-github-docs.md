---
source: https://learn.chatgpt.com/docs/third-party/github
source_date: undated
researched: 2026-09-26
---

# OpenAI Codex docs: code review on GitHub pull requests

First-party vendor documentation, read through a fetch tool that summarises pages (the older developers.openai.com URL redirects here), so wording needs re-checking. Undated. Only this page was read; the search snippets also said Codex "surfaces regressions, missing tests, and documentation issues", which was not confirmed on the page as fetched.

- Default focus: Codex flags "only P0 and P1 issues so review comments stay focused on high-priority risks." A weakened test may fall below that bar unless the team's rules say otherwise.
- Customisation: a `## Code Review Rules` section in `AGENTS.md` (nested files allowed). Guidance quoted: describe what to flag and why; "Leave formatting, lint, and other deterministic checks in CI".
- Triggered with `@codex review` in a PR comment; needs Codex cloud set up on the repository.
- No detection rates, no mention of test tampering.
- Classification: an inferential control, advisory.
