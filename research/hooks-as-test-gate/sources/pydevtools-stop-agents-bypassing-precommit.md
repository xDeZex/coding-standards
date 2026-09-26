---
source: https://pydevtools.com/handbook/how-to/how-to-stop-ai-agents-from-bypassing-pre-commit-hooks/
source_date: 2026-09-14
researched: 2026-09-26
---

# Tim Hopper, "How to stop AI agents from bypassing pre-commit hooks" (pydevtools handbook)

Reading method: fetched through a summarising tool; quotes as returned. Practitioner guide, secondary; its evidence is issue 40117, above.

- Bypass routes it lists: `--no-verify`; `git stash` to hide failing artifacts; quiet flags to mask output; routing commits through another interface such as an MCP tool.
- Layered defences it recommends: a policy line in CLAUDE.md; permission deny rules (called "partial"); a PreToolUse hook that rejects `--no-verify`; a PATH shim around git; a CI backstop that runs the same checks on every push.
- It says the layers block the flag but not stash or output suppression, and quotes: "A determined agent can still try `git stash` to hide failing test artifacts." It mentions an alternative of denying all git commits and routing them through a custom MCP server (attributed to Chris Richardson; not followed up).
- Takeaway for gate design: local hooks are one layer; a server-side check is the only one the agent cannot edit or skip. That last point is our inference from the CI-backstop advice. See [issue 40117](claude-code-issue-40117-agent-bypasses-precommit.md), [CircleCI on inner loop versus CI](../../testing-feedback-loop/sources/circleci-test-hooks-ai-development.md).
