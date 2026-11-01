"""`skillexperiencemaxlevel.bss` and `guildskillexperiencemaxlevel.bss`: the
max level of a skill point EXP table.

`PABR`, a u16 array with no count (one value on client 3464: the top level of
`skillexperience.dbss` or `guildskillexperience.dbss`), then the 12-byte PABR
trailer whose middle u32 is the end of the array. Full layout in
docs/file-formats/bss/skillexperiencemaxlevel_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PABR_MAGIC


_U16 = struct.Struct("<H")
_TRAILER = struct.Struct("<III")


def parse_skillexperiencemaxlevel_records(data: bytes, file_name: str) -> list[dict]:
    """One record per stored max level. Raises ValueError on a bad magic or trailer."""
    if len(data) < len(PABR_MAGIC) + _TRAILER.size or data[: len(PABR_MAGIC)] != PABR_MAGIC:
        raise ValueError(f"{file_name}: missing PABR magic")
    _, end_of_data, _ = _TRAILER.unpack_from(data, len(data) - _TRAILER.size)
    if end_of_data != len(data) - _TRAILER.size or (end_of_data - len(PABR_MAGIC)) % _U16.size:
        raise ValueError(f"{file_name}: trailer end offset {end_of_data} does not close the u16 array")
    values = data[len(PABR_MAGIC) : end_of_data]
    return [{"max_level": max_level} for (max_level,) in _U16.iter_unpack(values)]
