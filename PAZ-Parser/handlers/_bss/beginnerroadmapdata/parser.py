"""`beginnerroadmapdata.bss`: the slots of the beginner and season roadmap window.

    PABR | u32 row_count | row_count x row (40 bytes) | string table
    | u32 table_start | u32 0
    row: u32 roadmap_key | u32 title_ref | u32 desc_ref | u32 event_name_ref
         | u32 icon_texture_id_ref | u32 background_texture_id_ref
         | u32 character_texture_id_ref | i32[3] event_parameters

The `*_ref` fields index the string table; the records hold their text.
`event_parameters` is `-1` where unused; the first is the event category,
the second its target UI.
Layout 1 in docs/file-formats/bss/beginnerroadmapdata_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "beginnerroadmapdata.bss"

_ROW = struct.Struct("<7I3i")
_TEXT_FIELDS = (
    "title_kr", "desc_kr", "event_name_kr", "icon_texture_id", "background_texture_id", "character_texture_id",
)


def parse_beginnerroadmapdata_records(data: bytes) -> list[dict]:
    """Every roadmap slot in file order.

    Raises ValueError on a bad magic or when the rows do not fill the space
    before the string table.
    """
    starts = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records = []
    for start in starts:
        roadmap_key, *text_indexes, param_0, param_1, param_2 = _ROW.unpack_from(data, start)
        records.append(
            {
                "roadmap_key": roadmap_key,
                **{field: string_at(strings, index) for field, index in zip(_TEXT_FIELDS, text_indexes, strict=True)},
                "event_parameters": [param_0, param_1, param_2],
            }
        )
    return records
