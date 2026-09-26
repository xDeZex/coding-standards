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
