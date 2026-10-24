"""innstaticstatus.dbss preview handler: one row per inn room, a house character, with its house and town.

The file stores one row per inn with a list of room keys; the view shows
each room on its own row so the rooms can be searched and sorted.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _dbss.guildhouseinfo.house_rows import HouseRow, house_cell, house_fields, house_row_companions, house_rows
from .parser import FILE_NAME, KEY_FIELD, parse_innstaticstatus_records, parse_innstaticstatusoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
ROOM_FIELD = "character_key"


def inn_static_status_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_innstaticstatusoffset_rows, KEY_FIELD, "innKey")


def _room_record(inn_key: int, room_index: int, character_key: int, house_row: HouseRow | None) -> dict:
    return {
        KEY_FIELD: inn_key,
        "room_index": room_index,
        ROOM_FIELD: character_key,
        "name": character_name(character_key),
        **house_fields(house_row),
    }


class InnStaticStatusHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return house_row_companions(entry.internal_path)

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["innKey"], "num", sort_key=KEY_FIELD),
            Column(labels["roomKey"], "num", sort_key=ROOM_FIELD),
            Column(labels["house"], sort_key="name"),
            Column(labels["town"], sort_key="town"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        rows = house_rows(companions)
        return [
            _room_record(inn[KEY_FIELD], index, room_key, rows.get(room_key))
            for inn in parse_innstaticstatus_records(data)
            for index, room_key in enumerate(inn["room_keys"])
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            house_cell(str(record[ROOM_FIELD]), record[ROOM_FIELD], record["house_path"]),
            e(record["name"] or _EMPTY),
            e(record["town"] or _EMPTY),
        ]
