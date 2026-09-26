---
source: https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/
source_date: 2025-07-30
researched: 2026-09-26
---

# Armin Ronacher, "Agentic Coding Things That Didn't Work" (Hooks section)

Speaker: Armin Ronacher, creator of Flask, Jinja and other widely used Python and Rust tools, blogs at lucumr.pocoo.org on daily agentic coding (Claude Code). Counts as trusted: authored widely used tools and has published a sustained run of first-hand agent-coding posts. This is the one negative account of hooks found among the trusted people; it is from July 2025, early in Claude Code hooks' life, and he does not say whether he changed his view later. The June 2026 post "The Coming Loop" and his 2025 posts "Agentic Coding Recommendations" and "Tools: Code Is All You Need" contain no mention of hooks (searched the page text for "hook").

How read: raw HTML via curl, html-to-text, whole page; Hooks section read in full.

- Verdict: "I tried hard to make hooks work, but I haven't seen any efficiency gains from them yet. I think part of the problem is that I use yolo mode. I wish hooks could actually manipulate what gets executed. The only way to guide Claude today is through denies, which don't work in yolo mode."
- What he did instead: he tried a hook to make Claude use `uv` instead of `python` and "was unable to do so"; "Instead, I ended up preloading executables on the PATH that override the default ones, steering Claude toward the right tools." His `.claude/interceptors` shims print "This project uses uv, please use 'uv run python' instead." and `exit 1`, and he launches with `PATH="`pwd`/.claude/interceptors:${PATH}" claude --dangerously-skip-permissions`. So the control is in the tool environment, outside the harness, and applies to any agent.
- Formatting: "I also found it hard to hook into the right moment. I wish I could run formatters at the end of a long edit session. Currently, you must run formatters after each Edit tool operation, which often forces Claude to re-read files, wasting context. Even with the Edit tool hook, I'm not sure if I'm going to keep using it."
- Closing: "I'm actually really curious whether people manage to get good use out of hooks. I've seen some discussions on Twitter that suggest there are some really good ways of making them work, but I just went with much simpler solutions instead."

Caveats: written against 2025 Claude Code, when the hook set was smaller; the two complaints (cannot rewrite commands, no end-of-session formatter) may not hold now (the current docs read earlier list `updatedInput` and Stop events; see the reference note in this folder). Single practitioner, no measurements.
