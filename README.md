# Coding Standards

A thinking space where a human and an AI research, discuss and document coding standards for software development with AI. Vocabulary is in `CONTEXT.md`.

## Layout

- `kit/<type>/`: the portable kit, one folder per artifact type (`catalogue`, `skills`, `controls`; the set may change as research surfaces new types).
- `guide/`: the human guide.
- `research/<topic>/`: `conclusion.md` and `position.md` plus `sources/<source>.md`, one file per source.
- `docs/`: operating this repo (`agents/`, `adr/`).

## Adopting the kit

To adopt the kit in another repo, point an AI at this one from that repo ("adopt the kit from https://github.com/xDeZex/coding-standards"). The AI proposes first and writes only what the human has confirmed.

1. **Orient:** read `CONTEXT.md` for the vocabulary.
2. **Inspect the target repo:** record its languages, tests and CI, and which controls from `kit/controls/` it already has.
3. **Point the human to the guide:** tell them that [the human guide](guide/guide.md) explains harnesses and is worth reading before they confirm, and that they should understand and judge every proposal themselves.
4. **Propose controls (list 1):** judge every control in `kit/controls/` by its `Use when` against the target. List the controls the harness should have, each marked already present or to add, with a line on why. Done when the human has confirmed the set.
5. **Propose entries (list 2):** judge every entry in `kit/catalogue/` by its `Applies when`. List each entry that fits, mapped to a confirmed control. Judge every skill in `kit/skills/skills.md` by its `Use when` and list the fits separately. Flag an entry that fits no confirmed control as "no fit": the human adds a control (back to list 1) or drops it. Done when the human has confirmed the list.
6. **Choose how to implement:** ask the human whether to apply now or create tickets to pick up later, how they want the work split, and how to treat the target's existing content, removals included. These decisions are theirs.
7. **Do it:** apply the items or create the tickets. Word each instruction for the target, in the form its control's guide describes, so the target stands alone: no ids, links or provenance tags from this repo.
