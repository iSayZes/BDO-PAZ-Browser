"""`lifeexpmaxlevel.bss`: the max level of every life skill.

The file is a bare u32 array with no header: entry N is the max level of life
skill N, in the `lifeexp.dbss` block order. Full layout in
docs/file-formats/lifeexpmaxlevel_bss.md.
"""

from __future__ import annotations

import struct


_U32 = struct.Struct("<I")


def parse_lifeexpmaxlevel_records(data: bytes) -> list[dict]:
    """One record per life skill. Raises ValueError when the file is not whole u32s."""
    if len(data) % _U32.size:
        raise ValueError(f"lifeexpmaxlevel.bss holds {len(data)} bytes, not a whole number of u32 values")
    return [
        {"life_skill": life_skill, "max_level": max_level}
        for life_skill, (max_level,) in enumerate(_U32.iter_unpack(data))
    ]
