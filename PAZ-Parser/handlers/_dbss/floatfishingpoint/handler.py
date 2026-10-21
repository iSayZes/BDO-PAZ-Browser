"""floatfishingpoint.dbss preview handler: each floating fishing point with its drop group and character."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.character import character_name
from _common.html import Column, e, record_link
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_floatfishingpoint_records, parse_floatfishingpointoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
FLOATFISHING_PATH = "gamecommondata/binary/floatfishing.dbss"
_POSITION_FIELDS = ("start_position_x", "start_position_y", "start_position_z", "end_position_x", "end_position_z")
_POSITION_LABELS = ("startX", "startY", "startZ", "endX", "endZ")


def float_fishing_point_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_floatfishingpointoffset_rows, KEY_FIELD, "pointKey")


def position_text(value: float) -> str:
    """A world coordinate to the whole unit, `-91,097`."""
    return f"{round(value):,}"


class FloatFishingPointHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["pointKey"], "num", sort_key=KEY_FIELD),
            Column(labels["pointSize"], "num", sort_key="point_size"),
            *(
                Column(labels[label], "num", sort_key=field)
                for field, label in zip(_POSITION_FIELDS, _POSITION_LABELS, strict=True)
            ),
            Column(labels["fishingGroup"], "num", sort_key="fishing_group_key"),
            Column(labels["characterKey"], "num", sort_key="spawn_character_key"),
            Column(labels["character"], sort_key="spawn_character_name"),
            Column(labels["actionIndex"], "num", sort_key="spawn_action_index"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "spawn_character_name": character_name(record["spawn_character_key"])}
            for record in parse_floatfishingpoint_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        group_key = record["fishing_group_key"]
        return [
            e(record[KEY_FIELD]),
            e(f"{record['point_size']:,}"),
            *(e(position_text(record[field])) for field in _POSITION_FIELDS),
            record_link(str(group_key), FLOATFISHING_PATH, "fishing_group_key", group_key, "record-link"),
            e(record["spawn_character_key"]),
            e(record["spawn_character_name"] or "-"),
            e(record["spawn_action_index"]),
        ]
