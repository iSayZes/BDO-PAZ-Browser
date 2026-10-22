"""instancedungeonskillinfo.bss preview handler: one row per skill of each class list."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.class_type import class_name
from _common.html import Column, e, error, icon_html_label_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.skill import skill_name_tagged, split_skill_key
from _common.skill_cells import skill_link
from .parser import FILE_NAME, InstanceDungeonSkills, SkillEntry, parse_instancedungeonskillinfo


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"
_EMPTY = "-"


def _skill_fields(skill_no: int, entry: SkillEntry | None) -> dict:
    """The skill's name and, when the file has one, its skill entry's unknown fields."""
    return {
        "skill_no": skill_no,
        **pa_fields("skill", skill_name_tagged(skill_no)),
        "unknown_02": entry.unknown_02 if entry else None,
        "unknown_08": list(entry.unknown_08) if entry else None,
    }


def _records(parsed: InstanceDungeonSkills) -> list[dict]:
    """A record per listed skill, then one per skill entry no list names."""
    entries = {entry.skill_no: entry for entry in parsed.entries}
    records: list[dict] = []
    for skill_list in parsed.lists:
        for skill_key in skill_list.skill_keys:
            skill_no = split_skill_key(skill_key)[0]
            records.append(
                {
                    "class_type": skill_list.class_type,
                    "class": class_name(skill_list.class_type),
                    "list_index": skill_list.list_index,
                    "skill_key": skill_key,
                    **_skill_fields(skill_no, entries.get(skill_no)),
                }
            )
    listed = {record["skill_no"] for record in records}
    records.extend(
        {"class_type": None, "class": None, "list_index": None, "skill_key": None, **_skill_fields(entry.skill_no, entry)}
        for entry in parsed.entries
        if entry.skill_no not in listed
    )
    return records


class InstanceDungeonSkillInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["class"], sort_key="class"),
            Column(cols["list"], "num", sort_key="list_index"),
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: class type, then list, then position in the list.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            return _records(parse_instancedungeonskillinfo(data))
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
                e(r["class"]) if r["class"] is not None else _EMPTY,
                e(r["list_index"]) if r["list_index"] is not None else _EMPTY,
                skill_link(r["skill_no"], str(r["skill_no"])),
                icon_html_label_cell(icon_path(IconKind.SKILL, r["skill_no"]), pa_cell(r, "skill")),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
