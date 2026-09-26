---
source: https://google.github.io/eng-practices/review/reviewer/looking-for.html
source_date: undated
researched: 2026-09-26
---

# Google Engineering Practices: what to look for in a code review (tests)

Primary source: Google's public code review guide for reviewers. How it was read this time: fetched with curl and converted to text, full page; quotes verified.

- Design first: "The most important thing to cover in a review is the overall design of the CL."
- Tests: "Ask for unit, integration, or end-to-end tests as appropriate for the change. In general, tests should be added in the same CL as the production code unless the CL is handling an emergency."
- "Make sure that the tests in the CL are correct, sensible, and useful. Tests do not test themselves, and we rarely write tests for our tests—a human must ensure that tests are valid."
- "Will the tests actually fail when the code is broken? If the code changes beneath them, will they start producing false positives? Does each test make simple and useful assertions?" Also: tests are code that has to be maintained; do not accept complexity in tests.
- Written for human authors; no text on tests edited to pass or on agents. The "will they fail when the code is broken" question is the closest match, left to reviewer judgement with no signal or tool named.
