from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from .parser import parse_fairyequipskill_records


_LANG_DIR = Path(__file__).parent / "lang"
_LOC_TYPE = 10
# Within LOC type 10 the fourth sub-id selects name vs effect description.
_LOC_ID4_NAME = 0
_LOC_ID4_DESCRIPTION = 1


class FairyEquipSkillBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["equipSkillId"], "num", sort_key="equip_skill_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["skillName"], sort_key="skill_name"),
            Column(cols["description"], sort_key="skill_description"),
            Column(cols["skillType"], "num", sort_key="skill_type"),
            Column(cols["skillNo"], "num", sort_key="skill_no"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_fairyequipskill_records(data):
            row = dict(record)
            skill_no = row["skill_no"]
            row["skill_name"] = loc_text(_LOC_TYPE, skill_no, _LOC_ID4_NAME)
            row["skill_description"] = loc_text(_LOC_TYPE, skill_no, _LOC_ID4_DESCRIPTION)
            row["icon_path"] = icon_path(IconKind.FAIRY_EQUIP_SKILL, skill_no)
            records.append(row)

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        localized = sum(1 for record in records if record.get("skill_name"))
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        if localized:
            meta += handler_text(self.lang, _LANG_DIR, "meta.localized", localized=localized)

        rows = [
            [
                e(record["equip_skill_id"]),
                icon_cell(record["icon_path"]),
                e(record.get("skill_name") or record["skill_no"]),
                e(record.get("skill_description") or ""),
                e(record["skill_type"]),
                e(record["skill_no"]),
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)
