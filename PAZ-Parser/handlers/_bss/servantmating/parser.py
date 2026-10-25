"""`servantmating.bss`: horse breeding grade bands.

    u32 count | count x 20-byte Row, ending at EOF
    Row: u32 key | u32 key_dup | u16 average_grade | u16 result_max_grade
         | u16 result_min_grade | u16 imperial_steed_character_id
         | u32 imperial_steed_rate

Layout 2 in docs/file-formats/bss/servantmating_bss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "servantmating.bss"

_COUNT = struct.Struct("<I")
_ROW = struct.Struct("<IIHHHHI")


def parse_servantmating_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when the rows do not end exactly at EOF or a row's
    `key_dup` differs from its `key`.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")
    (count,) = _COUNT.unpack_from(data)
    rows_end = _COUNT.size + count * _ROW.size
    if rows_end != len(data):
        raise ValueError(f"{FILE_NAME} declares {count} rows ending at 0x{rows_end:X}, the file ends at 0x{len(data):X}")

    records = []
    for pos in range(_COUNT.size, rows_end, _ROW.size):
        key, key_dup, average_grade, max_grade, min_grade, steed_id, steed_rate = _ROW.unpack_from(data, pos)
        if key_dup != key:
            raise ValueError(f"{FILE_NAME} row at 0x{pos:X} repeats key {key_dup}, expected {key}")
        records.append(
            {
                "key": key,
                "average_grade": average_grade,
                "result_max_grade": max_grade,
                "result_min_grade": min_grade,
                "imperial_steed_character_id": steed_id,
                "imperial_steed_rate": steed_rate,
            }
        )
    return records
