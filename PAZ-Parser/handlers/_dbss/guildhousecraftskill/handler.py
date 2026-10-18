"""guildhousecraftskill.dbss preview handler: the guild skills each guild house use grants."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_html_list_cell, record_link, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from _common.lookup_builders import SKILL
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.skill import skill_name
from .parser import FILE_NAME, parse_guildhousecraftskill_records


_LANG_DIR = Path(__file__).parent / "lang"
_HOUSEINFORECEIPE = "gamecommondata/binary/houseinforeceipe.dbss"
# LOC type 16, str_id1 = receipe key: the house use name (houseinforeceipe_dbss.md).
_LOC_TYPE_RECEIPE = 16
_EMPTY = "-"
_LINK_CLASS = "record-link"


def guild_house_craft_skill_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("receipe_key", "receipeKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "receipe_key", "data_offset", "data_size"),
    )


def _skill_label(skill_no: int) -> str:
    """`65042 Building Boat Lv. 1`, or the bare number without a name."""
    return f"{skill_no} {skill_name(skill_no)}".strip()


def _with_display_fields(record: dict) -> dict:
    """The record with its house use name and its filled skill slots."""
    skills = [skill_no for skill_no in record["skill_nos"] if skill_no]
    return {
        **record,
        "name": loc_text(_LOC_TYPE_RECEIPE, record["receipe_key"]) or None,
        "skills": skills,
        "skill_count": len(skills),
        "skills_text": ", ".join(_skill_label(skill_no) for skill_no in skills) or None,
    }


def _skills_cell(skills: list[int]) -> str:
    """Each skill with its icon, linked to its first `skill.dbss` row."""
    if not skills:
        return _EMPTY
    entries = [
        (icon_path(IconKind.SKILL, skill_no), record_link(_skill_label(skill_no), SKILL, "skill_no", skill_no, _LINK_CLASS))
        for skill_no in skills
    ]
    return icon_html_list_cell(entries)


class GuildHouseCraftSkillHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["receipeKey"], "num", sort_key="receipe_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["skillCount"], "num", sort_key="skill_count"),
            Column(cols["skills"], sort_key="skills_text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_guildhousecraftskill_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_with_display_fields(record) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                record_link(str(r["receipe_key"]), _HOUSEINFORECEIPE, "receipe_key", r["receipe_key"], _LINK_CLASS),
                e(r["name"] or _EMPTY),
                e(r["skill_count"]),
                _skills_cell(r["skills"]),
            ]
            for r in records[start : start + page_size]
        ]
        skill_total = len({skill_no for r in records for skill_no in r["skills"]})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), skills=skill_total)
        return table(meta, self._columns(), rows)
