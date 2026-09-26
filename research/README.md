# Research

Working material, not carried into target repos. It exists for human and AI understanding, and as the basis for producing catalogue entries. Catalogue entries are what get copied into a repo during adoption.

```
research/<topic>/conclusion.md
research/<topic>/position.md
research/<topic>/sources/<source>.md
```

## Leads

`research/leads.md` lists people, companies, ideas and other things worth a look. It guides where research looks and is something humans can browse. A research agent reads it before choosing sources and may add leads it comes across. A lead is a pointer: rely on a claim only through a source note. Format is in the file.

## Who writes what

A research agent writes source notes and one `conclusion.md`, never the position. The conclusion is its synthesis of the sources, with unverified claims flagged, for the human to read and discuss (including how it connects to AI coding). The position is the human's, written after that discussion, and it is the only file catalogue entries point to. The conclusion is kept after the position exists, as the record of what the research found; never delete it.

## Conclusion

Exactly one per topic, free prose, no front matter. Findings only: what the sources say, how well they support it, what is unverified. No kit design, no catalogue entries, no recommendations for us.

## Source note

One file per source. The filename is a descriptive slug id and is never renamed. YAML front matter, then a free Markdown body recording what the source says, kept separate from our opinion.

```markdown
---
source: https://example.com/article
source_date: 2024-05
researched: 2026-09-26
---

# Title of the source

- What the source says...
```

`source_date` may be `undated` when a source carries no date.

## Position

Exactly one per topic, written with the human. Free prose: our stance, its trade-offs, when it does not hold. No front matter and no required sections. It rests by default on the source notes in the same topic folder; a specific claim that comes from one source links to that source note in the prose. Source links are not machine checked.

Give each conclusion that yields a catalogue entry its own heading, so the entry's `position` pointer can anchor to it.

## Position versus catalogue entry

Nuance stays in the position. What an AI would act on goes in a catalogue entry (`kit/catalogue/<topic>.yaml`), which points back to the position. See `kit/catalogue/README.md`.

Use relative Markdown links between files, so they work when clicked on GitHub.

## Before you finish

Run the validator and fix every error until it exits 0. It checks source note front matter, the topic layout, the catalogue and relative links in positions and the guide. Warnings (for example a topic with no position yet) do not fail it.

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # once
.venv/bin/python scripts/validate.py
```

A git pre-commit hook runs the validator before every commit. Enable it once per clone: `git config core.hooksPath .githooks`.

Its own tests: `cd scripts && ../.venv/bin/python -m unittest`.
