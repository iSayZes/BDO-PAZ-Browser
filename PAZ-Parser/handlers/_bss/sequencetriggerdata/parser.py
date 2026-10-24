"""`sequencetriggerdata.bss`: where each sequence starts, and the scripts it runs.

    PABR | u32 row_count | rows | String Table | u32 string_table_start | u32 0
    row: u32 file_name_hash | u32 file_name | u32 folder | u32 start_condition
         | u32 start_execute | u32 end_execute | u32 force_skip_end_execute
         | u32 skip_condition | u32 contents_group_open | f32[3] position
         | f32[3] resurrect_position | u64 region_count
         | u16[region_count] region_keys | u32 file_name_hash_dup | f32 radius
         | u8 x 6 flags (FLAG_FIELDS)

The text fields are indexes into the string table
(`_bss/sequence_scripts/reader.py`); `file_name_hash` is
`cutscene_file_hash()` of `file_name`. The file is compiled from
`sequence/sequencetriggerdata.xml`. Layout 4 in
docs/file-formats/sequencetriggerdata_bss.md.
"""

from __future__ import annotations

import struct

from _bss.sequence_scripts.reader import (
    SCRIPT_FIELDS,
    ScriptTable,
    check_rows_end,
    open_table,
    read_position,
    read_string_refs,
)


FILE_NAME = "sequencetriggerdata.bss"
TEXT_FIELDS = (
    "file_name",
    "folder",
    *SCRIPT_FIELDS,
    "force_skip_end_execute",
    "skip_condition",
    "contents_group_open",
)
# The six u8 flags that end a row, in file order.
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
_REGION_KEY_SIZE = 2
_AREA_AND_FLAGS = struct.Struct(f"<If{len(FLAG_FIELDS)}B")


def sequence_path(folder: str, file_name: str) -> str:
    """`Sadang/CS_SadangSeoul_06_02_Pyeseja`: the folder and file name as the source XML joins them."""
    return f"{folder}/{file_name}" if folder else file_name


def _read_row(table: ScriptTable, index: int) -> dict:
    label = f"{FILE_NAME} row {index}"
    reader = table.reader
    (file_name_hash,) = reader.unpack(_HASH)
    texts = read_string_refs(table, TEXT_FIELDS, label)
    position = read_position(reader)
    resurrect_position = read_position(reader)
    (region_count,) = reader.unpack(_REGION_COUNT)
    if region_count * _REGION_KEY_SIZE > reader.remaining():
        raise ValueError(f"{label} region count {region_count:,} runs past the rows")
    region_keys = list(reader.unpack(struct.Struct(f"<{region_count}H")))
    file_name_hash_dup, radius, *flags = reader.unpack(_AREA_AND_FLAGS)
    return {
        "file_name_hash": file_name_hash,
        **texts,
        "position": position,
        "resurrect_position": resurrect_position,
        "region_count": region_count,
        "region_keys": region_keys,
        "file_name_hash_dup": file_name_hash_dup,
        "radius": radius,
        **dict(zip(FLAG_FIELDS, flags)),
    }


def parse_sequencetriggerdata_records(data: bytes) -> list[dict]:
    """Every row in file order, its text fields resolved.

    Raises ValueError on a bad magic, a string index past the table, a region
    list that runs past the rows, or rows that do not end where the string
    table starts.
    """
    table = open_table(data, FILE_NAME)
    records = [_read_row(table, index) for index in range(table.row_count)]
    check_rows_end(table, FILE_NAME)
    return records
