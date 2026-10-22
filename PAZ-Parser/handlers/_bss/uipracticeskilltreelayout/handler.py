"""uipracticeskilltreelayout.bss preview handler: one row per class grid with its skill cells."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.class_type import class_name
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.skill_cells import skill_label, skill_list_cell
from .parser import FILE_NAME, ClassGrid, parse_uipracticeskilltreelayout


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"
_LIST_PREVIEW_ITEMS = 6


def _record(grid: ClassGrid) -> dict:
    return {
        "class_type": grid.class_type,
        "class": class_name(grid.class_type),
        "width": grid.width,
        "height": grid.height,
        "blank_cells": grid.blank_cells,
        "skill_cells": len(grid.skill_nos),
        "skill_nos": list(grid.skill_nos),
        "skills": [skill_label(skill_no) for skill_no in grid.skill_nos],
    }


class UiPracticeSkillTreeLayoutBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["class"], sort_key="class"),
            Column(cols["width"], "num", sort_key="width"),
            Column(cols["height"], "num", sort_key="height"),
            Column(cols["blankCells"], "num", sort_key="blank_cells"),
            Column(cols["skillCells"], "num", sort_key="skill_cells"),
            Column(cols["skills"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order, the class order of the developer sheets.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            return [_record(grid) for grid in parse_uipracticeskilltreelayout(data)]
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and _ERROR_FIELD in records[0]:
            return error(records[0][_ERROR_FIELD])

        start = page * page_size
        rows = [
            [
                e(r["class"]),
                e(r["width"]),
                e(r["height"]),
                e(r["blank_cells"]),
                e(r["skill_cells"]),
                skill_list_cell(r["skill_nos"], _LIST_PREVIEW_ITEMS),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
