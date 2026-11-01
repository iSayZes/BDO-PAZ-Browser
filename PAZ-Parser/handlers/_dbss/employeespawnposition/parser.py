"""`employeespawnposition.dbss`: where hireable sailors stand in a port town.

The main file is a u32 count and one 34-byte row per spawn position:

    u32 spawn_position_key | f32 pos_x, pos_y, pos_z
    | f32 dir_x, dir_y, dir_z | f32 unknown_1c | u16 region_key

`employeespawnpositionoffset.dbss` is a bare offset table of 12-byte
[u32 spawn_position_key][u32 offset][u32 size] rows. Full layout in
docs/file-formats/dbss/employeespawnposition_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import parse_bare_u32_offset_rows


_ROW = struct.Struct("<I3f3ffH")


def parse_employeespawnpositionoffset_records(data: bytes) -> list[dict]:
    return [
        {"spawn_position_key": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]


def _spawn_position_record(data: bytes, offset_row: dict) -> dict:
    data_offset = offset_row["data_offset"]
    data_size = offset_row["data_size"]
    label = f"spawn position {offset_row['spawn_position_key']}"
    if data_size != _ROW.size:
        raise ValueError(f"{label}: row size {data_size}, expected {_ROW.size}")
    if data_offset + data_size > len(data):
        raise ValueError(f"{label}: row exceeds file size")

    key, pos_x, pos_y, pos_z, dir_x, dir_y, dir_z, unknown_1c, region_key = _ROW.unpack_from(data, data_offset)
    if key != offset_row["spawn_position_key"]:
        raise ValueError(f"{label}: row holds key {key}")

    return {
        "spawn_position_key": key,
        "pos_x": pos_x,
        "pos_y": pos_y,
        "pos_z": pos_z,
        "dir_x": dir_x,
        "dir_y": dir_y,
        "dir_z": dir_z,
        "unknown_1c": unknown_1c,
        "region_key": region_key,
    }


def parse_employeespawnposition_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every spawn position the offset companion points at, in its order.

    Raises ValueError when a row lies outside the file, has another size or
    holds a key other than the offset row's.
    """
    return [_spawn_position_record(data, row) for row in parse_employeespawnpositionoffset_records(offset_data)]
