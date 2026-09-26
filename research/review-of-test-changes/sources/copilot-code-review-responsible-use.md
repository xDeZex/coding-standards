---
source: https://docs.github.com/en/enterprise-cloud@latest/copilot/responsible-use/code-review
source_date: undated
researched: 2026-09-26
---

# GitHub Docs: Responsible use of Copilot code review

First-party vendor documentation, read through a fetch tool that summarises pages, so quotes are as returned by that tool and need re-checking against the page. Undated page.

- What it does: reviews pull request diffs and metadata on GitHub.com, producing feedback comments and suggested changes.
- Limitation, missed problems: it "may not identify all of the problems that are present in code, especially where changes are large or complex."
- Limitation, false positives: "a risk of hallucination - it may highlight problems in reviewed code that do not exist or are based on misunderstandings of the code."
- Suggestions "may appear to be valid but may not actually be semantically or syntactically correct".
- Human role: "Use Copilot code review to supplement human reviews, not to replace them"; feedback should be "supplemented with careful human code review", before merging.
- The page (as summarised) does not mention tests being weakened or deleted, and gives no accuracy figures.
- Also seen only in search snippets, unverified: Copilot reviews a risk-selected subset of files in large PRs (community discussion #152385, not a first-party statement). If true, a test file could be skipped.
- Classification: an inferential control; the vendor itself says it misses problems and hallucinates.
