# Catalogue

One Markdown file per topic: `kit/catalogue/<topic>.md`, holding that topic's catalogue entries. The filename is the topic, matching `research/<topic>/`. Markdown, so links are clickable on GitHub and each entry can be linked to by its heading.

## Entry format

```markdown
# Testing

## run-tests-before-commit

Run the test suite before every commit.

- **Rationale:** Catches regressions while the change is still small.
- **Applies when:** when there are tests
- **Position:** [Tests first](../../research/testing/position.md#tests-first)
```

- The `##` heading is the id: a descriptive lowercase-hyphen slug, unique within the file, never renamed. Elsewhere it is referenced as `<topic>/<id>`.
- The paragraph under the heading is the statement: the instruction.
- All three lines are required. `Applies when` is loose free text the AI judges against a target repo ("when there are tests", "when doing UI"); an entry that always applies says "always".
- `Position` is a relative Markdown link to the position the entry comes from, with an optional `#anchor` naming the heading. Search for the path to find the entries a changed position affects.
- Entries carry no sources. Sources are reached through the position to its source notes.
- Entries are neutral about where they are used. Each countermeasure words and applies an entry in its own way.
- To retire an entry, delete it. Git history keeps it.

Run the validator after editing (see `research/README.md` for setup): `.venv/bin/python scripts/validate.py`.
