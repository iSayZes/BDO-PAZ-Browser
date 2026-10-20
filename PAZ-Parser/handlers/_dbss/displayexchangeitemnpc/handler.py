"""displayexchangeitemnpc.dbss preview handler: the item exchanges each NPC dialog lists, in file order."""
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
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.quest.dialog import dialog_cell, dialog_key, dialog_name
from .parser import FILE_NAME, parse_displayexchangeitemnpc_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def display_exchange_item_npc_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("dialog_key", "dialogKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "dialog_key", "data_offset", "data_size"),
    )


def _exchange_keys_text(keys: list[int]) -> str:
    """The `itemexchangebynpc.dbss` keys in list order, as `3, 4, 182`."""
    return ", ".join(str(key) for key in keys)


class DisplayExchangeItemNpcHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["npcId"], "num", sort_key="npc_character_key"),
            Column(cols["npcName"], sort_key="npc_name"),
            Column(cols["dialog"], "num", sort_key="dialog_index"),
            Column(cols["dialogName"], sort_key="dialog_name"),
            Column(cols["exchangeCount"], "num", sort_key="item_exchange_count"),
            Column(cols["exchangeKeys"], sort_key="item_exchange_keys_text"),
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
            records = parse_displayexchangeitemnpc_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "npc_name": character_name(record["npc_character_key"]),
                "has_character_row": has_character_row(row_ids, record["npc_character_key"]),
                "dialog_key": dialog_key(record["npc_character_key"], record["dialog_index"]),
                "dialog_name": dialog_name(record["npc_character_key"], record["dialog_index"]),
                "item_exchange_keys_text": _exchange_keys_text(record["item_exchange_keys"]),
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
                character_key_cell(r["npc_character_key"], r["has_character_row"]),
                e(r["npc_name"] or _EMPTY),
                dialog_cell(r["dialog_key"], str(r["dialog_index"])),
                e(r["dialog_name"] or _EMPTY),
                e(r["item_exchange_count"]),
                e(r["item_exchange_keys_text"]),
            ]
            for r in records[start : start + page_size]
        ]
        npc_count = len({r["npc_character_key"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), npc_count=npc_count)
        return table(meta, self._columns(), rows)
