"""`vehicleskillcount.dbss`: the highest `vehicleskill.dbss` skill key plus one.

One u8, the 2016 `gc::VehicleSkillStaticStatusManager::_count`, which the
client Lua reads as `vehicleSkillStaticStatus_skillCount()`. Layout 1 in
docs/file-formats/dbss/vehicleskillcount_dbss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "vehicleskillcount.dbss"

_COUNT = struct.Struct("<B")
FILE_SIZE = _COUNT.size


def parse_vehicleskillcount_record(data: bytes) -> dict:
    """The one value of the file.

    Raises ValueError when the file is not exactly one byte.
    """
    if len(data) != FILE_SIZE:
        raise ValueError(f"{FILE_NAME} is {FILE_SIZE} byte, the file has {len(data):,}")
    (count,) = _COUNT.unpack_from(data, 0)
    return {"count": count}
