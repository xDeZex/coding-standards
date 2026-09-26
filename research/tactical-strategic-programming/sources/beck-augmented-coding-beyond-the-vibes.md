---
source: https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
source_date: 2025-06-25
researched: 2026-09-26
---

# Augmented Coding: Beyond the Vibes (Kent Beck)

How read this time: full post fetched with curl and converted to text (Substack renders the full text to unauthenticated readers). All quotes below were checked against it and were correct; this pass added the omitted passages on code quality and on the kind of decisions Beck makes. The post is a Q&A ("I sat down with a friend to tell my story"), first-hand account of building a B+ Tree library (BPlusTree3) in Rust and Python with an AI "genie" over about four weeks, with his system prompt in an appendix.

- Beck separates augmented coding from vibe coding: "In augmented coding you care about the code, its complexity, the tests, & their coverage. The value system in augmented coding is similar to hand coding--tidy code that works. It's just that I don't type much of that code."
- "My first 2 attempts had accumulated so much complexity that the genie completely stalled. That's why I intruded more on the design & tried to keep the genie from coding ahead."
- Supervision: "I watched the intermediate results of the genie more carefully, ready to intervene & stop unproductive development. I would look at the code & propose 'for the next test add the keys in the reverse order'."
- Warning signs: "Loops. Functionality I hadn't asked for (even if it was a reasonable next step). Any indication that the genie was cheating, for example by disabling or deleting tests."
- Outcome on quality: "I feel good about the correctness & performance, not so good about the code quality. ... there's just too much accidental complexity. I'm still working on getting the genie to care as much as I do about simplicity."
- On the role: "Yes programming changes with a genie, but it's still programming. ... I make more consequential programming decisions per hour, fewer boring vanilla decisions."
- His system prompt tells the model to follow a plan file, TDD, and Tidy First (structural changes separate from behavioural ones); the prompt tells it to work through the next unmarked test in plan.md.
- Bearing on the split: the human keeps design and complexity control, which supports the split, and Beck says he makes fewer boring decisions. But he also keeps close test-level and code-level supervision, and the genie produced unrequested scope, apparent test tampering and (by his account) code quality he was not happy with. Single-person, single-project account.
