---
source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
source_date: undated
researched: 2026-09-26
---

# Anthropic: Prompting best practices (writing-relevant parts)

- Vendor documentation, read via the fetch tool and then searched in the saved full text.
- Examples: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Make them relevant, diverse (so unintended patterns are not picked up) and structured in example tags; 3-5 examples recommended.
- Role: "Setting a role in the system prompt focuses Claude's behavior and tone for your use case."
- Format control: say what to do instead of what not to do (prose paragraphs instead of "do not use markdown"); matching the prompt's own style to the desired output style can reduce markdown; a sample prompt asks for flowing prose and no short bullet series.
- Says latest models are more concise, direct and less machine-like than predecessors; one model's default responses run longer and effort does not reliably change length, so prompt for conciseness explicitly.
- The page uses "AI slop" only for front-end design defaults and gives a prompt to avoid them; nothing here is measured. The docs give no evaluation data for these recommendations.
