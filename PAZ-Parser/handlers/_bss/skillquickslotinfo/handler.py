"""skillquickslotinfo.bss preview handler: the skill each class has in its quick slots."""
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
from _common.skill import skill_name_tagged
from _common.skill_cells import skill_link
from .parser import FILE_NAME, parse_skillquickslotinfo


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"


class SkillQuickSlotInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["class"], sort_key="class"),
            Column(cols["slot"], "num", sort_key="slot"),
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill"),
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
            records = parse_skillquickslotinfo(data)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]
        return [
            {
                **record,
                "class": class_name(record["class_type"]),
                **pa_fields("skill", skill_name_tagged(record["skill_no"])),
            }
            for record in records
        ]

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
                skill_link(r["skill_no"], str(r["skill_no"])),
                icon_html_label_cell(icon_path(IconKind.SKILL, r["skill_no"]), pa_cell(r, "skill")),
            ]
            for r in records[start : start + page_size]
        ]
        classes = len({r["class_type"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), classes=classes)
        return table(meta, self._columns(), rows)
