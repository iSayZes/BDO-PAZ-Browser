"""`itemexchangetoclass.dbss`: the item each class gets for one weapon exchange group.

A u32 row count, then fixed-size rows: the i32 group key, the same key again,
one u32 item key per class type (index = class type) and a u8 exchange type.
`itemexchangetoclassoffset.dbss` points 4 bytes into a row, at the second
key, so the walk from the start needs no index. The class slot count is the
only difference between the layouts: 47 on client 3474 (Layout 2), 32 on
client 1784 (Layout 1). Layouts in docs/file-formats/itemexchangetoclass_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "itemexchangetoclass.dbss"
OFFSET_FILE = "itemexchangetoclassoffset.dbss"

_COUNT_SIZE = 4
# key, key_dup
_KEYS = struct.Struct("<ii")
_ITEM_KEY_SIZE = 4
_EXCHANGE_TYPE_SIZE = 1
# Class slots per row, newest layout first: Layout 2 (client 3474), Layout 1 (client 1784).
LAYOUT_CLASS_SLOTS = (47, 32)


def row_size(class_slots: int) -> int:
    """Bytes of one row with `class_slots` item keys."""
    return _KEYS.size + class_slots * _ITEM_KEY_SIZE + _EXCHANGE_TYPE_SIZE


def _class_slots(data: bytes, count: int) -> int:
    """The slot count of the layout whose rows fill the file exactly.

    Raises ValueError when no known layout fits.
    """
    for class_slots in LAYOUT_CLASS_SLOTS:
        if _COUNT_SIZE + count * row_size(class_slots) == len(data):
            return class_slots
    sizes = ", ".join(str(row_size(slots)) for slots in LAYOUT_CLASS_SLOTS)
    raise ValueError(f"{count:,} rows fit no known row size ({sizes} bytes) in {len(data):,} bytes")


def _parse_row(data: bytes, offset: int, class_slots: int) -> dict:
    key, key_dup = _KEYS.unpack_from(data, offset)
    items_offset = offset + _KEYS.size
    item_keys = list(struct.unpack_from(f"<{class_slots}I", data, items_offset))
    exchange_type = data[items_offset + class_slots * _ITEM_KEY_SIZE]
    return {
        "key": key,
        "key_dup": key_dup,
        "item_keys": item_keys,
        "exchange_type": exchange_type,
    }


def parse_itemexchangetoclass_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows of a known layout.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    class_slots = _class_slots(data, count)
    size = row_size(class_slots)
    return [_parse_row(data, _COUNT_SIZE + index * size, class_slots) for index in range(count)]
