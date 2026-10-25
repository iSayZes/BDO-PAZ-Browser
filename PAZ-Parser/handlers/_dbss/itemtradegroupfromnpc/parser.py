"""`itemtradegroupfromnpc.dbss`: item groups per NPC, in the client 1784 shape.

    u32 count | count x (u16 character_id | u32 item_count | item_count x entry)

    entry: u16 character_id | u32 item_id | str16 condition
           | 0x6D bytes of trade members, the itemtradegrouptonpc.dbss Layout 1 tail

Client 3473 ships the count `0` and no groups. On client 1784 the entries
open with a counted condition string, the Layout 1 entry of
`itemtradegrouptonpc.dbss`, so the fields after it sit at offsets from the
string's end. The record keys match `_dbss/itemtradegrouptonpc/parser.py`, so
its handler draws both tables; `territory_trade_no` and `is_for_magnate` are
the `BuyingFromNpc_Table` columns only this file fills. Layout in
docs/file-formats/dbss/itemtradegroupfromnpc_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader
from _dbss.itemtradegrouptonpc.parser import COUNT_SIZE, GROUP_HEADER


FILE_NAME = "itemtradegroupfromnpc.dbss"
OFFSET_FILE = "itemtradegroupfromnpcoffset.dbss"

# u16 character_id | u32 item_id
_ENTRY_HEAD = struct.Struct("<HI")
# After condition: bytes[40] price rate members | u8 trade_group_type
# | u8 is_sell_to_npc | bytes[51] price and stock members | u16 territory_supply_no
# | u16 territory_trade_no | i32 get_selling_trade_exp_rate | i32 event_price_rate_per_sell
# | u8 is_for_magnate | u8 trade_type | u8 commerce_type | u8 price_type
_ENTRY_TAIL = struct.Struct("<40xBB51xHH8xBBBB")
_ENTRY_TAIL_SIZE = 0x6D
assert _ENTRY_TAIL.size == _ENTRY_TAIL_SIZE


def parse_itemtradegroupfromnpc_records(data: bytes) -> list[dict]:
    """One record per item entry, in file order; none for the empty table of the live client.

    Raises ValueError when a group or entry runs past the file, an entry names
    another character than its group, or bytes follow the last group.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its group count")

    reader = RecordReader(data, COUNT_SIZE, len(data), FILE_NAME)
    records: list[dict] = []
    for _ in range(u32(data, 0)):
        character_id, item_count = reader.unpack(GROUP_HEADER)
        records.extend(_entry(reader, character_id) for _ in range(item_count))
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} groups end at 0x{reader.pos:X} but the file holds {len(data):,} bytes")
    return records


def _entry(reader: RecordReader, group_character_id: int) -> dict:
    start = reader.pos
    character_id, item_id = reader.unpack(_ENTRY_HEAD)
    if character_id != group_character_id:
        raise ValueError(
            f"{FILE_NAME} entry at 0x{start:X} names character {character_id}, its group {group_character_id}"
        )
    condition = reader.text(wide=True)
    (
        trade_group_type,
        is_sell_to_npc,
        territory_supply_no,
        territory_trade_no,
        is_for_magnate,
        trade_type,
        commerce_type,
        price_type,
    ) = reader.unpack(_ENTRY_TAIL)
    return {
        "character_id": character_id,
        "item_id": item_id,
        "condition": condition,
        "trade_group_type": trade_group_type,
        "commerce_type": commerce_type,
        "is_sell_to_npc": is_sell_to_npc,
        "territory_supply_no": territory_supply_no,
        "territory_trade_no": territory_trade_no,
        "is_for_magnate": is_for_magnate,
        "trade_type": trade_type,
        "price_type": price_type,
    }
