"""weatheractor.dbss preview handler: weather actors in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name, character_title
from _common.enum_name import enum_name
from _common.html import Column, e, icon_html_label_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_fields, pa_html, pa_key
from _common.pabr_offset import parse_bare_offset_rows
from _common.skill import skill_name_tagged, split_skill_key
from .parser import WEATHER_TYPE_NAMES, parse_weatheractor_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# A row without a skill holds skill key 0; the record holds None, so the
# empty cell sorts last.
_NO_SKILL = 0


def weather_actor_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_key", "characterId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_key"),
    )


def _skill_fields(skill_key: int) -> dict:
    """The skill number and level of `skill_key`, its tagged name and icon; all empty without a skill."""
    if skill_key == _NO_SKILL:
        return {"skill_key": None, "skill_no": None, "skill_level": None, **pa_fields("skill_name", ""), "skill_icon_path": ""}
    skill_no, level = split_skill_key(skill_key)
    return {
        "skill_key": skill_key,
        "skill_no": skill_no,
        "skill_level": level,
        **pa_fields("skill_name", skill_name_tagged(skill_no) or str(skill_no)),
        "skill_icon_path": icon_path(IconKind.SKILL, skill_no),
    }


def _skill_cell(record: dict) -> str:
    if record["skill_no"] is None:
        return _EMPTY
    return icon_html_label_cell(record["skill_icon_path"], pa_html(record[pa_key("skill_name")]))


class WeatherActorHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["title"], sort_key="title"),
            Column(cols["weatherType"], sort_key="weather_type"),
            Column(cols["radius"], "num", sort_key="radius"),
            Column(cols["skillId"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                "name": character_name(record["character_key"]),
                "title": character_title(record["character_key"]),
                **_skill_fields(record["skill_key"]),
            }
            for record in parse_weatheractor_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [
                e(r["character_key"]),
                e(r["name"] or r["character_key"]),
                e(r["title"] or _EMPTY),
                e(enum_name(WEATHER_TYPE_NAMES, r["weather_type"])),
                e(f"{r['radius']:g}"),
                e(r["skill_no"]) if r["skill_no"] is not None else _EMPTY,
                _skill_cell(r),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            skills=sum(1 for r in records if r["skill_no"] is not None),
        )
        return table(meta, self._columns(), rows)
