"""itemnakmessage.dbss preview handler: the item and the two message lines shown when someone finds it.

The message keys are `GAME` sheet keys of `stringtable.bss`; the text comes
from LOC type 37 under the key's hash, the same way `stringtable.bss` keys
resolve elsewhere. A key with no text shows the key itself.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_tagged
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_pabr_u32_offset_rows
from _common.row_table import RowTableHandler
from _common.string_hash import key_hash
from .parser import FILE_NAME, parse_itemnakmessage_records


_LANG_DIR = Path(__file__).parent / "lang"


def item_nak_message_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_pabr_u32_offset_rows, "item_key", "itemKey")


def _message_tagged(key: str) -> str:
    """The `GAME` sheet text of a message key with its colour tags, else the key."""
    return ui_hash_tagged(GAME_SHEET, key_hash(key)) or key


class ItemNakMessageHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemKey"], "num", sort_key="item_key"),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["mainMessage"], sort_key="main_message"),
            Column(labels["subMessage"], sort_key="sub_message"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "item_name": item_key_text(record["item_key"]),
                **pa_fields("main_message", _message_tagged(record["main_message_key"])),
                **pa_fields("sub_message", _message_tagged(record["sub_message_key"])),
            }
            for record in parse_itemnakmessage_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["item_key"]),
            item_key_list_cell([record["item_key"]], 1),
            pa_cell(record, "main_message"),
            pa_cell(record, "sub_message"),
        ]
