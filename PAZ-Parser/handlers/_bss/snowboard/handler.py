"""snowboard.bss preview handler: one row per checkpoint of a snowboard course.

The course name is the file's Korean text; the mode shows its
`__eSnowBoardCourseMode` name.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.enum_name import enum_name
from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_checkpoint_records


_LANG_DIR = Path(__file__).parent / "lang"
# __eSnowBoardCourseMode by stored mode: the only Item course is the 스코어 (score)
# course, whose menu tab shows the item ranking (snowboard_bss.md, Course Modes).
COURSE_MODE_NAMES: tuple[str, ...] = ("Item", "Speed")


def course_mode_text(mode: int) -> str:
    """`1 Speed`: a stored mode and its `__eSnowBoardCourseMode` name."""
    name = enum_name(COURSE_MODE_NAMES, mode)
    return name if name == str(mode) else f"{mode} {name}"


class SnowboardBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["courseKey"], "num", sort_key="course_key"),
            Column(labels["course"], sort_key="name_kr"),
            Column(labels["mode"], sort_key="mode"),
            Column(labels["checkpoint"], "num", sort_key="checkpoint_index"),
            Column(labels["nextCheckpoint"], "num", sort_key="next_checkpoint_index"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_checkpoint_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["course_key"]),
            e(record["name_kr"]),
            e(course_mode_text(record["mode"])),
            e(record["checkpoint_index"]),
            e(record["next_checkpoint_index"]),
        ]
