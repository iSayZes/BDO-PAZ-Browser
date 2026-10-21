"""employeeclientspawn.dbss preview handler: the sailor positions on each ship."""
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
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_employeeclientspawn_records, parse_employeeclientspawnoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _number_text(value: float) -> str:
    """`-1000.0` -> `-1,000`, `12.5` -> `12.5`."""
    return f"{value:,g}"


def employee_client_spawn_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_key", "characterKey"),
            OffsetColumn("index", "index"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        parse_employeeclientspawnoffset_records,
    )


class EmployeeClientSpawnHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterKey"], "num", sort_key="character_key"),
            Column(labels["ship"], sort_key="character_name"),
            Column(labels["index"], "num", sort_key="index"),
            Column(labels["x"], "num", sort_key="spawn_position_x"),
            Column(labels["y"], "num", sort_key="spawn_position_y"),
            Column(labels["z"], "num", sort_key="spawn_position_z"),
            Column(labels["direction"], "num", sort_key="spawn_direction"),
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
            }
            for record in parse_employeeclientspawn_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record["character_key"], record["has_character_row"]),
            e(record["character_name"] or _EMPTY),
            e(record["index"]),
            e(_number_text(record["spawn_position_x"])),
            e(_number_text(record["spawn_position_y"])),
            e(_number_text(record["spawn_position_z"])),
            e(_number_text(record["spawn_direction"])),
        ]
