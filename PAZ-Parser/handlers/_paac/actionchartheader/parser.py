"""Read `actionchartheader.paach` (docs/file-formats/other/actionchartheader_paach.md).

PABR, u32 version, u16 entry count, then per entry a u32 chart path hash, a
u16 flag count and that many flag bytes, then a u32 version and the (empty)
string table.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import checked_string_table_start

FILE_NAME = "actionchartheader.paach"
_HEAD = struct.Struct("<IH")
_COUNT = struct.Struct("<H")
_ENTRIES_START = 10
_VERSION_SIZE = 4


def parse_actionchartheader(data: bytes) -> list[dict]:
    """Every entry in file order. Raises ValueError when the entries miss the trailing version."""
    table_start = checked_string_table_start(data, FILE_NAME)
    entries_end = table_start - _VERSION_SIZE
    (count,) = _COUNT.unpack_from(data, 8)
    pos = _ENTRIES_START
    records = []
    for index in range(count):
        if pos + _HEAD.size > entries_end:
            raise ValueError(f"entry {index} at 0x{pos:X} runs past the entries")
        chart_hash, flag_count = _HEAD.unpack_from(data, pos)
        pos += _HEAD.size
        flags = data[pos:pos + flag_count]
        pos += flag_count
        records.append({"chart_hash": chart_hash, "flag_count": flag_count, "unknown_flags": list(flags)})
    if pos != entries_end:
        raise ValueError(f"the entries end at 0x{pos:X}, the trailing version sits at 0x{entries_end:X}")
    return records
