"""`instancefield.dbss` and `instancefieldoffset.dbss`: the instance fields.

    u32 count | count x record
    record: u16 key | i32 min_x, min_y, min_z | i32 max_x, max_y, max_z
            | u32 unknown_1a | u64 name_length | ascii name | u16 unknown_tail

The box is in world sectors of 12,800 units. Buff effect type 176 stores the
key in `param_3`. The offset file is a bare count plus [u16 key][u32 offset]
[u32 size] rows in hash order; the main file reads without it.
Full layout in docs/file-formats/instancefield_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import parse_bare_offset_rows
from _common.record_reader import RecordReader


_FILE = "instancefield.dbss"
_COUNT_SIZE = 4
_HEAD = struct.Struct("<H6iI")
_TAIL = struct.Struct("<H")


def _read_record(reader: RecordReader) -> dict:
    key, min_x, min_y, min_z, max_x, max_y, max_z, unknown_1a = reader.unpack(_HEAD)
    name = reader.text(wide=False)
    (unknown_tail,) = reader.unpack(_TAIL)
    return {
        "key": key,
        "name": name,
        "min_x": min_x,
        "min_y": min_y,
        "min_z": min_z,
        "max_x": max_x,
        "max_y": max_y,
        "max_z": max_z,
        "unknown_1a": unknown_1a,
        "unknown_tail": unknown_tail,
    }


def parse_instancefield_records(data: bytes) -> list[dict]:
    """Every instance field, in file order.

    Raises ValueError when a record runs past the file or the records do not
    end exactly at the end of the file.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{_FILE} is too short for its record count")
    count = u32(data, 0)
    reader = RecordReader(data, _COUNT_SIZE, len(data), _FILE)
    records = [_read_record(reader) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{_FILE}: {count:,} records end {reader.remaining():,} bytes before the end of the file")
    return records


def parse_instancefieldoffset_records(data: bytes) -> list[dict]:
    """Every `instancefieldoffset.dbss` row, in file order (a hash order)."""
    return [
        {"key": row.entry_id, "offset": row.offset, "size": row.size}
        for row in parse_bare_offset_rows(data)
    ]


def build_instance_field_name_index(data: bytes) -> dict[int, str]:
    """INSTANCE_FIELD_NAME: field key -> internal name (`A1_001`)."""
    return {record["key"]: record["name"] for record in parse_instancefield_records(data)}
