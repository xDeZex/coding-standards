---
source: https://martinfowler.com/bliki/TestCoverage.html
source_date: 2012-04-17
researched: 2026-09-26
---

# Martin Fowler, "Test Coverage" (bliki)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model; quotes are as returned by that tool and should be re-checked against the page. Human-developer canon; it never mentions agents.

- Coverage shows what is untested: "Test coverage is a useful tool for finding untested parts of a codebase."
- It does not show quality: "Test coverage is of little use as a numeric statement of how good your tests are." Also: "If a part of your test suite is weak in a way that coverage can detect, it's likely also weak in a way coverage can't detect."
- Target effect (Goodhart's law in all but name, not named by the page): "If you make a certain level of coverage a target, people will try to attain it. The trouble is that high coverage numbers are too easy to reach with low quality testing." He points to assertion-free testing as the hollow result.
- His sufficiency test is outcome-based: you rarely get bugs escaping to production, and you are rarely hesitant to change code for fear of them.
- Relevance to a gate: a green run is the same kind of number as coverage, a proxy that can be satisfied without the meaning behind it. This is our reading, not Fowler's.
- Related notes: [Fowler on self-testing code](../../testing-feedback-loop/sources/fowler-self-testing-code.md), [Beck, passing tests bore me](../../testing-feedback-loop/sources/beck-passing-tests-bore-me.md).
