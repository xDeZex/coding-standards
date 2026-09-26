---
source: https://code.claude.com/docs/en/best-practices
source_date: undated
researched: 2026-09-26
---

# Claude Code documentation: Best practices, "Give Claude a way to verify its work"

Primary source: first-party vendor documentation, read in full on 2026-09-26. The page carries no date and changes over time; it is used here for what the vendor says agents do and how instructions change that, not for vendor-specific guidance.

- Behaviour claim: "Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available, and you become the verification loop." With a pass/fail check, "Claude does the work, runs the check, reads the result, and iterates until the check passes."
- The check can be any signal readable in the conversation: test suite, build exit code, linter, script diffing output against a fixture, screenshot.
- Its examples of instruction wording: "write a validateEmail function. example test cases: ... run the tests after implementing"; "implement the OAuth flow from your plan. write tests for the callback handler, run the test suite and fix any failures"; for a build failure: "fix it and verify the build succeeds. address the root cause, don't suppress the error".
- Four ways to make the check gate the stop, in increasing strength: ask in the prompt; a session-level goal condition re-evaluated by a separate evaluator every turn; a Stop hook that runs the check as a script and blocks the turn ending until it passes (with a cap on consecutive blocks); a separate verification subagent so "the agent doing the work isn't the one grading it". The page says the prompt version works on any task, while the goal and hook versions "are what let an unattended run finish correctly without you."
- Instructions are described as advisory, hooks as deterministic: "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens." If Claude keeps skipping an instruction, the page suggests emphasis on that one line, and warns an over-long instruction file causes rules to be lost ("Claude ignores half of it"). (Assertions without a cited experiment.)
- Asks for evidence: "Have Claude show evidence rather than asserting success: the test output, the command it ran and what it returned."
- Failure pattern named "the trust-then-verify gap": Claude "produces a plausible-looking implementation that doesn't handle edge cases"; fix: "Always provide verification (tests, scripts, screenshots)."
- Example instruction-file lines the page includes: "Be sure to typecheck when you're done making a series of code changes" and "Prefer running single tests, and not the whole test suite, for performance"; it lists "Testing instructions and preferred test runners" among what to include.
- Warns that a reviewer prompted to find gaps "will usually report some, even when the work is sound", leading to over-engineering including "tests for cases that can't happen".

Not in this page: any measurement of how often the agent runs tests unprompted, or of tests being edited or fitted. The claims above are the vendor's description, with no data.
