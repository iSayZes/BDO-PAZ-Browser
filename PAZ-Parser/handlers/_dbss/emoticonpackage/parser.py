"""`emoticonpackage.dbss`: the emoticon packages and the emoticons each one unlocks.

    u32 count | count x row
    row: u32 package_key | u32 unknown_04 | str16 name_kr | u32 emoticon_count
         | emoticon_count x (u32 emoticon_key, u32 unknown_04)

`emoticonpackageoffset.dbss` (u32 count, then u32 key, u32 unknown_04, u32
offset and u32 size per row) points at the row start. Layout 1 in
docs/file-formats/emoticonpackage_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import counted_row_values, read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "emoticonpackage.dbss"
OFFSET_FILE = "emoticonpackageoffset.dbss"
KEY_FIELD = "package_key"

_HEAD = struct.Struct("<II")
_U32 = struct.Struct("<I")
_EMOTICON = struct.Struct("<II")
_OFFSET_ROW = struct.Struct("<IIII")
_OFFSET_FIELDS = (KEY_FIELD, "unknown_04", "data_offset", "data_size")


def _read_row(reader: RecordReader) -> dict:
    package_key, unknown_04 = reader.unpack(_HEAD)
    name_kr = reader.text(wide=True)
    (emoticon_count,) = reader.unpack(_U32)
    emoticons = [dict(zip(("emoticon_key", "unknown_04"), reader.unpack(_EMOTICON))) for _ in range(emoticon_count)]
    return {KEY_FIELD: package_key, "unknown_04": unknown_04, "name_kr": name_kr, "emoticons": emoticons}


def parse_emoticonpackage_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_emoticonpackageoffset_records(data: bytes) -> list[dict]:
    """Every index row. Raises ValueError when the rows do not fill the file."""
    return [dict(zip(_OFFSET_FIELDS, values, strict=True)) for values in counted_row_values(data, _OFFSET_ROW, OFFSET_FILE)]
