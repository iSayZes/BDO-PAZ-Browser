"""`majorsiegerewardstaticstatus.bss`: the Conquest War reward items per row, and the booty lists.

    PABR | u32 row_count | row_count x Row | u32 booty_count
    | booty_count x Booty | string table | u32 table_start | u32 0
    Row: u8 unknown_00 | 11 x Rewards | u32 unknown_plus_item_rewards_00
         | u32 item_id_1 | u32 item_id_2 | u32 item_id_3
    Rewards: u64 count | count x Reward (_common/reward_items.py)
    Booty: u16 territory_key | u64 item_count | item_count x u32 item_ids

Full layout in docs/file-formats/majorsiegerewardstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader
from _common.reward_items import read_reward_items


FILE_NAME = "majorsiegerewardstaticstatus.bss"
# The reward lists of a row, in file order; the doc's field names.
REWARD_LISTS: tuple[str, ...] = (
    "win_rewards",
    "lose_rewards",
    "release_win_rewards",
    *(f"release_rewards_{index}" for index in range(5)),
    "release_rewards",
    "plus_medal_rewards",
    "plus_item_rewards",
)
# The three u32 item IDs that end a row.
ROW_ITEM_FIELDS: tuple[str, ...] = ("item_id_1", "item_id_2", "item_id_3")
BOOTY_LIST = "booty_items"

_U32 = struct.Struct("<I")
_ROW_KEY = struct.Struct("<B")
_ROW_TAIL = struct.Struct("<4I")
_BOOTY_HEAD = struct.Struct("<HQ")


def _read_row(reader: RecordReader) -> dict:
    (unknown_00,) = reader.unpack(_ROW_KEY)
    lists = {name: read_reward_items(reader, FILE_NAME) for name in REWARD_LISTS}
    unknown_tail, *item_ids = reader.unpack(_ROW_TAIL)
    return {
        "unknown_00": unknown_00,
        **lists,
        "unknown_plus_item_rewards_00": unknown_tail,
        **dict(zip(ROW_ITEM_FIELDS, item_ids, strict=True)),
    }


def _read_booty(reader: RecordReader) -> dict:
    territory_key, item_count = reader.unpack(_BOOTY_HEAD)
    if item_count * _U32.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} booty item count {item_count:,} runs past the string table")
    return {"territory_key": territory_key, "item_ids": list(reader.unpack(struct.Struct(f"<{item_count}I")))}


def parse_major_siege_rewards(data: bytes) -> tuple[list[dict], list[dict]]:
    """The rows and the booty lists, in file order.

    Raises ValueError on a bad magic or trailer, or when the booty lists do
    not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - _U32.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_U32)
    rows = [_read_row(reader) for _ in range(row_count)]
    (booty_count,) = reader.unpack(_U32)
    booty = [_read_booty(reader) for _ in range(booty_count)]
    check_rows_end(data, reader.pos, f"{FILE_NAME} booty lists")
    return rows, booty


def _empty_item(item_id: int) -> dict:
    """An item stored without `unknown_04` or a count."""
    return {"item_id": item_id, "unknown_04": None, "count": None}


def _row_records(row: dict) -> list[dict]:
    """One record per item of a row's reward lists, then its three item IDs, each with the row's u8 and u32."""
    row_fields = {
        "unknown_00": row["unknown_00"],
        "unknown_plus_item_rewards_00": row["unknown_plus_item_rewards_00"],
        "territory_key": None,
    }
    records = [{**row_fields, "reward_list": name, **reward} for name in REWARD_LISTS for reward in row[name]]
    records += [{**row_fields, "reward_list": name, **_empty_item(row[name])} for name in ROW_ITEM_FIELDS]
    return records


def parse_reward_records(data: bytes) -> list[dict]:
    """One record per item, in file order: each row's reward items, then each booty list's items.

    `reward_list` is the list's field name (`item_id_1` to `item_id_3` for
    the row's three item IDs, `booty_items` for a booty list), `territory_key`
    the booty list's territory (None on a row's items). Raises ValueError
    like `parse_major_siege_rewards`.
    """
    rows, booty = parse_major_siege_rewards(data)
    records = [record for row in rows for record in _row_records(row)]
    records += [
        {
            "unknown_00": None,
            "unknown_plus_item_rewards_00": None,
            "territory_key": entry["territory_key"],
            "reward_list": BOOTY_LIST,
            **_empty_item(item_id),
        }
        for entry in booty
        for item_id in entry["item_ids"]
    ]
    return records
