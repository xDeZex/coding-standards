---
source: https://martinfowler.com/articles/harness-engineering.html
source_date: 2026-04-02
researched: 2026-09-26
---

# Harness engineering for coding agent users (Birgitta Böckeler), human-role passages

How read this time: full article fetched with curl and converted to text and read in full. Quotes below were checked against it; two were corrected (see marks). This note covers only the human-role and limits passages. (The repo may hold another note on the same article for its harness vocabulary.)

Primary practitioner article on martinfowler.com, dated 02 April 2026. It states the author used Claude and Claude Code for research and language polishing.

- "The human's job in this is to steer the agent by iterating on the harness."
- Section "The role of the human": "A coding agent has none of this: no social accountability, no aesthetic disgust at a 300-line function, no intuition that 'we don't do it that way here,' and no organisational memory." Humans also "carry organisational alignment" and "go in small steps and at our human pace".
- "A good harness should not necessarily aim to fully eliminate human input, but to direct it to where our input is most important."
- Architecture and controllability (sections "Harnessability" and "Ashby's Law"): "frameworks like Spring abstract away details the agent doesn't even have to worry about and therefore implicitly increase the agent's chances of success"; "An LLM-based coding agent can produce almost anything, but committing to a topology narrows that space, making a comprehensive harness more achievable." Greenfield teams "can bake harnessability in from day one - technology decisions and architecture choices determine how governable the codebase will be."
- Limits: "we still have a lot to do to figure out good harnesses for functional behaviour that increase our confidence enough to reduce supervision and manual testing." (Corrected: the earlier note cut off "and manual testing".) On the maintainability harness: "LLMs can partially address problems that require semantic judgment ... but expensively and probabilistically." (Corrected: the earlier note dropped "partially".) She adds that neither computational nor inferential sensors catch reliably "misdiagnosis of issues, overengineering and unnecessary features, misunderstood instructions ... not reliably enough to reduce supervision", and that the behaviour harness "puts a lot of faith into the AI-generated tests, that's not good enough yet."
- Bearing on the split: supports humans moving toward steering, architecture and harness design. It also says that behavioural correctness, overengineering and misdiagnosis are not reliably caught yet and that the agent lacks the human's taste, so the code level is not simply handed over. The article does not use tactical or strategic.
