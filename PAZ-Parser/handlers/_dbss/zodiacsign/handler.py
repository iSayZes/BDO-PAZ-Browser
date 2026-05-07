from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, error, table
from _common.zodiacsign.loc import resolve_loc_type7
from _common.zodiacsign.parser import parse_zodiacsign_records
from .parser import (
    parse_zodiacsignoffset_records,
    parse_zodiacsignorder_records,
    parse_zodiacsignorderoffset_records,
)


def _truncate(text: str, max_len: int = 100) -> str:
    return text if len(text) <= max_len else text[:max_len] + "…"


_SIGN_HEADERS: list[tuple[str, str, str]] = [
    ("ID",              "num", ""),
    ("Name",            "",    ""),
    ("Stars",           "num", ""),
    ("Pairs",           "num", ""),
    ("Constellation",   "",    ""),
    ("Traits",          "",    ""),
]

_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("Zodiac ID",    "num", ""),
    ("Data Offset",  "num", ""),
]

_ORDER_HEADERS: list[tuple[str, str, str]] = [
    ("Personality",  "num", ""),
    ("Zodiac",       "",    ""),
    ("Variant",      "num", ""),
    ("Triggers",     "num", ""),
    ("Sequence",     "",    ""),
]

_ORDER_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("Personality Type", "num", ""),
    ("Data Offset",      "num", ""),
]

class ZodiacSignHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_zodiacsign_records(data)
        if not records:
            return []

        zodiac_ids = [rec["zodiac_id"] for rec in records]
        loc_names, loc_traits = resolve_loc_type7(zodiac_ids)

        result: list[dict] = []
        for rec in records:
            zid = rec["zodiac_id"]
            result.append({
                "zodiac_id":         zid,
                "name":              loc_names.get(zid, f"#{zid}"),
                "float_count":       rec["float_count"],
                "pairs_count":       rec["pairs_count"],
                "constellation_name": rec["constellation_name"],
                "trait_text":        rec["trait_text"],
                "en_trait":          loc_traits.get(zid, ""),
            })

        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]

        loc_ok = any(r["en_trait"] for r in records)
        headers = list(_SIGN_HEADERS)
        headers[5] = ("Traits (EN)" if loc_ok else "Traits (KR)", "", "")

        meta = f"{len(records):,} zodiac signs"
        rows: list[list] = []
        for r in slice_:
            en_trait = r["en_trait"]
            trait_display = (
                _truncate(en_trait) if en_trait else _truncate(r["trait_text"], 60)
            )
            rows.append([
                e(r["zodiac_id"]),
                e(r["name"]),
                e(r["float_count"]),
                e(r["pairs_count"]),
                e(r["constellation_name"]),
                e(trait_display),
            ])

        return table(meta, headers, rows)


class ZodiacSignOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_zodiacsignoffset_records(data)
        return [
            {"zodiac_id": rec["zodiac_id"], "data_offset": rec["data_offset"]}
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
            [e(r["zodiac_id"]), e(f"0x{r['data_offset']:08X}")]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


class ZodiacSignOrderHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/zodiacsignorderoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("zodiacsignorderoffset.dbss")
        if offset_raw is None:
            raise ValueError("zodiacsignorderoffset.dbss companion not found.")

        records = parse_zodiacsignorder_records(data, offset_raw)
        if not records:
            return []

        unique_majors = list({rec["personality_type"] // 100 for rec in records})
        loc_names, _ = resolve_loc_type7(unique_majors)

        result: list[dict] = []
        for rec in records:
            pt = rec["personality_type"]
            major = pt // 100
            variant = pt % 100
            result.append({
                "row":              rec["row"],
                "personality_type": pt,
                "zodiac_name":      loc_names.get(major, f"#{major}"),
                "variant":          variant,
                "trigger_count":    rec["trigger_count"],
                "trigger_order":    rec["trigger_order"],
                "sequence":         "→".join(str(s) for s in rec["trigger_order"]),
            })

        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} order records"
        rows = [
            [
                e(r["row"]),
                e(r["personality_type"]),
                e(r["zodiac_name"]),
                e(r["variant"]),
                e(r["trigger_count"]),
                e(r["sequence"]),
            ]
            for r in slice_
        ]
        # Add "Row" column that was present in the original render()
        headers: list[tuple[str, str, str]] = [
            ("Row",          "num", ""),
        ] + _ORDER_HEADERS
        return table(meta, headers, rows)


class ZodiacSignOrderOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_zodiacsignorderoffset_records(data)
        return [
            {"personality_type": rec["personality_type"], "data_offset": rec["data_offset"]}
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
            [e(r["personality_type"]), e(f"0x{r['data_offset']:08X}")]
            for r in slice_
        ]
        return table(meta, _ORDER_OFFSET_HEADERS, rows)


