"""fairypotion.dbss: the potions a fairy may use, one item list per potion type.

The file is a u32 list count, then per list a u32 item count, that many u32
item IDs and a trailing u8 potion type (the list's key). See
docs/file-formats/fairypotion_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.offset_table import offset_records
from _common.pabr_offset import parse_bare_offset_rows


_FILE_NAME = "fairypotion.dbss"
_COUNT_SIZE = 4
_ITEM_ID_SIZE = 4
_POTION_TYPE_SIZE = 1


@dataclass(frozen=True)
class FairyPotionList:
    potion_type: int
    item_ids: tuple[int, ...]


def parse_fairypotion_lists(data: bytes) -> list[FairyPotionList]:
    """Every potion list in file order.

    Raises ValueError when a list runs past the end of the file or bytes
    remain after the last list.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{_FILE_NAME} is truncated: missing list count.")

    lists: list[FairyPotionList] = []
    pos = _COUNT_SIZE
    for index in range(u32(data, 0)):
        if pos + _COUNT_SIZE > len(data):
            raise ValueError(f"{_FILE_NAME} is truncated: list {index} has no item count.")

        item_count = u32(data, pos)
        items_start = pos + _COUNT_SIZE
        type_pos = items_start + item_count * _ITEM_ID_SIZE
        if type_pos + _POTION_TYPE_SIZE > len(data):
            raise ValueError(f"{_FILE_NAME} is truncated: list {index} runs past the end.")

        item_ids = struct.unpack_from(f"<{item_count}I", data, items_start)
        lists.append(FairyPotionList(potion_type=data[type_pos], item_ids=item_ids))
        pos = type_pos + _POTION_TYPE_SIZE

    if pos != len(data):
        raise ValueError(f"{_FILE_NAME} has {len(data) - pos} bytes after its last list.")

    return lists


def parse_fairypotion_records(data: bytes) -> list[dict]:
    """One row per listed item, ordered by potion type, then list order."""
    lists = sorted(parse_fairypotion_lists(data), key=lambda potion_list: potion_list.potion_type)
    return [
        {"potion_type": potion_list.potion_type, "item_id": item_id}
        for potion_list in lists
        for item_id in potion_list.item_ids
    ]


# The offset row points at the list's item count; the size covers the whole
# list including its trailing potion type byte.
parse_fairypotionoffset_records = offset_records(
    parse_bare_offset_rows,
    "potion_type",
    "data_offset",
    "data_size",
)
