from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from ..common.binary import parse_offset_table
from ..common.html import e, table


class TitleOffsetHandler(PreviewHandler):
    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        offset_map = parse_offset_table(data)
        meta = f"{len(offset_map):,} entries  ·  {len(data):,} B"

        headers = [
            ("Title ID", "num", ""),
            ("Offset", "num", ""),
            ("Size (B)", "num", ""),
        ]

        rows = [
            [e(title_id), e(f"0x{offset:08X}"), e(size)]
            for title_id, (offset, size) in sorted(offset_map.items())
        ]

        return table(meta, headers, rows)
