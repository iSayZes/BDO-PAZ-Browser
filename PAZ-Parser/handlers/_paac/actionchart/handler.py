"""`*.paac` preview handler: one row per action of a chart, package by package.

Action names come from the element of an action or, for a class chart, from
the string table of `pc/pc_actionchartpackagepcraw.paac`: the action keys
are lookup3 hashes of the names. On a Layout 1 (client 1784) class chart each
action also takes the shared element its Element Link points at, with the
element's animation, skill and stamina fields. The layout is the doc's
Layout 2 (client 3258 and later) or Layout 1 (client 1784), whichever reads
the file to its end (docs/file-formats/other/actionchart_paac.md).
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.pabr_strings import read_string_table
from _common.row_table import RowTableHandler
from ..layouts import LAYOUT_1
from ..parser import SHARED_TABLES_NAME, Chart, parse_chart, parse_shared_tables
from ..records import chart_records, hash_cell, text_cell

_LANG_DIR = Path(__file__).parent / "lang"
_CHART_ROOT = "character/binaryactionchart/"
# The class charts keep their action names in the shared tables file only.
_SHARED_TABLES_PATH = f"{_CHART_ROOT}pc/{SHARED_TABLES_NAME}"
_EMPTY = "-"


def _shared_names_and_elements(chart: Chart, shared: bytes) -> tuple[list[str], dict[int, Sequence[dict]]]:
    """The shared tables file's strings and, when it reads whole, its element groups.

    Only Layout 1 reads the shared tables file whole; for a Layout 2 chart, or
    a Layout 1 file that does not read, the string table still names the actions.
    """
    if chart.layout == LAYOUT_1.number:
        try:
            tables = parse_shared_tables(shared)
            return tables.strings, {group.key: group.elements for group in tables.groups}
        except ValueError:
            pass
    return read_string_table(shared), {}


def _count_cell(record: dict, field: str) -> str:
    """A whole number that is 0 when the action has none (skill, stamina cost)."""
    value = record.get(field)
    return e(str(value)) if value else _EMPTY


class ActionChartHandler(RowTableHandler):
    file_name = "action chart"
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["actionHash"], "num", sort_key="action_hash"),
            Column(labels["action"], sort_key="action_name"),
            Column(labels["package"], sort_key="package_path"),
            Column(labels["animation"], sort_key="animation"),
            Column(labels["skill"], "num", sort_key="skill_no"),
            Column(labels["staminaCost"], "num", sort_key="apply_sp"),
            Column(labels["staminaUse"], sort_key="sp_use_type"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        path = entry.internal_path.replace("\\", "/").lower()
        return [_SHARED_TABLES_PATH] if path.startswith(f"{_CHART_ROOT}pc/") else []

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        chart = parse_chart(data, self.file_name)
        shared = companions.get(SHARED_TABLES_NAME)
        if not shared:
            return chart_records(chart, [])
        names, element_groups = _shared_names_and_elements(chart, shared)
        return chart_records(chart, names, element_groups)

    def _stamina_use_cell(self, record: dict) -> str:
        value = record.get("sp_use_type")
        if value is None:
            return _EMPTY
        uses: Mapping[str, str] = load_handler_strings(self.lang, self.lang_dir).get("staminaUse", {})
        return e(uses.get(str(value), str(value)))

    def cells(self, record: dict) -> list[str]:
        return [
            e(hash_cell(record["action_hash"])),
            text_cell(record["action_name"]),
            text_cell(record["package_path"]),
            text_cell(record["animation"]),
            _count_cell(record, "skill_no"),
            _count_cell(record, "apply_sp"),
            self._stamina_use_cell(record),
        ]
