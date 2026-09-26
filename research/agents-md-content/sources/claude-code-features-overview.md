---
source: https://code.claude.com/docs/en/features-overview
source_date: undated
researched: 2026-09-26
---

# Extend Claude Code: when to use CLAUDE.md, skills, hooks

First-party documentation. Re-read 2026-09-26 from the raw HTML (curl, html.parser) in full; quotes checked, one corrected below. Assertions without cited data.

- Load model: CLAUDE.md loads in full at session start and costs context on every request. Skills load descriptions at session start and full content when used. Hooks load nothing unless they return output.
- CLAUDE.md versus skill: put it in CLAUDE.md "if Claude should always know it: coding conventions, build commands, project structure, 'never do X' rules"; in a skill "if it's reference material Claude needs sometimes ... or a workflow you trigger with /<name>". Rule of thumb: under 200 lines; move reference content to skills or path-scoped rules.
- Its own CLAUDE.md example line is "Use pnpm, not npm. Run tests before committing." Elsewhere: "Use CLAUDE.md for instructions every session needs: build commands, test conventions, project architecture." The page therefore recommends build commands and test conventions in CLAUDE.md.
- Hook versus skill: hook row of the comparison table: "Always fires on its event; the trigger is guaranteed"; skills: "Claude interprets the instructions; outcome can vary". "Put guardrails in hooks. An instruction like 'never edit .env' in CLAUDE.md or a skill is a request, not a guarantee." Hook output that lands in context (a lint run) is text Claude reads; a skill tells Claude how to resolve it.
- Hook-versus-skill wording also says "Use a hook when the action must happen the same way every time and doesn't need Claude to think" and "If a rule must hold every time, make it a hook rather than a prompt instruction"; a skill is for "workflows that need reasoning, reference material, multi-step tasks" and "Use a skill when Claude should decide how to apply the steps, or when the content is knowledge rather than a script". The CLAUDE.md-versus-skill row reads "reference material Claude needs sometimes (API docs, style guides) or a workflow you trigger with /<name> (deploy, review, release)", so skills are for invocable workflows as well as reference, not reference only.
- Trigger table: "Claude gets a convention or command wrong twice" then add it to CLAUDE.md; "You keep typing the same prompt to start a task" or paste a multi-step procedure for the third time then make a skill; "You want something to happen every time without asking" then a hook.
- Skill selection caveat: "Claude matches your task against skill descriptions ... If descriptions are vague or overlap, Claude may load the wrong skill or miss one that would help." Too many features "can also add noise that makes Claude less effective; skills may not trigger correctly, or Claude may lose track of your conventions."
- Links to a Claude blog post, "Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents", not read.
