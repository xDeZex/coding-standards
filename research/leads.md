# Leads

People, companies, ideas, books and talks worth a look. A lead is a pointer, not a source: it records no claims, and the research agent still writes source notes for anything it relies on. Humans can browse this to see where to look next.

Add a lead as one block with exactly these four fields. Search the repo by name to see whether it has been researched.

```markdown
## Name
- kind: person | company | idea | book | talk | other
- link: https://example.com
- why: one line on why it is worth a look
```

## Kent Beck
- kind: person
- link: https://newsletter.kentbeck.com
- why: Originator of TDD, now writing on augmented coding and testing with AI agents

## Birgitta Böckeler
- kind: person
- link: https://martinfowler.com/articles/harness-engineering.html
- why: Source of the harness and control vocabulary this repo uses

## Matt Pocock
- kind: person
- link: https://github.com/mattpocock/skills
- why: Publishes TDD and bug-diagnosis skills built around agent feedback loops; his AI Hero articles (including a Ralph-loop one not yet read) are worth following

## Magnus Gille
- kind: person
- link: https://github.com/Magnus-Gille
- why: Swedish AI practitioner, reported by the user to have spoken at their company and won a Swedish prompting championship; the research found this account (repos on Claude Code energy monitoring and AI memory) but no writing on tests, and did not read the repos

## Martin Fowler
- kind: person
- link: https://martinfowler.com
- why: Long-standing writing on the test pyramid, continuous integration, self-testing code and non-deterministic tests, and the host of Böckeler's harness articles

## Gergely Orosz
- kind: person
- link: https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent
- why: Interviewed Kent Beck on TDD with agents; only a written summary was read, so Beck's own words in the full episode are unchecked

## Stripe Minions
- kind: company
- link: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
- why: Describes one-shot coding agents run against deterministic checks; other Stripe engineering writing on the same system is unread

## OpenAI harness engineering
- kind: other
- link: https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html
- why: OpenAI's own harness-engineering post (deterministic linters, structural tests, "when the agent struggles, treat it as a signal") returned HTTP 403 and is known only through Böckeler's memo, linked here

## Test && commit || revert
- kind: idea
- link: https://newsletter.kentbeck.com/p/genie-sessions-tcr-skill
- why: Beck's TCR loop as an agent skill; his original 2018 post on it could not be fetched (HTTP 403)

## Approved fixtures
- kind: idea
- link: https://martinfowler.com/articles/harness-engineering.html
- why: Pattern Böckeler mentions for checking agent output without trusting agent-written tests; the pattern's own page only redirected and was not read

## Test exploitation and reward hacking
- kind: idea
- link: https://metr.org/blog/2025-06-05-recent-reward-hacking/
- why: The cluster of measured work on agents editing, special-casing or bypassing tests; Anthropic's emergent-misalignment work and several arXiv papers on it (2511.00197, 2606.07379, 2607.18057, 2609.20804) were not read

## Test-Driven Development: By Example
- kind: book
- link: https://www.oreilly.com/library/view/test-driven-development/0321146530/
- why: Beck's original TDD text; the canon research covers him through his posts only

## Succeeding with Agile
- kind: book
- link: https://www.mountaingoatsoftware.com/books/succeeding-with-agile
- why: Mike Cohn's book, the origin of the test pyramid; read only through Fowler's account

## The Pragmatic Programmer
- kind: book
- link: https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/
- why: Source of the "rate of feedback is your speed limit" epigraph Pocock builds on; the book itself was not read

## Continuous Delivery
- kind: book
- link: https://continuousdelivery.com/
- why: Humble and Farley on deployment pipelines and fast feedback, behind much of the CI and DORA material; not read

## DORA research
- kind: idea
- link: https://dora.dev/research/
- why: The survey studies behind the continuous integration and test automation capability pages; only the capability summaries were read

## Google flaky tests
- kind: idea
- link: https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html
- why: The post's body did not load, so its flakiness statistics are not recorded; worth reading for how flaky tests weaken a red run as a signal

