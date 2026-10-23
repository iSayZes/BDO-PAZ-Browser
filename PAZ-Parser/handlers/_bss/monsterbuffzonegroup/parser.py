"""`monsterbuffzonegroup.bss`: per region the structure monsters and their listed characters.

    u32 count | count x Row
    Row:   u16 region_key | u32 unknown_02 | u8 unknown_06 | u32 entry_count | entry_count x Entry
    Entry: u16 character_key | u8 unknown_02 | u16 character_key_dup | u16 unknown_05
           | u32 character_count | u16[character_count] character_keys

Layout 1 in docs/file-formats/monsterbuffzonegroup_bss.md.
"""

from __future__ import annotations

import struct
from typing import Any

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "monsterbuffzonegroup.bss"

_ROW_HEAD = struct.Struct("<HIBI")
_ENTRY_HEAD = struct.Struct("<HBHHI")
_ENTRY_FIELDS = ("character_key", "unknown_02", "character_key_dup", "unknown_05", "character_count")


def _read_entry(reader: RecordReader) -> dict:
    entry: dict[str, Any] = dict(zip(_ENTRY_FIELDS, reader.unpack(_ENTRY_HEAD), strict=True))
    entry["character_keys"] = list(reader.unpack(struct.Struct(f"<{entry['character_count']}H")))
    return entry


def _read_row(reader: RecordReader) -> dict:
    region_key, unknown_02, unknown_06, entry_count = reader.unpack(_ROW_HEAD)
    return {
        "region_key": region_key,
        "unknown_02": unknown_02,
        "unknown_06": unknown_06,
        "entry_count": entry_count,
        "entries": [_read_entry(reader) for _ in range(entry_count)],
    }


def parse_monsterbuffzonegroup_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not end at the last byte."""
    return read_counted_records(data, _read_row, FILE_NAME)
