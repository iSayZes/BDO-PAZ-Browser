"""`setoption.dbss`: the set effects of gear and furniture sets.

    u32 count | count x row
    row: u16 set_key | u32 set_option_type | u32[14] skill_keys
         | u64 equip_count | u32[equip_count] equip_items
         | u64 installation_count | u32[installation_count] installation_items
         | i32[14] points

Slot n (from 1) of `skill_keys` and `points` is the effect of n equipped
pieces. A gear set (`set_option_type` 0) fills `skill_keys` and
`equip_items`, a furniture set (1) `installation_items` and `points`.
`setoptionoffset.dbss` (u32 count, then u16 key, u32 offset and u32 size per
row, no PABR magic) points at the row start. Layout 1 in
docs/file-formats/dbss/setoption_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "setoption.dbss"
OFFSET_FILE = "setoptionoffset.dbss"
KEY_FIELD = "set_key"
# Set_1_Option to Set_14_Option of the EquipSetOption sheet: one slot per piece count.
SET_SLOTS = 14

_HEAD = struct.Struct("<HI")
_SLOTS = struct.Struct(f"<{SET_SLOTS}I")
_POINTS = struct.Struct(f"<{SET_SLOTS}i")
_U64 = struct.Struct("<Q")
_ITEM_SIZE = 4


def _read_items(reader: RecordReader, what: str) -> list[int]:
    (count,) = reader.unpack(_U64)
    if count * _ITEM_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} {what} count {count:,} at 0x{reader.pos - _U64.size:X} runs past the file")
    return list(reader.unpack(struct.Struct(f"<{count}I")))


def _read_row(reader: RecordReader) -> dict:
    set_key, set_option_type = reader.unpack(_HEAD)
    skill_keys = list(reader.unpack(_SLOTS))
    equip_items = _read_items(reader, "equip item")
    installation_items = _read_items(reader, "installation item")
    points = list(reader.unpack(_POINTS))
    return {
        KEY_FIELD: set_key,
        "set_option_type": set_option_type,
        "skill_keys": skill_keys,
        "equip_items": equip_items,
        "installation_items": installation_items,
        "points": points,
    }


def parse_setoption_records(data: bytes) -> list[dict]:
    """Every set in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_setoptionoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: set key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
