---
source: https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html
source_date: 2015-04-22
researched: 2026-09-26
---

# Mike Wacker, "Just Say No to More End-to-End Tests" (Google Testing Blog)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author Mike Wacker, 22 April 2015.
- Argues end-to-end tests give slow feedback, are flaky (environment dependence) and are costly to maintain; with mostly E2E tests "your test runtime (and the number of test flakes) will inflate significantly".
- Recommends a pyramid of roughly 70% unit, 20% integration, 10% end-to-end, adding "the exact mix will be different for each team, but in general, it should retain that pyramid shape."
- Diagnosis point: a failing E2E test shows that something broke but not where; finding the cause takes extra work and often exposes missing unit or integration tests.
