"""itemeffectgroupstaticstatus.bss preview handler: one row per glow effect.

The effect name is the `RESOURCE` sheet text of its string hash (LOC type 37),
as the dye window reads it with `PAGetStringByStringHash`.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.stringtable.parser import RESOURCE_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_name
from _common.row_table import RowTableHandler
from _dbss.dyeingpalette.display import color_cell
from .parser import FILE_NAME, KEY_FIELD, parse_itemeffectgroup_effects


_LANG_DIR = Path(__file__).parent / "lang"
_ONE_ITEM = 1
_EMPTY = "-"


def _effect_record(effect: dict) -> dict:
    dye_item_id = effect["dye_item_id"]
    return {
        **effect,
        # None keeps an effect without LOC text or pigment last in a sort.
        "name_text": ui_hash_text(RESOURCE_SHEET, effect["name"]) or None,
        # The colour text, else the RGB bytes the effects without text keep their colour in.
        "color_hex": f"#{effect['color'] or effect['color_rgb']}",
        "dye_item_name": (item_name(dye_item_id) or str(dye_item_id)) if dye_item_id else None,
    }


class ItemEffectGroupBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemGroupType"], "num", sort_key=KEY_FIELD),
            Column(labels["effectIndex"], "num", sort_key="effect_index"),
            Column(labels["name"], sort_key="name_text"),
            Column(labels["color"], sort_key="color_hex"),
            Column(labels["dyeItem"], sort_key="dye_item_name"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [_effect_record(effect) for effect in parse_itemeffectgroup_effects(data)]

    def cells(self, record: dict) -> list[str]:
        dye_item_id = record["dye_item_id"]
        return [
            e(record[KEY_FIELD]),
            e(record["effect_index"]),
            e(record["name_text"] or _EMPTY),
            color_cell(record["color_hex"]),
            item_key_list_cell([dye_item_id], _ONE_ITEM) if dye_item_id else _EMPTY,
        ]
