from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_pet_records, parse_petgrade_records, parse_petoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


class PetOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_petoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} pet offset records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("petId", "Pet ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
        ]
        rows = [
            [
                e(f"0x{r['pet_id']:04X} ({r['pet_id']})"),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class PetGradeHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_petgrade_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} pet grade records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("gradeColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("species", "Species"), "num", ""),
            (cols.get("variant", "Variant"), "num", ""),
            (cols.get("grade", "Grade"), "num", ""),
        ]
        rows = [
            [
                e(r["species"]),
                e(r["variant"]),
                e(r["grade"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class PetDbssHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            f"{folder}/petoffset.dbss",
            f"{folder}/petgrade.dbss",
            f"{folder}/languagedata_en.loc",
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
        has_loc = is_loc_loaded()
        strings = load_handler_strings(self.lang, _LANG_DIR)
        grade_names = strings.get("grades", {})
        for record in records:
            loc_name = ""
            if has_loc:
                loc_name = strip_pa_tags(loc_lookup(6, record["pet_id"])).strip()
            record["pet_name"] = loc_name
            record["display_name"] = loc_name or str(record["species"])
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
        meta = f"{len(records):,} pets · {species_count:,} species"
        if with_grade:
            meta += f" · {with_grade:,} with grade metadata"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("petId", "Pet ID"), "num", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("name", "Name"), "", ""),
            (cols.get("species", "Species ID"), "num", ""),
            (cols.get("tier", "Tier"), "num", ""),
            (cols.get("skillSlots", "Skill Slots"), "num", ""),
            (cols.get("maxLevel", "Max Level"), "num", ""),
            (cols.get("acquireType", "Acquire Type"), "num", ""),
            (cols.get("equipSkillId", "Equip Skill ID"), "num", ""),
            (cols.get("grade", "Grade"), "", ""),
        ]
        rows = [
            [
                e(r["pet_id"]),
                icon_cell(r["icon_path"]),
                e(r["display_name"]),
                e(r["species"]),
                e(r["tier"]),
                e(r["equip_skill_slots"]),
                e(r["max_level"]),
                e(r["acquire_type_id"]),
                e(r["equip_skill_id"]),
                e(r["grade_name"] or "-"),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
