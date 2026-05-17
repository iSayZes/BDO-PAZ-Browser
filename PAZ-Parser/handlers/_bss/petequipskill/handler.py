from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_petequipskill_records


_LANG_DIR = Path(__file__).parent / "lang"
_ICON_PATH = "ui_texture/icon/new_icon/08_servant_skill/02_pet/equipskill_{loc_id:08d}.dds"


def _skill_name(loc_id: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(10, loc_id)).strip()


class PetEquipSkillBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_petequipskill_records(data):
            row = dict(record)
            row["skill_name"] = _skill_name(row["loc_id"])
            row["icon_path"] = _ICON_PATH.format(loc_id=row["loc_id"])
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
        meta = f"{len(records):,} pet equip skill records"
        if localized:
            meta += f" · {localized:,} LOC names"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("equipSkillId", "Equip Skill ID"), "num", ""),
            (cols.get("skillName", "Skill Name"), "", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("skillType", "Skill Type"), "num", ""),
            (cols.get("section", "Section"), "", ""),
        ]

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

        return table(meta, headers, rows)
