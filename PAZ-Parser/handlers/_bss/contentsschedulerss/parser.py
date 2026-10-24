"""`contentsschedulerss.bss`: the contents a player can add to the Contents Schedule window.

    u32 count | count x Row
    Row: u8 content_type | str8 title | str8 icon_texture
         | u32 contents_group_count | u32[contents_group_count] contents_group_hashes

`title` is a `RESOURCE` sheet key, `icon_texture` a texture key. Layout 1 in
docs/file-formats/contentsschedulerss_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records, read_counted_u32s
from _common.record_reader import RecordReader


FILE_NAME = "contentsschedulerss.bss"
_CONTENT_TYPE = struct.Struct("<B")


def _read_row(reader: RecordReader) -> dict:
    (content_type,) = reader.unpack(_CONTENT_TYPE)
    title = reader.text(wide=False)
    icon_texture = reader.text(wide=False)
    hashes = read_counted_u32s(reader, f"{FILE_NAME} contents group")
    return {
        "content_type": content_type,
        "title": title,
        "icon_texture": icon_texture,
        "contents_group_count": len(hashes),
        "contents_group_hashes": hashes,
    }


def parse_contentsschedulerss_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not end at the last byte."""
    return read_counted_records(data, _read_row, FILE_NAME)
