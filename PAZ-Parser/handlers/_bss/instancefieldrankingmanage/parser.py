"""`instancefieldrankingmanage.bss`: the season rankings of instance contents.

    PABR | u32 record_count | record_count x 26-byte Row | String Table
    | u32 string_table_start | u32 0
    Row: u32 ranking_idx | u16 instance_type | u64 start_date_rank
         | u64 end_date_rank | u32 ranking_name

The times are seconds since 1970; `ranking_name` indexes the string table (a
`GAME` sheet key). Layout 1 in docs/file-formats/bss/instancefieldrankingmanage_bss.md.
"""

from __future__ import annotations

import struct
from typing import Any

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "instancefieldrankingmanage.bss"

_ROW = struct.Struct("<IHQQI")
_FIELDS = ("ranking_idx", "instance_type", "start_date_rank", "end_date_rank", "ranking_name")


def parse_instancefieldrankingmanage_records(data: bytes) -> list[dict]:
    """Every row in file order, with the key its `ranking_name` points at.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    offsets = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records = []
    for pos in offsets:
        record: dict[str, Any] = dict(zip(_FIELDS, _ROW.unpack_from(data, pos), strict=True))
        record["ranking_name_key"] = string_at(strings, record["ranking_name"])
        records.append(record)
    return records
