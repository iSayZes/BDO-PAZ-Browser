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
    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        records = _parse_all_loc_records(data)
        if not records:
            return '<div class="error">Failed to parse .loc file — not a valid LOC or decompression failed.</div>'

        total = len(records)
        rows_html = "".join(
            f"<tr>"
            f"<td>{_html.escape(str(str_id1))}</td>"
            f"<td>{_html.escape(str(str_id2))}</td>"
            f"<td>{str_id3:02X}·{str_id4:02X}</td>"
            f"<td>{_html.escape(str(str_type))}</td>"
            f"<td class='loc-text'>{_html.escape(text)}</td>"
            f"</tr>"
            for (_, str_type, str_id1, str_id2, str_id3, str_id4, text) in records
        )

        return f"""
<div class="loc-view">
  <div class="loc-header">
    <span class="loc-count">{total:,} strings</span>
    <input id="loc-search" type="text" placeholder="Filter strings…" oninput="locFilter(this.value)" autocomplete="off">
  </div>
  <table id="loc-table" class="loc-table">
    <thead>
      <tr>
        <th>ID 1</th>
        <th>ID 2</th>
        <th>ID 3·4</th>
        <th>Type</th>
        <th>Text</th>
      </tr>
    </thead>
    <tbody id="loc-body">
      {rows_html}
    </tbody>
  </table>
  <div id="loc-no-results" class="loc-no-results" style="display:none">No matching strings.</div>
</div>
<script>
(function() {{
  function locFilter(q) {{
    q = q.toLowerCase();
    var rows = document.getElementById('loc-body').rows;
    var shown = 0;
    for (var i = 0; i < rows.length; i++) {{
      var text = rows[i].cells[4].textContent.toLowerCase();
      var id1  = rows[i].cells[0].textContent;
      var match = !q || text.indexOf(q) !== -1 || id1.indexOf(q) !== -1;
      rows[i].style.display = match ? '' : 'none';
      if (match) shown++;
    }}
    document.getElementById('loc-no-results').style.display = shown === 0 ? '' : 'none';
  }}
  window.locFilter = locFilter;
}})();
</script>
"""


register_handler(".loc", LocHandler())
