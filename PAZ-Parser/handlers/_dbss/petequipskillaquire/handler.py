from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.equipskill_roll import flatten_roll_rows, read_skill_loc_ids
from _common.html import e, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import (
    parse_petequipskillaquire_records,
    parse_petequipskillaquireoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "petequipskillaquireoffset.dbss"
_CATALOG_FILE = "petequipskill.bss"
_LOC_TYPE = 10


def _skill_name(loc_id: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(_LOC_TYPE, loc_id, 0, 0, 0)).strip()


class PetEquipSkillAcquireOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_petequipskillaquireoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("acquireTypeId", "Acquire Type ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
            (cols.get("recordStart", "Record Start"), "num", ""),
        ]
        rows = [
            [
                e(r["acquire_type_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
                e(f"0x{r['record_start']:08X}"),
            ]
            for r in slice_
        ]
        return table(f"{len(records):,} pet roll offset records", headers, rows)


class PetEquipSkillAcquireHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}", f"{folder}/{_CATALOG_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        records = parse_petequipskillaquire_records(data, offset_raw)
        by_key = {r["acquire_type_id"]: r for r in records}

        catalog_raw = companions.get(_CATALOG_FILE)
        loc_ids = read_skill_loc_ids(catalog_raw) if catalog_raw else {}
        rows = flatten_roll_rows(records, loc_ids, _skill_name)

        for row in rows:
            source = by_key[row["acquire_type_id"]]
            row["group"] = source["group"]
            row["tier"] = source["tier"]

        return rows

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        types = len({r["acquire_type_id"] for r in records})
        meta = f"{len(records):,} roll entries across {types} acquire types"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("acquireTypeId", "Acquire Type ID"), "num", ""),
            (cols.get("equipSkillId", "Skill ID"), "num", ""),
            (cols.get("skillName", "Skill Name"), "", ""),
            (cols.get("chance", "Chance"), "num", ""),
            (cols.get("weight", "Weight"), "num", ""),
        ]
        rows = [
            [
                e(r["acquire_type_id"]),
                e(r["equip_skill_id"]),
                e(r["skill_name"] or r["loc_id"]),
                e(f"{round(r['chance_pct'], 2):g}%"),
                e(f"{r['weight']:,}"),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
