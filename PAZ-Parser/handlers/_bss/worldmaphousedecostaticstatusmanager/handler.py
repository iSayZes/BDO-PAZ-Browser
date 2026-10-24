"""worldmaphousedecostaticstatusmanager.bss preview handler: the world map model of each guild siege building."""
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
from .parser import FILE_NAME, KEY_FIELD, parse_worldmaphousedeco_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class WorldmapHouseDecoBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterKey"], "num", sort_key=KEY_FIELD),
            Column(labels["building"], sort_key="name"),
            Column(labels["model"], sort_key="world_map_object_file"),
            Column(labels["objectChangeLevel"], "num", sort_key="object_change_level"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "name": character_name(record[KEY_FIELD]),
                "has_character_row": has_character_row(row_ids, record[KEY_FIELD]),
            }
            for record in parse_worldmaphousedeco_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"] or _EMPTY),
            e(record["world_map_object_file"] or _EMPTY),
            e(record["object_change_level"]),
        ]
