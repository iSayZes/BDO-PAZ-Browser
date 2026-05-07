from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import strip_pa_tags

from _common.binary import parse_offset_table
from _common.html import debug_cell, e, error, table
from .parser import extract_titlebuff_records, find_title_effects_en


_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("Buff ID", "num", ""),
    ("Offset", "num", ""),
]

_BUFF_HEADERS: list[tuple[str, str, str]] = [
    ("Level", "num", ""),
    ("Required Titles", "num", ""),
    ("EN Buff Text", "", ""),
    ("KR Buff Text", "", ""),
    ("Offset", "num", ""),
]


class TitleBuffListOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_map = parse_offset_table(data)
        return [
            {"buff_id": buff_id, "offset": offset}
            for buff_id, (offset, size) in sorted(offset_map.items())
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} entries"
        rows = [
            [e(r["buff_id"]), e(f"0x{r['offset']:08X}")]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


class TitleBuffListHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/titlebufflistoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("titlebufflistoffset.dbss")
        if offset_raw is None:
            raise ValueError("titlebufflistoffset.dbss companion not found — cannot parse blocks.")

        offset_map = parse_offset_table(offset_raw)
        records = extract_titlebuff_records(data, offset_map)
        en_effects = find_title_effects_en()

        result: list[dict] = []
        for rec in records:
            debug_u32 = rec["debug_u32"]
            required_titles = debug_u32["u32_04"]
            result.append({
                "level": debug_u32["u32_00"] + 1,
                "required_titles": required_titles,
                "en_text": en_effects.get(required_titles, ""),
                "kr_text": rec["raw_text"],
                "offset": rec["offset"],
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

        has_en = any(r["en_text"] for r in records)
        meta = f"{len(records):,} buff blocks decoded" + ("  ·  EN effects from loc" if has_en else "")

        rows: list[list] = []
        for r in slice_:
            en_raw = r["en_text"]
            rows.append([
                e(r["level"]),
                e(r["required_titles"]),
                e(strip_pa_tags(en_raw)) if en_raw else "—",
                e(r["kr_text"]),
                e(f"0x{r['offset']:08X}"),
            ])

        return table(meta, _BUFF_HEADERS, rows)
