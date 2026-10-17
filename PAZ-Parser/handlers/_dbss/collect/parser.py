"""`collect.dbss`: gathering rules per Collect character.

A u32 row count, then rows back to back to the end of the file: the u16
character key, the name as a u64-prefixed UTF-16 string (empty on every
row), the key again, the gathering kind, time and HP, the product drop
group, three tool slots with a drop group each, 12 unknown bytes, the action
point and two spawn times. `collectoffset.dbss` points 2 bytes into a row,
at the name, so the walk from the start needs no index. Layout 2 in
docs/file-formats/collect_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "collect.dbss"
OFFSET_FILE = "collectoffset.dbss"
SLOT_COUNT = 3
# The tool type of an empty slot on the live client; its drop key is 0.
EMPTY_TOOL_TYPE = 19

_COUNT_SIZE = 4
_CHARACTER_KEY = struct.Struct("<H")
# character_key_dup, product_data_type, product_time, product_hp,
# product_decrease_hp, product_item_drop_key
_PRODUCT = struct.Struct("<HBIffI")
_TOOL_TYPES = struct.Struct(f"<{SLOT_COUNT}B")
_DROP_KEYS = struct.Struct(f"<{SLOT_COUNT}I")
_UNKNOWN = struct.Struct("<12s")
# action_point, spawn_delay_time, spawn_variable_time
_TAIL = struct.Struct("<III")


def parse_collect_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when a row runs past the file or the rows do not end
    where the file does.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    pos = _COUNT_SIZE
    records = []
    for _ in range(count):
        reader = RecordReader(data, pos, len(data), f"{FILE_NAME} row at 0x{pos:X}")
        records.append(_read_row(reader))
        pos = reader.pos
    if pos != len(data):
        raise ValueError(f"{FILE_NAME} has {len(data) - pos:,} bytes after its {count:,} rows")
    return records


def _read_row(reader: RecordReader) -> dict:
    (character_key,) = reader.unpack(_CHARACTER_KEY)
    name = reader.text(wide=True)
    (
        character_key_dup,
        product_data_type,
        product_time,
        product_hp,
        product_decrease_hp,
        product_item_drop_key,
    ) = reader.unpack(_PRODUCT)
    tool_types = reader.unpack(_TOOL_TYPES)
    drop_keys = reader.unpack(_DROP_KEYS)
    (unknown,) = reader.unpack(_UNKNOWN)
    action_point, spawn_delay_time, spawn_variable_time = reader.unpack(_TAIL)
    return {
        "character_key": character_key,
        "name": name,
        "character_key_dup": character_key_dup,
        "product_data_type": product_data_type,
        "product_time": product_time,
        "product_hp": product_hp,
        "product_decrease_hp": product_decrease_hp,
        "product_item_drop_key": product_item_drop_key,
        "collect_tool_types": list(tool_types),
        "collect_item_drop_keys": list(drop_keys),
        "unknown_name_22": unknown.hex(),
        "action_point": action_point,
        "spawn_delay_time": spawn_delay_time,
        "spawn_variable_time": spawn_variable_time,
    }
