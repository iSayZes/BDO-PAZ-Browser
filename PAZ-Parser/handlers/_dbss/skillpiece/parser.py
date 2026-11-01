"""`skillpiece.dbss`: the set effect tiers of each set skill.

A u32 count, then the records back to back to the end of the file. A record is
a u16 key prefix, the u16 set skill number, a u16 skill property, a u32 tier
count, the tiers and a zero u32. A tier is a u32 point threshold, the u16 `skill.dbss` level and three
u64-prefixed UTF-16 strings: set title, threshold label and bonus lines.
`skillpieceoffset.dbss` points 2 bytes into each record, past the key prefix,
so the walk from the start needs no index. Layout in
docs/file-formats/dbss/skillpiece_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.inline_text import decode_inline_text
from _common.record_reader import RecordReader


FILE_NAME = "skillpiece.dbss"
OFFSET_FILE = "skillpieceoffset.dbss"

_COUNT = struct.Struct("<I")
_KEY_PREFIX = struct.Struct("<H")
_HEAD = struct.Struct("<HHI")  # skill_no, skill_property, tier_count
_TIER_HEAD = struct.Struct("<IH")  # point, level
_END = struct.Struct("<I")


def parse_skillpiece_records(data: bytes) -> list[dict]:
    """Every set skill record with its tiers, in file order.

    Raises ValueError when a record runs past the file, its key prefix is not
    its skill number, or the records do not end where the file does.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")

    count = u32(data, 0)
    pos = _COUNT.size
    records: list[dict] = []
    for _ in range(count):
        record, pos = _parse_record(data, pos)
        records.append(record)
    if pos != len(data):
        raise ValueError(f"{FILE_NAME} has {len(data) - pos:,} bytes after its {count:,} records")
    return records


def _parse_record(data: bytes, start: int) -> tuple[dict, int]:
    reader = RecordReader(data, start, len(data), f"{FILE_NAME} record at 0x{start:X}")
    (key_prefix,) = reader.unpack(_KEY_PREFIX)
    skill_no, skill_property, tier_count = reader.unpack(_HEAD)
    if key_prefix != skill_no:
        raise ValueError(f"{FILE_NAME} record at 0x{start:X} has key {key_prefix} for skill {skill_no}")

    tiers = [_parse_tier(reader) for _ in range(tier_count)]
    (unknown_end,) = reader.unpack(_END)
    record = {
        "skill_no": skill_no,
        "skill_property": skill_property,
        "offset": start,
        "size": reader.pos - start,
        "tiers": tiers,
        "unknown_end": unknown_end,
    }
    return record, reader.pos


def _parse_tier(reader: RecordReader) -> dict:
    point, level = reader.unpack(_TIER_HEAD)
    return {
        "point": point,
        "level": level,
        "group_title_kr": decode_inline_text(reader.text(wide=True)),
        "desc_title_kr": decode_inline_text(reader.text(wide=True)),
        "desc_kr": decode_inline_text(reader.text(wide=True)),
    }
