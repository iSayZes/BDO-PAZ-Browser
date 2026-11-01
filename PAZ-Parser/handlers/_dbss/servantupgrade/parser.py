"""`servantupgrade.dbss`: ship upgrade recipes, grouped by the ship before the upgrade.

    u32 group_count | group_count x (u32 upgrade_count | upgrade_count x 172-byte Upgrade)
    Upgrade: u16 character_id | u16 upgrade_character_id
             | 4 x Item main_items | 10 x Item sub_items
    Item: u32 item_key | u64 count

`servantupgradeoffset.dbss` indexes each upgrade per ship and target ship.
Layout 1 in docs/file-formats/dbss/servantupgrade_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "servantupgrade.dbss"
OFFSET_FILE = "servantupgradeoffset.dbss"

_U32 = struct.Struct("<I")
_SHIPS = struct.Struct("<HH")
_ITEM = struct.Struct("<IQ")
_MAIN_ITEMS = 4
_SUB_ITEMS = 10
UPGRADE_SIZE = _SHIPS.size + (_MAIN_ITEMS + _SUB_ITEMS) * _ITEM.size
# u16 character_id | u32 upgrade_count, then the offset rows.
_OFFSET_GROUP_HEAD = struct.Struct("<HI")
# u16 upgrade_character_id | u32 offset | u32 size
_OFFSET_ROW = struct.Struct("<HII")


def _items(reader: RecordReader, slots: int) -> list[dict]:
    return [dict(zip(("item_key", "count"), reader.unpack(_ITEM), strict=True)) for _ in range(slots)]


def _parse_upgrade(reader: RecordReader, group_index: int) -> dict:
    character_id, upgrade_character_id = reader.unpack(_SHIPS)
    return {
        "character_id": character_id,
        "upgrade_character_id": upgrade_character_id,
        "group_index": group_index,
        "main_items": _items(reader, _MAIN_ITEMS),
        "sub_items": _items(reader, _SUB_ITEMS),
    }


def parse_servantupgrade_records(data: bytes) -> list[dict]:
    """Every upgrade in file order, with the index of its group.

    Raises ValueError when an upgrade runs past the file, a group mixes
    ships, or bytes follow the last declared group.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (group_count,) = reader.unpack(_U32)
    records: list[dict] = []
    for group_index in range(group_count):
        (upgrade_count,) = reader.unpack(_U32)
        upgrades = [_parse_upgrade(reader, group_index) for _ in range(upgrade_count)]
        ships = {upgrade["character_id"] for upgrade in upgrades}
        if len(ships) > 1:
            raise ValueError(f"{FILE_NAME} group {group_index} holds ships {sorted(ships)}")
        records.extend(upgrades)
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes follow group {group_count}")
    return records


def parse_servantupgrade_offset_records(data: bytes) -> list[dict]:
    """One row per indexed upgrade: ship, target ship, offset and size, in file order.

    Raises ValueError when a group runs past the file or bytes follow the last one.
    """
    reader = RecordReader(data, 0, len(data), OFFSET_FILE)
    (group_count,) = reader.unpack(_U32)
    rows: list[dict] = []
    for _ in range(group_count):
        character_id, upgrade_count = reader.unpack(_OFFSET_GROUP_HEAD)
        for _ in range(upgrade_count):
            upgrade_character_id, offset, size = reader.unpack(_OFFSET_ROW)
            rows.append(
                {
                    "character_id": character_id,
                    "upgrade_character_id": upgrade_character_id,
                    "offset": offset,
                    "size": size,
                }
            )
    if not reader.at_end():
        raise ValueError(f"{OFFSET_FILE}: {reader.remaining():,} bytes follow group {group_count}")
    return rows
