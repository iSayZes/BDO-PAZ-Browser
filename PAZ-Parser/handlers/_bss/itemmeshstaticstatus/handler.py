"""itemmeshstaticstatus.bss preview handler: the model and materials of each item mesh.

Each row shows the items that wear its mesh, from the `MESH_KEY_ITEMS`
lookup index (the `itemenchant.dbss` class entries turned around).
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.linked_items import item_list_cell, item_list_fields, linked_item_ids
from _common.lookup_index import IndexKind
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_itemmesh_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_NUMBER_FIELDS = ("weapon_material", "armor_material", "adult", "effects_change_type")


def _with_items(record: dict) -> dict:
    """The row plus the items that wear its mesh; an empty effect file becomes None (sorts last)."""
    return {
        **record,
        "effect_file": record["effect_file"] or None,
        **item_list_fields(linked_item_ids(IndexKind.MESH_KEY_ITEMS, [record[KEY_FIELD]])),
    }


class ItemMeshStaticStatusBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["meshKey"], "num", sort_key=KEY_FIELD),
            Column(labels["items"], sort_key="item_count"),
            Column(labels["model"], sort_key="mesh_file"),
            Column(labels["effectFile"], sort_key="effect_file"),
            Column(labels["weaponMaterial"], "num", sort_key="weapon_material"),
            Column(labels["armorMaterial"], "num", sort_key="armor_material"),
            Column(labels["adult"], "num", sort_key="adult"),
            Column(labels["effectsChange"], "num", sort_key="effects_change_type"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [_with_items(record) for record in parse_itemmesh_records(data)]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            item_list_cell(record["item_ids"]),
            e(record["mesh_file"]),
            e(record["effect_file"] or _EMPTY),
            *(e(record[field]) for field in _NUMBER_FIELDS),
        ]
