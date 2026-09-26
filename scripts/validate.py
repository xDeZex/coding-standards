#!/usr/bin/env python3
"""Validate research files, leads, the catalogue and links.

Run from anywhere: .venv/bin/python scripts/validate.py
Exits 1 with one line per error when something is wrong, 0 otherwise.
Warnings are printed but do not fail the run.
"""
import datetime
import re
import sys
from pathlib import Path

import yaml

SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
ENTRY_FIELD = re.compile(r"^- \*\*(.+?):\*\* (.+)$")
REQUIRED_FIELDS = {"Rationale", "Applies when", "Position"}
CONTROL_FIELD = ENTRY_FIELD
CONTROL_FIELDS = {"What it is"}
CONTROL_HEADINGS = ("Good at", "Bad at", "How to write a good one")
POSITION_LINK = re.compile(r"\]\([^)\s]*position\.md[^)]*\)")
SKILL_FIELDS = {"Where", "Why", "Use when"}
LEAD_FIELD = re.compile(r"^- (\w+): (.*)$")
LEAD_FIELDS = ("kind", "link", "why")
LEAD_KINDS = {"person", "company", "idea", "book", "talk", "other"}


def rel(root, path):
    return str(path.relative_to(root))


def strip_code(text):
    """Blank out fenced code blocks and inline code so their contents are ignored."""
    text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", text)


def slugify(heading):
    """GitHub's heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    s = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return s.replace(" ", "-")


def anchors(path):
    text = strip_code(path.read_text())
    return {slugify(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*#*$", text, re.M)}


def split_front_matter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def check_link(root, source, target, errors, label="link"):
    """Check a relative link written in `source`; report to `errors`."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
        return
    path_part, _, anchor = target.partition("#")
    dest = (source.parent / path_part).resolve()
    if not dest.exists():
        errors.append(f"{rel(root, source)}: {label} '{target}' points to a missing file")
        return
    if anchor and dest.suffix == ".md" and anchor not in anchors(dest):
        errors.append(f"{rel(root, source)}: {label} '{target}' has no heading '{anchor}' in {rel(root, dest)}")


def check_links(root, path, errors):
    for m in LINK.finditer(strip_code(path.read_text())):
        check_link(root, path, m.group(1), errors)


def check_source_note(root, path, errors):
    name = rel(root, path)
    if not SLUG.match(path.stem):
        errors.append(f"{name}: filename must be a lowercase-hyphen slug")
    fm_text, _ = split_front_matter(path.read_text())
    if fm_text is None:
        errors.append(f"{name}: missing YAML front matter (--- block at the top)")
        return
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        errors.append(f"{name}: front matter is not valid YAML ({e})")
        return
    if not isinstance(fm, dict):
        errors.append(f"{name}: front matter must be key: value pairs")
        return
    for key in ("source", "source_date", "researched"):
        if fm.get(key) in (None, ""):
            errors.append(f"{name}: front matter is missing '{key}'")
    for key in ("source_date", "researched"):
        v = fm.get(key)
        if v in (None, ""):
            continue
        v = v.isoformat() if isinstance(v, (datetime.date, datetime.datetime)) else str(v)
        ok = DATE.match(v) or (key == "source_date" and v == "undated")
        if not ok:
            hint = "YYYY[-MM[-DD]] or 'undated'" if key == "source_date" else "YYYY-MM-DD"
            errors.append(f"{name}: '{key}' is '{v}', expected {hint}")


def check_research(root, errors, warnings):
    base = root / "research"
    if not base.is_dir():
        return
    for topic in sorted(p for p in base.iterdir() if p.is_dir()):
        if not SLUG.match(topic.name):
            errors.append(f"{rel(root, topic)}: topic folder must be a lowercase-hyphen slug")
        position = topic / "position.md"
        if not position.is_file():
            warnings.append(f"{rel(root, topic)}: no position.md yet")
        for doc in (topic / "conclusion.md", position):
            if doc.is_file():
                check_links(root, doc, errors)
        for item in sorted(topic.iterdir()):
            if item.name not in ("conclusion.md", "position.md", "sources") and item.name != "CLAUDE.md":
                errors.append(f"{rel(root, item)}: unexpected; a topic holds only conclusion.md, position.md and sources/")
        sources = topic / "sources"
        if not sources.is_dir():
            warnings.append(f"{rel(root, topic)}: no sources/ folder")
            continue
        for note in sorted(sources.iterdir()):
            if note.suffix != ".md" or not note.is_file():
                errors.append(f"{rel(root, note)}: sources/ holds only .md source notes")
            else:
                check_source_note(root, note, errors)


