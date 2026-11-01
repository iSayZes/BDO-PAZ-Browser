"""`petpcroom.dbss`: the three equip skills of each PC room pet.

    u32 count | count x (u16 pet_id | u32 equip_skill_id_0 | u32 equip_skill_id_1
                         | u32 equip_skill_id_2)

`pet_id` is a `pet.dbss` key and each `equip_skill_id_*` a Section 1
`equip_skill_id` of `petequipskill.bss`. `petpcroomoffset.dbss` points at
each row's key, so the walk from the start needs no index. Layout 1 in
docs/file-formats/dbss/petpcroom_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "petpcroom.dbss"
OFFSET_FILE = "petpcroomoffset.dbss"

# One per Skillindex_0 to Skillindex_2 column of the Pet_PcRoom_Table sheet.
SKILL_FIELDS = ("equip_skill_id_0", "equip_skill_id_1", "equip_skill_id_2")

_COUNT_SIZE = 4
# pet_id, then the three equip skill ids
_ROW = struct.Struct("<H3I")


def parse_petpcroom_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    end = _COUNT_SIZE + count * _ROW.size
    if end != len(data):
        raise ValueError(f"{count:,} rows of {_ROW.size} bytes end at 0x{end:X}, the file is {len(data):,} bytes")

    return [
        {"pet_id": pet_id, **dict(zip(SKILL_FIELDS, skill_ids))}
        for pet_id, *skill_ids in _ROW.iter_unpack(data[_COUNT_SIZE:end])
    ]
