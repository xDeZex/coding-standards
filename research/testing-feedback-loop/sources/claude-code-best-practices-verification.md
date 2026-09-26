---
source: https://code.claude.com/docs/en/best-practices
source_date: undated
researched: 2026-09-26
---

# Best practices: give the agent a way to verify its work (first-party docs)

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere. One agent product's first-party guidance; used for how instruction files, hooks, review and goal loops are documented to differ. Page undated.

- Stop condition: the agent "stops when the work looks done. Without a check it can run, 'looks done' is the only signal available, and you become the verification loop." With a pass/fail check "the loop closes on its own": do the work, run the check, read the result, iterate.
- Checks named: test suite, build exit code, linter, script diffing output against a fixture, screenshot comparison.
- Four ways to make the check bind, "each step trades setup for attention": (1) ask in the prompt; (2) a session-level goal condition re-checked by a separate evaluator after every turn (it can stall and end with the goal unmet); (3) "a Stop hook runs your check as a script and blocks the turn from ending until it passes", with a cap on consecutive blocks; (4) a second-opinion subagent so "the agent doing the work isn't the one grading it."
- Ask for evidence (test output, command and result) rather than assertions of success.
- Instruction file: read at session start; "keep it short"; can list test commands and preferred runners. Failure mode: "Bloated CLAUDE.md files cause Claude to ignore your actual instructions"; if a rule keeps being broken the file is probably too long. Emphasis ("IMPORTANT") only helps if used sparingly. Compare: "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens." Advice: if the agent already does something without the instruction, delete it or convert it to a hook.
- Failure pattern "trust-then-verify gap": plausible code that misses edge cases; fix is to always provide verification.
- Review: an independent reviewer subagent in fresh context sees only the diff and criteria. Caveat: a reviewer told to find gaps "will usually report some, even when the work is sound"; chasing all findings leads to over-engineering, including "tests for cases that can't happen". Writer/reviewer split can also apply to tests (one session writes tests, another writes code to pass them).
- Non-interactive mode can run in CI or pre-commit hooks.

Unverified: no measurements are given for any of these; claims are the vendor's own guidance.
