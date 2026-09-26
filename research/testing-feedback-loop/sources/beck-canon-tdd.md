---
source: https://newsletter.kentbeck.com/p/canon-tdd
source_date: 2023-12-11
researched: 2026-09-26
---

# Kent Beck, "Canon TDD"

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author Kent Beck (originator of TDD), 11 December 2023. Primary source for the workflow. Originally at tidyfirst.substack.com (301 redirect to the address above).
- Steps: (1) list the expected variants of the new behaviour (the test list); (2) turn exactly one item into a real, runnable, automated test (setup, invocation, assertions); (3) change the code to make that test pass, plus all previous tests; (4) optionally refactor; (5) repeat until the list is empty.
- The test list step is behavioural analysis, not implementation planning.
- The test is expected to fail first (red), then pass (green). "Make it run, then make it right": do not mix refactoring into the make-it-pass step.
- Mistakes Beck lists: writing all tests up front; deleting assertions to get green; mixing refactoring into making the test pass; abstracting prematurely ("Duplication is a hint, not a command").
- Small steps: one test at a time, each cycle ends with the whole suite passing. Precise wording beyond the above not captured; unverified.
