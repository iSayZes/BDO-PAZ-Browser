"""`minigamereward.dbss`: energy and drop group of the cow, herbal machine and extractor minigames.

A u32 row count, then 13-byte rows back to back to the end of the file: the
u16 minigame key, the same key again, the i16 energy on a success and on a
failure, the u32 `itemmaingroup.bss` drop group and the u8 vehicle type the
player must be on. `minigamerewardoffset.dbss` points 2 bytes into a row, at
the second key, so the walk from the start needs no index. Layout in
docs/file-formats/dbss/minigamereward_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "minigamereward.dbss"
OFFSET_FILE = "minigamerewardoffset.dbss"

_COUNT_SIZE = 4
# minigame_key, minigame_key_dup, success_wp, fail_wp, drop_group, check_vehicle_type
_ROW = struct.Struct("<HHhhIB")
ROW_SIZE = _ROW.size


def parse_minigamereward_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file does not hold exactly its declared rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected = _COUNT_SIZE + count * ROW_SIZE
    if len(data) != expected:
        raise ValueError(f"{FILE_NAME} is {len(data):,} bytes; {count:,} rows of {ROW_SIZE} need {expected:,}")

    return [
        {
            "minigame_key": minigame_key,
            "success_wp": success_wp,
            "fail_wp": fail_wp,
            "drop_group": drop_group,
            "check_vehicle_type": check_vehicle_type,
            "minigame_key_dup": minigame_key_dup,
        }
        for minigame_key, minigame_key_dup, success_wp, fail_wp, drop_group, check_vehicle_type
        in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]
