"""itemenchantsafety.dbss preview handler: the failstack limits of enhancing, per gear type.

The file has no gear names; the lang files name types 0 to 4 after the
developer comment on the 1784 `Enchant_Safetymode` sheet (see
docs/file-formats/dbss/itemenchantsafety_dbss.md). Type 5 has no name there and
shows a dash.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.rate import rate_percent
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_itemenchantsafety_records, parse_itemenchantsafetyoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def item_enchant_safety_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_itemenchantsafetyoffset_rows, KEY_FIELD, "type")


class ItemEnchantSafetyHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["type"], "num", sort_key="type"),
            Column(labels["gear"], sort_key="gear"),
            Column(labels["minLevel"], "num", sort_key="min_level"),
            Column(labels["maxLevel"], "num", sort_key="max_level"),
            Column(labels["stack"], "num", sort_key="stack"),
            Column(labels["cautionStack"], "num", sort_key="caution_stack"),
            Column(labels["cautionRate"], "num", sort_key="caution_rate"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        gear_names: Mapping[str, str] = load_handler_strings(self.lang, _LANG_DIR)["gear"]
        return [
            {**record, "gear": gear_names.get(str(record["type"]), "")}
            for record in parse_itemenchantsafety_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["type"]),
            e(record["gear"] or _EMPTY),
            e(record["min_level"]),
            e(record["max_level"]),
            e(f"{record['stack']:,}"),
            e(f"{record['caution_stack']:,}"),
            e(rate_percent(record["caution_rate"])),
        ]
