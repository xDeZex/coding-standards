---
source: https://docs.github.com/en/enterprise-cloud@latest/copilot/responsible-use/code-review
source_date: undated
researched: 2026-09-26
---

# GitHub Docs: Responsible use of Copilot code review

First-party vendor documentation. How it was read this time: fetched with curl and converted to text; the code review sections were read and every quote below matches the page. The page now also covers the cloud agent and CLI. Undated.

- What it does: "Reviews pull request diffs and metadata on GitHub.com, producing feedback comments and suggested changes." Input is the code changes plus context such as the pull request's title and body and custom instructions, sent to a language model.
- Missed problems: "Copilot may not identify all of the problems that are present in code, especially where changes are large or complex."
- False positives: "Copilot code review has a risk of hallucination - it may highlight problems in reviewed code that do not exist or are based on misunderstandings of the code."
- Suggestions "may appear to be valid but may not actually be semantically or syntactically correct".
- Human role: "Use Copilot code review to supplement human reviews, not to replace them"; feedback should be "supplemented with careful human code review".
- The page does not mention tests being weakened or deleted, and gives no accuracy figures for code review.
- Separate, not first-party: community discussion https://github.com/orgs/community/discussions/152385 (fetched and read) collects user reports, e.g. "Copilot reviewed 5 out of 15 changed files in this pull request and generated no comments" with the unreviewed files given as "Evaluated as low risk", and another user reporting 115 of 191 files reviewed with only a couple of comments. These are user reports in a forum thread, not GitHub statements; a reply in the thread attributing it to risk-based skipping is unofficial. If they hold, a test file could be skipped.
- Classification: an inferential control; the vendor itself says it misses problems and hallucinates.
