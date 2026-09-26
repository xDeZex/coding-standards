---
source: https://testing.googleblog.com/2017/04/where-do-our-flaky-tests-come-from.html
source_date: 2017-04-17
researched: 2026-09-26
---

# Jeff Listfield, "Where do our flaky tests come from?" (Google Testing Blog)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author Jeff Listfield, 17 April 2017. First-party Google data.
- Analysed about 4.2 million tests. Flakiness rose with test size (binary size used as the measure), roughly linearly, with Android emulator tests notably flakier. Even very small tests showed some flakiness.
- Signal value: for one team, when a previously stable test turned flaky and could be traced to a specific code change, the cause was a real product bug about one time in six.
- Stated consequence: ignoring flaky tests risks eventually ignoring a real bug; the post argues for systematic identification, notification, triage and prevention.
- Exact figures beyond these were not captured; unverified.
