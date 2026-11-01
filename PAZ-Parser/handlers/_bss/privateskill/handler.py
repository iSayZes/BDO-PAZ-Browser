"""privateskill.bss preview handler: the active and passive skills and their classes."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.class_type import classes_label
from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from _bss.publicskill.skill_rows import SKILL_FIELD, SKILL_NO_FIELD, skill_key_fields, skill_name_cell, skill_no_cell
from .parser import FILE_NAME, parse_privateskill


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def row_classes_label(class_mask: int, class_slots: int, all_label: str) -> str:
    """`all_label` when the mask holds every class slot of its row or every playable class, else the class names.

    A file of 32 class slots (Layout 1, and Layout 2 up to client 2243) cannot
    hold the playable class types from `32` on in its every-class rows.
    """
    every_slot = (1 << class_slots) - 1
    return all_label if class_mask & every_slot == every_slot else classes_label(class_mask, all_label)


class PrivateSkillHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["skillNo"], "num", sort_key=SKILL_NO_FIELD),
            Column(labels["skill"], sort_key=SKILL_FIELD),
            Column(labels["kind"], sort_key="kind"),
            Column(labels["classes"], sort_key="classes"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        strings = load_handler_strings(self.lang, _LANG_DIR)
        kind_labels = strings["kind"]
        table = parse_privateskill(data)
        return [
            {
                **skill_key_fields(row["skill_key"]),
                "kind": row["kind"],
                "kind_label": kind_labels[str(row["kind"])],
                "class_mask": row["class_mask"],
                "classes": row_classes_label(row["class_mask"], table.class_slots, strings["allClasses"]),
            }
            for row in table.records
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            skill_no_cell(record),
            skill_name_cell(record),
            e(record["kind_label"]),
            e(record["classes"] or _EMPTY),
        ]
