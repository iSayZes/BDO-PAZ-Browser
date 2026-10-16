"""Headings and tables of a markdown doc, outside fenced code blocks."""
from __future__ import annotations

import re

from .model import Section, Table

_HEADING = re.compile(r"^(#{1,6}) +(.*?) *$")
_SEPARATOR = re.compile(r"^\|(?: *:?-+:? *\|)+$")
_FENCE = "```"


def numbered_lines(text: str) -> tuple[tuple[int, str], ...]:
    """Each line with its 1-based number, with lines inside code fences blanked."""
    lines: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith(_FENCE):
            in_fence = not in_fence
            lines.append((number, ""))
            continue
        lines.append((number, "" if in_fence else line))
    return tuple(lines)


def sections(lines: tuple[tuple[int, str], ...], level: int) -> tuple[Section, ...]:
    """The sections that start with a heading of exactly `level`."""
    found: list[Section] = []
    for index, (number, line) in enumerate(lines):
        match = _HEADING.match(line)
        if not match or len(match.group(1)) != level:
            continue
        end = next(
            (k for k in range(index + 1, len(lines)) if _heading_level(lines[k][1]) in range(1, level + 1)),
            len(lines),
        )
        found.append(Section(level, match.group(2), number, lines[index + 1 : end]))
    return tuple(found)


def tables(lines: tuple[tuple[int, str], ...]) -> tuple[Table, ...]:
    """Every table in `lines`: a header row, a separator row, then body rows."""
    found: list[Table] = []
    index = 0
    while index < len(lines) - 1:
        number, line = lines[index]
        if line.startswith("|") and _SEPARATOR.match(lines[index + 1][1].strip()):
            end = index + 2
            while end < len(lines) and lines[end][1].startswith("|"):
                end += 1
            rows = tuple((row_number, split_row(row)) for row_number, row in lines[index + 2 : end])
            found.append(Table(number, split_row(line), rows))
            index = end
            continue
        index += 1
    return tuple(found)


def split_row(line: str) -> tuple[str, ...]:
    """The trimmed cells of a table row; a `|` inside backticks or after `\\` stays in its cell."""
    cells: list[str] = []
    current: list[str] = []
    in_code = False
    previous = ""
    for char in line.strip().strip("|"):
        if char == "`":
            in_code = not in_code
        is_escaped, previous = previous == "\\", char
        if char == "|" and not in_code and not is_escaped:
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    cells.append("".join(current).strip())
    return tuple(cells)


def _heading_level(line: str) -> int:
    match = _HEADING.match(line)
    return len(match.group(1)) if match else 0
