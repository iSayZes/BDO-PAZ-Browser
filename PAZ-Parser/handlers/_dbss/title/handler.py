from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags

from ..common.binary import parse_offset_table, u32_hi, u32_lo
from ..common.constants import DEFAULT_PA_COLOR
from ..common.html import color_cell, debug_cell, e, error, table
from .parser import extract_title_records
from .styles import STYLE_NAMES, U32_20_STYLE_MAP, packed_word_cell, style_key


_HEADERS_BASE: list[tuple[str, str, str]] = [
    ("Layout", "", ""),
    ("Title ID", "num", ""),
    ("Style?", "num", ""),
    ("Style Label", "", ""),
    ("Style Offset", "num", ""),
    ("u32_04 Hex", "num", ""),
    ("u32_20 Hex", "num", ""),
    ("u32_20 Dec", "num", ""),
    ("u32_20 Hi", "num", ""),
    ("u32_20 Lo", "num", ""),
    ("Display Style Key", "", ""),
    ("Display Style", "", ""),
    ("u32_14 Hex", "num", ""),
    ("u32_14 Dec", "num", ""),
    ("u32_18 Hex", "num", ""),
    ("u32_18 Dec", "num", ""),
    ("u32_14 Hi", "num", ""),
    ("u32_14 Lo", "num", ""),
    ("Packed Candidates", "", ""),
    ("First PAColor Offset", "num", ""),
    ("PAColor Raw", "", ""),
    ("PAColor Visible", "", ""),
]

_HEADERS_LOC: list[tuple[str, str, str]] = [
    ("EN Name", "", ""),
    ("EN Req", "", ""),
]

_HEADERS_TAIL: list[tuple[str, str, str]] = [
    ("PAColor Tags", "", ""),
    ("Debug u32 Fields", "", ""),
]


class TitleDbssHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/titleoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("titleoffset.dbss")
        if offset_raw is None:
            raise ValueError("titleoffset.dbss companion not found — cannot parse blocks.")

        offset_map = parse_offset_table(offset_raw)
        records = extract_title_records(data, offset_map)

        result: list[dict] = []
        for rec in records:
            row: dict = dict(rec)
            if is_loc_loaded():
                row["en_name"] = loc_lookup(1, rec["title_id"])
                row["en_req"] = strip_pa_tags(loc_lookup(1, rec["title_id"], 0, 0, 1))
            result.append(row)

        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]

        has_loc = "en_name" in records[0] if records else is_loc_loaded()
        headers = _HEADERS_BASE + (_HEADERS_LOC if has_loc else []) + _HEADERS_TAIL

        meta = f"{len(records):,} blocks decoded"

        rows: list[list] = []
        for record in slice_:
            debug_u32 = record["debug_u32"]
            u32_20 = debug_u32["u32_20"]
            u32_14 = debug_u32["u32_14"]
            current_style_key = style_key(u32_20)
            visible_colors = [
                color
                for color in record["pa_colors"]
                if color.lower() != DEFAULT_PA_COLOR
            ]
            style_name = STYLE_NAMES.get(
                record["style_value"],
                f"Unknown ({record['style_value']})",
            )
            style_desc = U32_20_STYLE_MAP.get(current_style_key, "Unknown pattern")

            row: list = [
                e(record["layout"]),
                e(record["title_id"]),
                e(record["style_value"]),
                e(style_name),
                e(f"0x{record['style_offset']:02X}"),
                e(f"0x{debug_u32['u32_04']:08X}"),
                e(f"0x{u32_20:08X}"),
                e(u32_20),
                e(u32_hi(u32_20)),
                e(u32_lo(u32_20)),
                e(current_style_key),
                e(style_desc),
                e(f"0x{u32_14:08X}"),
                e(u32_14),
                e(f"0x{debug_u32['u32_18']:08X}"),
                e(debug_u32["u32_18"]),
                e(u32_hi(u32_14)),
                e(u32_lo(u32_14)),
                packed_word_cell(debug_u32, record["first_pa_color_offset"]),
                e("—" if record["first_pa_color_offset"] is None else f"0x{record['first_pa_color_offset']:02X}"),
                color_cell(record["pa_colors"]),
                color_cell(visible_colors),
            ]

            if has_loc:
                row += [
                    e(record.get("en_name", "")),
                    e(record.get("en_req", "")),
                ]

            row += [
                color_cell(visible_colors),
                debug_cell(debug_u32, record["style_offset"]),
            ]

            rows.append(row)

        return table(meta, headers, rows)
