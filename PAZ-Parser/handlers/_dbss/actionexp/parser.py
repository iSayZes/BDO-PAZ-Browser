"""`actionexp.dbss`: action EXP rows per class type and level.

The main file holds one block per class type, with no block count:

    blocks to the end of the file: u32 level_count | level_count x (u32 key_prefix | 85-byte row)

Each row is:

    u8 class_type | u32 level | bytes[80] unknown_05

`key_prefix` repeats the row's level. `actionexpoffset.dbss` has the same
block shape with 12-byte [u32 level][u32 offset][u32 size] rows; its block
index is the class type and each offset points past the row's key_prefix.
Full layout in docs/file-formats/dbss/actionexp_dbss.md.
"""

from __future__ import annotations

import struct


_U32 = struct.Struct("<I")
_OFFSET_ROW = struct.Struct("<III")
_LEVEL_ROW = struct.Struct("<BI80s")


def parse_actionexpoffset_records(data: bytes) -> list[dict]:
    """Every offset row, with the class type taken from its block index.

    Raises ValueError when a block runs past the end of the file.
    """
    records: list[dict] = []
    cursor = 0
    class_type = 0
    while cursor < len(data):
        if cursor + _U32.size > len(data):
            raise ValueError(f"actionexpoffset block {class_type} header exceeds file size")
        (level_count,) = _U32.unpack_from(data, cursor)
        cursor += _U32.size
        if cursor + level_count * _OFFSET_ROW.size > len(data):
            raise ValueError(f"actionexpoffset block {class_type} rows exceed file size")
        for _ in range(level_count):
            level, data_offset, data_size = _OFFSET_ROW.unpack_from(data, cursor)
            cursor += _OFFSET_ROW.size
            records.append({
                "class_type": class_type,
                "level": level,
                "data_offset": data_offset,
                "data_size": data_size,
            })
        class_type += 1
    return records


def _level_record(data: bytes, offset_row: dict) -> dict:
    data_offset = offset_row["data_offset"]
    data_size = offset_row["data_size"]
    label = f"class type {offset_row['class_type']} level {offset_row['level']}"
    if data_size != _LEVEL_ROW.size:
        raise ValueError(f"{label}: row size {data_size}, expected {_LEVEL_ROW.size}")
    if data_offset < _U32.size or data_offset + data_size > len(data):
        raise ValueError(f"{label}: row lies outside the file")

    (key_prefix,) = _U32.unpack_from(data, data_offset - _U32.size)
    class_type, level, unknown_05 = _LEVEL_ROW.unpack_from(data, data_offset)
    if (class_type, level) != (offset_row["class_type"], offset_row["level"]):
        raise ValueError(f"{label}: row holds class type {class_type} level {level}")
    if key_prefix != level:
        raise ValueError(f"{label}: key prefix {key_prefix} differs from the row's level")
    return {"class_type": class_type, "level": level, "unknown_05": unknown_05.hex()}


def parse_actionexp_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every level row the offset companion points at, in its order.

    Raises ValueError when a row lies outside the file, has another size, or
    holds another class type, level or key prefix than the offset row that
    points at it.
    """
    return [_level_record(data, row) for row in parse_actionexpoffset_records(offset_data)]
