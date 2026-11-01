"""sequencetutorial_equipment.bss and cutscenetutorial_equipment.bss preview
handler: one row per cutscene and class, with its six costume items.

Class names are LOC type 21, item names LOC type 0. A
`sequencetutorial_equipment.bss` row also shows its sequence path from
`sequencetriggerdata.bss`, looked up by the file name hash. The names stay
paths; the `.pas` cutscenes and the `sequence/` files have no handler.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.sequencetriggerdata.lookup import sequence_paths_by_hash, sequence_trigger_companion
from _common.class_type import class_name
from _common.html import Column, e
from _common.item_key import item_key_list_cell, item_name
from _common.row_table import RowTableHandler
from .parser import SEQUENCE_FILE_NAME, SLOT_FIELDS, parse_tutorial_equipment_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_ONE_ITEM = 1
# Each item field, the record field that holds its name, and its column label key.
_SLOTS = tuple(
    (field, field.replace("_item_id", "_item_name"), label)
    for field, label in zip(SLOT_FIELDS, ("mainWeapon", "subWeapon", "helmet", "armor", "gloves", "shoes"))
)


def _class_record(row: dict, entry: dict, sequence_path: str) -> dict:
    """One class entry of a row, with "no item" as None and the item and class names."""
    return {
        "file_name_hash": row["file_name_hash"],
        "cutscene_file_name": row["cutscene_file_name"],
        "sequence_path": sequence_path,
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
        # Only sequences have a trigger row; the cutscene table has no second name.
        self._has_sequence_path = file_name == SEQUENCE_FILE_NAME

    def companions(self, entry: PazEntry) -> list[str]:
        return [sequence_trigger_companion(entry)] if self._has_sequence_path else []

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        sequence_column = [Column(labels["sequenceFile"], sort_key="sequence_path")] if self._has_sequence_path else []
        return [
            Column(labels["cutsceneFile"], sort_key="cutscene_file_name"),
            *sequence_column,
            Column(labels["classType"], "num", sort_key="class_type"),
            Column(labels["className"], sort_key="class_name"),
            *(Column(labels[label], sort_key=name) for _, name, label in _SLOTS),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        sequence_paths = sequence_paths_by_hash(companions) if self._has_sequence_path else {}
        return [
            _class_record(row, entry, sequence_paths.get(row["file_name_hash"], ""))
            for row in parse_tutorial_equipment_rows(data, self.file_name)
            for entry in row["classes"]
        ]

    def cells(self, record: dict) -> list[str]:
        sequence_cell = [e(record["sequence_path"] or _EMPTY)] if self._has_sequence_path else []
        return [
            e(record["cutscene_file_name"]),
            *sequence_cell,
            e(record["class_type"]),
            e(record["class_name"]),
            *(
                item_key_list_cell([record[field]], _ONE_ITEM) if record[field] else _EMPTY
                for field, _, _ in _SLOTS
            ),
        ]
