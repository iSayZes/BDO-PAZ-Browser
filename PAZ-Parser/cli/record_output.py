"""Records as an aligned text table, JSON or CSV."""
from __future__ import annotations

import json
import unicodedata
from collections.abc import Sequence
from enum import Enum

from record_export import records_to_csv

from .stdio import write_raw
from .values import display_text, is_number

# Long cells are cut to this many terminal columns in the text table.
MAX_CELL_WIDTH = 40
_ELLIPSIS = "…"
_COLUMN_GAP = "  "


class OutputFormat(Enum):
    TABLE = "table"
    JSON = "json"
    CSV = "csv"


def record_fields(records: Sequence[dict]) -> list[str]:
    """Every key across the records, in first-seen order.

    Display-only fields (`_description_pa`) are kept: the CLI is for checking
    data, so it shows the text with its game tags next to the plain text.
    """
    seen: dict[str, None] = {}
    for record in records:
        for key in record:
            seen.setdefault(key, None)
    return list(seen)


def project(records: Sequence[dict], fields: Sequence[str]) -> list[dict]:
    """New records holding only `fields`, in that order; a missing key is None."""
    return [{field: record.get(field) for field in fields} for record in records]


def format_json(value: object) -> str:
    """`value` as indented JSON; bytes as hex, sets as sorted lists, enums by value."""
    return json.dumps(value, ensure_ascii=False, indent=2, default=_json_default) + "\n"


def format_records(records: list[dict], output: OutputFormat) -> str:
    if output is OutputFormat.JSON:
        return format_json(records)
    if output is OutputFormat.CSV:
        return records_to_csv(records)
    # A single row was asked for by name, so show it whole.
    return format_table(records, max_width=None if len(records) == 1 else MAX_CELL_WIDTH)


def format_table(records: Sequence[dict], max_width: int | None = MAX_CELL_WIDTH) -> str:
    """An aligned table, numbers right-aligned, long cells cut in the middle.

    `max_width=None` keeps every cell whole.
    """
    fields = record_fields(records)
    if not fields:
        return ""

    cells = [[_fit(display_text(r.get(f)), max_width) for f in fields] for r in records]
    widths = [
        max([_width(field)] + [_width(row[i]) for row in cells])
        for i, field in enumerate(fields)
    ]
    numeric = [_is_numeric_column(records, field) for field in fields]

    def line(values: Sequence[str]) -> str:
        parts = [
            _pad(value, widths[i], right=numeric[i])
            for i, value in enumerate(values)
        ]
        return _COLUMN_GAP.join(parts).rstrip()

    rule = _COLUMN_GAP.join("-" * width for width in widths)
    return "\n".join([line(fields), rule, *(line(row) for row in cells)]) + "\n"


def _is_numeric_column(records: Sequence[dict], field: str) -> bool:
    values = [r.get(field) for r in records if r.get(field) is not None]
    return bool(values) and all(is_number(v) for v in values)


def _char_width(char: str) -> int:
    """Terminal columns of one character: Hangul and other wide forms take two."""
    if unicodedata.combining(char):
        return 0
    return 2 if unicodedata.east_asian_width(char) in ("W", "F") else 1


def _width(text: str) -> int:
    return sum(_char_width(c) for c in text)


def _fit(text: str, max_width: int | None) -> str:
    """`text` cut in the middle to `max_width` columns, so both ends stay.

    The end is often what tells rows apart, such as an icon path's file name.
    """
    if max_width is None or _width(text) <= max_width:
        return text
    budget = max_width - _width(_ELLIPSIS)
    head = _take(text, (budget + 1) // 2)
    tail = _take(text[::-1], budget - _width(head))[::-1]
    return head + _ELLIPSIS + tail


def _take(text: str, max_width: int) -> str:
    """The longest start of `text` that fits in `max_width` columns."""
    used = 0
    for index, char in enumerate(text):
        used += _char_width(char)
        if used > max_width:
            return text[:index]
    return text


def _pad(text: str, width: int, *, right: bool) -> str:
    padding = " " * (width - _width(text))
    return padding + text if right else text + padding


def _json_default(value: object) -> object:
    if isinstance(value, (bytes, bytearray)):
        return value.hex()
    if isinstance(value, (set, frozenset)):
        return sorted(value, key=str)
    if isinstance(value, Enum):
        return value.value
    return str(value)


def write_records(records: list[dict], output: OutputFormat) -> None:
    write_raw(format_records(records, output))
