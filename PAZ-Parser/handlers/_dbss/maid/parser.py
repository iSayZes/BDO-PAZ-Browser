"""`maid.dbss`: the maids and butlers, their duties and their list icons.

    u32 count | count x (u16 key_prefix | row)
    row = u16 character_key | u32 max_action_index | i64 cool_time
          | 6 x u8 (warehouse in/out, market submit/buy, repair, PC room)
          | u32 skill_0 | u32 skill_1
          | u32 form_count | form_count x (i32 action_index | str16 icon_path)
          | u8 is_maid_chief | u8 is_maid_chief_market

`maidoffset.dbss` points at each row's `character_key`, after the key
prefix, so the walk from the start needs no index. Layout 1 in
docs/file-formats/maid_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "maid.dbss"
OFFSET_FILE = "maidoffset.dbss"

# The u8 flags at +0x0E to +0x13, one per Maid_Table column.
FLAG_FIELDS = (
    "is_able_in_warehouse",
    "is_able_out_warehouse",
    "is_able_submit_market",
    "is_able_buy_market",
    "is_able_repair",
    "pc_room_type",
)
CHIEF_FIELDS = ("is_maid_chief", "is_maid_chief_market")

_COUNT_SIZE = 4
_KEY_PREFIX = struct.Struct("<H")
# character_key, max_action_index, cool_time, the six flags, skill_0, skill_1, form_count
_ROW_HEAD = struct.Struct("<HIq6BIII")
_ACTION_INDEX = struct.Struct("<i")
_CHIEF_FLAGS = struct.Struct("<2B")


def _read_form(reader: RecordReader) -> dict:
    (action_index,) = reader.unpack(_ACTION_INDEX)
    return {"action_index": action_index, "icon_path": reader.text(wide=True)}


def _read_row(reader: RecordReader) -> dict:
    key, max_action_index, cool_time, *rest = reader.unpack(_ROW_HEAD)
    flags, (skill_0, skill_1, form_count) = rest[: len(FLAG_FIELDS)], rest[len(FLAG_FIELDS) :]
    forms = [_read_form(reader) for _ in range(form_count)]
    chiefs = reader.unpack(_CHIEF_FLAGS)
    return {
        "character_key": key,
        "max_action_index": max_action_index,
        "cool_time": cool_time,
        **dict(zip(FLAG_FIELDS, flags)),
        "skill_0": skill_0,
        "skill_1": skill_1,
        "forms": forms,
        **dict(zip(CHIEF_FIELDS, chiefs)),
    }


def parse_maid_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is shorter than its count, a key prefix
    differs from its row's `character_key`, or the rows do not end at the
    end of the file.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = []
    for index in range(count):
        (key_prefix,) = reader.unpack(_KEY_PREFIX)
        record = _read_row(reader)
        if record["character_key"] != key_prefix:
            raise ValueError(f"row {index} has key prefix {key_prefix} and character_key {record['character_key']}")
        records.append(record)

    if not reader.at_end():
        raise ValueError(f"{count:,} rows end at 0x{reader.pos:X}, the file is {len(data):,} bytes")
    return records
