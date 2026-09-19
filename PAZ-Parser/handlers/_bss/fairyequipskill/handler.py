from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.icon_index import IconKind, icon_path
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_fairyequipskill_records


_LANG_DIR = Path(__file__).parent / "lang"
_LOC_TYPE = 10
# Within LOC type 10 the fourth sub-id selects name vs effect description.
_LOC_ID4_NAME = 0
_LOC_ID4_DESCRIPTION = 1


def _loc_text(loc_id: int, id4: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(_LOC_TYPE, loc_id, 0, 0, id4)).strip()


class FairyEquipSkillBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_fairyequipskill_records(data):
            row = dict(record)
            loc_id = row["loc_id"]
            row["skill_name"] = _loc_text(loc_id, _LOC_ID4_NAME)
            row["skill_description"] = _loc_text(loc_id, _LOC_ID4_DESCRIPTION)
            row["icon_path"] = icon_path(IconKind.FAIRY_EQUIP_SKILL, loc_id)
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
        meta = f"{len(records):,} fairy skill records"
        if localized:
            meta += f" · {localized:,} LOC names"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("equipSkillId", "Equip Skill ID"), "num", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("skillName", "Skill Name"), "", ""),
            (cols.get("description", "Description"), "", ""),
            (cols.get("skillType", "Skill Type"), "num", ""),
            (cols.get("locId", "Loc ID"), "num", ""),
        ]

        rows = [
            [
                e(record["equip_skill_id"]),
                icon_cell(record["icon_path"]),
                e(record.get("skill_name") or record["loc_id"]),
                e(record.get("skill_description") or ""),
                e(record["skill_type"]),
                e(record["loc_id"]),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
