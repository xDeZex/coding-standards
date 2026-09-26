---
source: https://x.com/bcherny/status/2007179852047335529
source_date: 2026-01-02
researched: 2026-09-26
---

# Boris Cherny on how he and the Claude Code team use hooks (X threads, Jan to Mar 2026)

Speaker: Boris Cherny, creator of Claude Code and its lead at Anthropic (his X profile reads "Claude Code @anthropicai"). Counts as trusted: he authored the tool whose hooks are discussed and posts sustained first-hand accounts of running it on real work. Also a vendor voice: he promotes his own product's features, so his posts state how hooks are meant to be used and what he does, not what fails.

How read: the four posts below were fetched as raw JSON from `api.fxtwitter.com/bcherny/status/<id>` and read in full. Four of these ids were found through a third-party aggregator page (howborisusesclaudecode.com); only the raw posts are quoted here. The aggregator was not relied on. A fifth post (2074997571563479143, 2026-07-08, about a `/checkup` command) returned only "Here's what happened when I ran /checkup"; the aggregator's claim that /checkup "turns off slow hooks that tax every turn" is second-hand and unverified.

- Formatting (2026-01-02, tweet 9 of a thread on how he uses Claude Code): "We use a PostToolUse hook to format Claude's code. Claude usually generates well-formatted code out of the box, and the hook handles the last 10% to avoid formatting errors in CI later." The attached image (not read) shows the config; a secondary write-up (InfoQ, not a source for this note) shows the command `bun run format || true`. The `|| true` is part of what that write-up prints; it makes the hook never block.
- Long tasks (same thread, tweet 12): "For very long-running tasks, I will either (a) prompt Claude to verify its work with a background agent when it's done, (b) use an agent Stop hook to do that more deterministically, or (c) use the ralph-wiggum plugin (originally dreamt up by @GeoffreyHuntley)." So the Stop hook is offered as the "more deterministic" alternative to prompting.
- Permission routing (2026-01-31): "Route permission requests to Opus 4.5 via a hook — let it scan for attacks and auto-approve the safe ones". A model judges the permission request; the hook is the plumbing.
- Feature list (2026-02-11, tweet 9, "Set up hooks"): "Hooks are a way to deterministically hook into Claude's lifecycle. Use them to: Automatically route permission requests to Slack or Opus; Nudge Claude to keep going when it reaches the end of a turn (you can even kick off an agent or use a prompt to decide whether Claude should keep going); Pre-process or post-process tool calls, eg. to add your own logging". "Ask Claude to add a hook to get started."
- Feature list (2026-03-30, tweet 4): hooks "to deterministically run logic as part of the agent lifecycle", for example "Dynamically load in context each time you start Claude (SessionStart)", "Log every bash command the model runs (PreToolUse)", "Route permission prompts to WhatsApp for you to approve/deny (PermissionRequest)", "Poke Claude to keep going whenever it stops (Stop)".

What is absent: none of these posts says when not to use a hook, what goes wrong, or compares hooks with CLAUDE.md or CI. No numbers. The uses named cover formatting, context injection, logging, permission routing, and Stop-time verification; none is a hard block on a dangerous command.
