---
source: https://testdesiderata.com/
source_date: undated
researched: 2026-09-26
---

# Kent Beck, "Test Desiderata"

Reading method: fetched through a page-to-Markdown tool that summarises with a small model, not read verbatim end to end. Quotes below are as returned by that tool; treat exact wording as unverified against the page.

- Author Kent Beck (site credits Kelly Sutton). Page shows no date; the original essays were on Medium (from the fetch, not checked).
- Twelve properties a test may have, each with a stated definition: Isolated (same result regardless of order), Composable, Deterministic ("if nothing changes, the test result shouldn't change"), Fast, Writable, Readable, Behavioral (sensitive to behaviour changes), Structure-insensitive (result does not change when structure changes), Automated, Specific ("if a test fails, the cause of the failure should be obvious"), Predictive ("if the tests all pass, then the code under test should be suitable for production"), Inspiring ("passing the tests should inspire confidence").
- Trade-offs: some properties support each other (automation helps speed); others conflict (predictiveness tends to cost speed); composability can sometimes ease a conflict. Not every property is wanted in every test.