## Writing-Zero
- kind: idea
- link: https://arxiv.org/abs/2506.00103
- why: RL for creative writing with a generative reward model and claimed resistance to reward hacking; seen only as an abstract summary

## LongWriter
- kind: idea
- link: https://arxiv.org/abs/2408.07055
- why: SFT data and an agent pipeline for very long outputs, with the LongBench-Write benchmark; seen only as an abstract summary

## Limits of automatic evaluation of creativity
- kind: idea
- link: https://arxiv.org/abs/2608.23705
- why: 2026 paper on the limits of automatic creativity evaluation; the PDF could not be parsed and it was not read

## Excess vocabulary in LLM-assisted writing
- kind: idea
- link: https://arxiv.org/abs/2406.07016
- why: Excess-vocabulary study of LLM use in biomedical writing, and related work on whether banned words fade after publicity; seen only in search results

## John Ousterhout
- kind: person
- link: https://web.stanford.edu/~ouster/cgi-bin/book.php
- why: Author of A Philosophy of Software Design, the origin of tactical versus strategic programming; his own view of AI and design was read only through summaries

## A Philosophy of Software Design
- kind: book
- link: https://web.stanford.edu/~ouster/cgi-bin/book.php
- why: The primary text for the tactical/strategic split; the research read it only through notes and lecture pages

## Ousterhout, Talks at Google 2018
- kind: talk
- link: https://www.youtube.com/watch?v=bmSAYlu0NcY
- why: His own presentation of tactical versus strategic; the page did not load

## SE Radio 520, Ousterhout
- kind: talk
- link: https://se-radio.net/2022/07/episode-520-john-ousterhout-on-a-philosophy-of-software-design/
- why: Long interview with Ousterhout, not read

## Software Fundamentals Matter More Than Ever
- kind: talk
- link: https://ai.engineer/talks/software-fundamentals-for-ai-coding
- why: Pocock's AI Engineer talk; the full video or transcript would verify his exact claims

## Thariq Shihipar
- kind: person
- link: https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock
- why: Credited by Pocock as the source of the grill-me skill

## METR AI usage survey 2026
- kind: other
- link: https://metr.org/blog/2026-05-11-ai-usage-survey/
- why: Self-reported 2026 productivity data that follows METR's design update; not read

## AI-generated code debt studies
- kind: other
- link: https://arxiv.org/abs/2605.06464
- why: Large-scale maintenance and debt studies of agent code (also arXiv 2603.28592); unread

## Requirements-to-architecture LLM benchmark
- kind: idea
- link: https://arxiv.org/abs/2604.06683
- why: A direct test of AI on architecture work; the page was unreadable

## Architectural design decisions in AI agent harnesses
- kind: idea
- link: https://arxiv.org/pdf/2604.18071
- why: Unread

## GitHub Copilot coding agent best practices
- kind: company
- link: https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results
- why: First-party guidance on the human role with a coding agent; not read

## Spadini test review studies
- kind: idea
- link: https://research.tudelft.nl/en/publications/when-testing-meets-code-review-why-and-how-developers-review-test
- why: The main empirical work on reviewing test code (also arXiv 1907.13365); only abstracts were read

## Mutation-guided LLM test generation at Meta
- kind: idea
- link: https://www.researchgate.net/publication/394720083_Mutation-Guided_LLM-based_Test_Generation_at_Meta
- why: Meta's first-party paper, known only through an InfoQ report

## Addy Osmani
- kind: person
- link: https://addyosmani.com
- why: Credited by a practitioner post with naming the test-rewrite failure mode; his own writing was not read

## Agentic PR review studies
- kind: idea
- link: https://arxiv.org/abs/2601.15195
- why: AIDev-based studies of review effort and revisions for agent PRs (also arXiv 2605.06464 and 2509.14745); seen only in search snippets

## Test Double on mutation testing with agents
- kind: company
- link: https://testdouble.com/insights/keep-your-coding-agent-on-task-with-mutation-testing
- why: Practitioner mutation-testing loops with agents; other posts by the firm are unread

