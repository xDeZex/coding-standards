---
source: https://martinfowler.com/bliki/TestPyramid.html
source_date: 2012-05-01
researched: 2026-09-26
---

# Martin Fowler, "TestPyramid" (bliki)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author Martin Fowler, 1 May 2012. Secondary owner: he credits the idea to others.
- Attribution stated in the article: the pyramid comes from Mike Cohn (book *Succeeding with Agile*, 2009; Cohn discussed it with Lisa Crispin around 2003-4). Jason Huggins is said to have arrived at the same idea independently around 2006. The Cohn book itself was not read.
- Three levels: many low-level unit tests at the base, fewer service-layer ("subcutaneous", through an API rather than UI) tests in the middle, fewest GUI / end-to-end tests at the top.
- Stated reason for few UI tests: tests through the UI are "brittle, expensive to write, and time consuming to run".
- Names the "ice-cream cone" anti-pattern: high-level UI tests dominate the suite and cause maintenance pain.
- Caveat in the source: "If my high level tests are fast, reliable, and cheap to modify - then lower-level tests aren't needed." So the argument is about speed, reliability and cost, not about level as such.
- Not in the source as read: numeric proportions, time limits.
