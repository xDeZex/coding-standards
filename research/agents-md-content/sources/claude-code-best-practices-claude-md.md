---
source: https://code.claude.com/docs/en/best-practices
source_date: undated
researched: 2026-09-26
---

# Claude Code best practices: writing an effective CLAUDE.md, hooks, skills

First-party vendor documentation. Re-read 2026-09-26 from the raw HTML (curl, html.parser) in full; every quote below was checked against the page and matches. The same page is recorded for its verification section in [the testing note](../../testing-feedback-loop/sources/claude-code-docs-best-practices-verification.md); this note covers the parts on file content and choosing a mechanism.

- Purpose of CLAUDE.md: persistent context "it can't infer from code alone", read at the start of every conversation. "Keep it short and human-readable." Loaded every session, "so only include things that apply broadly"; domain knowledge or workflows only relevant sometimes go in skills, "loaded on demand without bloating every conversation."
- Test for each line: "Would removing this cause Claude to make mistakes? If not, cut it." "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"
- Include table: bash commands Claude cannot guess; style rules that differ from defaults; "Testing instructions and preferred test runners"; repo etiquette; project-specific architectural decisions; environment quirks; common gotchas. Exclude table: anything Claude can work out from code; standard language conventions; detailed API docs (link instead); information that changes often; long explanations; file-by-file codebase descriptions; self-evident practices.
- Diagnostic claims: if a rule is ignored the file is probably too long; if Claude asks a question the file answers, the phrasing may be ambiguous. Treat it like code: prune, and test changes by observing behaviour. `/doctor` proposes cuts for content derivable from the codebase. Adding "IMPORTANT" to one line helps; to many lines helps none.
- Failure pattern "the over-specified CLAUDE.md": "Claude ignores half of it"; fix: "Ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook."
- Hooks: "Use hooks for actions that must happen every time with zero exceptions." "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens."
- The page's own example CLAUDE.md contains "Be sure to typecheck when you're done making a series of code changes" and "Prefer running single tests, and not the whole test suite, for performance", and its include table lists testing instructions. The include-table line and the example line are the direct quotes for test guidance in the always-loaded file; the page never states "put test commands in CLAUDE.md" as a rule.
- Skills: examples given are API conventions (reference knowledge) and a `fix-issue` workflow whose steps include "Write and run tests to verify the fix".
- Verification section of the same page: "Give Claude a check it can run: tests, a build, a screenshot to compare"; the check can gate the stop in one prompt ("run the tests after implementing" in its example), as a `/goal` condition, or "As a deterministic gate: a Stop hook runs your check as a script and blocks the turn from ending until it passes." So the page names three places for a test check, none of them a skill.
- Also: "LLM performance degrades as context fills ... Claude may start 'forgetting' earlier instructions."
- Evidence status: assertions from the vendor's internal experience; no data is cited. The 200-line figure is on the memory and features pages.
