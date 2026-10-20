"""exceptionskillcooltimewidget.dbss preview handler: the skills the skill cooldown window shows in place of others."""
from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name, class_types_in_mask
from _common.html import Column, e, error, icon_html_label_cell, record_link, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.lookup_builders import SKILL
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.skill import skill_name_tagged, split_skill_key
from .parser import FILE_NAME, parse_exceptionskillcooltimewidget_records


_LANG_DIR = Path(__file__).parent / "lang"
_LINK_CLASS = "record-link"


class _SkillFields(NamedTuple):
    """The record fields of one of a row's three skills."""

    key: str
    skill_no: str
    name: str


_FROM = _SkillFields("skill_key_from", "skill_no_from", "skill_name_from")
_TO = _SkillFields("skill_key_to", "skill_no_to", "skill_name_to")
_LEARN_CHECK = _SkillFields("skill_learn_check_key", "skill_learn_check_no", "skill_learn_check_name")


def exception_skill_cool_time_widget_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("skill_key_from", "skillKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "skill_key_from"),
    )


def _skill_fields(record: dict, fields: _SkillFields) -> dict:
    """The skill number and LOC name of the key in `fields.key`."""
    skill_no, _ = split_skill_key(record[fields.key])
    return {fields.skill_no: skill_no, **pa_fields(fields.name, skill_name_tagged(skill_no))}


def _classes(class_mask: int) -> str:
    return ", ".join(class_name(class_type) for class_type in class_types_in_mask(class_mask))


def _skill_id_cell(record: dict, fields: _SkillFields) -> str:
    skill_no = record[fields.skill_no]
    return record_link(str(skill_no), SKILL, "skill_no", skill_no, _LINK_CLASS)


def _skill_name_cell(record: dict, fields: _SkillFields) -> str:
    return icon_html_label_cell(icon_path(IconKind.SKILL, record[fields.skill_no]), pa_cell(record, fields.name))


class ExceptionSkillCoolTimeWidgetHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["skillNo"], "num", sort_key=_FROM.skill_no),
            Column(cols["skill"], sort_key=_FROM.name),
            Column(cols["classes"], sort_key="classes"),
            Column(cols["shownSkillNo"], "num", sort_key=_TO.skill_no),
            Column(cols["shownSkill"], sort_key=_TO.name),
            Column(cols["learnCheckSkillNo"], "num", sort_key=_LEARN_CHECK.skill_no),
            Column(cols["learnCheckSkill"], sort_key=_LEARN_CHECK.name),
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
            records = parse_exceptionskillcooltimewidget_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [
            {
                **record,
                **_skill_fields(record, _FROM),
                "classes": _classes(record["class_mask"]),
                **_skill_fields(record, _TO),
                **_skill_fields(record, _LEARN_CHECK),
            }
            for record in records
        ]

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
                _skill_id_cell(r, _FROM),
                _skill_name_cell(r, _FROM),
                e(r["classes"]),
                _skill_id_cell(r, _TO),
                _skill_name_cell(r, _TO),
                _skill_id_cell(r, _LEARN_CHECK),
                _skill_name_cell(r, _LEARN_CHECK),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
