"""employeejobslotstaticstatus.bss preview handler: the sailor preset job slots of each ship."""
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
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_employeejobslot_file


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class EmployeeJobSlotHandler(RowTableHandler):
    """One record per ship; the entry table after the ships has no key to join and stays out."""

    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterKey"], "num", sort_key="character_key"),
            Column(labels["ship"], sort_key="name"),
            Column(labels["jobSlots"]),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "name": character_name(record["character_key"]) or None,
                "has_character_row": has_character_row(row_ids, record["character_key"]),
            }
            for record in parse_employeejobslot_file(data).rows
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record["character_key"], record["has_character_row"]),
            e(record["name"] or _EMPTY),
            e(", ".join(str(count) for count in record["job_slot_counts"])),
        ]
