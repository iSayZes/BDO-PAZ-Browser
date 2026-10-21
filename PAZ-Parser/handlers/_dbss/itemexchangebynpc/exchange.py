"""One `itemexchangebynpc.dbss` exchange as text and as a cell, for the views that list exchanges by key."""
from __future__ import annotations

from _common.html import e, icon_html_label_cell
from _common.item_key import item_count_text, item_key_icon_path, item_key_text_tagged
from _common.pa_text import pa_html
from .parser import parse_itemexchangebynpc_records

EXCHANGE_ARROW = "→"


def exchanges_by_key(data: bytes | None) -> dict[int, dict]:
    """Every row of `itemexchangebynpc.dbss` by its exchange key; empty when the file is missing.

    Raises ValueError when the file does not parse.
    """
    if data is None:
        return {}
    return {record["item_exchange_key"]: record for record in parse_itemexchangebynpc_records(data)}


def exchange_text(record: dict) -> str:
    """`Horse Race Seal x25 → Storm Horse Gear Box x1`, plain text for search and export."""
    need = item_count_text(record["need_item_key"], record["need_item_count"])
    result = item_count_text(record["result_item_key"], record["result_item_count"])
    return f"{need} {EXCHANGE_ARROW} {result}"


def _item_count_html(item_key: int, count: int) -> str:
    return icon_html_label_cell(item_key_icon_path(item_key), f"{pa_html(item_key_text_tagged(item_key))} x{count:,}")


def exchange_cell(record: dict) -> str:
    """The need item and count, an arrow, then the result item and count, each with its icon and grade colour."""
    need = _item_count_html(record["need_item_key"], record["need_item_count"])
    result = _item_count_html(record["result_item_key"], record["result_item_count"])
    return f"{need} {e(EXCHANGE_ARROW)} {result}"
