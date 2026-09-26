---
source: https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html
source_date: 2026-02-17
researched: 2026-09-26
---

# Harness Engineering - first thoughts (Birgitta Böckeler)

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere. Author and date as reported by the fetch: Birgitta Böckeler, 17 February 2026. A memo reacting to OpenAI's harness engineering post.

- Reports that OpenAI's harness combined LLM-based agents with "deterministic custom linters and structural tests", plus periodic "garbage collection" agents that look for documentation inconsistencies or architectural violations.
- Context side: a knowledge base kept in the codebase, and dynamic context such as observability data and browser navigation.
- Quotes OpenAI's stance: "When the agent struggles, we treat it as a signal: identify what is missing - tools, guardrails, documentation."
- Asks readers: "Do you have a pre-commit hook? What's in it? Do you have ideas for custom linters?" Names structural testing frameworks (ArchUnit) as worth exploring.
- Trade-off: giving up some "generate anything" flexibility for prompts, rules and harnesses "full of technical specifics" in return for maintainability at scale.

Unverified: OpenAI's original post could not be fetched (HTTP 403), so the OpenAI claims here are second-hand via Böckeler.
