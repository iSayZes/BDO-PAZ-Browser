from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.equipskill_roll import equip_skill_name
from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from .parser import parse_petequipskill_records


_LANG_DIR = Path(__file__).parent / "lang"


class PetEquipSkillBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["equipSkillId"], "num", sort_key="equip_skill_id"),
            Column(cols["skillName"], sort_key="skill_name"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["skillType"], "num", sort_key="skill_type"),
            Column(cols["section"], sort_key="section"),
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

        for record in parse_petequipskill_records(data):
            row = dict(record)
            row["skill_name"] = equip_skill_name(row["loc_id"])
            row["icon_path"] = icon_path(IconKind.PET_EQUIP_SKILL, row["loc_id"])
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
                e(record.get("skill_name") or record["loc_id"]),
                icon_cell(record["icon_path"]),
                e(record["skill_type"]),
                e(record["section"]),
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)
