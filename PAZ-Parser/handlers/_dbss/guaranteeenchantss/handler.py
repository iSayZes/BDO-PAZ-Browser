from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table
from _common.item_key import item_key_list_cell, item_name
from _common.lang import handler_text, load_handler_strings
from _common.lookup_index import IndexKind, lookup
from .parser import parse_guaranteeenchantss_records


_LANG_DIR = Path(__file__).parent / "lang"

_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3


def _type_items(enhancement_type: int, cache: dict[int, tuple[list[int], list[str]]]) -> tuple[list[int], list[str]]:
    """The base items of this enhancement type (IndexKind.ENHANCEMENT_TYPE_ITEMS) and their names.

    Every level of a type lists the same items, so each type is named once.
    """
    if enhancement_type not in cache:
        linked = lookup(IndexKind.ENHANCEMENT_TYPE_ITEMS, enhancement_type)
        item_ids = list(linked) if isinstance(linked, tuple) else []
        cache[enhancement_type] = item_ids, [item_name(item_id) or str(item_id) for item_id in item_ids]
    return cache[enhancement_type]


def _with_items(record: dict, type_items: tuple[list[int], list[str]]) -> dict:
    """The parsed record plus its items, for the Items column, search and export."""
    item_ids, item_names = type_items
    return {
        **record,
        # 0 shows no gauge in game; None sorts last and exports empty.
        "agris_count": record["agris_count"] or None,
        "item_ids": item_ids,
        "item_names": item_names,
        # None sorts last: no item carries some types (guaranteeenchantss_dbss.md).
        "item_count": len(item_ids) or None,
    }


class GuaranteeEnchantHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["enhancementType"], "num", sort_key="enhancement_type"),
            Column(cols["level"], "num", sort_key="enchant_level"),
            Column(cols["agrisCount"], "num", sort_key="agris_count"),
            Column(cols["items"], sort_key="item_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # Keep the parser's order: each enhancement type with its levels in a row.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        items_by_type: dict[int, tuple[list[int], list[str]]] = {}
        return [
            _with_items(record, _type_items(record["enhancement_type"], items_by_type))
            for record in parse_guaranteeenchantss_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        types = len({record["enhancement_type"] for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), types=types)
        rows = [
            [
                e(record["enhancement_type"]),
                e(record["enchant_level"]),
                _EMPTY if record["agris_count"] is None else e(record["agris_count"]),
                item_key_list_cell(record["item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
