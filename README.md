# Coding Standards

A thinking space where a human and an AI research, discuss and document coding standards for software development with AI. Vocabulary is in `CONTEXT.md`.

## Layout

- `kit/<type>/`: the portable kit, one folder per artifact type (`catalogue`, `skills`, `controls`; the set may change as research surfaces new types).
- `guide/`: the human guide.
- `research/<topic>/`: `conclusion.md` and `position.md` plus `sources/<source>.md`, one file per source.
- `docs/`: operating this repo (`agents/`, `adr/`).

## Adopting the kit

To adopt the kit in another repo, point an AI at this one from that repo ("adopt the kit from https://github.com/xDeZex/coding-standards"). The AI follows these steps and writes nothing until the human has confirmed.

1. **Orient:** read this file and `CONTEXT.md` for the vocabulary.
2. **Inspect the target repo:** its languages, tests and CI, and the controls it already has (AGENTS.md, skills, hooks, linters, reviews).
3. **Propose controls (list 1):** from `kit/controls/` and the `Use when` lines, list the controls the target's harness should have. Mark each as already present or to be added, with a line on why. The human confirms the set.
4. **Propose entries (list 2):** from `kit/catalogue/`, select the entries whose `Applies when` fits the target and map each to a confirmed control. List skills from `kit/skills/skills.md` separately, chosen by `Use when`. An entry that fits no confirmed control is flagged "no fit"; the human adds a control or drops the entry. The human confirms the list.
5. **Choose how to implement:** ask the human whether to apply the items now or create tickets to pick up later, and how they want the work split.
6. **Do it:** apply the items, or create the tickets. Write each instruction reworded for the target, in the form its control's guide describes. Nothing points back to this repo: no ids, no links, no provenance tags.

Adoption only adds what the human confirmed. How existing content in the target is treated, including removing controls, is the human's decision and outside this repo.
