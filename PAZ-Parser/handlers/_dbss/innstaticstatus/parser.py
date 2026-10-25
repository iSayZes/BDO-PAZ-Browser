"""`innstaticstatus.dbss`: the inns and the house characters that are rooms of each.

    u32 count | count x row
    row: u16 inn_key | u32 room_count | room_count x u16 room key

`innstaticstatusoffset.dbss` (u32 count, then u16 key, offset and size per
row) points 2 bytes into a row, at `room_count`. Layout 1 in
docs/file-formats/dbss/innstaticstatus_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "innstaticstatus.dbss"
OFFSET_FILE = "innstaticstatusoffset.dbss"
KEY_FIELD = "inn_key"

_HEAD = struct.Struct("<HI")
_ROOM_KEY_SIZE = 2


def _read_row(reader: RecordReader) -> dict:
    inn_key, room_count = reader.unpack(_HEAD)
    if room_count * _ROOM_KEY_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME}: inn {inn_key} lists {room_count:,} rooms, more than the file holds")
    return {KEY_FIELD: inn_key, "room_keys": list(reader.unpack(struct.Struct(f"<{room_count}H")))}


def parse_innstaticstatus_records(data: bytes) -> list[dict]:
    """Every inn in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_innstaticstatusoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
