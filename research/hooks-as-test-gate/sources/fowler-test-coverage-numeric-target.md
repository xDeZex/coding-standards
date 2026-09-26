---
source: https://martinfowler.com/bliki/TestCoverage.html
source_date: 2012-04-17
researched: 2026-09-26
---

# Martin Fowler, "Test Coverage" (bliki)

Re-read pass 2026-09-26: the whole (short) page was downloaded with curl as HTML, converted to text and read end to end; every quote below was checked verbatim and matches. Page date 17 April 2012 confirmed. No summarising tool. Human-developer canon; it never mentions agents.

- Coverage shows what is untested: "Test coverage is a useful tool for finding untested parts of a codebase."
- It does not show quality: "Test coverage is of little use as a numeric statement of how good your tests are." Also: "If a part of your test suite is weak in a way that coverage can detect, it's likely also weak in a way coverage can't detect."
- Target effect (Goodhart's law in all but name, not named by the page): "If you make a certain level of coverage a target, people will try to attain it. The trouble is that high coverage numbers are too easy to reach with low quality testing." He points to assertion-free testing as the hollow result.
- More detail on the page: he would "expect a coverage percentage in the upper 80s or 90s" from thoughtful testing and "be suspicious of anything like 100%"; "low coverage numbers, say below half, are a sign of trouble". The two lines quoted above about weak suites are attributed on the page to Brian Marick (the "weak in a way that coverage can detect" line) and the page quotes Marick: "I expect a high level of coverage. Sometimes managers require one. There's a subtle difference."
- Test speed and staging, directly relevant to a gate: "Some people think that you have too many tests if they take too long to run. I'm less convinced by this argument. You can always move slow tests to a later stage in your deployment pipeline, or even pull them out of the pipeline and run them periodically. Doing these things will slow down the feedback from those tests, but that's part of the trade-off of build times versus test confidence."
- His sufficiency test is outcome-based: you rarely get bugs escaping to production, and you are rarely hesitant to change code for fear of them.
- Relevance to a gate: a green run is the same kind of number as coverage, a proxy that can be satisfied without the meaning behind it. This is our reading, not Fowler's.
- Related notes: [Fowler on self-testing code](../../testing-feedback-loop/sources/fowler-self-testing-code.md), [Beck, passing tests bore me](../../testing-feedback-loop/sources/beck-passing-tests-bore-me.md).
