from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.buff import buff_label, buff_list_cell
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields, pa_key, pa_list_cell, pa_list_fields
from _common.pabr_offset import parse_bare_offset_rows
from _common.skill import skill_buff_ids, skill_key, skill_name_tagged
from .parser import parse_skillpiece_records
from .text import TierText, tier_text


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 4
_EFFECT_PREVIEW_LINES = 6


def skill_piece_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("skill_no", "skillId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "skill_no"),
    )


def _tier_record(record: dict, tier: dict) -> dict:
    """One table row: a tier with its text in the user's language and its buffs."""
    skill_no = record["skill_no"]
    korean = TierText(tier["group_title_kr"], tier["desc_title_kr"], tier["desc_kr"])
    text = tier_text(skill_no, tier["level"], korean)
    key = skill_key(skill_no, tier["level"])
    # From the SKILL_BUFFS lookup index; empty when it is not loaded.
    buff_ids = skill_buff_ids([key])
    return {
        "skill_key": key,
        "skill_no": skill_no,
        **tier,
        # Records without tier text are named after their skill.
        **pa_fields("set_name", text.group_title or skill_name_tagged(skill_no)),
        **pa_fields("requires", text.desc_title),
        **pa_list_fields("effects", [line for line in text.desc.split("\n") if line.strip()]),
        "buff_ids": buff_ids,
        "buffs": [buff_label(buff_id) for buff_id in buff_ids],
        "unknown_end": record["unknown_end"],
    }


class SkillPieceHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["skillId"], "num", sort_key="skill_no"),
            Column(cols["set"], sort_key="set_name"),
            Column(cols["points"], "num", sort_key="point"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["requires"], sort_key="requires"),
            # List columns: they would only sort by their string form.
            Column(cols["effect"]),
            Column(cols["buffs"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = [
            _tier_record(record, tier)
            for record in parse_skillpiece_records(data)
            for tier in record["tiers"]
        ]
        # Skill order, so the tiers of one set stay in level order under the
        # default sort.
        return sorted(records, key=lambda record: record["skill_key"])

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            sets=len({record["skill_no"] for record in records}),
        )
        rows = [
            [
                e(r["skill_no"]),
                pa_cell(r, "set_name"),
                e(r["point"]),
                e(r["level"]),
                pa_cell(r, "requires"),
                pa_list_cell(r[pa_key("effects")], _EFFECT_PREVIEW_LINES),
                buff_list_cell(r["buff_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
