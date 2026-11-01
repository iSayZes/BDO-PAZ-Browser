"""`dropuimaincategoryinfo.bss`: the region tabs of the drop item window.

    PABR | u32 count | count x 10-byte row | string table
    | u32 string_table_start | u32 0

Each row holds the tab key, its territory (LOC type 12) and the string table
index of its icon texture key. `dropuihuntinggroundinfo.bss` puts each hunting
ground on a tab. Layout in docs/file-formats/bss/dropuimaincategoryinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "dropuimaincategoryinfo.bss"

# u32 key | u16 territory_key | u32 icon_ref
_ROW = struct.Struct("<IHI")


def parse_main_category_records(data: bytes) -> list[dict]:
    """Every tab row in file order, with its icon texture key resolved.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    offsets = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        key, territory_key, icon_ref = _ROW.unpack_from(data, offset)
        records.append({
            "key": key,
            "territory_key": territory_key,
            "icon_texture": string_at(strings, icon_ref),
        })
    return records


def parse_territory_keys(data: bytes) -> dict[int, int]:
    """Region tab key -> territory key.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    return {record["key"]: record["territory_key"] for record in parse_main_category_records(data)}
