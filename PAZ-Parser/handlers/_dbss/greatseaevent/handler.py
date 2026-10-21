"""greatseaevent.dbss preview handler: the Great Ocean event result messages per group."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_greatseaevent_records, parse_greatseaeventoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


def great_sea_event_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("group_key", "groupKey"),
            OffsetColumn("select_index", "selectIndex"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        parse_greatseaeventoffset_records,
    )


class GreatSeaEventHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["groupKey"], "num", sort_key="group_key"),
            Column(labels["selectIndex"], "num", sort_key="select_index"),
            Column(labels["result"], sort_key="result_string_kr"),
            Column(labels["imagePath"], sort_key="image_path"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_greatseaevent_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["group_key"]),
            e(record["select_index"]),
            e(record["result_string_kr"]),
            e(record["image_path"]),
        ]
