---
source: https://abseil.io/resources/swe-book/html/ch11.html
source_date: 2020
researched: 2026-09-26
---

# Software Engineering at Google, ch. 11 "Testing Overview" (Adam Bender; O'Reilly)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Book published 2020 (year from memory, not shown in the fetch; unverified). Authors of the chapter per the fetch: Adam Bender, edited by Tom Manshreck.
- Test size is defined by resources, not lines: small tests run in a single process (no I/O, sleeping or network calls); medium tests may use several processes, threads and localhost network calls on one machine; large tests may span machines.
- Speed and determinism: "the most important qualities we want from our test suite are speed and determinism, regardless of the scope of the test." Small tests are "almost always faster and more deterministic" because the constraints remove sources of slowness.
- Flakiness arithmetic: 10,000 tests at 0.1% flakiness means about 10 flakes investigated per day. Google reports about 0.15% flakiness, fights to keep it there, and says "as you approach 1% flakiness, the tests begin to lose value."
- Pyramid proportions Google aims for: about 80% narrow unit tests, 15% medium integration, 5% end-to-end. The chapter presents these as guidelines.
- Velocity: "The more and faster you want to change your systems, the more you need a fast way to test them." Case study: after automated testing was introduced for the Google Web Server team, emergency pushes fell by half.
- Brittle tests (over-specified, heavy boilerplate) resist change; heavy mock use has led some engineers to say "no more mocks".
