"""`skillawakeningability.dbss`: the Skill Add-on effects, one row per ability index.

    u32 count | count x Row
    Row: u32 ability_index | u32 ability_index_dup | u32 buff_id
         | str16 description_kr | u32 unknown_description_kr_00

`skillawakeningabilityoffset.dbss` (u32 count, then u32 ability index, offset
and size per row) points 4 bytes into a row, at `ability_index_dup`. Layout 2
in docs/file-formats/skillawakeningability_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "skillawakeningability.dbss"
OFFSET_FILE = "skillawakeningabilityoffset.dbss"
KEY_FIELD = "ability_index"

_HEAD = struct.Struct("<3I")
_TAIL = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    ability_index, ability_index_dup, buff_id = reader.unpack(_HEAD)
    description_kr = reader.text(wide=True)
    (unknown_description_kr_00,) = reader.unpack(_TAIL)
    return {
        KEY_FIELD: ability_index,
        "ability_index_dup": ability_index_dup,
        "buff_id": buff_id,
        "description_kr": description_kr,
        "unknown_description_kr_00": unknown_description_kr_00,
    }


def parse_skillawakeningability_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_skillawakeningabilityoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)
