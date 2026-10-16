"""Reads the `## Layout N` sections of a doc into `Layout` records."""
from __future__ import annotations

import re

from .markdown import sections, tables
from .model import Field, Layout, Problem, Section, SizeSpec, Structure, Table

LAYOUT_COLUMNS = ("Offset", "Type", "Field")
NOTES_COLUMN = "Notes"
FILE_LAYOUT = "File Layout"
_LAYOUT_HEADING = re.compile(r"^Layout (\d+)$")
_COMPANION_HEADING = re.compile(r"^`[a-z0-9_.]+`$")
_STRUCTURE_HEADING = re.compile(r"^(?P<name>[A-Z][A-Za-z0-9 ]*?) \((?P<size>.+)\)$")
_FIXED_SIZE = re.compile(r"^(?P<bytes>\d[\d,]*) bytes?$")
_VARIABLE_SIZE = re.compile(
    r"^variable: (?P<bytes>\d[\d,]*) bytes?(?: \+ (?:(?!, size from ).)+)?(?:, size from `?(?P<file>[a-z0-9_.]+)`?)?$"
)


def layout_number(section: Section) -> int | None:
    match = _LAYOUT_HEADING.match(section.title)
    return int(match.group(1)) if match else None


def read_layout(section: Section, number: int) -> tuple[Layout, tuple[Problem, ...]]:
    """The structures of one `## Layout N` section and the problems in their headings and tables."""
    structures: list[Structure] = []
    problems: list[Problem] = []
    for heading in sections(section.body, 3):
        name, size, problem = _parse_heading(heading)
        if problem:
            problems.append(problem)
            continue
        layout_tables = [table for table in tables(heading.body) if table.header and table.header[0] == "Offset"]
        if len(layout_tables) != 1:
            problems.append(Problem(heading.line, f"`{heading.title}` needs exactly one layout table, has {len(layout_tables)}"))
            continue
        table = layout_tables[0]
        problems.extend(_header_problems(table))
        problems.extend(
            Problem(line, f"a layout row has {len(cells)} cells, the header {len(table.header)}")
            for line, cells in table.rows
            if len(cells) != len(table.header)
        )
        structures.append(Structure(name, heading.line, size, _fields(table)))
    return Layout(number, section.line, tuple(structures)), tuple(problems)


def _parse_heading(heading: Section) -> tuple[str, SizeSpec | None, Problem | None]:
    title = heading.title
    if title == FILE_LAYOUT or _COMPANION_HEADING.match(title):
        return title, None, None
    match = _STRUCTURE_HEADING.match(title)
    if not match:
        return title, None, Problem(heading.line, f"`### {title}` gives no size, e.g. `### Row (24 bytes)`")
    size_text = match.group("size")
    fixed = _FIXED_SIZE.match(size_text)
    if fixed:
        return match.group("name"), SizeSpec(False, _number(fixed.group("bytes"))), None
    variable = _VARIABLE_SIZE.match(size_text)
    if variable:
        spec = SizeSpec(True, _number(variable.group("bytes")), variable.group("file"))
        return match.group("name"), spec, None
    return title, None, Problem(heading.line, f"`({size_text})` is not `(N bytes)` or `(variable: N bytes ...)`")


def _header_problems(table: Table) -> tuple[Problem, ...]:
    header = table.header
    if header[:3] != LAYOUT_COLUMNS or header[-1] != NOTES_COLUMN:
        return (Problem(table.line, "a layout table starts `Offset | Type | Field` and ends with `Notes`"),)
    return ()


def _fields(table: Table) -> tuple[Field, ...]:
    extra_headers = table.header[len(LAYOUT_COLUMNS) : -1]
    return tuple(
        Field(
            line, cells[0], cells[1].strip("`"), cells[2].strip("`"), cells[-1],
            tuple(zip(extra_headers, cells[len(LAYOUT_COLUMNS) : -1])),
        )
        for line, cells in table.rows
        if len(cells) == len(table.header)
    )


def _number(text: str) -> int:
    return int(text.replace(",", ""))
