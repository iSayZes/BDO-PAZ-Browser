"""itemeffectchange.dbss preview handler: the model of each item mesh per enhancement level.

Each entry shows the items that wear its mesh, from the `MESH_KEY_ITEMS`
lookup index (the `itemenchant.dbss` class entries turned around).
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.linked_items import item_list_cell, item_list_fields, linked_item_ids
from _common.lookup_index import IndexKind
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


def _with_items(records: list[dict]) -> list[dict]:
    """Each entry plus the items that wear its mesh; every entry of a group shares them."""
    items_by_mesh: dict[int, dict] = {}
    for record in records:
        mesh_key = record["mesh_key"]
        if mesh_key not in items_by_mesh:
            items_by_mesh[mesh_key] = item_list_fields(linked_item_ids(IndexKind.MESH_KEY_ITEMS, [mesh_key]))
    return [{**record, **items_by_mesh[record["mesh_key"]]} for record in records]


class ItemEffectChangeHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["meshKey"], "num", sort_key="mesh_key"),
            Column(labels["items"], sort_key="item_count"),
            Column(labels["enchantLevel"], "num", sort_key="enchant_level"),
            Column(labels["levels"], "num", sort_key="entry_count"),
            Column(labels["model"], sort_key="mesh_file"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return _with_items(parse_itemeffectchange_records(data))

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["mesh_key"]),
            item_list_cell(record["item_ids"]),
            e(record["enchant_level"]),
            e(record["entry_count"]),
            e(record["mesh_file"]),
        ]
