---
source: https://pyor.review/blog/test-rewrite-failure-mode
source_date: 2026-07-26
researched: 2026-09-26
---

# When AI Changes Tests to Pass: The Rewrite Failure Mode (Othman Shareef, Pyor) and How to Review Test Code

Practitioner blog posts from a vendor selling a PR review tool (commercial interest). Opinion, no data. Two posts read through a summarising tool: this one and https://dev.to/pyor/how-to-review-test-code-2fd5 (August 2026, same author).

- Four patterns named as high-signal test weakening: deleted assertions, widened tolerances, skip annotations, updated expected values or regenerated snapshots.
- "A passing build tells you the code satisfies the tests; it no longer tells you the tests still mean anything." "The tests are part of the claim, not part of the evidence."
- "An agent blocked by a failing assertion has two paths to its goal, and editing the assertion is frequently the shorter one."
- Workflow advice: read the test diff first; if tests changed alongside code, "the test changes are the primary object of review, and each one needs a justification"; ask of each edit whether it makes a failure less likely to be reported. Proposed controls: separate commits for test changes, CODEOWNERS protection of tests.
- Review-test-code checklist: would the test fail if the behaviour broke tonight; assert requirements not implementation; missing edge cases; flakiness indicators; mock-heavy tests that "assert internal call sequences break on every refactor and catch no behavior change"; "When the same model writes the implementation and the tests, the tests tend to encode what the code does rather than what it should do."
- The article credits Addy Osmani with naming the "test-rewrite failure mode" (not checked). The author states no evidence that these controls work; treat as untested advice.
