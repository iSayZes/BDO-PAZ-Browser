"""pcactionpackagename.bss preview handler: one row per action chart package of a class.

Empty cells get no row. The class name is LOC type 21, the section label
comes from the handler's lang file.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import SORT_ASC, TableSort

from _common.class_type import class_name
from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_pcactionpackagename


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class PcActionPackageNameBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["classType"], "num", sort_key="class_type"),
            Column(labels["className"], sort_key="class_name"),
            Column(labels["section"], sort_key="section_name"),
            Column(labels["equipType"], "num", sort_key="equip_type"),
            Column(labels["vehicleType"], sort_key="vehicle_name"),
            Column(labels["package"], sort_key="package"),
        ]

    def default_sort(self) -> TableSort | None:
        # Class type order with each class's packages in file order.
        return TableSort("class_type", SORT_ASC)

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        sections = load_handler_strings(self.lang, _LANG_DIR)["sections"]
        return [
            {
                **record,
                "class_name": class_name(record["class_type"]),
                "section_name": sections[record["section"]],
            }
            for record in parse_pcactionpackagename(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["class_type"]),
            e(record["class_name"]),
            e(record["section_name"]),
            _optional(record["equip_type"]),
            _optional(record["vehicle_name"]),
            e(record["package"]),
        ]


def _optional(value: int | str | None) -> str:
    return _EMPTY if value is None else e(value)
