"""privateskill.bss preview handler: the active and passive skills and their classes."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.class_type import classes_label
from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from _bss.publicskill.skill_rows import SKILL_FIELD, SKILL_NO_FIELD, skill_key_fields, skill_name_cell, skill_no_cell
from .parser import FILE_NAME, parse_privateskill_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


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
        return [
            {
                **skill_key_fields(row["skill_key"]),
                "kind": row["kind"],
                "kind_label": kind_labels[str(row["kind"])],
                "class_mask": row["class_mask"],
                "classes": classes_label(row["class_mask"], strings["allClasses"]),
            }
            for row in parse_privateskill_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            skill_no_cell(record),
            skill_name_cell(record),
            e(record["kind_label"]),
            e(record["classes"] or _EMPTY),
        ]
