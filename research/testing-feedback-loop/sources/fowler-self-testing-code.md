---
source: https://martinfowler.com/bliki/SelfTestingCode.html
source_date: 2014-05-01
researched: 2026-09-26
---

# Martin Fowler, "SelfTestingCode" (bliki)

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author Martin Fowler; page dated 1 May 2014 (first published 5 May 2005 per the fetch).
- Definition: you can run automated tests against the code base and be confident that, "should the tests pass, your code is free of any substantial defects".
- Frequency: "By running the test suite frequently, at least several times a day, you're able to detect such bugs soon after they are introduced"; recent changes are fresh in mind, so finding the cause is easy.
- Confidence: enables refactoring without fear; described as a "virtuous spiral", in contrast to legacy code no one dares change.
- Practice: on a production bug, first write a test that exposes it, then fix.
