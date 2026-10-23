"""experiencedata.bss preview handler: one row per first-experience trigger.

The rows have no key; the Row column is the place in the file.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, flag_cell
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_experiencedata_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class ExperienceDataBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["row"], "num", sort_key="row"),
            Column(labels["onceCondition"], sort_key="once_condition"),
            Column(labels["constantCondition"], sort_key="constant_condition"),
            Column(labels["execute"], sort_key="execute"),
            Column(labels["repeat"], sort_key="repeat"),
            Column(labels["deleteCondition"], sort_key="delete_condition"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_experiencedata_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["row"]),
            e(record["once_condition"] or _EMPTY),
            e(record["constant_condition"] or _EMPTY),
            e(record["execute"] or _EMPTY),
            flag_cell(bool(record["repeat"])),
            e(record["delete_condition"] or _EMPTY),
        ]
