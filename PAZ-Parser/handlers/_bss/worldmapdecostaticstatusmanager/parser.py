"""`worldmapdecostaticstatusmanager.bss`: the decoration models of the world map.

    u32 count | count x row
    row: u16 deco_index | str8 world_map_object_file | f32 location_x | f32 location_y
         | f32 location_z | f32 scale | f32 rotation | u16 unknown_world_map_object_file_14

No PABR magic and no string table. Layout 1 in
docs/file-formats/worldmapdecostaticstatusmanager_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "worldmapdecostaticstatusmanager.bss"
KEY_FIELD = "deco_index"

_KEY = struct.Struct("<H")
_PLACEMENT = struct.Struct("<5fH")
_PLACEMENT_FIELDS = (
    "location_x",
    "location_y",
    "location_z",
    "scale",
    "rotation",
    "unknown_world_map_object_file_14",
)


def _read_row(reader: RecordReader) -> dict:
    (deco_index,) = reader.unpack(_KEY)
    world_map_object_file = reader.text(wide=False)
    return {
        KEY_FIELD: deco_index,
        "world_map_object_file": world_map_object_file,
        **dict(zip(_PLACEMENT_FIELDS, reader.unpack(_PLACEMENT), strict=True)),
    }


def parse_worldmapdeco_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end before it."""
    return read_counted_records(data, _read_row, FILE_NAME)
