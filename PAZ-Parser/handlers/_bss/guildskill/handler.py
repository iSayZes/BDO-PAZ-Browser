"""guildskill.bss preview handler: one row per guild skill, with its cell in the guild skill tree."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_html_label_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.skill import skill_name_tagged
from _common.skill_cells import skill_link
from .parser import FILE_NAME, TREE_FILE_NAME, TreeCell, parse_guild_skills, tree_cells


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"
_EMPTY = "-"


def _record(row: dict, cells: dict[int, TreeCell]) -> dict:
    skill_no = row["skill_no"]
    # None for a skill the tree does not place; its dashed cell sorts last.
    cell = cells.get(skill_no)
    return {
        **row,
        "icon_path": icon_path(IconKind.SKILL, skill_no),
        **pa_fields("skill", skill_name_tagged(skill_no)),
        "tree_column": cell.column if cell is not None else None,
        "tree_row": cell.row if cell is not None else None,
    }


def _optional_cell(value: int | None) -> str:
    return e(value) if value is not None else _EMPTY


class GuildSkillBssHandler(PreviewHandler):
    """The guild skills and where the guild window draws each one."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill"),
            Column(cols["skillLevel"], "num", sort_key="skill_level"),
            Column(cols["treeColumn"], "num", sort_key="tree_column"),
            Column(cols["treeRow"], "num", sort_key="tree_row"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{TREE_FILE_NAME}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            rows = parse_guild_skills(data)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]
        tree_data = companions.get(TREE_FILE_NAME)
        try:
            cells = tree_cells(tree_data) if tree_data is not None else {}
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{TREE_FILE_NAME} could not be parsed: {ex}"}]
        return [_record(row, cells) for row in rows]

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
                skill_link(r["skill_no"], str(r["skill_no"])),
                icon_html_label_cell(r["icon_path"], pa_cell(r, "skill")),
                e(r["skill_level"]),
                _optional_cell(r["tree_column"]),
                _optional_cell(r["tree_row"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