## Code review as decision-making
- kind: idea
- link: https://link.springer.com/article/10.1007/s10664-025-10791-2
- why: A cognitive model of reviewer questions that may explain reviewer attention; unread

## TRACE dataset (Patronus AI)
- kind: idea
- link: https://huggingface.co/datasets/PatronusAI/trace-dataset
- why: Reward-hack detection benchmark; per-category results, including test-suite exploitation, and false-positive rates were not read

## Do LLM evaluators prefer themselves for a reason?
- kind: idea
- link: https://arxiv.org/abs/2504.03846
- why: Follow-up to the self-preference paper asking whether the bias is genuine; not read

## Reward Hacking Benchmark
- kind: idea
- link: https://arxiv.org/abs/2605.02964
- why: Exploit rates across 13 models, relevant to chain-of-thought monitoring; only the abstract was read

## Sphinx PR review benchmark
- kind: idea
- link: https://arxiv.org/abs/2601.04252
- why: Another LLM pull-request review benchmark; seen only in search results

## Prompt-elicited trajectories and training-time reward hacking
- kind: idea
- link: https://arxiv.org/pdf/2604.23488
- why: Asks whether monitor results on prompted hacks transfer to real training-time hacks; seen only in search results

## Mutation testing
- kind: idea
- link: https://dl.acm.org/doi/10.1145/3183519.3183521
- why: The standard check on whether tests still catch faults; not studied on agent-weakened tests, results pages unread

## Practical Mutation Testing at Scale
- kind: idea
- link: https://arxiv.org/abs/2102.11378
- why: Google's follow-up on cost and where to place mutation checks; not read

## Goodhart's law
- kind: idea
- link: https://en.wikipedia.org/wiki/Goodhart%27s_law
- why: Why a passing proxy metric stops showing quality; primary sources (Goodhart 1975, Strathern 1997) were not fetched