def check_catalogue(root, errors):
    base = root / "kit" / "catalogue"
    if not base.is_dir():
        return
    for path in sorted(base.glob("*.md")):
        if path.name in ("README.md", "CLAUDE.md"):
            continue
        name = rel(root, path)
        if not SLUG.match(path.stem):
            errors.append(f"{name}: filename must be a lowercase-hyphen topic slug")
        if not (root / "research" / path.stem).is_dir():
            errors.append(f"{name}: no research/{path.stem}/ topic folder")
        text = path.read_text()
        if not re.match(r"# .+", text):
            errors.append(f"{name}: must start with an '# <Topic>' title")
        parts = re.split(r"^## ", text, flags=re.M)[1:]
        seen = set()
        for part in parts:
            heading, _, body = part.partition("\n")
            entry = heading.strip()
            where = f"{name} [{entry}]"
            if not SLUG.match(entry):
                errors.append(f"{where}: entry heading must be a lowercase-hyphen id")
            if entry in seen:
                errors.append(f"{where}: duplicate id")
            seen.add(entry)
            lines = body.split("\n")
            first = next((l for l in lines if l.strip()), "")
            if not first.strip() or first.startswith("- "):
                errors.append(f"{where}: missing statement (the paragraph under the heading)")
            fields = {}
            for l in lines:
                m = ENTRY_FIELD.match(l)
                if m:
                    fields[m.group(1)] = m.group(2)
            for missing in sorted(REQUIRED_FIELDS - fields.keys()):
                errors.append(f"{where}: missing '**{missing}:**' line")
            for extra in sorted(fields.keys() - REQUIRED_FIELDS):
                errors.append(f"{where}: unknown field '{extra}'")
            pos = fields.get("Position")
            if pos:
                m = re.fullmatch(r"\[[^\]]+\]\(([^)\s]+)\)", pos)
                if not m:
                    errors.append(f"{where}: Position must be one Markdown link, [text](path#anchor)")
                else:
                    target = m.group(1)
                    if not re.search(r"research/[^/]+/position\.md", target):
                        errors.append(f"{where}: Position must link to a research/<topic>/position.md")
                    check_link(root, path, target, errors, label=f"[{entry}] Position")
        check_links(root, path, errors)


def check_controls(root, errors, warnings):
    base = root / "kit" / "controls"
    if not base.is_dir():
        return
    for path in sorted(base.glob("*.md")):
        if path.name in ("README.md", "CLAUDE.md"):
            continue
        name = rel(root, path)
        if not SLUG.match(path.stem):
            errors.append(f"{name}: filename must be a lowercase-hyphen slug")
        text = path.read_text()
        if not re.match(r"# .+", text):
            errors.append(f"{name}: must start with an '# <Control>' title")
        fields = {m.group(1) for l in text.split("\n") if (m := CONTROL_FIELD.match(l))}
        for missing in sorted(CONTROL_FIELDS - fields):
            errors.append(f"{name}: missing '**{missing}:**' line")
        headings = {m.group(1).strip() for m in re.finditer(r"^## (.+)$", strip_code(text), re.M)}
        for heading in CONTROL_HEADINGS:
            if heading not in headings:
                errors.append(f"{name}: missing '## {heading}' heading")
        if not POSITION_LINK.search(text):
            warnings.append(f"{name}: no link to a position.md yet")
        check_links(root, path, errors)


def check_skills(root, errors):
    path = root / "kit" / "skills" / "skills.md"
    if not path.is_file():
        return
    name = rel(root, path)
    text = path.read_text()
    if not re.match(r"# .+", text):
        errors.append(f"{name}: must start with an '# <title>'")
    seen = set()
    for block in re.split(r"(?m)^## ", strip_code(text))[1:]:
        skill = block.split("\n", 1)[0].strip()
        if not SLUG.match(skill):
            errors.append(f"{name}: skill id '{skill}' must be a lowercase-hyphen slug")
        if skill in seen:
            errors.append(f"{name}: duplicate skill id '{skill}'")
        seen.add(skill)
        fields = {}
        for l in block.split("\n")[1:]:
            if m := ENTRY_FIELD.match(l):
                fields[m.group(1)] = m.group(2)
        for missing in sorted(SKILL_FIELDS - fields.keys()):
            errors.append(f"{name}: {skill}: missing '**{missing}:**' line")
        if "Where" in fields and not LINK.search(fields["Where"]):
            errors.append(f"{name}: {skill}: 'Where' must be a Markdown link")
    check_links(root, path, errors)


def check_leads(root, errors):
    path = root / "research" / "leads.md"
    if not path.is_file():
        return
    name = rel(root, path)
    text = re.sub(r"^```.*?^```", "", path.read_text(), flags=re.S | re.M)
    seen = set()
    for block in re.split(r"^## +", text, flags=re.M)[1:]:
        title, _, body = block.partition("\n")
        title = title.strip()
        if title in seen:
            errors.append(f"{name}: duplicate lead '{title}'")
        seen.add(title)
        fields = {}
        for line in body.splitlines():
            if not line.strip():
                continue
            m = LEAD_FIELD.match(line)
            if not m or m.group(1) not in LEAD_FIELDS:
                errors.append(f"{name}: lead '{title}': expected '- kind|link|why: value', got '{line}'")
            elif m.group(1) in fields:
                errors.append(f"{name}: lead '{title}': duplicate field '{m.group(1)}'")
            else:
                fields[m.group(1)] = m.group(2).strip()
        for key in LEAD_FIELDS:
            if not fields.get(key):
                errors.append(f"{name}: lead '{title}': missing or empty '{key}'")
        if fields.get("kind") and fields["kind"] not in LEAD_KINDS:
            errors.append(f"{name}: lead '{title}': kind '{fields['kind']}' is not one of {sorted(LEAD_KINDS)}")
        if fields.get("link") and not re.match(r"^https?://\S+$", fields["link"]):
            errors.append(f"{name}: lead '{title}': link must be an http(s) URL")


def check_guide(root, errors):
    for path in sorted((root / "guide").glob("*.md")) if (root / "guide").is_dir() else []:
        if path.name != "CLAUDE.md":
            check_links(root, path, errors)


def validate(root):
    errors, warnings = [], []
    check_research(root, errors, warnings)
    check_leads(root, errors)
    check_catalogue(root, errors)
    check_controls(root, errors, warnings)
    check_skills(root, errors)
    check_guide(root, errors)
    return errors, warnings


def main():
    root = Path(__file__).resolve().parent.parent
    errors, warnings = validate(root)
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    if errors:
        print(f"\n{len(errors)} error(s). Fix them and run again.")
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
