---
source: https://github.com/Aider-AI/aider/issues/5057
source_date: 2026-04-21
researched: 2026-09-26
---

# Aider issue 5057 (and 5376): default runtime commits bypass pre-commit hooks

How read: issue bodies and comments read as raw JSON from the GitHub REST API (issues 5057 and 5376 and their comments). Practitioner reports, not verified by us or the maintainers; both issues were open at fetch time with no maintainer comment seen.

- #5057 (opened 2026-04-21 by tchen200311, Aider v0.86.3.dev, model gpt-4o-mini): says Aider skips repository pre-commit hooks by default and cites the same code and docs line as the [docs note](aider-git-docs-commit-verify-default.md). Argues hooks are "real security controls, not just formatting checks" (secret scanning, blocking dangerous subprocess patterns, policy enforcement).
- Reproduction as reported: a `.git/hooks/pre-commit` that blocks `subprocess.check_output`; a manual commit with that pattern is blocked; asking Aider to add and commit the same pattern succeeds, producing commit 26c1aa2. Not reproduced by us.
- Asks for Aider to respect hooks by default or require explicit opt-out.
- #5376 (opened 2026-07-01 by QiuYucheng2003): the same finding, from static source reading, framed as a "security risk" if the model writes flawed code, hard-codes keys, or is prompt-injected; proposes flipping the default to True. Comments: several volunteers say they will fix it (no linked change seen); one commenter says a similar skipped-hook default in a CI pipeline let API keys reach production (anecdote, unverified); another comment is a vendor pitch for an OS-level git wrapper that "cannot be disabled via --no-verify in child shells" (promotional, unverified).
- What it shows: a tool default can defeat a git hook for every commit the agent makes, with no agent decision involved. What it does not show: how many Aider users rely on hooks, or any incident caused by it.
