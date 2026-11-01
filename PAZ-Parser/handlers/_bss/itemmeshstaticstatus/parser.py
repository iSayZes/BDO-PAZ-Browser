"""`itemmeshstaticstatus.bss`: the item mesh table, one row per mesh key.

    u32 row_count | row_count x Row
    Row: str8 mesh_file | str8 effect_file | u64 unknown_effect_file_00
    | u32 mesh_key | u8 weapon_material | u8 unknown_effect_file_0d
    | u8 armor_material | u8 adult | u8 effects_change_type

No PABR magic and no string table. `mesh_key` is the `item_mesh_key` of
the itemenchant.dbss class entries, `mesh_file` a `.pac` path under
`character/model/`. Layout 1 in docs/file-formats/bss/itemmeshstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "itemmeshstaticstatus.bss"
KEY_FIELD = "mesh_key"

_TAIL = struct.Struct("<QI5B")
_TAIL_FIELDS = (
    "unknown_effect_file_00",
    KEY_FIELD,
    "weapon_material",
    "unknown_effect_file_0d",
    "armor_material",
    "adult",
    "effects_change_type",
)


def _read_row(reader: RecordReader) -> dict:
    mesh_file = reader.text(wide=False)
    effect_file = reader.text(wide=False)
    return {
        "mesh_file": mesh_file,
        "effect_file": effect_file,
        **dict(zip(_TAIL_FIELDS, reader.unpack(_TAIL), strict=True)),
    }


def parse_itemmesh_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or the rows end before it.
    """
    return read_counted_records(data, _read_row, FILE_NAME)
