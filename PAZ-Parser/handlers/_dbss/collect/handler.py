"""collect.dbss preview handler: gathering rules per Collect character in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, error, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from .parser import EMPTY_TOOL_TYPE, FILE_NAME, parse_collect_records
from .tools import tool_display_name


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_SLOTS_SHOWN = 3


def collect_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_key", "characterId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_key", "data_offset", "data_size"),
    )


def _tool_texts(tool_types: list[int], drop_keys: list[int]) -> list[str]:
    """Each filled slot as "tool (drop group)"; the drop groups are in no client file."""
    return [
        f"{tool_display_name(tool_type)} ({drop_key})"
        for tool_type, drop_key in zip(tool_types, drop_keys)
        if tool_type != EMPTY_TOOL_TYPE
    ]


def _float_text(value: float) -> str:
    return f"{value:g}"


class CollectHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="character_name"),
            Column(cols["productType"], sort_key="product_type_name"),
            # A list column: it would only sort by its string form.
            Column(cols["tools"]),
            Column(cols["productDrop"], "num", sort_key="product_item_drop_key"),
            Column(cols["productTime"], "num", sort_key="product_time"),
            Column(cols["productHp"], "num", sort_key="product_hp"),
            Column(cols["productDecreaseHp"], "num", sort_key="product_decrease_hp"),
            Column(cols["actionPoint"], "num", sort_key="action_point"),
            Column(cols["spawnDelay"], "num", sort_key="spawn_delay_time"),
            Column(cols["spawnVariable"], "num", sort_key="spawn_variable_time"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_collect_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        product_types = load_handler_strings(self.lang, _LANG_DIR)["productTypes"]
        return [
            {
                **record,
                "character_name": character_name(record["character_key"]),
                "has_character_row": has_character_row(row_ids, record["character_key"]),
                "product_type_name": product_types.get(
                    str(record["product_data_type"]), str(record["product_data_type"])
                ),
                # Tools as text, so tab search and CSV export see them.
                "tools": _tool_texts(record["collect_tool_types"], record["collect_item_drop_keys"]),
            }
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                character_key_cell(r["character_key"], r["has_character_row"]),
                e(r["character_name"] or _EMPTY),
                e(r["product_type_name"]),
                text_list_cell(r["tools"], _SLOTS_SHOWN) or _EMPTY,
                e(r["product_item_drop_key"]),
                e(f"{r['product_time']:,}"),
                e(_float_text(r["product_hp"])),
                e(_float_text(r["product_decrease_hp"])),
                e(r["action_point"]),
                e(f"{r['spawn_delay_time']:,}"),
                e(f"{r['spawn_variable_time']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
