---
source: https://martinfowler.com/articles/sensors-for-coding-agents.html
source_date: 2026-05-27
researched: 2026-09-26
---

# Sensors for coding agents (Birgitta Böckeler)

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere. Author and date as reported by the fetch: Birgitta Böckeler, 27 May 2026. Follow-up to the harness engineering article; an experiment on maintainability sensors in one application.

- Tests as regression sensors: "they help us detect regressions, i.e. they tell us when we break pre-existing functionality with a change." They let the agent tell intentional change from accidental breakage during refactoring.
- Coverage is weak evidence: "Coverage is not a sufficient indicator of test effectiveness." Mutation testing (Stryker) found 13 surviving mutants in a file with 100% coverage and no real unit tests.
- Getting the agent to run sensors: a Markdown instruction (guide) was "quite unreliable. I had to ask the agents many, many times why it had not run the sensors check." A git pre-commit hook "can be a good way" for agents that commit often in small steps. A custom agent extension was tried but needed longer use to judge.
- Sensor output design: a custom ESLint formatter that embeds guidance in the failure message steered self-correction better than external documentation.
- She deliberately used no guides, to see sensors' effect alone, and asks "Once we feel confident in a set of sensors, what guides can we delete?"
- Computational vs inferential: computational sensors (linter, type checker, dependency checker) handle file-level hygiene well but cross-file concerns (modularity, coupling) were "very noisy". An LLM modularity review found "quite concerning and very valid findings" computational tools missed, but an LLM coupling analysis mischaracterised intentional patterns as problems ("noise") without enough context; it needs strong prompting and grounding in deterministic data.
- Trade-off seen: max-lines rules pushed refactors into smaller functions that moved complexity elsewhere; "more trade-offs like that are probably lurking."

Unverified: single experiment by one author; not read line by line.
