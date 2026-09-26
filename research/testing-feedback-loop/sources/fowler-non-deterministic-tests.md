---
source: https://martinfowler.com/articles/nonDeterminism.html
source_date: 2011-04-14
researched: 2026-09-26
---

# Martin Fowler, "Eradicating Non-Determinism in Tests"

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author Martin Fowler, 14 April 2011.
- Definition: tests that sometimes pass and sometimes fail "without any noticeable change in the code, tests, or environment".
- Harm 1, lost signal: "When a regression test goes red, you have no idea whether its due to a bug, or just part of the non-deterministic behavior."
- Harm 2, spreading: "Once you start ignoring a regression test failure, then that test is useless... it has an infectious quality." His example: a few non-deterministic failures in a suite lead a team to ignore failures generally.
- Remedy stated first: quarantine non-deterministic tests in a separate suite from healthy ones, with a limit (a count cap or a time limit) so quarantined tests are not forgotten.
- Causes and treatments listed: lack of isolation (rebuild fixtures rather than rely on cleanup; roll back transactions); asynchrony (no bare sleeps, use callbacks or polling with configurable timeouts); remote services (test doubles with contract tests); time (wrap the system clock so it can be substituted); resource leaks (pool sizes of 1 in tests to surface leaks).
