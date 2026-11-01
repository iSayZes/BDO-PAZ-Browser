"""`guildbossfieldinfo.bss`: a point per guild boss, keyed by `boss_spawn.bss` key.

    u32 count | count x (u32 boss_spawn_key | f32 x | f32 y | f32 z
                         | u32 boss_spawn_key_dup | f32 unknown_14)

No PABR magic and no string table. Layout 1 in
docs/file-formats/bss/guildbossfieldinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows


FILE_NAME = "guildbossfieldinfo.bss"
KEY_FIELD = "boss_spawn_key"

_ROW = struct.Struct("<I3fIf")
_FIELDS = (KEY_FIELD, "x", "y", "z", "boss_spawn_key_dup", "unknown_14")


def parse_guildbossfieldinfo_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)
