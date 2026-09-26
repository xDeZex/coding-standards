---
source: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
source_date: 2026-06-18
researched: 2026-09-26
---

# Anthropic blog: Steering Claude Code, when to use CLAUDE.md, skills, hooks and subagents

Vendor blog post by an Anthropic staff member (Michael Segner, per the byline), read in full as raw page text (curl and html.parser). It is first-party guidance, not a measurement.

- Frames seven ways to instruct Claude Code (CLAUDE.md, rules, skills, subagents, hooks, output styles, appended system prompt), each differing in "When an instruction loads into context; Whether it persists through long sessions (compaction behavior); and How much authority it carries."
- Hooks row of its table: fire on lifecycle events; "Bypass compaction entirely"; context cost "Low. Configuration lives outside main context; some output may return (e.g., blocking errors)"; when to use: "Deterministic automation: run linters, post to Slack on completion, block commands, back up chat history on PreCompact".
- Definition: hooks "provide more deterministic control over Claude's behavior by firing on specific events". "All hooks are deterministically triggered. The first three [command, HTTP, mcp_tool] execute deterministically while the latter two, prompt and agent, use Claude's judgment rather than a set of rules to determine the output."
- Context cost: hooks "have low context costs because they are code that the harness runs rather than instructions to Claude that get loaded into context"; most hook output does not reach the main window "unless the configuration explicitly returns it", but a blocking hook's stderr is saved in context so Claude knows why a call was denied.
- Contrast with CLAUDE.md: "Every line costs tokens whether relevant or not" (High context cost); a shared CLAUDE.md "grows the way any unowned config file does: every team appends its own instructions and nothing gets deleted"; "Keep CLAUDE.md under 200 lines". Rules with no `paths` are "mechanically identical" to CLAUDE.md content.
- When to switch to a hook, as the post states it: "'Every time X, always do Y' in CLAUDE.md. If the behavior should happen reliably, like running prettier after every edit or posting to Slack on completion, use a hook ... The model choosing to run a formatter is different from the formatter running automatically."
- On "never do this": "When there's something that absolutely must not happen, an instruction is the wrong tool. Claude will follow the instruction most of the time, but when under pressure, in a long session or an ambiguous situation, or due to a prompt injection in a file accessed as part of the task, the model can fail to follow a prompted rule. A real guardrail needs to be deterministic, and the enforcement methods are hooks and permissions." "Managed settings go further: they are admin-deployed, cannot be overridden by a user's local config, and are the only way to enforce a deterministic, organization-wide guardrail."
- The post gives no numbers or study behind the claim that instructions fail under pressure; it is stated as fact. It also does not discuss hook failure modes (silent no-fire, fail-open, timeouts), which the reference documents.
- Its own guidance that a compaction-surviving instruction belongs in CLAUDE.md or path-scoped rules and a procedure in a skill sits beside the hook advice; the post's table says hooks "Bypass compaction entirely"; our reading (not stated in the post) is that this is because the harness re-runs them, not because their earlier output persists.
