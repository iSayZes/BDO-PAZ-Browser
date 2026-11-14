"""`*.paac` preview handler: one row per action of a chart, package by package.

Action names come from the element of an action or, for a class chart, from
the string table of `pc/pc_actionchartpackagepcraw.paac`: the action keys
are lookup3 hashes of the names. The layout is the doc's Layout 2 (client
3258 and later) or Layout 1 (client 1784), whichever reads the file to its
end (docs/file-formats/other/actionchart_paac.md).
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e
from _common.pabr_strings import read_string_table
from _common.row_table import RowTableHandler
from ..parser import SHARED_TABLES_NAME, parse_chart
from ..records import chart_records, hash_cell, text_cell

_LANG_DIR = Path(__file__).parent / "lang"
_CHART_ROOT = "character/binaryactionchart/"
# The class charts keep their action names in the shared tables file only.
_SHARED_TABLES_PATH = f"{_CHART_ROOT}pc/{SHARED_TABLES_NAME}"


class ActionChartHandler(RowTableHandler):
    file_name = "action chart"
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["actionHash"], "num", sort_key="action_hash"),
            Column(labels["action"], sort_key="action_name"),
            Column(labels["package"], sort_key="package_path"),
            Column(labels["animation"], sort_key="animation"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        path = entry.internal_path.replace("\\", "/").lower()
        return [_SHARED_TABLES_PATH] if path.startswith(f"{_CHART_ROOT}pc/") else []

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        shared = companions.get(SHARED_TABLES_NAME)
        extra_names = read_string_table(shared) if shared else []
        return chart_records(parse_chart(data, self.file_name), extra_names)

    def cells(self, record: dict) -> list[str]:
        return [
            e(hash_cell(record["action_hash"])),
            text_cell(record["action_name"]),
            text_cell(record["package_path"]),
            text_cell(record["animation"]),
        ]
