"""skillcomboguide.bss preview handler: each class's skill combos, step by step."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.class_type import class_name
from _common.html import Column, e, error, html_list_cell, icon_html_label_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_html, pa_key, pa_list_fields
from _common.skill import skill_name
from _common.skill_cells import skill_label, skill_link
from _bss.stringtable.parser import GAME_SHEET, parse_key_hashes
from _bss.stringtable.text import STRINGTABLE_FILE
from .commands import command_tagged
from .parser import FILE_NAME, Combo, parse_skillcomboguide


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"
_STEP_SEPARATOR = " → "


def _record(combo: Combo, game_key_hashes: dict[str, int]) -> dict:
    skill_nos = [step.skill_no for step in combo.steps]
    return {
        "class_type": combo.class_type,
        "class": class_name(combo.class_type),
        "combo_no": combo.combo_no,
        "combo_skill_count": combo.combo_skill_count,
        "skill_nos": skill_nos,
        "skills": [skill_label(skill_no) for skill_no in skill_nos],
        "command_indexes": [step.command_index for step in combo.steps],
        **pa_list_fields("commands", [command_tagged(step.command, game_key_hashes) for step in combo.steps]),
    }


def _steps_cell(record: dict) -> str:
    """Each step's skill icon, linked name and key bindings, in order."""
    steps = [
        icon_html_label_cell(
            icon_path(IconKind.SKILL, skill_no),
            f"{skill_link(skill_no, skill_name(skill_no) or str(skill_no))} {pa_html(command)}",
        )
        for skill_no, command in zip(record["skill_nos"], record[pa_key("commands")], strict=True)
    ]
    return html_list_cell(steps, separator=_STEP_SEPARATOR) or "-"


def _game_key_hashes(companions: dict[str, bytes]) -> dict[str, int]:
    data = companions.get(STRINGTABLE_FILE)
    return parse_key_hashes(data, GAME_SHEET) if data is not None else {}


def _game_order(record: dict) -> tuple[int, int]:
    return record["class_type"], record["combo_no"]


class SkillComboGuideBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["class"], sort_key="class"),
            Column(cols["combo"], "num", sort_key="combo_no"),
            Column(cols["skillCount"], "num", sort_key="combo_skill_count"),
            Column(cols["steps"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # get_records() orders by class type, then combo; no one column gives that.
        return None

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STRINGTABLE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            combos = parse_skillcomboguide(data)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]
        game_key_hashes = _game_key_hashes(companions)
        return sorted((_record(combo, game_key_hashes) for combo in combos), key=_game_order)

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
                e(r["combo_no"]),
                e(r["combo_skill_count"]),
                _steps_cell(r),
            ]
            for r in records[start : start + page_size]
        ]
        classes = len({r["class_type"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), classes=classes)
        return table(meta, self._columns(), rows)
