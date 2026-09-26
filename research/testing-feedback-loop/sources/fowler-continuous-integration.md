---
source: https://martinfowler.com/articles/continuousIntegration.html
source_date: 2024-01-18
researched: 2026-09-26
---

# Martin Fowler, "Continuous Integration" (revised 2024; first published 2000)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Date: revised 18 January 2024; the original is from 10 September 2000. Author Martin Fowler. The article quotes Kent Beck / Extreme Programming for several rules.
- Self-testing build: the build includes a comprehensive automated test suite "run before each integration to flush out as many bugs as possible". Relates to "self testing code": a sound suite would never let damage through "without a test turning red".
- Broken build: quotes Kent Beck, "nobody has a higher priority task than fixing the build". The build "needs to be fixed right away". The usual remedy described is to revert the latest commit from the mainline, returning to the last known good build.
- Speed: "the XP guideline of a ten minute build is perfectly within reason"; "every minute chiseled off the build time is a minute saved for each developer every time they commit".
- Frequency: quotes Beck, no code sits unintegrated for more than a couple of hours; the article's own rule is that every developer commits to the mainline every day, in small chunks of a few hours' work.
- Staged builds: a commit to the mainline triggers the "commit build", which must be quick and therefore "will take a number of shortcuts that will reduce the ability to detect bugs"; slower stages run tests that use a real database and end-to-end behaviour.
- Test failure as signal: "a test failure alerts that there's a conflict between changes"; the test "gives me some clue about what's gone wrong". Also: "imperfect tests, run frequently, are much better than perfect tests that are never written at all". And "any test failing is enough to fail the build, 99.9% green is still red".
- Flaky tests: the fetch found no dedicated discussion in this article (see the separate note on non-deterministic tests). Unverified whether the article has a short passage I missed.
