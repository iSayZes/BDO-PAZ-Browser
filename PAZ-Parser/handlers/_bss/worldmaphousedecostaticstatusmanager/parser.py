"""`worldmaphousedecostaticstatusmanager.bss`: the world map models of the guild siege buildings.

    u32 count | count x row
    row: u16 character_key | u16 character_key_dup | str8 world_map_object_file
         | u32 object_change_level

No PABR magic and no string table. Layout 1 in
docs/file-formats/worldmaphousedecostaticstatusmanager_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "worldmaphousedecostaticstatusmanager.bss"
KEY_FIELD = "character_key"

_KEYS = struct.Struct("<HH")
_LEVEL = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    character_key, character_key_dup = reader.unpack(_KEYS)
    world_map_object_file = reader.text(wide=False)
    (object_change_level,) = reader.unpack(_LEVEL)
    return {
        KEY_FIELD: character_key,
        "character_key_dup": character_key_dup,
        "world_map_object_file": world_map_object_file,
        "object_change_level": object_change_level,
    }


def parse_worldmaphousedeco_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end before it."""
    return read_counted_records(data, _read_row, FILE_NAME)
