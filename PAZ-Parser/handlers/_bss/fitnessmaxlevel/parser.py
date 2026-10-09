"""`fitnessmaxlevel.bss`: the max level of every fitness type.

`PABR`, a u32 array with no count (entry N is the max level of fitness type N,
in the `fitnesslevel.dbss` block order), then the 12-byte PABR trailer whose
middle u32 is the end of the array. Full layout in
docs/file-formats/fitnessmaxlevel_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PABR_MAGIC


_U32 = struct.Struct("<I")
_TRAILER = struct.Struct("<III")


def parse_fitnessmaxlevel_records(data: bytes) -> list[dict]:
    """One record per fitness type. Raises ValueError on a bad magic or trailer."""
    if len(data) < len(PABR_MAGIC) + _TRAILER.size or data[: len(PABR_MAGIC)] != PABR_MAGIC:
        raise ValueError("fitnessmaxlevel.bss: missing PABR magic")
    _, end_of_data, _ = _TRAILER.unpack_from(data, len(data) - _TRAILER.size)
    if end_of_data != len(data) - _TRAILER.size or (end_of_data - len(PABR_MAGIC)) % _U32.size:
        raise ValueError(f"fitnessmaxlevel.bss: trailer end offset {end_of_data} does not close the u32 array")
    values = data[len(PABR_MAGIC) : end_of_data]
    return [
        {"fitness_type": fitness_type, "max_level": max_level}
        for fitness_type, (max_level,) in enumerate(_U32.iter_unpack(values))
    ]
