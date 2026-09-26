---
source: https://testdouble.com/insights/keep-your-coding-agent-on-task-with-mutation-testing
source_date: 2025-10-21
researched: 2026-09-26
---

# Mutation testing with coding agents: Test Double post and Meta ACH report

Two sources on mutation score as a signal about agent-written tests. How they were read this time: the Test Double post via curl and html-to-text, full; the InfoQ report via curl and html-to-text, full; Meta's own paper (arXiv 2501.12862, "Mutation-Guided LLM-based Test Generation at Meta", FSE Companion 2025) via arxiv PDF and pdftotext, read for abstract and the engineers' evaluation section.

- Test Double (Neal Lindsay, 2025-10-21): tells agents to run formatting, linting, typechecking and unit tests after every change; says "There is no full substitute to reading and understanding the code". Has the agent run Stryker (JS/TS) on changed files; when the agent complies ("It can take some coaxing") "it can increase the quality of the tests it writes dramatically, requiring your attention less often". Evidence is personal experience and one screen recording he asks readers not to read. Claude reported a final score of 96.30% that was 94.44% when he re-ran it: "a reminder to not take these tools at their word". Agents sometimes give up before 100%, sometimes reasonably, with no guarantee they will not give up too early. Anecdote, not measurement.
- InfoQ (Leela Kumili, 2026-01-06, https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/): quotes Meta: from October to December 2024, "privacy engineers accepted 73% of the tests, with 36% judged as privacy relevant".
- Meta paper (primary): ACH ran on 10,795 Android Kotlin classes in 7 platforms, generating 9,095 mutants and 571 privacy-hardening tests; the 73% comes from two test-a-thons in the week of 9 December 2024 (WhatsApp and Messenger, 6 reviewers each): of 191 tests reviewed, 140 accepted (73%); WhatsApp 56%, Messenger 90% (94% in a pre-screened phase). About 36% scored as privacy relevant (Likert 4 or 5); the authors note engineers accepted tests for other reasons (added coverage, tricky corner cases). It measures engineers accepting generated tests, not a guard against weakened tests. The InfoQ text is faithful to the paper's own abstract; "trial" in InfoQ refers to the whole deployment, the 73% is from the test-a-thons.
- The earlier note's claims about mutation score gating on the PR diff and AI assistants reaching high line coverage with surviving mutants came from search snippets and are removed as unverified.
- Neither source tests mutation score against an agent deliberately weakening tests. Whether a mutation-score drop would reveal weakened assertions is plausible and not shown by either.
