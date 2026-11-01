"""`emoticon.dbss`: the chat emoticons (emoji) and their icons.

    u32 count | count x row
    row: u32 emoticon_key | u32 unknown_04 | str16 icon_path | u8 icon_count
         | u32 row_count | u32 column_count | str16 keyword_kr
         | str16 sequence_path | u8 group | str16 name_kr | u32 unknown_name_kr_00

`emoticonoffset.dbss` (u32 count, then u32 key, u32 unknown_04, u32 offset
and u32 size per row) points at the row start. Layout 1 in
docs/file-formats/dbss/emoticon_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import counted_row_values, read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "emoticon.dbss"
OFFSET_FILE = "emoticonoffset.dbss"
KEY_FIELD = "emoticon_key"

_HEAD = struct.Struct("<II")
_GRID = struct.Struct("<BII")
_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
_OFFSET_ROW = struct.Struct("<IIII")
_OFFSET_FIELDS = (KEY_FIELD, "unknown_04", "data_offset", "data_size")


def _read_row(reader: RecordReader) -> dict:
    emoticon_key, unknown_04 = reader.unpack(_HEAD)
    icon_path = reader.text(wide=True)
    icon_count, row_count, column_count = reader.unpack(_GRID)
    keyword_kr = reader.text(wide=True)
    sequence_path = reader.text(wide=True)
    (group,) = reader.unpack(_U8)
    name_kr = reader.text(wide=True)
    (unknown_name_kr_00,) = reader.unpack(_U32)
    return {
        KEY_FIELD: emoticon_key,
        "unknown_04": unknown_04,
        "icon_path": icon_path,
        "icon_count": icon_count,
        "row_count": row_count,
        "column_count": column_count,
        "keyword_kr": keyword_kr,
        "sequence_path": sequence_path,
        "group": group,
        "name_kr": name_kr,
        "unknown_name_kr_00": unknown_name_kr_00,
    }


def parse_emoticon_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_emoticonoffset_records(data: bytes) -> list[dict]:
    """Every index row. Raises ValueError when the rows do not fill the file."""
    return [dict(zip(_OFFSET_FIELDS, values, strict=True)) for values in counted_row_values(data, _OFFSET_ROW, OFFSET_FILE)]
