"""`guildhouseinfo.dbss`: the guild houses, their town, node and uses.

    u32 count | count x row
    row: u16 affiliated_town | u32 parent_node_key | u32 craft_count
         | craft_count x (u32 receipe_key, u32 level)
         | u16 character_key | u16 unknown_crafts_02

The row key sits after the crafts. `guildhouseinfooffset.dbss` (u32 count,
then u16 character key, offset and size per row) points at the row start.
Layout 1 in docs/file-formats/dbss/guildhouseinfo_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "guildhouseinfo.dbss"
OFFSET_FILE = "guildhouseinfooffset.dbss"
KEY_FIELD = "character_key"

_HEAD = struct.Struct("<HII")
_CRAFT = struct.Struct("<II")
_TAIL = struct.Struct("<HH")


def _read_row(reader: RecordReader) -> dict:
    affiliated_town, parent_node_key, craft_count = reader.unpack(_HEAD)
    crafts = [dict(zip(("receipe_key", "level"), reader.unpack(_CRAFT))) for _ in range(craft_count)]
    character_key, unknown_crafts_02 = reader.unpack(_TAIL)
    return {
        KEY_FIELD: character_key,
        "affiliated_town": affiliated_town,
        "parent_node_key": parent_node_key,
        "crafts": crafts,
        "unknown_crafts_02": unknown_crafts_02,
    }


def parse_guildhouseinfo_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_guildhouseinfooffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
