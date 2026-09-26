---
source: https://code.claude.com/docs/en/best-practices
source_date: undated
researched: 2026-09-26
---

# Best practices for Claude Code (Anthropic docs)

How read this time: full page fetched with curl and converted to text, read in the relevant sections (workflow, verification, adversarial review, common failure patterns, spec interview). Verified against the page; no claim in the earlier note needed correcting. Living document, so wording can change. Confirmed with curl that the old URL anthropic.com/engineering/claude-code-best-practices returns HTTP 308 to this page.

First-party vendor guidance.

- Recommended workflow has four phases: Explore, Plan, Implement, Commit. "Separate research and planning from implementation to avoid solving the wrong problem." Plan Mode has Claude read files and answer questions without making changes; Ctrl+G opens the plan in an editor for direct editing before Claude proceeds.
- Planning is optional: "If you could describe the diff in one sentence, skip the plan." Planning is most useful "when you're uncertain about the approach, when the change modifies multiple files, or when you're unfamiliar with the code being modified". For a typo, log line or rename, "ask Claude to do it directly."
- The human can have Claude interview them and write a spec; "Time spent making the spec precise pays off more than time spent watching the implementation."
- Verification: the page titles a section "Give Claude a way to verify its work". Without a check Claude can run, "you become the verification loop: every mistake waits for you to notice it." Failure pattern listed: "The trust-then-verify gap. Claude produces a plausible-looking implementation that doesn't handle edge cases." Fix: "If you can't verify it, don't ship it."
- Adversarial review by a fresh-context subagent is advised for longer unattended work; the page warns that a reviewer "will usually report some" gaps "even when the work is sound" and that chasing every finding "leads to over-engineering: extra abstraction layers, defensive code, and tests for cases that can't happen."
- Performance degrades as the context window fills; the page calls context "the most important resource to manage".
- Bearing on the split: the human role described is planning, specifying, verifying and course-correcting, and Claude implements. The guide treats code-level output as untrustworthy until checked and never says the AI is good at tactical work; the emphasis is on verification. Vendor guidance, so not independent evidence of AI capability. The page does not use the words tactical or strategic.
