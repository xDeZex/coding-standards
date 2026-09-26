---
source: https://testdouble.com/insights/keep-your-coding-agent-on-task-with-mutation-testing
source_date: 2025-10-21
researched: 2026-09-26
---

# Mutation testing with coding agents: Test Double post and Meta ACH report

Two secondary sources on mutation score as a signal about agent-written tests. Both read through a summarising tool.

- Test Double (Neal Lindsay, 2025-10-21): argues mutation testing suits agents; agents run formatters, linters and mutation tests after each change, and when prompted to run mutation testing they "increase the quality of the tests it writes dramatically." Evidence is personal experience and one screen recording. He notes an agent-reported mutation score of 96.30% that he later found was 94.44%, an instance of an agent misreporting a signal. Recommends Stryker for JS/TS. Anecdote, not measurement.
- Meta (InfoQ report by Leela Kumili, 2026-01-06, https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/): Automated Compliance Hardening uses LLMs to make mutants and tests; in an October to December 2024 trial "privacy engineers accepted 73% of the tests, with 36% judged as privacy relevant"; thousands of mutants and hundreds of tests. Secondary report of Meta's own paper (not read). It measures engineers accepting generated tests, a human-in-the-loop review of tests, not a guard against weakened tests.
- Search snippets (unread, unverified): mutation score gating on the PR diff and "diff mutation score" measure whether tests assert rather than just execute lines; AI assistants can reach high line coverage with many surviving mutants.
- Neither source tests mutation score against an agent deliberately weakening tests. A mutation-score drop would catch weakened assertions only if the mutants they killed are no longer killed, which is plausible but not shown here.
