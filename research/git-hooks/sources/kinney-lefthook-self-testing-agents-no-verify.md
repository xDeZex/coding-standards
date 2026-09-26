---
source: https://stevekinney.com/courses/self-testing-ai-agents/git-hooks-with-lefthook
source_date: undated
researched: 2026-09-26
---

# Steve Kinney, Git Hooks with Lefthook (Self-Testing AI Agents workshop)

Read in full via curl and html-to-text (18,800 characters); the code for the Cursor block script was skimmed. The page carries no visible date (an unlabelled 2026-09-14 string is in its HTML, meaning unknown), so it is undated here.

Speaker: Steve Kinney, a developer educator who teaches courses on front-end and AI-assisted engineering; this page is a lesson in his workshop. This is a weaker trust case than the others: I judge it by a first-hand teaching account that names concrete rules, not by a widely adopted tool or a long record I could verify. Treat as a practitioner's view, below the tool authors.

- Prefers Lefthook to Husky plus lint-staged for new projects ("one YAML file"), but "If you already have Husky wired up ... there's no reason to migrate." He notes one reason to like it for agents: "When the agent needs to know what gates it has to pass, you can point the agent rules at a single file."
- Speed rule: "pre-commit takes under ten seconds, pre-push takes under two minutes. Anything slower belongs in CI." Slow checks (typecheck, knip, unit tests) go in a pre-push hook. His agent-instruction snippet says "The pre-commit hook completes in under 10 seconds. If you see commits taking longer, report it."
- Secret scanning is "the one I care about most": Gitleaks on the staged diff, so "Zero agents and zero humans should be committing secrets".
- Bypass: "`git commit --no-verify` skips the hook. ... use it for real emergencies, not as a reflex. If the team starts reaching for `--no-verify` regularly, the hook is too strict. Tune it." For agents he writes an instruction: "Never use `--no-verify` when committing. If a hook is failing, fix the code the hook is complaining about, not the hook." Then: "That instruction belongs in your agent instructions ... but if you want an actual enforcement boundary, use the agent's hook or permissions system." He gives a Claude Code PreToolUse hook that denies commands containing `--no-verify`, and a Cursor `beforeShellExecution` hook that does the same (with shell-word parsing so it does not block unrelated commands). So he layers an instruction, an agent hook that guards the git hook, and the git hook.
- When not to: "If you're tempted to put logic in pre-rebase, you're probably solving a process problem with a technical tool."
- Not said: measured effect, or the hook missing when a commit does not go through git's hook path.

The speaker description above is background I know, not read from the page (except where the page itself says it), and is unverified.
