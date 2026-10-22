"""cashproduct_instant.bss preview handler: the cost to finish a task at once, per task type and remaining time."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.enum_name import enum_name
from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, INSTANT_TYPE_NAMES, parse_cashproduct_instant_records


_LANG_DIR = Path(__file__).parent / "lang"


class CashProductInstantHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["instantType"], "num", sort_key="instant_type"),
            Column(labels["instantTypeName"], sort_key="instant_type_name"),
            Column(labels["minute"], "num", sort_key="minute"),
            Column(labels["cost"], "num", sort_key="pearl_count"),
        ]

    def default_sort(self) -> TableSort | None:
        # File order: each task type, its remaining times rising; two fields give it.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "instant_type_name": enum_name(INSTANT_TYPE_NAMES, record["instant_type"])}
            for record in parse_cashproduct_instant_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["instant_type"]),
            e(record["instant_type_name"]),
            e(f"{record['minute']:,}"),
            e(f"{record['pearl_count']:,}"),
        ]
