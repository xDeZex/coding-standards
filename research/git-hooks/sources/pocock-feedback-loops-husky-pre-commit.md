---
source: https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects
source_date: 2026-01-16
researched: 2026-09-26
---

# Matt Pocock, Essential AI Coding Feedback Loops For TypeScript Projects (AI Hero)

Read in full via curl and an html-to-text script (raw page, no summarising tool). This re-checks the two earlier notes in [testing-feedback-loop](../../testing-feedback-loop/sources/matt-pocock-ai-coding-feedback-loops.md), which were written from a summarised fetch. Their quotes match the raw page. The byline "Matt Pocock" is on the page; the page shows "Updated Jan 16, 2026", so that is the last-updated date, not necessarily first publication. It is a short recipe article of about 600 words with no data.

Speaker: Matt Pocock, TypeScript educator (Total TypeScript, AI Hero) and author of a widely used public set of agent skills (github.com/mattpocock/skills). Counts as trusted because he publishes sustained first-hand material on running agents, including AFK loops, and his skills are widely installed.

What the page says:

- Premise: "When working with AI coding agents, especially those operating independently, you need feedback loops so the AI can verify its own work. Feedback loops are especially important when you're doing AFK coding, such as with Ralph Wiggum."
- Section 3, "Install Husky for Pre-commit Hooks": "Husky enforces feedback loops before every commit." The `.husky/pre-commit` file shown runs `npx lint-staged`, `npm run typecheck`, `npm run test`. "If any step fails, the commit is blocked and the AI gets an error message."
- Section 4 adds lint-staged with Prettier to auto-format staged files and restage them: "All AI-generated code now conforms to your formatting standards." He adds that ESLint could also run there.
- "Why This Works for AI": "AI agents don't get frustrated by repetition. When code fails type checking or tests, the agent simply tries again. This makes feedback loops (and pre-commit hooks, especially) incredibly powerful for AI-driven development."
- The hook here runs the full test suite and type check on every commit, not a fast subset.
- Not on the page: any risk that the agent bypasses the hook (`--no-verify`), hook runtime, or that the hook is per clone. It does not compare the hook with CI or with agent hooks. Whether he likes it: yes, strongly ("incredibly powerful"), as a commit gate for agent work.
