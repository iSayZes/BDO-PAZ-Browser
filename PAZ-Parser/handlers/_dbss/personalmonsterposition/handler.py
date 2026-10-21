"""personalmonsterposition.dbss preview handler: the Dark Rift boss spawn points."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import (
    FILE_NAME,
    KEY_FIELD,
    parse_personalmonsterposition_records,
    parse_personalmonsterpositionoffset_rows,
)


_LANG_DIR = Path(__file__).parent / "lang"
_AXES = ("x", "y", "z")


def personal_monster_position_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(
        _LANG_DIR, parse_personalmonsterpositionoffset_rows, KEY_FIELD, "positionIndex"
    )


class PersonalMonsterPositionHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["positionIndex"], "num", sort_key=KEY_FIELD),
            *(Column(labels[axis], "num", sort_key=axis) for axis in _AXES),
            Column(labels["spawnDistance"], "num", sort_key="spawn_distance"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_personalmonsterposition_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            *(e(f"{record[axis]:,.0f}") for axis in _AXES),
            e(f"{record['spawn_distance']:,.0f}"),
        ]
