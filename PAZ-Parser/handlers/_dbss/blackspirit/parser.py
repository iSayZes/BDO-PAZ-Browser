"""`blackspirit.dbss`: the Black Spirit forms and the condition that unlocks each.

    u32 count | count x (u8 index | str16 condition)

`blackspiritoffset.dbss` (u32 count, then u8 index, offset and size per
row) points at the row start. Layout 1 in
docs/file-formats/dbss/blackspirit_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_u8_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "blackspirit.dbss"
OFFSET_FILE = "blackspiritoffset.dbss"
KEY_FIELD = "index"

_INDEX = struct.Struct("<B")


def _read_row(reader: RecordReader) -> dict:
    (index,) = reader.unpack(_INDEX)
    return {KEY_FIELD: index, "condition": reader.text(wide=True)}


def parse_blackspirit_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_blackspiritoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u8_offset_rows(data)
