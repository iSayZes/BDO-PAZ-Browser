"""`actionchartheader.paach` preview handler: one row per action chart entry.

The key is the lookup3 hash of the chart path relative to
`character/binaryactionchart/`, lower case, without `.paac`; the flag bytes
have no known meaning yet, so they stay on the record without a column.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from ..records import hash_cell
from .parser import FILE_NAME, parse_actionchartheader

_LANG_DIR = Path(__file__).parent / "lang"


class ActionChartHeaderHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["chartHash"], "num", sort_key="chart_hash"),
            Column(labels["flagCount"], "num", sort_key="flag_count"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_actionchartheader(data)

    def cells(self, record: dict) -> list[str]:
        return [e(hash_cell(record["chart_hash"])), e(record["flag_count"])]
