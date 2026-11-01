"""`instancefieldcommon.bss`: the entry limits of an instance type and mode.

    PABR | u32 record_count | record_count x Row | String Table
    | u32 string_table_start | u32 0
    Row: u16 instance_mode | u16 instance_type | u32 limited_character_level
         | u16 limited_quest_group | u16 limited_quest_id | u32 limited_quest_string
         | u32 unknown_10 | u16[unknown_10] unknown_14

`limited_quest_string` indexes the string table (the Korean limit message).
Layout 2 in docs/file-formats/bss/instancefieldcommon_bss.md.
"""

from __future__ import annotations

import struct
from typing import Any

from _common.binary import u32
from _common.inline_text import decode_inline_text
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "instancefieldcommon.bss"
_COUNT_OFFSET = 4

_HEAD = struct.Struct("<HHIHHII")
_HEAD_FIELDS = (
    "instance_mode",
    "instance_type",
    "limited_character_level",
    "limited_quest_group",
    "limited_quest_id",
    "limited_quest_string",
    "unknown_10",
)


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    record: dict[str, Any] = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    record["unknown_14"] = list(reader.unpack(struct.Struct(f"<{record['unknown_10']}H")))
    record["limited_quest_text_kr"] = decode_inline_text(string_at(strings, record["limited_quest_string"]))
    return record


def parse_instancefieldcommon_records(data: bytes) -> list[dict]:
    """Every row in file order, with its limit message.

    Raises ValueError on a missing magic, a row that runs past the string
    table, or rows that end before it.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, end, FILE_NAME)
    records = [_read_row(reader, strings) for _ in range(u32(data, _COUNT_OFFSET))]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records
