"""Fixture tests for validate.py. Run: python3 -m unittest discover scripts"""
import tempfile
import unittest
from pathlib import Path

from validate import validate

NOTE = "---\nsource: https://example.com\nsource_date: undated\nresearched: 2026-09-26\n---\n\n# Note\n"
ENTRY = """# Testing

## run-tests-before-commit

Run the test suite before every commit.

- **Rationale:** Catches regressions early.
- **Applies when:** when there are tests
- **Position:** [Tests first](../../research/testing/position.md#tests-first)
"""


def build(files):
    root = Path(tempfile.mkdtemp())
    for name, text in files.items():
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    return root


GOOD = {
    "research/testing/position.md": "# Testing\n\n## Tests first\n\nSee [a note](sources/a-note.md).\n",
    "research/testing/sources/a-note.md": NOTE,
    "kit/catalogue/testing.md": ENTRY,
    "guide/guide.md": "See [the position](../research/testing/position.md#tests-first).\n",
}


class ValidateTest(unittest.TestCase):
    def errors(self, **changes):
        files = {**GOOD, **changes}
        files = {k: v for k, v in files.items() if v is not None}
        return validate(build(files))

    def test_good_tree_passes(self):
        errors, warnings = self.errors()
        self.assertEqual((errors, warnings), ([], []))

    def test_missing_position_is_a_warning(self):
        errors, warnings = self.errors(**{"research/testing/position.md": None, "kit/catalogue/testing.md": None, "guide/guide.md": None})
        self.assertEqual(errors, [])
        self.assertTrue(any("no position.md" in w for w in warnings))

    def test_source_note_needs_front_matter(self):
        errors, _ = self.errors(**{"research/testing/sources/a-note.md": "# no front matter\n"})
        self.assertTrue(any("missing YAML front matter" in e for e in errors))

    def test_source_note_missing_and_bad_dates(self):
        bad = "---\nsource: x\nsource_date: last week\n---\n"
        errors, _ = self.errors(**{"research/testing/sources/a-note.md": bad})
        self.assertTrue(any("missing 'researched'" in e for e in errors))
        self.assertTrue(any("'source_date' is 'last week'" in e for e in errors))

    def test_entry_missing_applies_when(self):
        errors, _ = self.errors(**{"kit/catalogue/testing.md": ENTRY.replace("- **Applies when:** when there are tests\n", "")})
        self.assertTrue(any("missing '**Applies when:**'" in e for e in errors))

    def test_entry_position_must_resolve(self):
        errors, _ = self.errors(**{"kit/catalogue/testing.md": ENTRY.replace("#tests-first", "#nope")})
        self.assertTrue(any("no heading 'nope'" in e for e in errors))

    def test_entry_position_must_be_a_link(self):
        errors, _ = self.errors(**{"kit/catalogue/testing.md": ENTRY.replace("[Tests first](../../research/testing/position.md#tests-first)", "research/testing/position.md")})
        self.assertTrue(any("must be one Markdown link" in e for e in errors))

    def test_duplicate_id(self):
        errors, _ = self.errors(**{"kit/catalogue/testing.md": ENTRY + "\n" + ENTRY.split("\n", 2)[2]})
        self.assertTrue(any("duplicate id" in e for e in errors))

    def test_broken_guide_link(self):
        errors, _ = self.errors(**{"guide/guide.md": "See [x](../research/missing/position.md).\n"})
        self.assertTrue(any("missing file" in e for e in errors))

    def test_links_in_code_are_ignored(self):
        errors, _ = self.errors(**{"guide/guide.md": "`[x](nope.md)`\n\n```\n[y](nope.md)\n```\n"})
        self.assertEqual(errors, [])

    def test_unexpected_file_in_topic(self):
        errors, _ = self.errors(**{"research/testing/notes.md": "x"})
        self.assertTrue(any("unexpected" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
