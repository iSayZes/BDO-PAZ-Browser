"""sequencedatatable.bss preview handler: one row per cutscene start.

The region name is LOC type 17 of the region key. The file name stays a
path; the `.pas` cutscene and the `sequence/` files it names have no handler.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from _common.town import town_name
from .parser import FILE_NAME, parse_sequencedatatable_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class SequenceDataTableBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["cutsceneFile"], sort_key="cutscene_file_name"),
            Column(labels["regionKey"], "num", sort_key="region_key"),
            Column(labels["region"], sort_key="region_name"),
            Column(labels["startCondition"], sort_key="start_condition"),
            Column(labels["startExecute"], sort_key="start_execute"),
            Column(labels["endExecute"], sort_key="end_execute"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "region_name": town_name(record["region_key"])}
            for record in parse_sequencedatatable_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["cutscene_file_name"]),
            e(record["region_key"]),
            e(record["region_name"] or _EMPTY),
            e(record["start_condition"] or _EMPTY),
            e(record["start_execute"] or _EMPTY),
            e(record["end_execute"] or _EMPTY),
        ]
