"""fieldwalkingcameradata.bss preview handler: one row per camera point of each event.

The field of view is stored in radians and shows in degrees, as the source
XML writes it. The region name is LOC type 17 of the region key.
"""

from __future__ import annotations

import math
from collections.abc import Mapping
from pathlib import Path

from _bss.sequence_scripts.display import position_text
from _common.html import Column, e, flag_cell
from _common.row_table import RowTableHandler
from _common.town import town_name
from .parser import FILE_NAME, parse_fieldwalkingcameradata_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _rotation_text(rotation: list[float]) -> str:
    """`-0.1094, -0.7819, -0.1431, 0.5968`: the rotation quaternion, x, y, z, w."""
    return ", ".join(f"{value:.4f}" for value in rotation)


class FieldWalkingCameraDataBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["event"], sort_key="event_name"),
            Column(labels["regionKey"], "num", sort_key="region_key"),
            Column(labels["region"], sort_key="region_name"),
            Column(labels["point"], "num", sort_key="point_index"),
            Column(labels["position"], sort_key="position_text"),
            Column(labels["rotation"], sort_key="rotation_text"),
            Column(labels["fov"], "num", sort_key="fov_degrees"),
            Column(labels["speedOrTime"], "num", sort_key="speed_or_time"),
            Column(labels["speedMode"], sort_key="is_speed_mode"),
            Column(labels["spline"], sort_key="is_spline"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                "event_name_hash": row["event_name_hash"],
                "event_name": row["event_name"],
                "region_key": row["region_key"],
                "region_name": town_name(row["region_key"]),
                "point_count": row["point_count"],
                "unknown_points_00": row["unknown_points_00"],
                "point_index": point_index,
                **point,
                "position_text": position_text(point["position"]),
                "rotation_text": _rotation_text(point["rotation"]),
                "fov_degrees": round(math.degrees(point["fov"]), 2),
            }
            for row in parse_fieldwalkingcameradata_rows(data)
            for point_index, point in enumerate(row["points"])
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["event_name"]),
            e(record["region_key"]),
            e(record["region_name"] or _EMPTY),
            e(record["point_index"]),
            e(record["position_text"]),
            e(record["rotation_text"]),
            e(f"{record['fov_degrees']:g}"),
            e(f"{record['speed_or_time']:g}"),
            flag_cell(bool(record["is_speed_mode"])),
            flag_cell(bool(record["is_spline"])),
        ]
