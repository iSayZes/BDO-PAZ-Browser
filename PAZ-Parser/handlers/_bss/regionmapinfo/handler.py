"""regionmapinfo.bss preview handler: each map bitmap with its type, sector rectangle and image."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.enum_name import enum_name
from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_regionmapinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
# `gc::BitmapMapInfoType` of the 2016 client, without its prefix; later values show as numbers.
MAP_TYPE_NAMES = ("Region", "Fishing", "Water", "Siege", "VillageSiege", "Underground")
_AXES = ("x", "y")


def _sector_range(record: dict, axis: str) -> str:
    """`-160..112`: the map's sector span on one axis."""
    return f"{record[f'sector_start_{axis}']}..{record[f'sector_end_{axis}']}"


class RegionMapInfoBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["mapIndex"], "num", sort_key=KEY_FIELD),
            Column(labels["image"], sort_key="image_path"),
            Column(labels["type"], sort_key="map_type"),
            # Each span sorts by its lower bound.
            *(Column(labels[f"sector{axis.upper()}"], "num", sort_key=f"sector_start_{axis}") for axis in _AXES),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "map_type_name": enum_name(MAP_TYPE_NAMES, record["map_type"])}
            for record in parse_regionmapinfo_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["image_path"]),
            e(record["map_type_name"]),
            *(e(_sector_range(record, axis)) for axis in _AXES),
        ]
