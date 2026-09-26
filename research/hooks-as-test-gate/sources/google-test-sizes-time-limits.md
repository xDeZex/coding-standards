---
source: https://testing.googleblog.com/2010/12/test-sizes.html
source_date: 2010-12-13
researched: 2026-09-26
---

# Simon Stewart, "Test Sizes" (Google Testing Blog)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model; quotes as returned, exact wording unverified.

- Small tests: "less than 60 seconds"; must be isolated from each other; no network access, no database, no file system.
- Medium tests: "less than 600 seconds (10 minutes)"; may use the file system and network; must be able to run in parallel.
- Large tests: no time limit; end-to-end system tests; may require human interaction.
- The point of the post is defining sizes by measurable constraints instead of vague terms.
- Limits for our use: these are Google's 2010 per-test limits, not a latency budget for a gating hook. The post says nothing about hooks, commits or agents. Whether a suite is small enough to gate every commit or stop is our inference.
- Related notes: [Google, just say no to e2e tests](../../testing-feedback-loop/sources/google-just-say-no-to-e2e-tests.md), [Google SWE book testing overview](../../testing-feedback-loop/sources/google-swe-book-testing-overview.md), [Fowler, non-deterministic tests](../../testing-feedback-loop/sources/fowler-non-deterministic-tests.md), [Google, flaky tests mitigation](../../testing-feedback-loop/sources/google-flaky-tests-mitigation.md).
