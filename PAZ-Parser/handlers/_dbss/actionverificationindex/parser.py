"""`actionverificationindex.dbss`: the class types with an action verification list.

The main file is a u32 count and one 9-byte record per class type:

    u8 key_prefix | u8 class_type | bytes[7] unknown_01

`key_prefix` repeats the class type. `actionverificationindexoffset.dbss` is a
bare offset table of 12-byte [u32 class_type][u32 offset][u32 size] rows; each
offset points past the record's key_prefix, at `class_type`.
Full layout in docs/file-formats/actionverificationindex_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import parse_bare_u32_offset_rows


_KEY_PREFIX_SIZE = 1
_PAYLOAD = struct.Struct("<B7s")


def parse_actionverificationindexoffset_records(data: bytes) -> list[dict]:
    """Every offset row, in file order.

    Raises ValueError on a count the file cannot hold.
    """
    return [
        {"class_type": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]


def _class_type_record(data: bytes, offset_row: dict) -> dict:
    data_offset = offset_row["data_offset"]
    data_size = offset_row["data_size"]
    key = offset_row["class_type"]
    label = f"class type {key}"
    if data_size != _PAYLOAD.size:
        raise ValueError(f"{label}: payload size {data_size}, expected {_PAYLOAD.size}")
    if data_offset < _KEY_PREFIX_SIZE or data_offset + data_size > len(data):
        raise ValueError(f"{label}: payload lies outside the file")

    key_prefix = data[data_offset - _KEY_PREFIX_SIZE]
    class_type, unknown_01 = _PAYLOAD.unpack_from(data, data_offset)
    if class_type != key:
        raise ValueError(f"{label}: payload holds class type {class_type}")
    if key_prefix != key:
        raise ValueError(f"{label}: key prefix {key_prefix} differs from the class type")
    return {"class_type": class_type, "unknown_01": unknown_01.hex()}


def parse_actionverificationindex_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every record the offset companion points at, in its order.

    Raises ValueError when a payload lies outside the file, has another size,
    or holds another class type or key prefix than the offset row's key.
    """
    return [
        _class_type_record(data, row)
        for row in parse_actionverificationindexoffset_records(offset_data)
    ]
