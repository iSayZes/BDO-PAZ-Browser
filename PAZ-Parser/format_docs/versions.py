"""The `## Versions` section: which clients each layout fits, with sizes and coverage.

The doc check writes it between the two markers. Rows only grow: a client
widens its layout's range, and sizes come from the newest client checked.
The Clients table lists every client the doc check read, with the layout
the files fit, `No documented layout` when they are there but no layout of
the doc reads them, or `No file` when none of the doc's files is in that
client.
"""
from __future__ import annotations

import re
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, replace

from .markdown import numbered_lines, tables
from .walk_model import FileFit, LayoutFit

VERSIONS_BEGIN = "<!-- versions:begin"
VERSIONS_END = "<!-- versions:end -->"
_LEAD = "Sizes and coverage from the client in the Checked column. The newest layout is the current one."
_SIZES_HEADER = ("Layout", "Clients", "Checked", "File", "Bytes", "Records", "Row bytes")
_COVERAGE_HEADER = ("Layout", "File", "Known", "Unknown")
_CLIENTS_LEAD = "Every client the doc check read, and the layout its files fit."
_CLIENTS_HEADER = ("Client", "Result")
NO_FILE = "No file"
NO_LAYOUT = "No documented layout"
_LAYOUT_RESULT = re.compile(r"^Layout (?P<layout>\d+)$")
_CLIENTS = re.compile(r"^(?P<first>\d+)(?: to (?P<last>\d+)| and later)?$")
_BYTES = re.compile(r"^(?P<bytes>[\d,]+)(?: B|$)")
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


@dataclass(frozen=True)
class ClientCheck:
    """A client the doc check read: the layout its files fit, or None when none does.

    `has_file` tells the two Nones apart: the files are there but no documented layout reads them, or none is there.
    """

    client: int
    layout: int | None
    has_file: bool

    @property
    def result(self) -> str:
        if self.layout is not None:
            return f"Layout {self.layout}"
        return NO_LAYOUT if self.has_file else NO_FILE


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


def merge_clients(old: Iterable[ClientCheck], new: Iterable[ClientCheck]) -> tuple[ClientCheck, ...]:
    """`old` with `new` added, newest client first; a client read again takes its new result."""
    merged = {check.client: check for check in old}
    merged.update((check.client, check) for check in new)
    return tuple(sorted(merged.values(), key=lambda check: -check.client))


def read_clients(text: str) -> tuple[ClientCheck, ...]:
    """The Clients table of a doc's Versions section, newest client first."""
    block = _block(text)
    if block is None:
        return ()
    table = next((table for table in tables(numbered_lines(block)) if table.header == _CLIENTS_HEADER), None)
    if table is None:
        return ()
    checks: list[ClientCheck] = []
    for _, cells in table.rows:
        if not _is_row(cells, _CLIENTS_HEADER):
            continue
        match = _LAYOUT_RESULT.match(cells[1])
        if match:
            checks.append(ClientCheck(int(cells[0]), int(match.group("layout")), True))
        elif cells[1] in (NO_FILE, NO_LAYOUT):
            checks.append(ClientCheck(int(cells[0]), None, cells[1] == NO_LAYOUT))
    return merge_clients((), checks)


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
    covered = {
        (int(cells[0]), cells[1].strip("`")): (_bytes(cells[2]), _bytes(cells[3]))
        for _, cells in coverage.rows
        if _is_row(cells, _COVERAGE_HEADER)
    }
    rows: list[VersionRow] = []
    for _, cells in sizes.rows:
        if not _is_row(cells, _SIZES_HEADER):
            continue
        layout, clients, checked, file, size, records, row_bytes = cells
        match = _CLIENTS.match(clients)
        if not match or not checked.isdigit():
            continue
        name = file.strip("`")
        known, unknown = covered.get((int(layout), name), (0, 0))
        rows.append(VersionRow(int(layout), int(match.group("first")), int(checked), name, _bytes(size), records, row_bytes, known, unknown))
    return tuple(rows)


def write_rows(text: str, rows: Sequence[VersionRow], clients: Sequence[ClientCheck], newest_layout: int) -> str:
    """`text` with the Versions block rewritten from `rows` and `clients`; unchanged when it has no markers."""
    lines = text.splitlines(keepends=True)
    span = marker_span(lines)
    if span is None:
        return text
    begin, end = span
    newline = "\r\n" if lines[begin].endswith("\r\n") else "\n"
    body = render_rows(rows, clients, newest_layout)
    middle = newline + newline.join(body.splitlines()) + newline + newline if body else newline
    return "".join(lines[: begin + 1]) + middle + "".join(lines[end:])


def render_rows(rows: Sequence[VersionRow], clients: Sequence[ClientCheck], newest_layout: int) -> str:
    parts: list[str] = []
    if rows:
        parts.append(_sizes_and_coverage(rows, newest_layout))
    if clients:
        results = [(str(check.client), check.result) for check in clients]
        parts.append(f"{_CLIENTS_LEAD}\n\n{_table(_CLIENTS_HEADER, results)}")
    return "\n\n".join(parts)


def _sizes_and_coverage(rows: Sequence[VersionRow], newest_layout: int) -> str:
    sizes = [
        (str(row.layout), clients_text(row, newest_layout), str(row.checked), f"`{row.file}`", f"{row.size:,}", row.records, row.row_bytes)
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


def clients_text(row: VersionRow, newest_layout: int) -> str:
    """`3464 and later` for the newest layout, `3401 to 3458` or one client for an older one."""
    if row.layout == newest_layout:
        return f"{row.first} and later"
    return str(row.first) if row.first == row.checked else f"{row.first} to {row.checked}"


def _share(part: int, whole: int) -> str:
    percent = 100 * part / whole if whole else 0.0
    return f"{part:,} B ({percent:.1f}%)"


def _bytes(cell: str) -> int:
    match = _BYTES.match(cell.strip())
    return int(match.group("bytes").replace(",", "")) if match else 0


def _is_row(cells: Sequence[str], header: Sequence[str]) -> bool:
    """A table row the reader can use: one cell per column and a Layout number, so hand edits do not crash it."""
    return len(cells) == len(header) and cells[0].isdigit()


def _table(header: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    widths = [max(len(cell) for cell in column) for column in zip(header, *rows)]
    lines = [header, tuple("-" * width for width in widths), *rows]
    return "\n".join("| " + " | ".join(cell.ljust(width) for cell, width in zip(line, widths)) + " |" for line in lines)


def marker_span(lines: Sequence[str]) -> tuple[int, int] | None:
    """The indexes of the `versions:begin` and `versions:end` lines, or None unless both are there in that order."""
    begin = next((index for index, line in enumerate(lines) if line.strip().startswith(VERSIONS_BEGIN)), None)
    end = next((index for index, line in enumerate(lines) if line.strip() == VERSIONS_END), None)
    if begin is None or end is None or end < begin:
        return None
    return begin, end


def _block(text: str) -> str | None:
    lines = text.splitlines()
    span = marker_span(lines)
    return None if span is None else "\n".join(lines[span[0] + 1 : span[1]])
