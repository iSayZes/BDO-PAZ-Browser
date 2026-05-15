from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from .parser import parse_petskill_records, parse_petskilloffset_records


class PetSkillOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_petskilloffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        headers: list[tuple[str, str, str]] = [
            ("Pet Skill ID", "num", ""),
            ("Data Offset", "num", ""),
            ("Data Size", "num", ""),
        ]
        rows = [
            [
                e(r["pet_skill_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(f"{len(records):,} pet skill offset records", headers, rows)


class PetSkillHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/petskilloffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("petskilloffset.dbss")
        if offset_raw is None:
            raise ValueError("petskilloffset.dbss companion not found.")
        return parse_petskill_records(data, offset_raw)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        skill_count = len({r["pet_skill_id"] for r in records})
        meta = f"{skill_count:,} pet skills · {len(records):,} level rows"
        headers: list[tuple[str, str, str]] = [
            ("Pet Skill ID", "num", ""),
            ("Skill Group", "num", ""),
            ("Level", "num", ""),
            ("Value A", "num", ""),
            ("Value B", "num", ""),
        ]
        rows = [
            [
                e(r["pet_skill_id"]),
                e(r["skill_group"]),
                e(r["level"]),
                e(r["raw_value_a"]),
                e(r["raw_value_b"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
