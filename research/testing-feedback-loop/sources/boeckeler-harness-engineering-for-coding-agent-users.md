---
source: https://martinfowler.com/articles/harness-engineering.html
source_date: 2026-04-02
researched: 2026-09-26
---

# Harness engineering for coding agent users (Birgitta Böckeler)

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere. Author and date as reported by the fetch: Birgitta Böckeler, 2 April 2026.

## Classes of control

- Guides are feedforward controls: they "anticipate the agent's behaviour and aim to steer it before it acts", to raise the probability of a good first attempt.
- Sensors are feedback controls: they "observe after the agent acts and help it self-correct". She says they are "particularly powerful when they produce signals that are optimised for LLM consumption."
- Both are needed: "Separately, you get either an agent that keeps repeating the same mistakes (feedback-only) or an agent that encodes rules but never finds out whether they worked (feed-forward-only)."
- Execution type is a second axis. Computational: "Deterministic and fast, run by the CPU. Tests, linters, type checkers, structural analysis. Run in milliseconds to seconds; results are reliable." Inferential: "Semantic analysis, AI code review, 'LLM as judge'... Slower and more expensive; results are more non-deterministic."
- Trade-off stated: computational controls raise the probability of good results with deterministic tooling; inferential controls "are of course more expensive and non-deterministic, but allow us to both provide rich guidance, and add additional semantic judgment."

## Tests, hooks, CI, AI review

- Tests are placed among computational sensors. Computational sensors "catch the structural stuff reliably: duplicate code, cyclomatic complexity, missing test coverage, architectural drift, style violations."
- Behaviour harness limit: the approach "puts a lot of faith into the AI-generated tests, that's not good enough yet." The "approved fixtures" pattern is mentioned as used "selectively where it fits, it's not a wholesale answer to the test quality problem."
- Mutation and structural testing are named as computational feedback sensors "underused in the past, but are now having a resurgence."
- Hooks: pre-push hooks are mentioned only via Stripe's write-up (pre-push hooks that run relevant linters based on a heuristic; "shifting feedback left").
- CI timing: teams integrating continuously have always had to spread tests, checks and reviews across the timeline; for continuous delivery, "you want to have checks as far left in the path to production as possible, since the earlier you find issues, the cheaper they are to fix." Post-integration stages hold "more expensive sensors" that rerun earlier ones.
- AI review: LLMs "can partially address problems that require semantic judgment - semantically duplicate code, redundant tests, brute-force fixes, over-engineered solutions - but expensively and probabilistically. Not on every commit." Custom review skills (for example a detailed-review skill) run post-integration in pipelines.
- Human role: a good harness should not aim to fully eliminate human input but "direct it to where our input is most important." Open question: how far agents can be trusted to make trade-offs when instructions and feedback signals conflict.

## Outbound sources it rests on (as listed by the fetch)

OpenAI harness-engineering post; Stripe minions post; Böckeler's sensors article and harness-engineering memo; approved-fixtures pattern (augmented-coding-patterns); Fowler on continuous integration and continuous delivery; Thoughtworks Radar on fitness functions; Ashby's law of requisite variety.

## Unverified

- Full text not read line by line; the fetch tool summarised it.
