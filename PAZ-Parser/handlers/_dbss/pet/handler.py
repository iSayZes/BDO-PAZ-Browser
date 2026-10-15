from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.petequipskill.parser import parse_petequipskill_records
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, KeyHashes, ui_key_hashes
from _common.character import character_name
from _common.equipskill_roll import equip_skill_name
from _common.html import Column, e, icon_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _dbss.petskill.parser import parse_petskill_records
from _dbss.petskill.skill_type import pet_skill_type_name, pet_skill_types
from .parser import (
    parse_pet_records,
    parse_petgrade_records_with_offsets,
    parse_petgradeoffset_records,
    parse_petoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_SKILL_CATALOG_FILE = "petequipskill.bss"
_PET_SKILL_FILE = "petskill.dbss"
_PET_SKILL_OFFSET_FILE = "petskilloffset.dbss"
# base_skill_id keys Section 2 of the catalog (Pet_BaseSkill_Table).
_BASE_SKILL_SECTION = "S2"


def _pet_key_text(value: int) -> str:
    return f"0x{value:04X} ({value})"


def _pet_skill_names(companions: dict[str, bytes]) -> dict[int, str]:
    """`pet_skill_id -> pet window text of its type`; empty without `petskill.dbss`."""
    skill_raw = companions.get(_PET_SKILL_FILE)
    offset_raw = companions.get(_PET_SKILL_OFFSET_FILE)
    if skill_raw is None or offset_raw is None:
        return {}

    hashes: KeyHashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
    types = pet_skill_types(parse_petskill_records(skill_raw, offset_raw))
    return {skill_id: pet_skill_type_name(hashes, skill_type) for skill_id, skill_type in types.items()}


def _base_skill_names(catalog: bytes | None) -> dict[int, str]:
    """`base_skill_id -> skill name` from Section 2 of `petequipskill.bss`; empty without it."""
    if catalog is None:
        return {}

    return {
        record["equip_skill_id"]: equip_skill_name(record["loc_id"])
        for record in parse_petequipskill_records(catalog)
        if record["section"] == _BASE_SKILL_SECTION
    }


def pet_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("pet_id", "petId", _pet_key_text),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_petoffset_records,
    )


class PetGradeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["gradeColumns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["species"], "num", sort_key="species"),
            Column(cols["variant"], "num", sort_key="variant"),
            Column(cols["grade"], sort_key="grade"),
            Column(cols["dataOffset"], "num", sort_key="data_offset"),
            Column(cols["dataSize"], "num", sort_key="data_size"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/petgradeoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("petgradeoffset.dbss")
        if offset_raw is None:
            raise ValueError("petgradeoffset.dbss companion not found.")

        records = parse_petgrade_records_with_offsets(data, offset_raw)
        grade_names = load_handler_strings(self.lang, _LANG_DIR)["grades"]
        for record in records:
            grade = record["grade"]
            record["grade_name"] = grade_names.get(str(grade), f"Unknown ({grade})")
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.gradeCount", count=len(records))
        rows = [
            [
                e(f"0x{r['key']:04X} ({r['key']})"),
                e(r["species"]),
                e(r["variant"]),
                e(r["grade_name"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)


def pet_grade_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("key", "key", _pet_key_text),
            OffsetColumn("species", "species"),
            OffsetColumn("variant", "variant"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_petgradeoffset_records,
        lang_block="gradeOffsetColumns",
    )


class PetDbssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["petId"], "num", sort_key="pet_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["name"], sort_key="display_name"),
            Column(cols["species"], "num", sort_key="species"),
            Column(cols["tier"], "num", sort_key="tier"),
            Column(cols["expKey"], "num", sort_key="exp_key"),
            Column(cols["maxLevel"], "num", sort_key="max_level"),
            Column(cols["acquireType"], "num", sort_key="acquire_type_id"),
            Column(cols["baseSkillId"], "num", sort_key="base_skill_id"),
            Column(cols["baseSkill"], sort_key="base_skill_name"),
            Column(cols["lootSkill"], sort_key="loot_skill_name"),
            Column(cols["specialSkill"], sort_key="race_skill_name"),
            Column(cols["grade"], sort_key="grade"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            f"{folder}/petoffset.dbss",
            f"{folder}/petgrade.dbss",
            f"{folder}/{_SKILL_CATALOG_FILE}",
            f"{folder}/{_PET_SKILL_FILE}",
            f"{folder}/{_PET_SKILL_OFFSET_FILE}",
            f"{folder}/{STRINGTABLE_FILE}",
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("petoffset.dbss")
        if offset_raw is None:
            raise ValueError("petoffset.dbss companion not found.")
        grade_raw = companions.get("petgrade.dbss")
        records = parse_pet_records(data, offset_raw, grade_raw)
        base_skill_names = _base_skill_names(companions.get(_SKILL_CATALOG_FILE))
        pet_skill_names = _pet_skill_names(companions)
        strings = load_handler_strings(self.lang, _LANG_DIR)
        grade_names = strings["grades"]
        for record in records:
            loc_name = character_name(record["pet_id"])
            record["pet_name"] = loc_name
            record["display_name"] = loc_name or str(record["species"])
            record["base_skill_name"] = base_skill_names.get(record["base_skill_id"], "")
            record["loot_skill_name"] = pet_skill_names.get(record["loot_skill_id"], "")
            record["race_skill_name"] = pet_skill_names.get(record["race_skill_id"], "")
            grade = record.get("grade")
            record["grade_name"] = grade_names.get(str(grade), str(grade) if grade is not None else "")
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        species_count = len({r["species"] for r in records})
        with_grade = sum(1 for r in records if r.get("grade") is not None)
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), species_count=species_count)
        if with_grade:
            meta += handler_text(self.lang, _LANG_DIR, "meta.withGrade", with_grade=with_grade)
        rows = [
            [
                e(r["pet_id"]),
                icon_cell(r["icon_path"]),
                e(r["display_name"]),
                e(r["species"]),
                e(r["tier"]),
                e(r["exp_key"]),
                e(r["max_level"]),
                e(r["acquire_type_id"]),
                e(r["base_skill_id"]),
                e(r["base_skill_name"]),
                e(r["loot_skill_name"]),
                e(r["race_skill_name"]),
                e(r["grade_name"] or "-"),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
