"""itemeffectchange.dbss preview handler: the model of each item mesh per enhancement level."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_itemeffectchange_records, parse_itemeffectchangeoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


def item_effect_change_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("mesh_key", "meshKey"),
            OffsetColumn("enchant_level", "enchantLevel"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_itemeffectchangeoffset_records,
    )


class ItemEffectChangeHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["meshKey"], "num", sort_key="mesh_key"),
            Column(labels["enchantLevel"], "num", sort_key="enchant_level"),
            Column(labels["levels"], "num", sort_key="entry_count"),
            Column(labels["model"], sort_key="mesh_file"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_itemeffectchange_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["mesh_key"]),
            e(record["enchant_level"]),
            e(record["entry_count"]),
            e(record["mesh_file"]),
        ]
