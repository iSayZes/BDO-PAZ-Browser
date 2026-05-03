from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import loc_lookup
from ..common.html import e, table
from .parser import parse_npcpersonality_records, parse_npcpersonalityoffset_records


def _decode_personality_type(code: int) -> str:
    major = code // 100
    name = loc_lookup(7, major)
    return name if name else f"?{major}"


def _group_str(group_id: int, item_count: int) -> str:
    if group_id == 0:
        return "—"
    return f"{group_id} ×{item_count}"


_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("Personality ID", "num", ""),
    ("Data Offset",    "num", ""),
]

_PERSONALITY_HEADERS: list[tuple[str, str, str]] = [
    ("Row",                "num", ""),
    ("ID",                 "num", ""),
    ("Group A (ID ×cnt)", "num", ""),
    ("Group B (ID ×cnt)", "num", ""),
    ("Group C (ID ×cnt)", "num", ""),
    ("Int Min",            "num", ""),
    ("Int Max",            "num", ""),
    ("Fav Min",            "num", ""),
    ("Fav Max",            "num", ""),
    ("Horoscope",          "",    ""),
]


class NpcPersonalityOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_npcpersonalityoffset_records(data)
        return [
            {"personality_id": rec["personality_id"], "data_offset": rec["data_offset"]}
            for rec in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} offset records"
        rows = [
            [e(r["personality_id"]), e(f"0x{r['data_offset']:08X}")]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


class NpcPersonalityHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_npcpersonality_records(data)
        return [
            {
                "row":                rec["row"],
                "personality_id":     rec["personality_id"],
                "group_a_id":         rec["group_a_id"],
                "group_a_count":      rec["group_a_count"],
                "group_b_id":         rec["group_b_id"],
                "group_b_count":      rec["group_b_count"],
                "group_c_id":         rec["group_c_id"],
                "group_c_count":      rec["group_c_count"],
                "interest_min":       rec["interest_min"],
                "interest_max_excl":  rec["interest_max_excl"],
                "favor_min":          rec["favor_min"],
                "favor_max_excl":     rec["favor_max_excl"],
                "personality_type":   rec["personality_type"],
            }
            for rec in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} personality records"
        rows = [
            [
                e(r["row"]),
                e(r["personality_id"]),
                e(_group_str(r["group_a_id"], r["group_a_count"])),
                e(_group_str(r["group_b_id"], r["group_b_count"])),
                e(_group_str(r["group_c_id"], r["group_c_count"])),
                e(int(r["interest_min"])),
                e(int(r["interest_max_excl"])),
                e(int(r["favor_min"])),
                e(int(r["favor_max_excl"])),
                e(_decode_personality_type(r["personality_type"])),
            ]
            for r in slice_
        ]
        return table(meta, _PERSONALITY_HEADERS, rows)
