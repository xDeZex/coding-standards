# Research

Working material, not carried into target repos. It exists for human and AI understanding, and as the basis for producing catalogue entries. Catalogue entries are what get copied into a repo during adoption.

```
research/<topic>/conclusion.md
research/<topic>/position.md
research/<topic>/sources/<source>.md
```

## Leads

`research/leads.md` lists people, companies, ideas and other things worth a look. It guides where research looks and is something humans can browse. A lead is a pointer: rely on a claim only through a source note. Format is in the file.

A research agent reads it before choosing sources. After the research, and before finishing, it adds a lead for each new person, company, idea, book or talk that the sources surfaced and that looks worth a look, including ones it did not have time to follow. It skips anything already in the file (search by name) and never edits or removes existing leads.

## Who writes what

A research agent writes source notes and one `conclusion.md`, never the position. The conclusion is its synthesis of the sources, with unverified claims flagged, for the human to read and discuss (including how it connects to AI coding). The position is the human's, written after that discussion, and it is the only file catalogue entries point to. The conclusion is kept after the position exists, as the record of what the research found; never delete it.

## Reading sources

A source note records what the page says, so the agent must have read the page itself. A search result, an abstract or a summary is a pointer, not a source. In the first round of research here, most notes were written from snippets and summaries, and the re-read of about half of them found wrong quotes and numbers, wrong scope (which agent, which file type, which condition) and one claim that the page contradicted.

- Do not use WebFetch to read a source. It passes the page through a small summarising model, which gets numbers right when they are in the abstract but drops or invents scope and context. Use it only to find pages, or as a last resort, and say so in the note.
- Fetch the raw page and read the text yourself. Use a scratch directory of your own (parallel agents overwrite each other's files in a shared one), and pull out only the passages you need so the context stays small.
  - HTML: `curl -sL -A 'Mozilla/5.0' URL -o page.html`, then strip the tags with a short `html.parser` script. Follow redirects (`-L`). Vendor docs, blogs, Substack and Stanford pages all worked this way.
  - PDF: `curl -sL` the file, then `pdftotext -layout`. For arXiv use `https://arxiv.org/pdf/<id>`. Two-column layouts interleave and tables come out in reading order, so pair rows and columns by hand.
  - GitHub files: `raw.githubusercontent.com`.
  - X/Twitter posts: the raw page is a JavaScript shell. `https://api.fxtwitter.com/<user>/status/<id>` returned the full text as JSON. The syndication endpoint truncates at 280 characters.
  - Some pages do not serve their body to a plain fetch (a transcript loaded by JavaScript, a paywall, HTTP 402/403). Try a mirror or the archive, and if none works, say the source is unreadable and mark its claims unverified. Do not fill the gap from a snippet.
- Quote from the text you read. Check every number against the page, and check which agent, dataset or file type it applies to.
- Say in the note body how it was read: for example "read in full via curl and html-to-text", "PDF via pdftotext, whole paper", "abstract only", "could not be fetched: reason". A claim from an unread page stays out of the conclusion, or is flagged as unverified.
- A vendor guide that shows an example prompt is not a stated rule for hand-written files. Report what the page states, not what it implies.

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

Nuance stays in the position. What an AI would act on goes in a catalogue entry (`kit/catalogue/<topic>.md`), which points back to the position. See `kit/catalogue/README.md`.

Use relative Markdown links between files, so they work when clicked on GitHub.

## Before you finish

Run the validator and fix every error until it exits 0. It checks source note front matter, the topic layout, the leads, the catalogue and relative links in positions and the guide. Warnings (for example a topic with no position yet) do not fail it.

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # once
.venv/bin/python scripts/validate.py
```

A git pre-commit hook runs the validator before every commit. Enable it once per clone: `git config core.hooksPath .githooks`.

Its own tests: `cd scripts && ../.venv/bin/python -m unittest`.
