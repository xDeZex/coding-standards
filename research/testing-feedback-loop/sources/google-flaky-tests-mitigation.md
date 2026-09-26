---
source: https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html
source_date: 2016-05-27
researched: 2026-09-26
---

# John Micco, "Flaky Tests at Google and How We Mitigate Them" (Google Testing Blog)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author John Micco, 27 May 2016. First-party account from Google.
- Coverage limit: the fetch returned mostly metadata and the comment thread, not the post body. The statistics I remember from this post (about 1.5% of runs flaky, about 16% of tests with some flakiness) were NOT confirmed and are not recorded as findings.
- Confirmed from the fetch: the post says a test that fails reliably is far better than a flaky one, because a persistent failure gives a clear signal about what to do.
- Mitigations described: separate results by flags and configuration to assess flakiness; mark known-flaky tests; rerun only marked-flaky tests or on request; quantify cost to developer workflow. The post says Google does not keep an accurate count of cases where flakiness hid a real bug.
- Comments on the page (not the author's claims) discuss lost developer time; ignored here.
