---
source: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
source_date: 2026-03-12
researched: 2026-09-26
---

# HumanLayer, "Skill Issue: Harness Engineering for Coding Agents" (hooks and closing notes)

Speaker: the HumanLayer team's blog, byline "Kyle" (a HumanLayer engineer; the post says "we" and "our repo"). HumanLayer is Dex Horthy's company; Horthy authored "12-factor agents" and coined "context engineering", a widely used practice. Counts as trusted: a team reporting "dozens of projects and hundreds of agent sessions" of first-hand work, and Addy Osmani cites the post approvingly. The byline is a colleague, not Horthy, so the trust is by team.

How read: raw HTML via curl and html-to-text; whole page read, hook sections in full.

- Framing: hooks are one of five configuration points ("Skills, MCP servers, sub-agents, hooks, and back-pressure mechanisms"). The section is titled "Hooks Are for Control Flow". "Hooks are conceptually similar to git hooks, but they're quite flexible." They note Opencode has plugins and "(Sadly, Codex doesn't have an equivalent.)" (March 2026; the vendor page read for the conclusion says Codex now has hooks).
- Uses they run: notifications ("play sounds when they finish or when they need attention"); approvals ("we automatically deny any Bash() tool calls that try to run migrations, with an instruction to ask the user to run them instead"); integrations (Slack message, GitHub PR, preview environment on finish); verification ("If your framework and repository can run a typecheck or build in under a handful of seconds, run it every time the agent stops to surface errors to it").
- Their Stop hook runs the biome formatter and TypeScript type check and exits 2 on errors: "On success the hook is completely silent — nothing ends up in the agent's context. On failure, only the errors are surfaced, and exit code 2 tells the harness to re-engage the agent". They also describe a Stop hook that "prompts the agent to increase coverage if it drops". Their script comments that `biome --write` exits 1 when it made changes, so they run it twice to avoid a false failure.
- Context cost of checks: "early on we had our agent run the full test suite after every change, and 4,000 lines of passing tests would flood the context window. The agent would then lose track of the actual task and start hallucinating about test files it had just read. Now we swallow the output and only surface errors."
- What did not work: "Trying to design the ideal harness configuration upfront before we'd even hit real failures"; "Running our entire test suite (5+ minutes) at the end of every agent session (run a subset instead)". What did: "Starting simple and adding configuration only when the agent actually failed"; "I have thrown away many more hooks than we actually use today"; distributing configurations to the team via repository-level config.
- Instructions and hooks together: they give the agent "concise instructions about how to use all of these mechanisms in our CLAUDE.md file", so instructions explain the checks and the hooks force them.
- Stance: "bias towards shipping"; "It is entirely possible to spend more time optimizing your coding agent setup than actually shipping code with it — we've been there."

Unverified: no measurements beyond the anecdote of the 4,000-line test output.
