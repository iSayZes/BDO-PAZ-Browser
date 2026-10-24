"""videotriggerdata.bss preview handler: one row per video trigger.

The video stays a name: the `.bk2` files under `ui_movie/` have no handler.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.sequence_scripts.display import EMPTY, contents_group_key, position_text, radius_text
from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_videotriggerdata_records


_LANG_DIR = Path(__file__).parent / "lang"


class VideoTriggerDataBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["video"], sort_key="video_name"),
            Column(labels["contentsGroup"], "num", sort_key="contents_group_key"),
            Column(labels["position"], sort_key="position_text"),
            Column(labels["radius"], "num", sort_key="radius"),
            Column(labels["startCondition"], sort_key="start_condition"),
            Column(labels["startExecute"], sort_key="start_execute"),
            Column(labels["endExecute"], sort_key="end_execute"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "contents_group_key": contents_group_key(record["contents_group_open"]),
                "position_text": position_text(record["position"]),
            }
            for record in parse_videotriggerdata_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["video_name"]),
            e(record["contents_group_open"] or EMPTY),
            e(record["position_text"]),
            e(radius_text(record["radius"])),
            e(record["start_condition"] or EMPTY),
            e(record["start_execute"] or EMPTY),
            e(record["end_execute"] or EMPTY),
        ]
