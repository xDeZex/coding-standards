---
source: https://testing.googleblog.com/2010/12/test-sizes.html
source_date: 2010-12-13
researched: 2026-09-26
---

# Simon Stewart, "Test Sizes" (Google Testing Blog)

Reading method: re-read 2026-09-26 as raw page text (curl, HTML stripped with a small python parser). The earlier summarising fetch had wrong limits; corrected below. Flaky-test figures were read from the raw page of a second post, named below.

- The post gives a table, "Time limit (seconds)": Small 60, Medium 300, Large 900+. The earlier note said medium 600 s (10 minutes) and large no limit; both were wrong. The 60 s small / 10 min medium figures in the task brief do not match the page: medium is 300 s (5 minutes).
- Small: no network access, no database, no file system access, no external systems, no multiple threads, no sleep statements, no system properties. Medium: network "localhost only", database and file system allowed, external systems "Discouraged", threads and sleeps allowed. Large: all of those allowed ("Yes").
- Mapping stated: "A Small test equates neatly to a unit test, a Large test to an end-to-end or system test and a Medium test to tests that ensure that two tiers in an application can communicate properly (often called an integration test)."
- Isolation: "tests can be run in any order (they frequently are!) which in turn means that tests need high isolation", which makes parallel running easier. This is stated for tests generally, not as a medium-only rule. The page does not say large tests may need human interaction.
- Limits can be policed: e.g. a Java security manager configured per test size, and a size annotation (no annotation means Small).
- The point of the post is defining sizes by measurable constraints instead of vague terms.
- Limits for our use: these are Google's 2010 per-test limits, not a latency budget for a gating hook. The post says nothing about hooks, commits or agents. Whether a suite is small enough to gate every commit or stop is our inference.
- Flaky-test figures, from a different primary page, John Micco, "Flaky Tests at Google and How We Mitigate Them", Google Testing Blog, 2016-05-27 (https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html), read raw: about 1.5% of all test runs report a flaky result ("a test that exhibits both a passing and a failing result with the same code"); "Almost 16% of our tests have some level of flakiness"; "about 84% of the transitions we observe from pass to fail involve a flaky test" in post-submit CI. For a gate: a flaky test in a blocking hook produces false blocks, and the post says people ignore alarms with a history of false signals.
- Related notes: [Google, just say no to e2e tests](../../testing-feedback-loop/sources/google-just-say-no-to-e2e-tests.md), [Google SWE book testing overview](../../testing-feedback-loop/sources/google-swe-book-testing-overview.md), [Fowler, non-deterministic tests](../../testing-feedback-loop/sources/fowler-non-deterministic-tests.md), [Google, flaky tests mitigation](../../testing-feedback-loop/sources/google-flaky-tests-mitigation.md).
