"""`jewelgroupstaticstatus.bss`: the crystal groups.

    PABR | u32 count | count x 8-byte row | string table
    | u32 string_table_start | u32 0

Each row holds the string table index of the group's Korean name, the group
number (the crystal footer of `itemenchant.dbss`, LOC type 121) and the most
crystals of the group one crystal preset holds. Layout in
docs/file-formats/jewelgroupstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "jewelgroupstaticstatus.bss"

# u32 name_ref | u16 group | u16 max_count
_ROW = struct.Struct("<IHH")


def parse_jewel_group_records(data: bytes) -> list[dict]:
    """Every group row in file order, with its Korean name resolved.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    offsets = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        name_ref, group, max_count = _ROW.unpack_from(data, offset)
        records.append({
            "group": group,
            "max_count": max_count,
            "name_kr": string_at(strings, name_ref),
        })
    return records
