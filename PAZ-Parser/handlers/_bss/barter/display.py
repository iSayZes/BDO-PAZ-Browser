"""Columns, record text and cells of the Exchange, shared by the barter handlers.

Each handler puts `exchange_columns()` among its own columns, adds
`exchange_text_fields()` to its records and `exchange_cells()` to its rows,
so the barter tables show an exchange the same way: the from and to items
with their per-level icon and grade colour, their count ranges, then the
limits. A `barter_normal.bss` entry that names a sub group leaves its
Exchange zero; its Exchange fields become None and its cells dashes.
"""

from __future__ import annotations

from pathlib import Path

from _common.html import Column, e, icon_html_label_cell
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.lang import load_handler_strings
from _common.pa_text import pa_html
from .exchange import EXCHANGE_FIELDS

_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_TEXT_FIELDS = ("from_item", "from_count", "to_item", "to_count")
# One cell per column of exchange_columns().
_CELL_COUNT = 8


def count_range_text(low: int, high: int) -> str:
    """`5` for a fixed count, `900 - 1,000` for a range."""
    return f"{low:,}" if low == high else f"{low:,} - {high:,}"


def is_empty_exchange(record: dict) -> bool:
    """True when every Exchange field is 0, as on the sub group entries of `barter_normal.bss`."""
    return not any(record[field] for field in EXCHANGE_FIELDS)


def exchange_text_fields(record: dict) -> dict:
    """The item names and count ranges of a record's Exchange, for tab search and CSV export.

    An empty Exchange gets None in its text fields and its raw fields, so
    its dashed cells sort last.
    """
    if is_empty_exchange(record):
        return dict.fromkeys((*EXCHANGE_FIELDS, *_TEXT_FIELDS))
    return {
        "from_item": item_key_text(record["from_item_key"]),
        "from_count": count_range_text(record["from_min_count"], record["from_max_count"]),
        "to_item": item_key_text(record["to_item_key"]),
        "to_count": count_range_text(record["to_min_count"], record["to_max_count"]),
    }


def exchange_columns(lang: str) -> list[Column]:
    """The Exchange columns, in doc order."""
    cols = load_handler_strings(lang, _LANG_DIR)["columns"]
    return [
        Column(cols["fromItem"], sort_key="from_item"),
        Column(cols["fromCount"], "num", sort_key="from_min_count"),
        Column(cols["toItem"], sort_key="to_item"),
        Column(cols["toCount"], "num", sort_key="to_min_count"),
        Column(cols["needPoint"], "num", sort_key="barter_need_point"),
        Column(cols["exchanges"], "num", sort_key="exchange_max_count"),
        Column(cols["exchangeMin"], "num", sort_key="exchange_min"),
        Column(cols["exchangeMax"], "num", sort_key="exchange_max"),
    ]


def _item_cell(item_key: int) -> str:
    return icon_html_label_cell(item_key_icon_path(item_key), pa_html(item_key_text_tagged(item_key)))


def exchange_cells(record: dict) -> list[str]:
    """The cells of `exchange_columns()` for one record, dashes for an empty Exchange."""
    if record["from_item_key"] is None:
        return [_EMPTY] * _CELL_COUNT
    return [
        _item_cell(record["from_item_key"]),
        e(record["from_count"]),
        _item_cell(record["to_item_key"]),
        e(record["to_count"]),
        e(f"{record['barter_need_point']:,}"),
        e(record["exchange_max_count"]),
        e(f"{record['exchange_min']:,}"),
        e(f"{record['exchange_max']:,}"),
    ]
