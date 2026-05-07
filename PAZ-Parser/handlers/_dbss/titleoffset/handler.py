from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import parse_offset_table
from _common.html import e, table


_HEADERS: list[tuple[str, str, str]] = [
    ("Title ID", "num", ""),
    ("Offset",   "num", ""),
]


class TitleOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_map = parse_offset_table(data)
        return [
            {"title_id": title_id, "offset": offset}
            for title_id, (offset, size) in sorted(offset_map.items())
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
            [e(r["title_id"]), e(f"0x{r['offset']:08X}")]
            for r in slice_
        ]
        return table(meta, _HEADERS, rows)
