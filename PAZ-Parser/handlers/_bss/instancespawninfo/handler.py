"""instancespawninfo.bss preview handler: the private monster zones of the Personal Field window."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.binary import whole_float
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_instancespawninfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_CM_PER_M = 100
_AXES = ("x", "y", "z")


def _display_fields(record: dict) -> dict:
    item_key = record["enter_item_key"] or None
    return {
        "offense": whole_float(record["offense_point"]),
        "enter_item_key": item_key,
        "enter_item": item_key_text(item_key) if item_key else None,
        "radius_m": record["radius"] / _CM_PER_M,
    }


class InstanceSpawnInfoHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["key"], "num", sort_key="key"),
            Column(labels["area"], sort_key="area_name_kr"),
            Column(labels["offense"], "num", sort_key="offense"),
            Column(labels["enterItem"], sort_key="enter_item"),
            Column(labels["enterType"], "num", sort_key="enter_type"),
            *(Column(labels[axis], "num", sort_key=axis) for axis in _AXES),
            Column(labels["radius"], "num", sort_key="radius_m"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [{**record, **_display_fields(record)} for record in parse_instancespawninfo_records(data)]

    def cells(self, record: dict) -> list[str]:
        item_key = record["enter_item_key"]
        return [
            e(record["key"]),
            e(record["area_name_kr"]),
            e(record["offense"]),
            item_key_list_cell([item_key], 1) if item_key else _EMPTY,
            e(record["enter_type"]),
            *(e(f"{record[axis]:,.0f}") for axis in _AXES),
            e(f"{record['radius_m']:,.0f}"),
        ]
