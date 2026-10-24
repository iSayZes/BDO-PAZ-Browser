"""`charactervoice.bss`: the voices a character can pick, per appearance type.

    PABR | u32 record_count | record_count x row | String Table
    | u32 string_table_start | u32 0
    row: u16 character_key | 2 x (u32 voice_type_count | voice_type_count x u32 voice_types)
         | u32 voice_count[2]

Each `voice_types` entry indexes the string table (`PC_VCE_1Warrior_1`).
The two lists and counts are appearance types 0 and 1. Layout 2 in
docs/file-formats/charactervoice_bss.md; client 794 (Layout 1) stores the
names inline and is not read.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "charactervoice.bss"
KEY_FIELD = "character_key"
APPEARANCE_TYPES = 2

_COUNT_OFFSET = 4
_KEY = struct.Struct("<H")
_U32 = struct.Struct("<I")
_VOICE_COUNTS = struct.Struct(f"<{APPEARANCE_TYPES}I")


def _read_voice_types(reader: RecordReader) -> list[int]:
    (count,) = reader.unpack(_U32)
    return list(reader.unpack(struct.Struct(f"<{count}I")))


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    (character_key,) = reader.unpack(_KEY)
    voice_types = [_read_voice_types(reader) for _ in range(APPEARANCE_TYPES)]
    return {
        KEY_FIELD: character_key,
        "voice_types": voice_types,
        "voice_names": [[string_at(strings, index) for index in indexes] for indexes in voice_types],
        "voice_count": list(reader.unpack(_VOICE_COUNTS)),
    }


def parse_charactervoice_records(data: bytes) -> list[dict]:
    """Every row in file order, with the voice names its indexes point at.

    Raises ValueError on a missing magic, a row that runs into the string
    table or rows that end before it, or a string table that runs past the
    trailer.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    records = [_read_row(reader, strings) for _ in range(u32(data, _COUNT_OFFSET))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X}, the string table starts at 0x{rows_end:X}")
    return records
