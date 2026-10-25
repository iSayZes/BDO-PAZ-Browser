"""`sequencetriggerdata.bss`: where each sequence starts, and the scripts it runs.

    PABR | u32 row_count | rows | String Table | u32 string_table_start | u32 0
    row (Layout 9, the live client): u32 file_name_hash | u32 file_name
         | u32 folder | u32 start_condition | u32 start_execute | u32 end_execute
         | u32 force_skip_end_execute | u32 skip_condition | u32 contents_group_open
         | f32[3] position | f32[3] resurrect_position | u64 region_count
         | u16[region_count] region_keys | u32 file_name_hash_dup | f32 radius
         | u8 x 6 flags (FLAG_FIELDS)

Older layouts drop text fields and flags, and Layouts 1 to 6 store one u16
region key with no count (`LAYOUTS`). Nothing in the file names its layout,
so it is read with the first layout (newest first) whose rows end where the
string table starts. A text field or flag the layout lacks reads as empty
text or `0`.

The text fields are indexes into the string table
(`_bss/sequence_scripts/reader.py`); `file_name_hash` is
`cutscene_file_hash()` of `file_name`. The file is compiled from
`sequence/sequencetriggerdata.xml`. Layouts 1 to 9 in
docs/file-formats/bss/sequencetriggerdata_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from functools import cached_property

from _bss.sequence_scripts.reader import (
    SCRIPT_FIELDS,
    ScriptTable,
    check_rows_end,
    open_table,
    read_position,
    read_string_refs,
)
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "sequencetriggerdata.bss"
TEXT_FIELDS = (
    "file_name",
    "folder",
    *SCRIPT_FIELDS,
    "force_skip_end_execute",
    "skip_condition",
    "contents_group_open",
)
# The six u8 flags that end a row of the live client, in file order.
FLAG_FIELDS = (
    "use_client_spawn",
    "exit_character_select",
    "pre_update_fade_out",
    "party_sequence",
    "character_swap_sequence",
    "force_skip_sequence",
)

_HASH = struct.Struct("<I")
_REGION_COUNT = struct.Struct("<Q")
_SINGLE_REGION_KEY = struct.Struct("<H")
_REGION_KEY_SIZE = 2
_AREA = struct.Struct("<If")

# Layouts 2 to 5 have no `force_skip_end_execute`, Layout 1 no `folder` either.
_LAYOUT_2_TEXT_FIELDS = tuple(field for field in TEXT_FIELDS if field != "force_skip_end_execute")
_LAYOUT_1_TEXT_FIELDS = tuple(field for field in _LAYOUT_2_TEXT_FIELDS if field != "folder")
# Layouts 6 and 7 have no `character_swap_sequence`.
_LAYOUT_6_FLAGS = tuple(field for field in FLAG_FIELDS if field != "character_swap_sequence")


@dataclass(frozen=True)
class RowLayout:
    """One documented Row shape; `number` is its Layout N in the doc.

    `has_region_count` is False for the layouts that store one u16 region
    key with no count before it.
    """

    number: int
    text_fields: tuple[str, ...]
    has_region_count: bool
    flag_fields: tuple[str, ...]

    @cached_property
    def flags(self) -> struct.Struct:
        return struct.Struct(f"<{len(self.flag_fields)}B")


# Newest first.
LAYOUTS = (
    RowLayout(9, TEXT_FIELDS, True, FLAG_FIELDS),
    RowLayout(8, TEXT_FIELDS, True, (*FLAG_FIELDS[:5], "unknown_region_keys_0d", "force_skip_sequence")),
    RowLayout(7, TEXT_FIELDS, True, _LAYOUT_6_FLAGS),
    RowLayout(6, TEXT_FIELDS, False, _LAYOUT_6_FLAGS),
    RowLayout(5, _LAYOUT_2_TEXT_FIELDS, False, FLAG_FIELDS[:4]),
    RowLayout(4, _LAYOUT_2_TEXT_FIELDS, False, FLAG_FIELDS[:3]),
    RowLayout(3, _LAYOUT_2_TEXT_FIELDS, False, ("use_client_spawn", "unknown_43")),
    RowLayout(2, _LAYOUT_2_TEXT_FIELDS, False, ("use_client_spawn",)),
    RowLayout(1, _LAYOUT_1_TEXT_FIELDS, False, ("use_client_spawn",)),
)


def sequence_path(folder: str, file_name: str) -> str:
    """`Sadang/CS_SadangSeoul_06_02_Pyeseja`: the folder and file name as the source XML joins them."""
    return f"{folder}/{file_name}" if folder else file_name


def _read_region_keys(reader: RecordReader, layout: RowLayout, label: str) -> list[int]:
    if not layout.has_region_count:
        return list(reader.unpack(_SINGLE_REGION_KEY))
    (region_count,) = reader.unpack(_REGION_COUNT)
    if region_count * _REGION_KEY_SIZE > reader.remaining():
        raise ValueError(f"{label} region count {region_count:,} runs past the rows")
    return list(reader.unpack(struct.Struct(f"<{region_count}H")))


def _read_row(table: ScriptTable, layout: RowLayout, index: int) -> dict:
    label = f"{FILE_NAME} row {index}"
    reader = table.reader
    (file_name_hash,) = reader.unpack(_HASH)
    texts = read_string_refs(table, layout.text_fields, label)
    position = read_position(reader)
    resurrect_position = read_position(reader)
    region_keys = _read_region_keys(reader, layout, label)
    file_name_hash_dup, radius = reader.unpack(_AREA)
    flags = reader.unpack(layout.flags)
    return {
        "file_name_hash": file_name_hash,
        **dict.fromkeys(TEXT_FIELDS, ""),
        **texts,
        "position": position,
        "resurrect_position": resurrect_position,
        "region_count": len(region_keys),
        "region_keys": region_keys,
        "file_name_hash_dup": file_name_hash_dup,
        "radius": radius,
        **dict.fromkeys(FLAG_FIELDS, 0),
        **dict(zip(layout.flag_fields, flags)),
    }


def _read_rows(data: bytes, layout: RowLayout) -> list[dict]:
    """Every row read with `layout`; raises ValueError when they do not end at the string table."""
    table = open_table(data, FILE_NAME)
    records = [_read_row(table, layout, index) for index in range(table.row_count)]
    check_rows_end(table, FILE_NAME)
    return records


def parse_sequencetriggerdata_records(data: bytes) -> list[dict]:
    """Every row in file order, its text fields resolved, read with the first layout that fits.

    Raises ValueError on a bad magic or trailer, or when no layout's rows end
    where the string table starts with every string index inside the table.
    """
    checked_string_table_start(data, FILE_NAME)
    breaks: list[str] = []
    for layout in LAYOUTS:
        try:
            return _read_rows(data, layout)
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")
