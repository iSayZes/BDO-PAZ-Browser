"""`specialemployeeinfostaticstatus.dbss`: the special sailors hired with an item.

The file is groups back to back to its end, each a u32 row count and rows:

    Row: u8 category | u16 type | u16 character_key | u32 need_item_key
         | u64 need_item_count | u32 employ_success_rate
         | str16 employ_success_word_kr | str16 employ_fail_word_kr
         | u32 unknown_employ_fail_word_kr_00

`specialemployeeinfostaticstatusoffset.dbss` holds a u32 group count and
the same groups of index rows (u16 type, u32 offset, u32 size), each
pointing at a row start. Layout 1 in
docs/file-formats/dbss/specialemployeeinfostaticstatus_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow
from _common.record_reader import RecordReader


FILE_NAME = "specialemployeeinfostaticstatus.dbss"
OFFSET_FILE = "specialemployeeinfostaticstatusoffset.dbss"
KEY_FIELD = "type"

COUNT_SIZE = 4
_COUNT = struct.Struct("<I")
# category, type, character_key, need_item_key, need_item_count, employ_success_rate
_HEAD = struct.Struct("<BHHIQI")
_HEAD_FIELDS = ("category", KEY_FIELD, "character_key", "need_item_key", "need_item_count", "employ_success_rate")
_TAIL = struct.Struct("<I")
_OFFSET_ROW = struct.Struct("<HII")


def _read_row(reader: RecordReader) -> dict:
    record: dict[str, int | str] = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    record["employ_success_word_kr"] = reader.text(wide=True)
    record["employ_fail_word_kr"] = reader.text(wide=True)
    (record["unknown_employ_fail_word_kr_00"],) = reader.unpack(_TAIL)
    return record


def parse_specialemployeeinfostaticstatus_records(data: bytes) -> list[dict]:
    """Every row of every group, in file order.

    Raises ValueError when a group or row runs past the file.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    records: list[dict] = []
    while not reader.at_end():
        (count,) = reader.unpack(_COUNT)
        records.extend(_read_row(reader) for _ in range(count))
    return records


def parse_specialemployeeinfostaticstatusoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row of every group, in file order.

    Raises ValueError when the groups do not end at the last byte of the file.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{OFFSET_FILE} is too short to hold its group count")

    group_count = u32(data, 0)
    reader = RecordReader(data, COUNT_SIZE, len(data), OFFSET_FILE)
    rows: list[PabrOffsetRow] = []
    for _ in range(group_count):
        (count,) = reader.unpack(_COUNT)
        rows.extend(PabrOffsetRow(*reader.unpack(_OFFSET_ROW)) for _ in range(count))
    if not reader.at_end():
        raise ValueError(f"{OFFSET_FILE} has {reader.remaining():,} bytes after its {group_count:,} groups")
    return rows
