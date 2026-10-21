"""instancefieldcommonlimitentertime.bss preview handler: the entries of each game service."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, GAME_SERVICE_TYPES, parse_instancefieldcommonlimitentertime_records


_LANG_DIR = Path(__file__).parent / "lang"


class InstanceFieldCommonLimitEnterTimeHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["serviceType"], "num", sort_key="service_type"),
            Column(labels["service"], sort_key="service_name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "service_name": GAME_SERVICE_TYPES.get(record["service_type"], "")}
            for record in parse_instancefieldcommonlimitentertime_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [e(record["service_type"]), e(record["service_name"] or "-")]
