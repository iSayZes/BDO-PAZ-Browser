"""monsterbuffzonegroup.bss preview handler: the structure monsters of each region."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.character import character_name
from _common.html import Column, e, text_list_cell
from _common.row_table import RowTableHandler
from _common.town import town_name
from .parser import FILE_NAME, parse_monsterbuffzonegroup_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAX_SHOWN = 10


def _character_text(character_key: int) -> str:
    """`Olun's Golem (21249)`, or the bare key without a LOC name."""
    name = character_name(character_key)
    return f"{name} ({character_key})" if name else str(character_key)


def _display_fields(record: dict) -> dict:
    entries = record["entries"]
    return {
        # LOC type 17 is the region name; the town names are region names too.
        "region_name": town_name(record["region_key"]) or None,
        "structures": [_character_text(entry["character_key"]) for entry in entries],
        # The used slots only; unused ones hold 0 from client 2765 on.
        "listed_characters": [key for entry in entries for key in entry["character_keys"] if key],
    }


class MonsterBuffZoneGroupHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["regionKey"], "num", sort_key="region_key"),
            Column(labels["region"], sort_key="region_name"),
            Column(labels["structures"]),
            Column(labels["characters"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [{**record, **_display_fields(record)} for record in parse_monsterbuffzonegroup_records(data)]

    def cells(self, record: dict) -> list[str]:
        listed = record["listed_characters"]
        return [
            e(record["region_key"]),
            e(record["region_name"] or _EMPTY),
            text_list_cell(record["structures"], _MAX_SHOWN) if record["structures"] else _EMPTY,
            text_list_cell(listed, _MAX_SHOWN) if listed else _EMPTY,
        ]
