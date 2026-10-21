"""`possiblefusionpet.bss`: the pets of each fusion key.

No PABR magic and no trailer:

    u32 count | Row[count] (u8 variant | u8 species | u8 unknown_02 | u8 tier | u16 pet_id)

The four key bytes are the fusion key of `pet.dbss`; the rows are sorted by
it read as a u32. Layout 1 in docs/file-formats/possiblefusionpet_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _dbss.pet.joins import fusion_key


FILE_NAME = "possiblefusionpet.bss"

_COUNT_SIZE = 4
_ROW = struct.Struct("<BBBBH")


def parse_possiblefusionpet_records(data: bytes) -> list[dict]:
    """Every row in file order, with its fusion key as one u32 (`fusion_key`).

    Raises ValueError when the file is shorter or longer than its count says.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")
    count = u32(data, 0)
    expected = _COUNT_SIZE + count * _ROW.size
    if len(data) != expected:
        raise ValueError(f"{FILE_NAME} is {len(data):,} bytes, {count:,} rows need {expected:,}")

    return [
        {
            "variant": variant,
            "species": species,
            "unknown_02": unknown_02,
            "tier": tier,
            "pet_id": pet_id,
            "fusion_key": fusion_key(variant, species, unknown_02, tier),
        }
        for variant, species, unknown_02, tier, pet_id in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]
