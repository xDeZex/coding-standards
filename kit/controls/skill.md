# Skill

- **What it is:** A folder with a `SKILL.md` that the agent loads on demand: a description always in context, and a body read only when the skill fires. The kit lists skills worth using in the [Skills list](../skills/README.md).
- **Use when:** the agent needs a procedure or reference only some tasks reach, such as how to run this repo's tests, and it should not sit in context on every turn.

## Where it sits

A skill is a guide: it steers the agent before it acts and observes nothing afterward. It is inferential in effect: the model reads and interprets the text, so the same skill can be followed differently from run to run, and it enforces nothing the way a hook or a test does. Pair it with a sensor when the result must be guaranteed.

## How to write a good one

Write it as a document for an agent. The principles are in the repo's `writing-for-agents` skill (`.claude/skills/writing-for-agents/SKILL.md`), and its `SKILL-MECHANICS.md` covers frontmatter and invocation.

- **The description is a pointer.** It sits in context every turn and decides when the skill fires. Front-load the trigger, give one trigger per branch, and keep it short.
- **Keep the body to steps and the reference they need.** Each step ends on a criterion the agent can check. Push material only some branches reach into a sibling file behind a pointer.
- **Choose the invocation.** Model-invoked when the agent must reach it alone; user-invoked (`disable-model-invocation: true`) when only you would type it.
- **Do not restate what the environment holds.** Point at the command or config instead of copying it.

## Worked example: running the tests

The position on [testing as the agent's feedback loop](../../research/testing-feedback-loop/position.md) says that if the agent has to be told explicitly how to run the tests, that instruction belongs in a skill and not in AGENTS.md. For example, a skill whose description names the trigger ("running the tests, before finishing or committing"), whose body gives the command, says what a red run means, and says to stop and report after repeated failures rather than force green.

This is the author's experience and is unmeasured. No source compares an instruction file, a skill and a hook for getting tests run, so treat it as a stance to try and check in your repo, not a proven result. A skill also does not guarantee the tests run; a commit hook does (see [Hook](hook.md)).
