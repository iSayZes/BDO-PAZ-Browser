from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name
from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.skill import skill_name
from .parser import ClassSkillList, parse_classskilllist_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 4


def _record_dict(row: ClassSkillList) -> dict:
    return {
        "class_type": row.class_type,
        "class_name": class_name(row.class_type),
        "skill_count": len(row.skill_nos),
        "skill_nos": list(row.skill_nos),
        "skills": [f"{skill_no} {skill_name(skill_no)}".rstrip() for skill_no in row.skill_nos],
    }


class ClassSkillListBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["className"], sort_key="class_name"),
            Column(cols["skillCount"], "num", sort_key="skill_count"),
            Column(cols["skills"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [_record_dict(row) for row in parse_classskilllist_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["class_type"]),
                e(r["class_name"]),
                e(r["skill_count"]),
                text_list_cell(r["skills"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
