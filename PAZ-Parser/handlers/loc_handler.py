from __future__ import annotations

import html as _html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import struct

from bdo_models import PazEntry
from bdo_preview import PreviewHandler, register_handler
from _common.loc import decompress_loc
from _dbss.common.binary import u32


def _u16(data: bytes, pos: int) -> int:
    return struct.unpack_from("<H", data, pos)[0]


def _u8(data: bytes, pos: int) -> int:
    return data[pos]


def _parse_all_loc_records(raw: bytes) -> list[tuple[int, int, int, int, int, int, str]]:
    """Parse all loc records: (str_size, str_type, str_id1, str_id2, str_id3, str_id4, text)."""
    data = decompress_loc(raw)
    if data is None:
        return []

    records: list[tuple[int, int, int, int, int, int, str]] = []
    pos = 0

    while pos + 16 <= len(data):
        str_size = u32(data, pos)
        str_type = u32(data, pos + 4)
        str_id1  = u32(data, pos + 8)
        str_id2  = _u16(data, pos + 12)
        str_id3  = _u8(data, pos + 14)
        str_id4  = _u8(data, pos + 15)

        text_start = pos + 16
        text_end   = text_start + str_size * 2

        if text_end + 4 > len(data):
            break

        text = data[text_start:text_end].decode("utf-16-le", errors="replace")
        records.append((str_size, str_type, str_id1, str_id2, str_id3, str_id4, text))
        pos = text_end + 4

    return records


class LocHandler(PreviewHandler):
    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict] | None:
        raw = _parse_all_loc_records(data)
        if not raw:
            return None
        return [
            {"str_type": t, "str_id1": i1, "str_id2": i2, "str_id3": i3, "str_id4": i4, "text": text}
            for (_, t, i1, i2, i3, i4, text) in raw
        ]

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        total = len(records)
        start = page * page_size
        end   = min(start + page_size, total)
        rows_html = "".join(
            f"<tr>"
            f"<td>{_html.escape(str(r['str_type']))}</td>"
            f"<td>{_html.escape(str(r['str_id1']))}</td>"
            f"<td>{_html.escape(str(r['str_id2']))}</td>"
            f"<td>{r['str_id3']}</td>"
            f"<td>{r['str_id4']}</td>"
            f"<td class='loc-text'>{_html.escape(r['text'])}</td>"
            f"</tr>"
            for r in records[start:end]
        )
        return f"""
<div class="loc-view">
  <div class="loc-header">
    <span class="loc-count">Showing {start + 1:,}–{end:,} of {total:,} strings</span>
  </div>
  <table class="loc-table">
    <thead>
      <tr>
        <th>Type</th>
        <th>ID 1</th>
        <th>ID 2</th>
        <th>ID 3</th>
        <th>ID 4</th>
        <th>Text</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>
</div>
"""

    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        from bdo_preview import PARSED_RECORDS_PER_PAGE
        records = self.get_records(data, entry, companions)
        if records is None:
            return '<div class="error">Failed to parse .loc file — not a valid LOC or decompression failed.</div>'
        return self.render_records_page(records, 0, PARSED_RECORDS_PER_PAGE)


register_handler(".loc", LocHandler())
