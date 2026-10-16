"""The `## Versions` section: which clients each layout fits, with sizes and coverage.

The doc check writes it between the two markers. Rows only grow: a client
widens its layout's range, and sizes come from the newest client checked.
"""
from __future__ import annotations

import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, replace

from .doc_checks import VERSIONS_BEGIN, VERSIONS_END
from .markdown import numbered_lines, tables
from .walk_model import FileFit, LayoutFit

_LEAD = "Sizes and coverage from the client in the Checked column. The newest layout is the current one."
_SIZES_HEADER = ("Layout", "Clients", "Checked", "File", "Bytes", "Records", "Row bytes")
_COVERAGE_HEADER = ("Layout", "File", "Known", "Unknown")
_CLIENTS = re.compile(r"^(?P<first>\d+)(?: to (?P<last>\d+)| and later)?$")
_BYTES = re.compile(r"^(?P<bytes>[\d,]+) B")
# A structure walked once (a string table, a header) says nothing about the record count.
_SINGLE = 1


@dataclass(frozen=True)
class VersionRow:
    """One file of one layout, as the last client checked for it saw it."""

    layout: int
    first: int
    checked: int
    file: str
    size: int
    records: str
    row_bytes: str
    known: int
    unknown: int


def rows_from_fit(fit: LayoutFit, client: int) -> tuple[VersionRow, ...]:
    return tuple(_row(fit.layout, client, file) for file in fit.files)


def merge_rows(old: Iterable[VersionRow], new: Iterable[VersionRow]) -> tuple[VersionRow, ...]:
    """`old` with `new` added: ranges widen, sizes follow the newest client, no row is dropped."""
    merged = {(row.layout, row.file): row for row in old}
    for row in new:
        known = merged.get((row.layout, row.file))
        if known is None:
            merged[(row.layout, row.file)] = row
            continue
        first = min(known.first, row.first)
        newest = row if row.checked >= known.checked else known
        merged[(row.layout, row.file)] = replace(newest, first=first, checked=max(known.checked, row.checked))
    return tuple(sorted(merged.values(), key=lambda row: (-row.layout, row.file)))


def read_rows(text: str) -> tuple[VersionRow, ...]:
    """The rows the Versions section of a doc holds now."""
    block = _block(text)
    if block is None:
        return ()
    found = tables(numbered_lines(block))
    sizes = next((table for table in found if table.header == _SIZES_HEADER), None)
    coverage = next((table for table in found if table.header == _COVERAGE_HEADER), None)
    if sizes is None or coverage is None:
        return ()
    covered = {(int(cells[0]), cells[1].strip("`")): (_bytes(cells[2]), _bytes(cells[3])) for _, cells in coverage.rows}
    rows: list[VersionRow] = []
    for _, cells in sizes.rows:
        layout, clients, checked, file, size, records, row_bytes = cells
        match = _CLIENTS.match(clients)
        if not match:
            continue
        name = file.strip("`")
        known, unknown = covered.get((int(layout), name), (0, 0))
        rows.append(VersionRow(int(layout), int(match.group("first")), int(checked), name, _bytes(size), records, row_bytes, known, unknown))
    return tuple(rows)


def write_rows(text: str, rows: Sequence[VersionRow], newest_layout: int) -> str:
    """`text` with the Versions block rewritten from `rows`; unchanged when it has no markers."""
    begin = next((index for index, line in enumerate(text.splitlines()) if line.startswith(VERSIONS_BEGIN)), None)
    lines = text.splitlines(keepends=True)
    end = next((index for index, line in enumerate(lines) if line.strip() == VERSIONS_END), None)
    if begin is None or end is None or end < begin:
        return text
    newline = "\r\n" if lines[begin].endswith("\r\n") else "\n"
    body = render_rows(rows, newest_layout)
    middle = newline + newline.join(body.splitlines()) + newline + newline if body else newline
    return "".join(lines[: begin + 1]) + middle + "".join(lines[end:])


def render_rows(rows: Sequence[VersionRow], newest_layout: int) -> str:
    if not rows:
        return ""
    sizes = [
        (str(row.layout), _clients(row, newest_layout), str(row.checked), f"`{row.file}`", f"{row.size:,}", row.records, row.row_bytes)
        for row in rows
    ]
    coverage = [
        (str(row.layout), f"`{row.file}`", _share(row.known, row.size), _share(row.unknown, row.size))
        for row in rows
    ]
    return f"{_LEAD}\n\n{_table(_SIZES_HEADER, sizes)}\n\n{_table(_COVERAGE_HEADER, coverage)}"


def _row(layout: int, client: int, file: FileFit) -> VersionRow:
    repeated = {name: stats for name, stats in file.rows.items() if stats.count > _SINGLE} or file.rows
    records = ", ".join(f"{stats.count:,} {name}" for name, stats in repeated.items())
    main = max(repeated.values(), key=lambda stats: stats.count, default=None)
    if main is None:
        row_bytes = "-"
    elif main.smallest == main.largest:
        row_bytes = f"{main.smallest:,}"
    else:
        row_bytes = f"{main.smallest:,} to {main.largest:,}, {round(main.average):,} on average"
    return VersionRow(layout, client, client, file.file, file.size, records or "-", row_bytes, file.known, file.unknown)


def _clients(row: VersionRow, newest_layout: int) -> str:
    if row.layout == newest_layout:
        return f"{row.first} and later"
    return str(row.first) if row.first == row.checked else f"{row.first} to {row.checked}"


def _share(part: int, whole: int) -> str:
    percent = 100 * part / whole if whole else 0.0
    return f"{part:,} B ({percent:.1f}%)"


def _bytes(cell: str) -> int:
    match = _BYTES.match(cell.strip()) or re.match(r"^(?P<bytes>[\d,]+)$", cell.strip())
    return int(match.group("bytes").replace(",", "")) if match else 0


def _table(header: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    widths = [max(len(cell) for cell in column) for column in zip(header, *rows)]
    lines = [header, tuple("-" * width for width in widths), *rows]
    return "\n".join("| " + " | ".join(cell.ljust(width) for cell, width in zip(line, widths)) + " |" for line in lines)


def _block(text: str) -> str | None:
    lines = text.splitlines()
    begin = next((index for index, line in enumerate(lines) if line.startswith(VERSIONS_BEGIN)), None)
    end = next((index for index, line in enumerate(lines) if line.strip() == VERSIONS_END), None)
    if begin is None or end is None or end < begin:
        return None
    return "\n".join(lines[begin + 1 : end])
