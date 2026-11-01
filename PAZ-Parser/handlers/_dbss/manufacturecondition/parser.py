"""`manufacturecondition.dbss`: when each processing action shows and can be used.

A u32 record count, then records back to back to the end of the file: the
u32 hash of the action name, the name as a u64-prefixed ASCII string, the
same hash again, and two u64-prefixed UTF-16LE condition scripts (visible,
enable). `manufactureconditionoffset.dbss` points 4 bytes into a record, at
the name, so the walk from the start needs no index. Layout in
docs/file-formats/dbss/manufacturecondition_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "manufacturecondition.dbss"
OFFSET_FILE = "manufactureconditionoffset.dbss"

_COUNT_SIZE = 4
_HASH = struct.Struct("<I")


def parse_manufacturecondition_records(data: bytes) -> list[dict]:
    """Every action record, in file order.

    Raises ValueError when a record runs past the file or the records do not
    end where the file does.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")

    count = u32(data, 0)
    pos = _COUNT_SIZE
    records = []
    for _ in range(count):
        reader = RecordReader(data, pos, len(data), f"{FILE_NAME} record at 0x{pos:X}")
        (action_hash,) = reader.unpack(_HASH)
        action_name = reader.text(wide=False)
        (action_hash_dup,) = reader.unpack(_HASH)
        check_visible_condition = reader.text(wide=True)
        check_enable_condition = reader.text(wide=True)
        records.append({
            "action_hash": action_hash,
            "action_name": action_name,
            "action_hash_dup": action_hash_dup,
            "check_visible_condition": check_visible_condition,
            "check_enable_condition": check_enable_condition,
        })
        pos = reader.pos
    if pos != len(data):
        raise ValueError(f"{FILE_NAME} has {len(data) - pos:,} bytes after its {count:,} records")
    return records
