"""`zodiacsign.dbss`: the 12 zodiac signs, walked record by record from the counts.

    u32 count | count x record

    record: u8 zodiac_id | u32 float_count | f32[float_count][3] star_positions
            | u32 pairs_count | u16[pairs_count][2] star_pairs
            | str16 name_kr | str16 trait_text | str16 icon_small | str16 icon_large
            | 13-byte tail (u8 x3, u16 next_zodiac_id, u8 x4, u32)

Every string is a u64 UTF-16 code-unit count plus UTF-16LE text. The records
run back to back and the last one ends at end of file. Full layout in
docs/file-formats/dbss/zodiacsign_dbss.md.
"""
from __future__ import annotations

import struct

from _common.record_reader import RecordReader
from .model import ZodiacSignRecord

_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")

_STAR_POSITION_SIZE = 12  # f32 x, y and a constant 1.0
_STAR_PAIR_SIZE = 4  # u16 a, u16 b
# zodiac_id_dup, zodiac_id_dup2 and unknown_tail_02 before next_zodiac_id.
_TAIL_HEAD_SIZE = 3
# unknown_tail_05 to unknown_tail_08 and the u32 unknown_end after it.
_TAIL_END_SIZE = 8


def _read_record(reader: RecordReader, row: int) -> ZodiacSignRecord:
    (zodiac_id,) = reader.unpack(_U8)
    (float_count,) = reader.unpack(_U32)
    reader.skip(float_count * _STAR_POSITION_SIZE)
    (pairs_count,) = reader.unpack(_U32)
    reader.skip(pairs_count * _STAR_PAIR_SIZE)
    constellation_name = reader.text(wide=True)
    trait_text = reader.text(wide=True)
    icon_small = reader.text(wide=True)
    icon_large = reader.text(wide=True)
    reader.skip(_TAIL_HEAD_SIZE)
    (next_zodiac_id,) = reader.unpack(_U16)
    reader.skip(_TAIL_END_SIZE)
    return ZodiacSignRecord(
        row=row,
        zodiac_id=zodiac_id,
        float_count=float_count,
        pairs_count=pairs_count,
        constellation_name=constellation_name,
        trait_text=trait_text,
        icon_small=icon_small,
        icon_large=icon_large,
        next_zodiac_id=next_zodiac_id,
    )


def parse_zodiacsign_records(data: bytes) -> list[ZodiacSignRecord]:
    """Every record in file order.

    Raises ValueError when a record runs past the file or bytes are left after
    the last one, since the layout would then have changed.
    """
    reader = RecordReader(data, 0, len(data), "zodiacsign.dbss")
    (count,) = reader.unpack(_U32)
    records = [_read_record(reader, row) for row in range(count)]
    if not reader.at_end():
        raise ValueError(f"zodiacsign.dbss has {reader.remaining()} bytes after its {count} records")
    return records
