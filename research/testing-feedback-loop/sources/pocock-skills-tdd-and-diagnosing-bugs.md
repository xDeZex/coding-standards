---
source: https://github.com/mattpocock/skills (commit c55ee46, 2026-09-18; README.md, skills/engineering/tdd/SKILL.md, skills/engineering/diagnosing-bugs/SKILL.md)
source_date: 2026-09-18
researched: 2026-09-26
---

# Matt Pocock, "skills" repository: TDD and diagnosing-bugs skills

Read directly from a clone of the repository (raw files, not summarised). Practitioner source: one author's instructions for AI coding agents, not testing research. Whether this Matt Pocock is the person the requester meant is not verified beyond the repo owner name.

- README, "The Code Doesn't Work": says feedback loops are needed so the agent is not "flying blind": "static types, browser access, and automated tests". For tests, "a red-green-refactor loop is critical": write a failing test first, then fix it, giving the agent "a consistent level of feedback".
- README epigraph, attributed there to David Thomas and Andrew Hunt (*The Pragmatic Programmer*; book not read by me): "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that's too big."
- tdd/SKILL.md, rules of the loop: "Red before green" (write the failing test, then only enough code to pass); "One slice at a time" (one seam, one test, one minimal implementation per cycle). Anti-pattern "horizontal slicing": writing all tests then all code; preferred is vertical slices, each test a "tracer bullet". Anti-patterns "implementation-coupled" (test breaks on refactor with behaviour unchanged) and "tautological" (assertion recomputes the code's own logic, passes by construction).
- diagnosing-bugs/SKILL.md, Phase 1 "Build a feedback loop": "This is the skill." A tight pass/fail signal that goes red on the specific bug is required before hypothesising. Loop must be red-capable (asserts the user's exact symptom, not "runs without erroring"), deterministic, fast ("seconds, not minutes"), agent-runnable. "A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight."
- docs/engineering/tdd.md (repo doc): a user report of an agent burning a long loop on a slow browser test and concluding the test was broken; doc says slow browser tests can make the red-green loop stop paying for itself.
- Not found in the repo: the claim, seen in secondary blog posts, that Pocock asks agents to "prove a change would fail without it". Not verified.
