"""skillcommand.dbss preview handler: each skill's key command for the Skill Guide, keyboard and controller."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.classskilllist.parser import FILE_NAME as CLASSSKILLLIST_FILE
from _common.html import Column, e, flag_cell, icon_html_label_cell
from _common.lang import load_handler_strings
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_cell
from _common.row_table import RowTableHandler
from _common.skill_cells import skill_link
from .parser import FILE_NAME, KEY_FIELD, parse_skillcommand_records, parse_skillcommandoffset_rows
from .records import skill_classes, skill_command_record


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def skill_command_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_skillcommandoffset_rows, KEY_FIELD, "skillNo")


class SkillCommandHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{CLASSSKILLLIST_FILE}"]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["skillNo"], "num", sort_key=KEY_FIELD),
            Column(labels["skill"], sort_key="name"),
            Column(labels["classes"], sort_key="classes"),
            Column(labels["command"], sort_key="command"),
            Column(labels["consoleCommand"], sort_key="console_command"),
            Column(labels["level"], "num", sort_key="pc_level_for_learning"),
            Column(labels["showCheck"], sort_key="show_check"),
            Column(labels["awakening"], sort_key="awaken_command"),
            Column(labels["form"], sort_key="form"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        forms = load_handler_strings(self.lang, _LANG_DIR)["forms"]
        classes = skill_classes(companions.get(CLASSSKILLLIST_FILE))
        return [skill_command_record(row, classes, forms) for row in parse_skillcommand_records(data)]

    def cells(self, record: dict) -> list[str]:
        skill_no = record[KEY_FIELD]
        return [
            skill_link(skill_no, str(skill_no)) if record["has_skill_link"] else e(skill_no),
            icon_html_label_cell(record["icon"], e(record["name"])),
            e(record["classes"] or _EMPTY),
            pa_cell(record, "command"),
            pa_cell(record, "console_command"),
            e(record["pc_level_for_learning"]),
            flag_cell(bool(record["show_check"])),
            flag_cell(bool(record["awaken_command"])),
            e(record["form"] or _EMPTY),
        ]

