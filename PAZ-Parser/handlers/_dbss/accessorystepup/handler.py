"""accessorystepup.dbss preview handler: one row per accessory step with its materials.

A file row holds an accessory and its five steps; the table shows one row
per step, the accessory at the level the step reaches, so the materials of
each step get a row of their own.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.item_key import item_count_list_cell, item_count_text, item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_accessorystepup_records


_LANG_DIR = Path(__file__).parent / "lang"
_ENCHANT_LEVEL_SHIFT = 24


def _step_records(record: dict) -> list[dict]:
    """One record per step: the step's materials and the accessory at the level it reaches."""
    head = {key: value for key, value in record.items() if key != "steps"}
    records = []
    for step, materials in enumerate(record["steps"]):
        enchant_level = step + 1
        goal_item_key = enchant_level << _ENCHANT_LEVEL_SHIFT | record["item_key"]
        records.append(
            {
                **head,
                "enchant_level": enchant_level,
                "goal_item_key": goal_item_key,
                "goal_item_name": item_key_text(goal_item_key),
                "materials": materials,
                "materials_text": ", ".join(
                    item_count_text(material["item_key"], material["need_count"]) for material in materials
                ),
            }
        )
    return records


class AccessoryStepUpHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["accessoryIndex"], "num", sort_key="accessory_index"),
            Column(labels["groupNo"], "num", sort_key="group_no"),
            Column(labels["accessory"], sort_key="goal_item_name"),
            Column(labels["enchantLevel"], "num", sort_key="enchant_level"),
            Column(labels["materials"], sort_key="materials_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [step for record in parse_accessorystepup_records(data) for step in _step_records(record)]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["accessory_index"]),
            e(record["group_no"]),
            item_key_list_cell([record["goal_item_key"]], 1),
            e(record["enchant_level"]),
            item_count_list_cell((material["item_key"], material["need_count"]) for material in record["materials"]),
        ]
