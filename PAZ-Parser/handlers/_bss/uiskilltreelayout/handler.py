"""Skill tree layout preview handler: one row per skill cell of the grid."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, error, icon_html_label_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.skill import skill_name_tagged
from _common.skill_cells import skill_link
from .parser import SkillCell, parse_skill_tree


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"
# The fusion tree's cells are slots: they hold skill number 0.
_NO_SKILL = 0


def _record(cell: SkillCell) -> dict:
    has_skill = cell.skill_no != _NO_SKILL
    return {
        "column": cell.column,
        "row": cell.row,
        "arrow_type": cell.arrow_type,
        "skill_no": cell.skill_no,
        "icon_path": icon_path(IconKind.SKILL, cell.skill_no) if has_skill else "",
        **pa_fields("skill", skill_name_tagged(cell.skill_no) if has_skill else ""),
    }


def _skill_no_cell(skill_no: int) -> str:
    return skill_link(skill_no, str(skill_no)) if skill_no != _NO_SKILL else e(skill_no)


class UiSkillTreeLayoutBssHandler(PreviewHandler):
    """The guild, fusion, life skill and territory policy skill trees."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["column"], "num", sort_key="column"),
            Column(cols["row"], "num", sort_key="row"),
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: column by column, as the grid stores its cells.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        file_name = entry.internal_path.rsplit("/", 1)[-1]
        try:
            tree = parse_skill_tree(data, file_name)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{file_name} could not be parsed: {ex}"}]
        return [_record(cell) for cell in tree.skill_cells]

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
                e(r["column"]),
                e(r["row"]),
                _skill_no_cell(r["skill_no"]),
                icon_html_label_cell(r["icon_path"], pa_cell(r, "skill")),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
