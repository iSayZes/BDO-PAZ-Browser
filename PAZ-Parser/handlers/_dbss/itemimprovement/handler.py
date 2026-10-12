from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_key_list_cell, item_key_text, item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import SOURCE_FILE, parse_itemimprovement_records, parse_itemimprovementsource_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 4


def _offset_handler(key_field: str, key_label: str) -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn(key_field, key_label),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, key_field),
    )


def item_improvement_offset_handler() -> OffsetTableHandler:
    return _offset_handler("key", "key")


def item_improvement_source_offset_handler() -> OffsetTableHandler:
    return _offset_handler("item_id", "itemId")


def _stones_by_group(source_data: bytes | None) -> dict[int, list[int]]:
    """Stone item IDs per reform group; empty without the stone file."""
    stones: dict[int, list[int]] = defaultdict(list)
    if source_data is not None:
        for stone in parse_itemimprovementsource_records(source_data):
            stones[stone["group"]].append(stone["item_id"])
    return stones


def _gear_record(record: dict, stones: dict[int, list[int]]) -> dict:
    result_id = record["result_id"]
    stone_ids = stones.get(record["group"], [])
    return {
        **record,
        # None sorts last, as the dash of a record without a result.
        "result": item_key_text(result_id) if result_id is not None else None,
        "input": item_key_text(record["input_id"]),
        "stone_ids": stone_ids,
        "stones": [item_key_text(stone_id) for stone_id in stone_ids],
    }


class ItemImprovementHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["result"], sort_key="result"),
            Column(cols["input"], sort_key="input"),
            Column(cols["group"], "num", sort_key="group"),
            # A list column: it would only sort by its string form.
            Column(cols["stones"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{SOURCE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        stones = _stones_by_group(companions.get(SOURCE_FILE))
        return [_gear_record(record, stones) for record in parse_itemimprovement_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["key"]),
                item_key_list_cell([r["result_id"]], 1) if r["result_id"] is not None else _EMPTY,
                item_key_list_cell([r["input_id"]], 1),
                e(r["group"]),
                item_key_list_cell(r["stone_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)


class ItemImprovementSourceHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["stone"], sort_key="item_name"),
            Column(cols["category"], "num", sort_key="category"),
            Column(cols["group"], "num", sort_key="group"),
            Column(cols["defaultDisplay"], sort_key="is_default_display"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
            }
            for record in parse_itemimprovementsource_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.stones", count=len(records))
        rows = [
            [
                e(r["item_id"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name") if r["item_name"] else e(r["item_id"]),
                e(r["category"]),
                e(r["group"]),
                flag_cell(r["is_default_display"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
