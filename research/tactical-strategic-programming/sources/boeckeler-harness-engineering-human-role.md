---
source: https://martinfowler.com/articles/harness-engineering.html
source_date: 2026-04-02
researched: 2026-09-26
---

# Harness engineering for coding agent users (Birgitta Böckeler), human-role passages

Primary practitioner article on martinfowler.com. Fetched through a summariser; quotes as returned. This note covers only the human-role and limits passages. (The repo may hold another note on the same article for its harness vocabulary.)

- "The human's job in this is to steer the agent by iterating on the harness."
- "A coding agent has none of this: no social accountability, no aesthetic disgust at a 300-line function, no intuition that 'we don't do it that way here.'"
- "A good harness should not necessarily aim to fully eliminate human input, but to direct it to where our input is most important."
- Architecture matters to how controllable the agent is: "committing to a topology narrows that space, making a comprehensive harness more achievable"; frameworks such as Spring "abstract away details the agent doesn't even have to worry about."
- Limits: "we still have a lot to do to figure out good harnesses for functional behaviour that increase our confidence enough to reduce supervision." LLMs can address semantic-judgment problems "but expensively and probabilistically."
- Bearing on the split: supports humans moving to steering, architecture and harness design (strategic). But it says behaviour correctness, a code-level concern, is not yet trustworthy enough to stop supervising, and that the agent lacks taste at the code level (300-line function). So the tactical level is not simply handed over.
