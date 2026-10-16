"""`itemtradegroupfromnpc.dbss`: item groups per NPC, in the client 1784 shape.

    u32 count | count x (u16 character_id | u32 item_count | item_count x entry)

    entry: u16 character_id | u32 item_id | str16 unknown_condition
           | 0x6D bytes with the trade group type and the trade category

Client 3473 ships the count `0` and no groups. On client 1784 the entries
open with a counted condition string, the Layout 1 entry of
`itemtradegrouptonpc.dbss`, so the fields after it sit at offsets from the
string's end. The record keys match `_dbss/itemtradegrouptonpc/parser.py`, so
its handler draws both tables. Layout in
docs/file-formats/itemtradegroupfromnpc_dbss.md.
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
# After unknown_condition: bytes[40] unknown_condition_00 | u8 trade_group_type
# | u8 unknown_37 | bytes[51] unknown_38 | u16 unknown_6b | bytes[11] unknown_6d
# | u8 unknown_7c | u8 commerce_type | u8 unknown_7e
_ENTRY_TAIL = struct.Struct("<40xBB51xH11xBBB")
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
    unknown_condition = reader.text(wide=True)
    trade_group_type, unknown_37, unknown_6b, unknown_7c, commerce_type, unknown_7e = reader.unpack(_ENTRY_TAIL)
    return {
        "character_id": character_id,
        "item_id": item_id,
        "unknown_condition": unknown_condition,
        "trade_group_type": trade_group_type,
        "commerce_type": commerce_type,
        "unknown_37": unknown_37,
        "unknown_6b": unknown_6b,
        "unknown_7c": unknown_7c,
        "unknown_7e": unknown_7e,
    }
