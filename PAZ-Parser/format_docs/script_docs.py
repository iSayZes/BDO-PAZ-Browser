"""The per-script `.luac` docs in docs/file-formats/lua/: their sections and call table.

`luascript_luac.md` (the bytes every script shares) is a layout doc; every
other doc in `lua/` describes one script, in the order its Script Docs
section gives.
"""
from __future__ import annotations

from pathlib import Path

from .doc_paths import LUA_GROUP
from .markdown import numbered_lines, sections, tables
from .model import Problem

CONTAINER_DOC = "luascript_luac.md"
CALLS_SECTION = "Calls Into Client Data"
SECTION_ORDER = ("Purpose", CALLS_SECTION, "Enums Used", "Versions", "Open Questions")
REQUIRED_SECTIONS = ("Purpose", CALLS_SECTION, "Versions")
CALLS_HEADER = ("Call", "What the script does with it", "Format doc field", "Client")
_SECTION_LEVEL = 2


def is_script_doc(path: Path) -> bool:
    """True for a doc of one Lua script: in the `lua/` group folder, and not the container doc."""
    return path.parent.name == LUA_GROUP and path.name != CONTAINER_DOC


def script_doc_problems(text: str) -> list[Problem]:
    """Unknown, missing or out-of-order `##` sections, and a call table without its four columns."""
    found = sections(numbered_lines(text), _SECTION_LEVEL)
    problems = [Problem(section.line, f"`## {section.title}` is not a script doc section") for section in found if section.title not in SECTION_ORDER]
    titles = [section.title for section in found if section.title in SECTION_ORDER]
    problems += [Problem(1, f"no `## {title}` section") for title in REQUIRED_SECTIONS if title not in titles]
    if titles != sorted(titles, key=SECTION_ORDER.index):
        problems.append(Problem(1, f"sections go {', '.join(SECTION_ORDER)}"))
    calls = next((section for section in found if section.title == CALLS_SECTION), None)
    if calls is not None and not any(table.header == CALLS_HEADER for table in tables(calls.body)):
        problems.append(Problem(calls.line, f"the call table has the columns {' | '.join(CALLS_HEADER)}"))
    return problems
