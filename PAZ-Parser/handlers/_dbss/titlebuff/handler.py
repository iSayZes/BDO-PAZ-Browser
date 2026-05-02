from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import strip_pa_tags

from ..common.binary import parse_offset_table
from ..common.html import debug_cell, e, error, table
from .parser import extract_titlebuff_records, find_title_effects_en


class TitleBuffListOffsetHandler(PreviewHandler):
    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        offset_map = parse_offset_table(data)
        meta = f"{len(offset_map):,} entries  ·  {len(data):,} B"

        headers = [
            ("Buff ID", "num", ""),
            ("Offset", "num", ""),
            ("Size (B)", "num", ""),
        ]

        rows = [
            [
                e(buff_id),
                e(f"0x{offset:08X}"),
                e(size),
            ]
            for buff_id, (offset, size) in sorted(offset_map.items())
        ]

        return table(meta, headers, rows)


class TitleBuffListHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]

        return [
            f"{folder}/titlebufflistoffset.dbss",
            f"{folder}/languagedata_en.loc",
        ]

    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        offset_raw = companions.get("titlebufflistoffset.dbss")
        loc_raw = companions.get("languagedata_en.loc")

        if offset_raw is None:
            return error("titlebufflistoffset.dbss companion not found — cannot parse blocks.")

        offset_map = parse_offset_table(offset_raw)
        records = extract_titlebuff_records(data, offset_map)
        en_effects = find_title_effects_en(loc_raw) if loc_raw else {}

        meta = (
            f"{len(records):,} buff blocks decoded  ·  {len(data):,} B"
            + ("  ·  EN effects from loc" if en_effects else "")
        )

        headers = [
            ("Level", "num", ""),
            ("Required Titles", "num", ""),
            ("EN Buff Text", "", ""),
            ("KR Buff Text", "", ""),
            ("Offset", "num", ""),
            ("Debug u32 Fields", "", ""),
        ]

        rows: list[list] = []

        for record in records:
            debug_u32 = record["debug_u32"]
            internal_id = debug_u32["u32_00"]
            required_titles = debug_u32["u32_04"]
            en_text = en_effects.get(required_titles, "")

            rows.append([
                e(internal_id + 1),
                e(required_titles),
                e(strip_pa_tags(en_text)) if en_text else "—",
                e(record["raw_text"]),
                e(f"0x{record['offset']:08X}"),
                debug_cell(record["debug_u32"], -1),
            ])

        return table(meta, headers, rows)
