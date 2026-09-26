---
source: https://google.github.io/eng-practices/review/reviewer/looking-for.html
source_date: undated
researched: 2026-09-26
---

# Google Engineering Practices: what to look for in a code review (tests)

Primary source: Google's public code review guide for reviewers. Fetched through a summarising tool, so the quotes need re-checking against the page.

- Design comes first: "The most important thing to cover in a review is the overall design of the CL."
- Tests: "Ask for unit, integration, or end-to-end tests as appropriate for the change. In general, tests should be added in the same CL as the production code unless the CL is handling an emergency."
- The reviewer is told to check test quality, not only presence: "Will the tests actually fail when the code is broken? If the code changes beneath them, will they start producing false positives?"
- The guide is written for human authors. It has no text on tests being edited to pass, or on agents; the "will they fail when the code is broken" question is the closest match, and it is left to reviewer judgement with no signal or tool named.
