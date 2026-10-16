"""`dropuisubcategoryinfo.bss`: the filter categories of the drop item window.

    PABR | u32 count | count x 12-byte row | string table
    | u32 string_table_start | u32 0

Each row holds the category key (LOC type 115) and the string table indexes
of its Korean name and its button icon texture key. Layout in
docs/file-formats/dropuisubcategoryinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "dropuisubcategoryinfo.bss"

# u32 key | u32 name_ref | u32 icon_ref
_ROW = struct.Struct("<3I")


def parse_sub_category_records(data: bytes) -> list[dict]:
    """Every category row in file order, with its strings resolved.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    offsets = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        key, name_ref, icon_ref = _ROW.unpack_from(data, offset)
        records.append({
            "key": key,
            "name_kr": string_at(strings, name_ref),
            "icon_texture": string_at(strings, icon_ref),
        })
    return records
