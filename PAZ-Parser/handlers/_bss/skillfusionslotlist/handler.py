"""skillfusionslotlist.bss preview handler: the Skill Enhancement choices of each class slot."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.class_type import class_name
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.skill import split_skill_key
from _common.skill_cells import skill_label, skill_list_cell
from .parser import FILE_NAME, parse_skillfusionslotlist


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"
_LIST_PREVIEW_ITEMS = 6


def _record(record: dict) -> dict:
    skill_nos = [split_skill_key(key)[0] for key in record["skill_fusion_keys"]]
    return {
        **record,
        "class": class_name(record["class_type"]),
        "choice_count": len(skill_nos),
        "skill_nos": skill_nos,
        "skills": [skill_label(skill_no) for skill_no in skill_nos],
    }


class SkillFusionSlotListBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["class"], sort_key="class"),
            Column(cols["slot"], "num", sort_key="slot"),
            Column(cols["choiceCount"], "num", sort_key="choice_count"),
            Column(cols["skills"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: class type, then slot.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            return [_record(record) for record in parse_skillfusionslotlist(data)]
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
                e(r["slot"]),
                e(r["choice_count"]),
                skill_list_cell(r["skill_nos"], _LIST_PREVIEW_ITEMS),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
