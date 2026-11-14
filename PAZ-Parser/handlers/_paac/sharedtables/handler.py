"""`pc_actionchartpackagepcraw.paac` preview handler: one row per shared element.

The class charts take their elements from this file. Only Layout 1 (client
1784) reads it whole; the frame events of client 3483's copy are not decoded
yet (docs/file-formats/other/actionchart_paac.md, Open Questions).
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from ..parser import SHARED_TABLES_NAME, parse_shared_tables
from ..records import hash_cell, shared_element_records, text_cell

_LANG_DIR = Path(__file__).parent / "lang"


class SharedTablesHandler(RowTableHandler):
    file_name = SHARED_TABLES_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["groupKey"], "num", sort_key="key"),
            Column(labels["action"], sort_key="action_name"),
            Column(labels["animation"], sort_key="animation"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return shared_element_records(parse_shared_tables(data))

    def cells(self, record: dict) -> list[str]:
        return [e(hash_cell(record["key"])), text_cell(record["action_name"]), text_cell(record["animation"])]