## Claude Code Stop-hook loop issues
- kind: other
- link: https://github.com/anthropics/claude-code/issues/3573
- why: A cluster of loop reports (#3573, #54360, #58348, #94041) that were not read

## Block-no-verify approaches
- kind: idea
- link: https://github.com/anthropics/claude-code/issues/40117
- why: Defences against agents skipping git hooks (PATH shim, routing commits through an MCP server); secondary and unchecked

## Antigravity CLI
- kind: other
- link: https://geminicli.com/docs/hooks/
- why: Replaced Gemini CLI for some tiers on 2026-06-18; its hook support was not checked

## Claude Code /goal
- kind: idea
- link: https://code.claude.com/docs/en/goal
- why: Built-in model-judged Stop-hook loop, an alternative to a deterministic test gate; only the top of the page was read

## pre-commit framework
- kind: other
- link: https://pre-commit.com
- why: The common git hook manager, relevant to hooks being per-clone opt-in; not read

## Husky and lefthook
- kind: other
- link: https://typicode.github.io/husky/
- why: JavaScript ecosystem ways to install git hooks automatically; not read

## Copilot hooks, VS Code variant
- kind: other
- link: https://docs.github.com/en/copilot/reference/hooks-configuration
- why: The reference mentions a VS Code compatible config that was not read

## Steering Claude Code (Anthropic blog)
- kind: other
- link: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
- why: Anthropic's guide to choosing between CLAUDE.md, skills, hooks and subagents; not read

## Vercel agent evals
- kind: company
- link: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
- why: The only skill versus AGENTS.md measurement found; the harness and follow-ups are unread

## Gloaguen et al. (ETH Zurich SRI Lab)
- kind: person
- link: https://www.sri.inf.ethz.ch/publications/gloaguen2026agentsmd
- why: Authors of the main context-file study; their CtxBench benchmark could test where test-running instructions belong

## Probe-and-Refine Tuning of Repository Guidance
- kind: idea
- link: https://arxiv.org/pdf/2606.20512
- why: Follow-up on tuning repository guidance for coding agents; seen only in search results

## Agent Skill Evaluation and Evolution
- kind: idea
- link: https://arxiv.org/html/2606.11435v1
- why: Survey of skill benchmarks that may cover trigger rates; seen only in search results

## Lost in the middle
- kind: idea
- link: https://arxiv.org/abs/2307.03172
- why: Standard measurement of position effects in long context; not fetched

## Claude Code hook non-firing issues
- kind: other
- link: https://github.com/anthropics/claude-code/issues/36071
- why: A cluster of reports that PreToolUse hooks are skipped in some contexts (#36071 allowedTools "*", #35557 EnterWorktree, #34240 background agents, #52822 JSON allow, #20063 and #30143 headless mode); only #88738, #92675, #34692, #33343 were read

## Cline hooks
- kind: other
- link: https://docs.cline.bot/customization/hooks
- why: Another coding agent with hooks; the docs page is a JavaScript shell and returned no body to a plain fetch, so it was not read

## Kiro hook triggers and best practices
- kind: other
- link: https://kiro.dev/docs/hooks/
- why: The Hook Triggers, Hook Actions, Best Practices and Troubleshooting subpages (including agent-prompt actions that behave as instructions) were not opened

## Claude Code security-guidance plugin
- kind: other
- link: https://code.claude.com/docs/en/hooks-guide
- why: The guide points to it as a production example of hooks that run a separate model review and feed findings back; a model-judged hook use not read here

## Hooks for security and platform teams (Cursor)
- kind: other
- link: https://cursor.com/docs/agent/hooks
- why: The page cites a Cursor blog post on hooks for security and governance with partners (Snyk, Semgrep, Endor Labs, 1Password); the post and any measurements were not read

## Agentic coding is straining CI (Anthropic)
- kind: other
- link: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
- why: Sibling Anthropic post (2026-09-14) on scaling test impact analysis for agent-driven CI, listed in that page's related posts; relevant to CI as the control next to hooks; not opened

## Cursor third-party hooks compatibility
- kind: other
- link: https://cursor.com/docs/agent/hooks
- why: Cursor loads hooks from tools like Claude Code; the compatibility page was not opened, so which fields carry over is unknown

## Config-based git hooks (git hook)
- kind: idea
- link: https://git-scm.com/docs/git-hook
- why: Hooks defined in git config and shared across repos; changes how "not shared by clone" works; the git version that added them and how widely it is deployed were not checked

## git-receive-pack quarantine and push rules
- kind: idea
- link: https://git-scm.com/docs/git-receive-pack
- why: The server-side gate an agent cannot skip locally; only the quarantine section was read

## GitHub rulesets and push rules
- kind: other
- link: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- why: The github.com equivalent of server-side enforcement, with bypass lists; only branch protection was read

## pre-commit.ci
- kind: company
- link: https://pre-commit.ci
- why: Hosted CI backstop for pre-commit hooks; not read

## lint-staged
- kind: other
- link: https://github.com/lint-staged/lint-staged
- why: Runs checks on staged files only; not read

## Claude Code worktree hooksPath issue cluster
- kind: other
- link: https://github.com/anthropics/claude-code/issues/27474
- why: Agent worktrees rewrite core.hooksPath so hooks silently do not run; related issues 72714, 85039, 67196, 67914 and 90456 were not read

## Aider lint and test docs
- kind: other
- link: https://aider.chat/docs/usage/lint-test.html
- why: The maintainer's answer to skipped pre-commit is --test-cmd pre-commit; page not read; there is an open request for an Aider hook system (issue 5712)

## Claude Code PreCommit hook request
- kind: other
- link: https://github.com/anthropics/claude-code/issues/4834
- why: Cited by issue 90887 as an earlier request for a commit gate; not read

## Codex issue 5034 (git-shadow-dir workaround)
- kind: other
- link: https://github.com/openai/codex/issues/5034
- why: Seen only as a link in a comment on the sandbox-blocks-commit issue

## Copilot coding agent and Cursor commit behaviour
- kind: other
- link: https://docs.github.com/en/copilot/concepts/coding-agent/about-copilot-coding-agent
- why: The pages read showed no git-hook statement; another source is needed on whether these agents run git hooks on their commits

## Boris Cherny
- kind: person
- link: https://x.com/bcherny
- why: Claude Code creator at Anthropic; posts sustained first-hand usage threads that mention hooks for formatting, verification and permissions

## Armin Ronacher
- kind: person
- link: https://lucumr.pocoo.org
- why: Flask creator with a long-running agentic-coding blog; the one clear negative account of agent hooks (July 2025); later posts not checked

## Shrivu Shankar
- kind: person
- link: https://blog.sshh.io
- why: Widely cited Claude Code write-up on an enterprise repo, including block-at-commit hooks

## Dex Horthy / HumanLayer
- kind: person
- link: https://www.humanlayer.dev/blog
- why: Authors of 12-factor agents and the skill-issue harness post on hooks and back-pressure; talk not read

## Jesse Vincent
- kind: person
- link: https://github.com/obra/superpowers
- why: Author of Superpowers; uses a session-start hook and notes worktrees silently lose git hooks; his blog was not reachable

## Geoffrey Huntley
- kind: person
- link: https://ghuntley.com
- why: Creator of the Ralph loop; lists pre-commit analyzers as one back-pressure layer; his back-pressure post is paywalled

## Peter Steinberger
- kind: person
- link: https://steipete.me
- why: Long first-hand accounts of running many agents in parallel; one remark that no hook stops a determined agent; other posts unread

## Steve Kinney
- kind: person
- link: https://stevekinney.com/courses/self-testing-ai-agents/git-hooks-with-lefthook
- why: Workshop on agents with pre-commit and pre-push hooks; gives speed rules; weaker trust, other lessons unread

## Ryan Carson
- kind: person
- link: https://x.com/ryancarson/status/1948869082511802648
- why: Tip on running an agent review inside a pre-commit hook; weakest trust of the practitioners read

## Viv Trivedy
- kind: person
- link: https://addyosmani.com
- why: Credited by Osmani with coining harness engineering and the Anatomy of an Agent Harness post; not read

## Harness Engineering is not Enough (Dex Horthy)
- kind: talk
- link: https://daily.dev/posts/harness-engineering-is-not-enough-why-software-factories-fail-dex-horthy-humanlayer-04e6rdy4v
- why: Horthy's talk on the limits of harness controls; not read

## Hook incidents drive hook design
- kind: idea
- link: https://blakecrosley.com/blog/claude-code-hooks
- why: Recurring practitioner claim that each hook should come from a real failure; this source is an independent developer, weak trust

## Deterministic tool gate RFC
- kind: idea
- link: https://github.com/anthropics/claude-code/issues/45427
- why: Argues hooks are necessary but insufficient for governance; not read

## Ralph Wiggum loop
- kind: idea
- link: https://ghuntley.com/loop/
- why: The Stop-hook continuation pattern that Cherny and Osmani both cite; not read closely

## Stripe Minions Part 2
- kind: other
- link: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
- why: Holds the pre-push hook and CI-round passage; the author is unconfirmed

## Huntley, don't waste your back pressure
- kind: other
- link: https://ghuntley.com/pressure/
- why: Paywalled; may name pre-commit hooks as back pressure

## Forcing Claude Code to reliably pass lint with Lefthook
- kind: other
- link: https://liambx.com/blog/ai-agent-lint-enforcement-lefthook-claude-code
- why: First-hand practice post on lint enforcement with a git hook; author trust unchecked

## Böckeler sensors article, remaining sections
- kind: other
- link: https://martinfowler.com/articles/sensors-for-coding-agents.html
- why: Hook passages were read closely, the rest skimmed

## Kent Beck (GitHub)
- kind: person
- link: https://github.com/KentBeck
- why: Pushes code live during his "genie session" recordings, including the tcr-skill repo from the TCR-as-agent-skill session; profile itself not browsed beyond confirming identity (bio "tidyfirst")
