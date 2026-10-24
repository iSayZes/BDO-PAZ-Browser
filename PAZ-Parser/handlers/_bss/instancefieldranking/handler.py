"""instancefieldranking.bss preview handler: the season rankings of each instance field type."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, text_list_cell
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_instancefieldranking_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAX_SHOWN = 10


class InstanceFieldRankingHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["instanceFieldType"], "num", sort_key="instance_field_type"),
            Column(labels["rankingCount"], "num", sort_key="ranking_count"),
            Column(labels["rankings"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_instancefieldranking_records(data)

    def cells(self, record: dict) -> list[str]:
        rankings = record["ranking_idxs"]
        return [
            e(record["instance_field_type"]),
            e(record["ranking_count"]),
            text_list_cell(rankings, _MAX_SHOWN) if rankings else _EMPTY,
        ]
