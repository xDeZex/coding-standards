---
source: https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
source_date: 2025-06-25
researched: 2026-09-26
---

# Kent Beck: Augmented Coding: Beyond the Vibes (newsletter Q&A)

Primary source: first-hand practitioner account by Kent Beck on his own newsletter (page HTML read; the piece is a Q&A about his BPlusTree3 project). One author's experience, not a measurement.

- Distinguishes vibe coding ("you don't care about the code, just the behavior... If there's an error, you feed it back into the genie") from augmented coding, where "you care about the code, its complexity, the tests, & their coverage."
- Says he was "trying to get the genie to use TDD" from the first commits; his first two attempts accumulated complexity until "the genie completely stalled", so he intruded more on the design and "tried to keep the genie from coding ahead", watching intermediate results to stop unproductive work.
- Warning signs he watched for: "Loops. Functionality I hadn't asked for (even if it was a reasonable next step). Any indication that the genie was cheating, for example by disabling or deleting tests."
- His system prompt (appendix, quoted from the page) tells the agent to follow the TDD cycle Red, Green, Refactor; "Write the simplest failing test first"; "Implement the minimum code needed to make tests pass"; and a commit discipline: "Only commit when: 1. ALL tests are passing 2. ALL compiler/linter warnings have been resolved 3. The change represents a single logical unit of work". It also says to validate that structural changes do not alter behaviour "by running tests before and after" and to "Run tests after each refactoring step". A plan.md is used with an instruction to find the next unmarked test and implement it.
- Outcome he reports: good about correctness and performance, "not so good about the code quality"; still trying to get the agent "to care as much as I do about simplicity."
- Does not report frequency data on how often the agent deleted or disabled tests, nor whether the prompt reduced it; it lists it only as something to watch for.
