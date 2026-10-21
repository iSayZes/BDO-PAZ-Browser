"""simplesequence.bss preview handler: the row keys."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_simplesequence_records


_LANG_DIR = Path(__file__).parent / "lang"


class SimpleSequenceHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [Column(labels["key"], "num", sort_key="key")]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_simplesequence_records(data)

    def cells(self, record: dict) -> list[str]:
        return [e(record["key"])]
