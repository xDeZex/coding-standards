---
source: https://martinfowler.com/articles/harness-engineering.html
source_date: 2026-04-02
researched: 2026-09-26
---

# Birgitta Böckeler, Harness engineering for coding agent users (martinfowler.com)

Read via curl and html-to-text (raw page, about 19,000 characters); read the passages on hooks, timing and examples in full, not every paragraph. The page says "02 April 2026: published full article", with an earlier memo from 17 February 2026. Speaker and why trusted: see [bockeler-sensors-git-hook-as-integration-option](bockeler-sensors-git-hook-as-integration-option.md). It is the source of the repo's vocabulary.

- Her table of examples lists "Structural tests", feedback, computational, as "A pre-commit (or coding agent) hook running ArchUnit tests that check for violations of module boundaries". So a git hook and an agent hook appear as alternative places to run the same sensor, with no ranking.
- Section "Timing: Keep quality left": "You want to have checks as far left in the path to production as possible, since the earlier you find issues, the cheaper they are to fix." She asks "What is reasonably fast and should be run even before integration, or even before a commit is even created? (e.g. linters, fast test suites, basic code review agent)" and "What is more expensive and should therefore only be run post-integration in the pipeline, in addition to a repetition of the fast controls? (e.g. mutation testing, a more broad code review ...)". So her frame puts fast checks before the commit and expensive ones in the pipeline, with the fast ones repeated there.
- On LLM checks: "LLMs can partially address problems that require semantic judgment ... but expensively and probabilistically. Not on every commit."
- The steering loop: "Whenever an issue happens multiple times, the feedforward and feedback controls should be improved to make the issue less probable to occur in the future, or even prevent it."
- Stripe is cited: "pre-push hooks that run relevant linters based on a heuristic ... 'shift feedback left'" (see [stripe-minions-part-2-pre-push-hooks-and-ci-rounds](stripe-minions-part-2-pre-push-hooks-and-ci-rounds.md), read from Stripe's own post).
- She says neither computational nor inferential sensors catch reliably "Misdiagnosis of issues, overengineering and unnecessary features, misunderstood instructions", so a commit gate does not cover those.
