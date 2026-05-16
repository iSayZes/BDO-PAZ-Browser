from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_plantworkerpassiveskill_records


_LANG_DIR = Path(__file__).parent / "lang"


def _loc_skill_text(skill_id: int, field_id: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(22, skill_id, 0, 0, field_id)).strip()


class PlantWorkerPassiveSkillBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        for record in parse_plantworkerpassiveskill_records(data):
            row = dict(record)
            row["display_name"] = (
                _loc_skill_text(row["skill_id"], 0) or row["inline_name"]
            )
            row["display_description"] = (
                _loc_skill_text(row["skill_id"], 1) or row["inline_description"]
            )
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
        localized = sum(
            1
            for record in records
            if record.get("display_name") != record.get("inline_name")
            or record.get("display_description") != record.get("inline_description")
        )

        meta = f"{len(records):,} worker passive skill records"
        if localized:
            meta += f" · {localized:,} with LOC text"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("skillId", "Skill ID"), "num", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("name", "Name"), "", ""),
            (cols.get("description", "Description"), "", ""),
            (cols.get("weight", "Weight"), "num", ""),
            (cols.get("effectType", "Effect Type"), "num", ""),
            (cols.get("target", "Target"), "num", ""),
            (cols.get("effectA", "Effect A"), "num", ""),
            (cols.get("effectB", "Effect B"), "num", ""),
        ]

        rows = [
            [
                e(record["skill_id"]),
                icon_cell(record["icon_path"]),
                e(record.get("display_name") or "-"),
                e(record.get("display_description") or "-"),
                e(record["acquisition_weight"]),
                e(record["effect_type"]),
                e(record["effect_target"]),
                e(record["effect_value_a"]),
                e(record["effect_value_b"] or "-"),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
