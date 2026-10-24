"""worldmapdecostaticstatusmanager.bss preview handler: each world map decoration model and where it stands."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_worldmapdeco_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_AXES = ("location_x", "location_y", "location_z")


def _number(value: float) -> str:
    """A float with at most two decimals and no trailing zeros (`96.27`, `100`)."""
    return f"{value:,.2f}".rstrip("0").rstrip(".")


class WorldmapDecoBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["decoIndex"], "num", sort_key=KEY_FIELD),
            Column(labels["model"], sort_key="world_map_object_file"),
            Column(labels["locationX"], "num", sort_key="location_x"),
            Column(labels["locationY"], "num", sort_key="location_y"),
            Column(labels["locationZ"], "num", sort_key="location_z"),
            Column(labels["scale"], "num", sort_key="scale"),
            Column(labels["rotation"], "num", sort_key="rotation"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_worldmapdeco_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["world_map_object_file"] or _EMPTY),
            *(e(_number(record[axis])) for axis in _AXES),
            e(_number(record["scale"])),
            e(_number(record["rotation"])),
        ]
