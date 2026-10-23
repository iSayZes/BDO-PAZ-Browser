"""sequencetutorial_equipment.bss and cutscenetutorial_equipment.bss preview
handler: one row per cutscene and class, with its six costume items.

Class names are LOC type 21, item names LOC type 0. The file name stays a
path; the `.pas` cutscene and the `sequence/` files it names have no handler.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.class_type import class_name
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_name
from _common.row_table import RowTableHandler
from .parser import SLOT_FIELDS, parse_tutorial_equipment_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_ONE_ITEM = 1
# Each item field, the record field that holds its name, and its column label key.
_SLOTS = tuple(
    (field, field.replace("_item_id", "_item_name"), label)
    for field, label in zip(SLOT_FIELDS, ("mainWeapon", "subWeapon", "helmet", "armor", "gloves", "shoes"))
)


def _class_record(row: dict, entry: dict) -> dict:
    """One class entry of a row, with "no item" as None and the item and class names."""
    return {
        "file_name_hash": row["file_name_hash"],
        "cutscene_file_name": row["cutscene_file_name"],
        "class_type": entry["class_type"],
        "class_name": class_name(entry["class_type"]),
        **{field: entry[field] or None for field, _, _ in _SLOTS},
        **{name: item_name(entry[field]) if entry[field] else "" for field, name, _ in _SLOTS},
    }


class TutorialEquipmentBssHandler(RowTableHandler):
    lang_dir = _LANG_DIR

    def __init__(self, file_name: str) -> None:
        super().__init__()
        self.file_name = file_name

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["cutsceneFile"], sort_key="cutscene_file_name"),
            Column(labels["classType"], "num", sort_key="class_type"),
            Column(labels["className"], sort_key="class_name"),
            *(Column(labels[label], sort_key=name) for _, name, label in _SLOTS),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            _class_record(row, entry)
            for row in parse_tutorial_equipment_rows(data, self.file_name)
            for entry in row["classes"]
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["cutscene_file_name"]),
            e(record["class_type"]),
            e(record["class_name"]),
            *(
                item_key_list_cell([record[field]], _ONE_ITEM) if record[field] else _EMPTY
                for field, _, _ in _SLOTS
            ),
        ]
