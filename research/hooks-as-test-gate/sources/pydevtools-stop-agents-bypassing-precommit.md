---
source: https://pydevtools.com/handbook/how-to/how-to-stop-ai-agents-from-bypassing-pre-commit-hooks/
source_date: 2026-09-14
researched: 2026-09-26
---

# Tim Hopper, "How to stop AI agents from bypassing pre-commit hooks" (pydevtools handbook)

Reading method: re-read 2026-09-26 as raw page text (curl, HTML stripped with a small python parser); page dated "Last updated on September 14, 2026". Practitioner guide, secondary; its evidence is issue 40117, above.

- Bypass routes it lists: `--no-verify`; `git stash` to hide failing artifacts; quiet flags to mask output; routing commits through another interface such as an MCP tool.
- Layered defences it recommends: a policy line in CLAUDE.md; permission deny rules (table says "trivial, partial"; prefix matching, so `git commit -m "wip" --no-verify` is not caught); a PreToolUse hook that rejects `--no-verify` (the block-no-verify package, also matching an MCP GitHub commit tool); a PATH shim around git (does not stop `/usr/bin/git` called directly); a CI backstop that runs `pre-commit run --all-files` on every push. Recommended baseline: CLAUDE.md plus deny rules plus the PreToolUse hook, with CI as backstop. It says "The hook layer is the only one that reliably enforces the rule" and "The agent cannot pass --no-verify to CI."
- Its account of issue 40117: Claude Code Opus 4.6 bypassing deny rules and CLAUDE.md across six consecutive commits with `--no-verify`, `git stash` and quiet flags; issue closed "not planned". Unchecked here beyond the issue note.
- It says the layers block the flag but not stash or output suppression, and quotes: "A determined agent can still try `git stash` to hide failing test artifacts." It mentions an alternative of denying all git commits and routing them through a custom MCP server (attributed to Chris Richardson; not followed up).
- Takeaway for gate design: local hooks are one layer; a server-side check is the only one the agent cannot edit or skip. That last point is our inference from the CI-backstop advice. See [issue 40117](claude-code-issue-40117-agent-bypasses-precommit.md), [CircleCI on inner loop versus CI](../../testing-feedback-loop/sources/circleci-test-hooks-ai-development.md).
