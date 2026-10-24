"""`form.dbss`: the forms (looks) of horses and other mounts.

    u32 count | count x row
    row: u16 index | u16 index_dup | u8 type | u32 action_index | u16 tier
         | str16 icon_1 | str16 icon_2
         | u32 character_key_count | character_key_count x u16 character_keys

`formoffset.dbss` (u32 count, then u16 index, offset and size per row)
points 2 bytes into a row, at `index_dup`. Layout 2 in
docs/file-formats/form_dbss.md; clients without the character key list
(Layout 1) are not read.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "form.dbss"
OFFSET_FILE = "formoffset.dbss"
KEY_FIELD = "index"

_HEAD = struct.Struct("<HHBIH")
_HEAD_FIELDS = (KEY_FIELD, "index_dup", "type", "action_index", "tier")
_U32 = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    head: dict[str, object] = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    icon_1 = reader.text(wide=True)
    icon_2 = reader.text(wide=True)
    (count,) = reader.unpack(_U32)
    character_keys = list(reader.unpack(struct.Struct(f"<{count}H")))
    return {**head, "icon_1": icon_1, "icon_2": icon_2, "character_keys": character_keys}


def parse_form_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_formoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
