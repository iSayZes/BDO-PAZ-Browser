"""`collectresourcename.dbss`: gathering models and the Collect character each stands for.

A u32 record count, then records back to back to the end of the file: the
u32 hash of the model name, the same hash again, the name as a u64-prefixed
ASCII string and a u16 character key. `collectresourcenameoffset.dbss` points
4 bytes into a record, at the second hash, so the walk from the start needs
no index. Layout in docs/file-formats/dbss/collectresourcename_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "collectresourcename.dbss"
OFFSET_FILE = "collectresourcenameoffset.dbss"

_COUNT_SIZE = 4
_HASHES = struct.Struct("<II")  # name_hash, name_hash_dup
_CHARACTER_KEY = struct.Struct("<H")

def parse_collectresourcename_records(data: bytes) -> list[dict]:
    """Every model record, in file order.

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
        name_hash, name_hash_dup = reader.unpack(_HASHES)
        resource_file_name = reader.text(wide=False)
        (character_key,) = reader.unpack(_CHARACTER_KEY)
        records.append({
            "name_hash": name_hash,
            "resource_file_name": resource_file_name,
            "character_key": character_key,
            "name_hash_dup": name_hash_dup,
        })
        pos = reader.pos
    if pos != len(data):
        raise ValueError(f"{FILE_NAME} has {len(data) - pos:,} bytes after its {count:,} records")
    return records
