"""houseinfoviewposition.dbss preview handler: a position and facing per house and house use type."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.enum_name import enum_name
from _common.html import Column, e
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from _dbss.guildhouseinfo.house_rows import house_cell, house_fields, house_row_companions, house_rows
from _dbss.houseinforeceipe.house_enums import HOUSE_USE_TYPE_NAMES
from .parser import (
    FILE_NAME,
    KEY_FIELD,
    parse_houseinfoviewposition_records,
    parse_houseinfoviewpositionoffset_records,
    yaw_degrees,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def house_info_view_position_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn(KEY_FIELD, "houseKey"),
            OffsetColumn("house_group_type", "useType"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        parse_houseinfoviewpositionoffset_records,
    )


def _position_text(position: list[float]) -> str:
    return ", ".join(f"{value:,.0f}" for value in position)


class HouseInfoViewPositionHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return house_row_companions(entry.internal_path)

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["houseKey"], "num", sort_key=KEY_FIELD),
            Column(labels["house"], sort_key="name"),
            Column(labels["town"], sort_key="town"),
            Column(labels["useType"], sort_key="house_group_type_name"),
            Column(labels["position"], sort_key="position_text"),
            Column(labels["yaw"], "num", sort_key="yaw"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        rows = house_rows(companions)
        records = []
        for record in parse_houseinfoviewposition_records(data):
            records.append({
                **record,
                "name": character_name(record[KEY_FIELD]),
                **house_fields(rows.get(record[KEY_FIELD])),
                "house_group_type_name": enum_name(HOUSE_USE_TYPE_NAMES, record["house_group_type"]),
                "position_text": _position_text(record["position"]),
                "yaw": round(yaw_degrees(record["direction"]), 1),
            })
        return records

    def cells(self, record: dict) -> list[str]:
        return [
            house_cell(str(record[KEY_FIELD]), record[KEY_FIELD], record["house_path"]),
            e(record["name"] or _EMPTY),
            e(record["town"] or _EMPTY),
            e(record["house_group_type_name"]),
            e(record["position_text"]),
            e(f'{record["yaw"]:g}'),
        ]
