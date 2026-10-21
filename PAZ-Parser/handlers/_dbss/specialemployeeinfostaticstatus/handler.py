"""specialemployeeinfostaticstatus.dbss preview handler: the special sailors hired with an item."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e
from _common.item_key import item_count_list_cell, item_count_text
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.rate import rate_percent
from _common.row_table import RowTableHandler
from .parser import (
    FILE_NAME,
    KEY_FIELD,
    parse_specialemployeeinfostaticstatus_records,
    parse_specialemployeeinfostaticstatusoffset_rows,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def special_employee_info_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_specialemployeeinfostaticstatusoffset_rows, KEY_FIELD, "type")


class SpecialEmployeeInfoHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["type"], "num", sort_key="type"),
            Column(labels["category"], "num", sort_key="category"),
            Column(labels["characterKey"], "num", sort_key="character_key"),
            Column(labels["name"], sort_key="character_name"),
            Column(labels["needItem"], sort_key="need_item"),
            Column(labels["successRate"], "num", sort_key="employ_success_rate"),
            Column(labels["successWord"], sort_key="employ_success_word_kr"),
            Column(labels["failWord"], sort_key="employ_fail_word_kr"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "character_name": character_name(record["character_key"]),
                "has_character_row": has_character_row(row_ids, record["character_key"]),
                "need_item": item_count_text(record["need_item_key"], record["need_item_count"]),
            }
            for record in parse_specialemployeeinfostaticstatus_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["type"]),
            e(record["category"]),
            character_key_cell(record["character_key"], record["has_character_row"]),
            e(record["character_name"] or _EMPTY),
            item_count_list_cell([(record["need_item_key"], record["need_item_count"])]),
            e(rate_percent(record["employ_success_rate"])),
            e(record["employ_success_word_kr"] or _EMPTY),
            e(record["employ_fail_word_kr"] or _EMPTY),
        ]
