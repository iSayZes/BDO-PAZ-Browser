"""`musiclevel.dbss`: the music levels, their EXP, bar and note counts and rank letters.

    u32 count | u32 unknown_04 | count x (u32 key_prefix | row)
    row: u32 music_level | u64 music_level_exp | u32 increasing_bar_number
         | u32 increasing_note_number | str16 music_rank

`musicleveloffset.dbss` (u32 count, then u32 music_level, u32 offset, u32
size per row) points at each row past its key prefix. Layout 1 in
docs/file-formats/dbss/musiclevel_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "musiclevel.dbss"
OFFSET_FILE = "musicleveloffset.dbss"
KEY_FIELD = "music_level"
# The two counts before the first entry.
HEADER_SIZE = 8

_HEAD = struct.Struct("<IIQII")


def _read_entry(reader: RecordReader) -> dict:
    key_prefix, music_level, exp, bars, notes = reader.unpack(_HEAD)
    return {
        KEY_FIELD: music_level,
        "key_prefix": key_prefix,
        "music_level_exp": exp,
        "increasing_bar_number": bars,
        "increasing_note_number": notes,
        "music_rank": reader.text(wide=True),
    }


def parse_musiclevel_records(data: bytes) -> list[dict]:
    """Every level in file order.

    Raises ValueError when the file is too short for its two counts, an
    entry runs past the file or the entries end before it.
    """
    if len(data) < HEADER_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its two counts")
    reader = RecordReader(data, HEADER_SIZE, len(data), FILE_NAME)
    records = [_read_entry(reader) for _ in range(u32(data, 0))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} entries end at 0x{reader.pos:X}, the file at 0x{len(data):X}")
    return records


def parse_musicleveloffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: music level, offset and size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)
