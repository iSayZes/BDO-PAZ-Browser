"""The empty-cell check of tests/test_handler_sort.py: a handler stores an
empty sort value behind each cell it renders as a dash or blank, so those rows
sort last ("Store none as None" in docs/handler.md)."""
from __future__ import annotations

import html
import re

from bdo_preview import PreviewHandler
from table_sort import is_empty

_HEADER_RE = re.compile(r"<th\b([^>]*)>")
_SORT_KEY_RE = re.compile(r'data-sort-key="([^"]+)"')
_TAG_RE = re.compile(r"<[^>]+>")
# Image cells (icons, sprite regions) have no text even when they show something.
_IMAGE_MARKERS = ("<img", "background")
_EMPTY_TEXTS = frozenset({"", "-"})
_MAX_REPORTED = 5

# The page holds every record (70,450 rows for itemenchant.dbss on client
# 3474), so rows and cells are cut with str.split: over all cases the scan
# takes 8.7 s, against 15 s with a row and a cell regex.
_ROW_START = "<tr>"
_ROW_END = "</tr>"
_CELL_START = "<td"
_CELL_END = "</td>"


def _header_sort_keys(page: str) -> list[str | None]:
    """The sort key of each rendered column, None for an unsortable one."""
    head = page[page.index("<thead>") : page.index("</thead>")]
    keys: list[str | None] = []
    for attrs in _HEADER_RE.findall(head):
        match = _SORT_KEY_RE.search(attrs)
        keys.append(html.unescape(match.group(1)) if match else None)
    return keys


def _row_cells(row: str) -> list[str]:
    """The inner HTML of each `<td>` in `row`."""
    cells: list[str] = []
    for chunk in row.split(_CELL_END)[:-1]:
        start = chunk.find(_CELL_START)
        if start != -1:
            cells.append(chunk[chunk.index(">", start) + 1 :])
    return cells


def _body_rows(page: str) -> list[list[str]]:
    body = page[page.index("<tbody>") :]
    rows = (chunk.split(_ROW_END, 1) for chunk in body.split(_ROW_START)[1:])
    return [_row_cells(parts[0]) for parts in rows if len(parts) == 2]


def _visible_text(cell: str) -> str | None:
    """The cell's text without tags, or None for an image cell."""
    if "<" not in cell:
        # Most cells are plain text, and both image markers sit inside a tag.
        return html.unescape(cell).strip()
    if any(marker in cell for marker in _IMAGE_MARKERS):
        return None
    return html.unescape(_TAG_RE.sub("", cell)).strip()


def _sorts_by_a_value(value: object, text: str) -> bool:
    """True when an empty-looking cell's record holds a value, unless the
    cell shows that value itself, like a name that is "-" in the game data."""
    if is_empty(value):
        return False
    return not (isinstance(value, str) and value.strip() == text)


def assert_empty_cells_sort_last(handler: PreviewHandler, records: list[dict]) -> None:
    """Render every record and fail on an empty-looking cell whose sort value is not empty."""
    page = handler.render_records_page(records, 0, len(records))
    sortable = [(index, key) for index, key in enumerate(_header_sort_keys(page)) if key is not None]
    rows = _body_rows(page)
    assert len(rows) == len(records), "rendered rows do not match the records"

    mismatches: list[str] = []
    for record, cells in zip(records, rows):
        for index, key in sortable:
            if index >= len(cells):
                break
            text = _visible_text(cells[index])
            if text is None or text not in _EMPTY_TEXTS:
                continue
            value = record.get(key)
            if _sorts_by_a_value(value, text):
                mismatches.append(f"{key}={value!r}")

    assert not mismatches, (
        f"{len(mismatches)} empty cells sort by a value: {mismatches[:_MAX_REPORTED]}"
    )
