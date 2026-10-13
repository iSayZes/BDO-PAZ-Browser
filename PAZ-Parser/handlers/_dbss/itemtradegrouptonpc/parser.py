"""`itemtradegrouptonpc.dbss`: the trade goods listed under each trade NPC.

A u32 group count, then one group per character key: the u16 key, a u32 item
count and that many 127-byte item entries. Each entry repeats the key, then
holds the u32 item ID, its trade group type (the code `itemtradeetc.bss`
pairs for the desert buff) and the item's trade category (`enCommerceType`)
near its end; the rest is zero but for three unknown fields. No `PABR` magic and no
string table. `itemtradegrouptonpcoffset.dbss` points at each group, so
reading the groups in order needs no index. Layout in
docs/file-formats/itemtradegrouptonpc_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "itemtradegrouptonpc.dbss"
OFFSET_FILE = "itemtradegrouptonpcoffset.dbss"

COUNT_SIZE = 4
# u16 character key, u32 item count.
GROUP_HEADER = struct.Struct("<HI")
ENTRY_SIZE = 127

# u16 character key, u32 item ID at the start of an entry.
_ENTRY_HEAD = struct.Struct("<HI")
_TRADE_GROUP_TYPE = 0x36
_UNKNOWN_37 = 0x37
_UNKNOWN_6B = struct.Struct("<H")
_UNKNOWN_6B_OFFSET = 0x6B
_UNKNOWN_7C = 0x7C
_COMMERCE_TYPE = 0x7D


def parse_itemtradegrouptonpc_records(data: bytes) -> list[dict]:
    """One record per item entry, in file order.

    Raises ValueError when a group or entry runs past the file, an entry names
    another character than its group, or bytes follow the last group.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its group count")

    records: list[dict] = []
    pos = COUNT_SIZE
    for group in range(u32(data, 0)):
        if pos + GROUP_HEADER.size > len(data):
            raise ValueError(f"{FILE_NAME} group {group} starts past the end of the file")
        character_id, item_count = GROUP_HEADER.unpack_from(data, pos)
        pos += GROUP_HEADER.size
        end = pos + item_count * ENTRY_SIZE
        if end > len(data):
            raise ValueError(
                f"{FILE_NAME} group {group} (character {character_id}) declares {item_count:,} items past the end"
            )
        records.extend(_entry(data, start, character_id) for start in range(pos, end, ENTRY_SIZE))
        pos = end

    if pos != len(data):
        raise ValueError(f"{FILE_NAME} groups end at {pos:,} but the file holds {len(data):,} bytes")
    return records


def _entry(data: bytes, start: int, group_character_id: int) -> dict:
    character_id, item_id = _ENTRY_HEAD.unpack_from(data, start)
    if character_id != group_character_id:
        raise ValueError(
            f"{FILE_NAME} entry at {start:,} names character {character_id}, its group {group_character_id}"
        )
    return {
        "character_id": character_id,
        "item_id": item_id,
        "trade_group_type": data[start + _TRADE_GROUP_TYPE],
        "commerce_type": data[start + _COMMERCE_TYPE],
        "unknown_37": data[start + _UNKNOWN_37],
        "unknown_6b": _UNKNOWN_6B.unpack_from(data, start + _UNKNOWN_6B_OFFSET)[0],
        "unknown_7c": data[start + _UNKNOWN_7C],
    }
