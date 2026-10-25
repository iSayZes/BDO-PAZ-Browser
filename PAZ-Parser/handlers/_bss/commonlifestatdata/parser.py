"""`commonlifestatdata.bss`: the Gathering and Processing mastery a life level gives.

    PABR | f32 mastery per level, from level 1 | u32 0 (empty string table)
    | u32 string_table_start | u32 0

There is no row count: the values run from +0x04 up to the string table.
`traininglevelskillstat.bss` has the same layout with 8-byte entries and
reads them through `parse_level_entries`.
Full layout in docs/file-formats/bss/commonlifestatdata_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import check_pabr, check_rows_end, string_table_start

_FILE_NAME = "commonlifestatdata.bss"
_VALUE = struct.Struct("<f")
# The PABR magic; the level 1 entry follows it.
_ENTRIES_START = 4
_FIRST_LEVEL = 1


def parse_level_entries(data: bytes, entry: struct.Struct, file_name: str) -> list[tuple[int, tuple]]:
    """(level, unpacked entry) for each entry between the magic and the string table.

    Raises ValueError on a missing magic or when the entries do not fill the
    space before the string table.
    """
    check_pabr(data, file_name)
    table_start = string_table_start(data)
    entries_end = _ENTRIES_START + max(table_start - _ENTRIES_START, 0) // entry.size * entry.size
    check_rows_end(data, entries_end, f"{file_name} entries")
    entries = entry.iter_unpack(data[_ENTRIES_START:entries_end])
    return [(_FIRST_LEVEL + index, values) for index, values in enumerate(entries)]


def parse_commonlifestat_records(data: bytes) -> list[dict]:
    """One record per life level; see `parse_level_entries` for the errors."""
    return [{"level": level, "mastery": mastery} for level, (mastery,) in parse_level_entries(data, _VALUE, _FILE_NAME)]
