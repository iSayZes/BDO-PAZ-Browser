from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, flag_cell, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_pabr_offset_rows
from _common.vehicle_skill import VEHICLE_SKILL_FILE, vehicle_skill_companion, vehicle_skill_name
from _dbss.vehicleskill.parser import vehicle_skill_names_kr
from .parser import parse_vehicleskillowner_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_VEHICLE_SKILL_PATH = f"gamecommondata/binary/{VEHICLE_SKILL_FILE}"
_LINK_CLASS = "record-link"
# The fields of one skill entry; a servant without skills gets one row with these empty.
_SKILL_FIELDS = ("skill_key", "skill_name", "able", "add_exp", "is_learn", "unknown_0d", "unknown_0e")


def vehicle_skill_owner_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_offset_rows, "character_id"),
    )


def _number(value: int | None) -> str:
    return _EMPTY if value is None else f"{value:,}"


class VehicleSkillOwnerHandler(PreviewHandler):
    """One table row per skill entry, each with its servant's fields."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["cantLearnableRate"], "num", sort_key="cant_learnable_rate"),
            Column(cols["skillKey"], "num", sort_key="skill_key"),
            Column(cols["skill"], sort_key="skill_name"),
            Column(cols["able"], "num", sort_key="able"),
            Column(cols["addExp"], "num", sort_key="add_exp"),
            Column(cols["isLearn"], sort_key="is_learn"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [
            characterstatic_offset_companion(entry.internal_path),
            vehicle_skill_companion(entry.internal_path),
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        row_ids = character_row_ids(companions)
        try:
            skill_names_kr = vehicle_skill_names_kr(companions.get(VEHICLE_SKILL_FILE))
        except ValueError as ex:
            raise ValueError(f"{VEHICLE_SKILL_FILE}: {ex}") from ex

        rows: list[dict] = []
        for servant in parse_vehicleskillowner_records(data):
            character_id = servant["character_id"]
            head = {
                "character_id": character_id,
                "name": character_name(character_id) or str(character_id),
                "cant_learnable_rate": servant["cant_learnable_rate"],
                "has_character_row": has_character_row(row_ids, character_id),
            }
            skills = [
                {**skill, "skill_name": vehicle_skill_name(skill["skill_key"], skill_names_kr)}
                for skill in servant["skills"]
            ]
            rows.extend({**head, **skill} for skill in skills or [dict.fromkeys(_SKILL_FIELDS)])
        return rows

    def _row(self, r: dict) -> list[str]:
        skill_key = r["skill_key"]
        has_skill = skill_key is not None
        return [
            character_key_cell(r["character_id"], r["has_character_row"]),
            e(r["name"]),
            _number(r["cant_learnable_rate"]),
            record_link(str(skill_key), _VEHICLE_SKILL_PATH, "key", skill_key, _LINK_CLASS) if has_skill else _EMPTY,
            e(r["skill_name"] or _EMPTY),
            _number(r["able"]),
            _number(r["add_exp"]),
            flag_cell(bool(r["is_learn"])) if has_skill else _EMPTY,
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        skills = sum(1 for r in records if r["skill_key"] is not None)
        servants = len({r["character_id"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=skills, servants=servants)
        rows = [self._row(r) for r in records[start : start + page_size]]
        return table(meta, self._columns(), rows)
