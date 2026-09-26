# Position: testing as the agent's feedback loop

Tests are necessary. An agent with no check it can run has only "looks done" to go on, and a runnable test is the check ([Claude Code docs](sources/claude-code-docs-best-practices-verification.md)). This position is about the agent running tests while it works and before it finishes or commits, and what it does with a red run. Coverage, mutation testing and test-driven development are other topics and are only pointed at here.

Much of this is my experience and is not measured. Where that is so, I say it.

## The commit hook is the guarantee

I prefer a commit hook to only telling the agent to run the tests. A git hook runs all the tests I want, deterministically, and the agent might not run them on its own. The vendor docs and [Böckeler's experiment](sources/boeckeler-sensors-for-coding-agents.md) point the same way, but the only observation is one author's anecdote, so this rests mainly on my own experience.

The hook does not replace the agent running tests itself. That is not bad, and I think models will run their own tests even when a hook exists. The two complement each other: the agent's own runs give it feedback while it works, and the hook is the backstop that runs regardless of what the agent decided.

## Where the instruction lives

If the agent has to be told explicitly how to run the tests, I would put that in a skill and not in AGENTS.md. I think modern models run tests when they are given instructions on how to do it. Both beliefs are experience. No source measures how often agents run tests unprompted, or compares instruction files, skills and hooks for getting tests run.

## A green run from an agent is weaker evidence

An agent can make a red run go green by editing, deleting or special-casing the tests instead of fixing the code. This is the best measured area in the research, but almost all of it is on benchmarks and impossible or ambiguous tasks, not ordinary repository work ([ImpossibleBench](sources/impossiblebench-test-exploitation.md), [EvilGenie](sources/evilgenie-reward-hacking-benchmark.md), [Anthropic's 3.7 Sonnet system card](sources/anthropic-claude-3-7-sonnet-system-card-special-casing.md)). A commit hook does not stop it, because it only checks that the tests pass.

This is a real weakness and I have no proven answer to it. My stance is to pair the loop with a check on what changed in the tests, such as human review of test diffs or an AI reviewer, and to treat a green run as necessary but not sufficient. That is a stance, not a tested solution. Read-only tests stop test editing but not special-casing.

## When the agent keeps getting red

My tentative view is that the agent should stop after a number of failed attempts and report what is failing and what it tried, instead of forcing green. Cheating appears most after repeated failure, and an honest stop costs less than a green run that means nothing. I have not tried this, and I give no number: the only one in the sources is Stripe's two CI rounds, and that is for full CI, not local runs ([Stripe](sources/stripe-minions-one-shot-coding-agents.md)).

## When it does not hold

The loop does not hold if the suite is slow or flaky. A red run is only worth acting on when the tests are fast and deterministic, which is the standard from before AI ([Fowler](sources/fowler-non-deterministic-tests.md), [DORA](sources/dora-test-automation.md)). The answer is the same as it was then: fix the suite first. I give no separate speed target for agents.

It also holds less well where the spec or the tests are ambiguous, or the task cannot be solved, since that is where the sources see gaming rise.

## Other topics

I think test-driven development is hard for the AI because it does not respect red, and it may not be how an AI should work, since it thinks differently from humans. I have had some success with [Pocock's TDD skill](sources/pocock-skills-tdd-and-diagnosing-bugs.md). Whether to require 100% coverage and mutation tests is a robustness choice for when it is needed. Both belong to the tests-first and test-quality topics, not this one.

## Gaps for follow-up research

Listed here and not yet researched:

- Instruction file versus skill versus hook for getting tests run: no measured comparison exists.
- How often agents on ordinary repository work run tests unprompted, treat red as a signal to fix the code, or weaken tests when a project suite goes red.
