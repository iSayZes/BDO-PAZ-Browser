from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.item_key import item_key_list_cell, item_name
from _common.lang import handler_text, load_handler_strings
from _common.lookup_index import IndexKind, lookup
from .parser import parse_itemviewstackenchantgroupss_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3
_KEY_PREVIEW_COUNT = 8


def _key_items(enchant_key: int) -> list[int]:
    """The base items that enhance with this key (IndexKind.ENCHANT_KEY_ITEMS), ascending."""
    linked = lookup(IndexKind.ENCHANT_KEY_ITEMS, enchant_key)
    return list(linked) if isinstance(linked, tuple) else []


def _group_items(group_enchant_keys: list[int]) -> list[int]:
    """The items of every key in the group, in group order, each once."""
    return list(dict.fromkeys(item_id for key in group_enchant_keys for item_id in _key_items(key)))


def _with_items(record: dict, group_items: dict[tuple[int, ...], list[int]]) -> dict:
    """The parsed row plus its items and the group's items, by ID and name for search and export."""
    item_ids = _key_items(record["enchant_key"])
    group = tuple(record["group_enchant_keys"])
    if group not in group_items:
        group_items[group] = _group_items(record["group_enchant_keys"])
    return {
        **record,
        "item_ids": item_ids,
        "item_names": [item_name(item_id) or str(item_id) for item_id in item_ids],
        # None sorts last: some keys belong to no item.
        "item_count": len(item_ids) or None,
        "group_item_ids": group_items[group],
    }


class ItemViewStackEnchantGroupSsBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["enchantKey"], "num", sort_key="enchant_key"),
            Column(cols["items"], sort_key="item_count"),
            Column(cols["groupSize"], "num", sort_key="group_count"),
            # List columns: they would only sort by their string form.
            Column(cols["groupKeys"]),
            Column(cols["groupItems"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        # Every key of a group repeats the group, so its items are collected once.
        group_items: dict[tuple[int, ...], list[int]] = {}
        return [_with_items(record, group_items) for record in parse_itemviewstackenchantgroupss_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        groups = len({tuple(sorted(record["group_enchant_keys"])) for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), groups=groups)
        rows = [
            [
                e(record["enchant_key"]),
                item_key_list_cell(record["item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(record["group_count"]),
                text_list_cell(record["group_enchant_keys"], _KEY_PREVIEW_COUNT),
                item_key_list_cell(record["group_item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
