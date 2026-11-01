"""`servantexperiencemaxlevel.bss`: the top level of each servant (mount or ship).

A u32 count, then `count` rows of (u16 character_id, u16 max_level) up to the
end of the file; no magic and no trailer. Layout in
docs/file-formats/bss/servantexperiencemaxlevel_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "servantexperiencemaxlevel.bss"

_COUNT_SIZE = 4
_ROW = struct.Struct("<HH")


def parse_servantexperiencemaxlevel_records(data: bytes) -> list[dict]:
    """One record per servant, in file order. Raises ValueError when the rows do not fill the file."""
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")
    count = u32(data, 0)
    if _COUNT_SIZE + count * _ROW.size != len(data):
        raise ValueError(f"{FILE_NAME} declares {count:,} rows but holds {len(data) - _COUNT_SIZE:,} row bytes")
    return [
        {"character_id": character_id, "max_level": max_level}
        for character_id, max_level in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]
