---
source: https://pyor.review/blog/test-rewrite-failure-mode
source_date: 2026-07-26
researched: 2026-09-26
---

# When AI Changes Tests to Pass: The Rewrite Failure Mode (Othman Shareef, Pyor) and How to Review Test Code

Practitioner blog posts from a vendor selling a PR review tool (commercial interest). Opinion, no data. How they were read this time: both posts fetched with curl and converted to text, read in full: this one, and https://dev.to/pyor/how-to-review-test-code-2fd5 (posted 2026-08-16 on dev.to, originally pyor.review 2026-08-15, same author).

- Four patterns named as high-signal test weakening: deleted or gutted assertions, widened tolerances, skips and exclusions (including tests renamed so the runner no longer collects them), updated expected values (snapshots or golden files regenerated).
- "A passing build tells you the code satisfies the tests; it no longer tells you the tests still mean anything." "In an agent PR, the tests are part of the claim, not part of the evidence" (quoted as a sentence from the author's other piece).
- "An agent blocked by a failing assertion has two paths to its goal, and editing the assertion is frequently the shorter one."
- Advice: read the test diff first; if tests changed alongside code, "the test changes are now the primary object of review, and each one needs a justification that would survive being read aloud". Policy: separate test changes into their own commit or PR; tell agents to stop and report rather than edit tests, noting they follow that "imperfectly". Automation: a CI job that diffs assertion counts, a bot flagging added skips, widened tolerances or snapshot regeneration, CODEOWNERS on high-value test directories.
- dev.to post: one question ("if the behavior this test covers broke tonight, would the test fail?"), a "mental mutation" check, assert requirements not implementation, edge cases, flakiness smells; "When the same model writes the implementation and the tests, the tests tend to encode what the code does rather than what it should do, so they pass by construction" (an unsupported assertion).
- Osmani credit: the post says Addy Osmani "flags this test-rewrite failure mode as one of the defining risks" and links https://addyosmani.com/blog/agentic-code-review/ (read; see osmani-agentic-code-review-test-changes.md). That page describes the behaviour but does not use the phrase "test-rewrite failure mode"; the name appears to be Pyor's.
- The page gives no evidence that these controls work; treat as untested advice.
