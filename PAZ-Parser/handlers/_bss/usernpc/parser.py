"""`usernpc.bss`: the Fishing God NPCs that take a player character's look.

    PABR | u32 count | count x 29-byte row | string table | u32 string_table_start | u32 0

Each row names the player character by number, places the NPC in the world
and points at the action it plays in the string table. Full layout in
docs/file-formats/usernpc_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


# u64 player_character_no | f32 pos_x, pos_y, pos_z | f32 direction | u32 action_ref | u8 class_type
_ROW = struct.Struct("<Q3ffIB")
_ROW_SIZE = 29
assert _ROW.size == _ROW_SIZE

_FILE_NAME = "usernpc.bss"


def parse_usernpc_records(data: bytes) -> list[dict]:
    """Every user NPC row in file order, with its action name resolved.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = fixed_row_offsets(data, _ROW_SIZE, _FILE_NAME)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        character_no, pos_x, pos_y, pos_z, direction, action_ref, class_type = _ROW.unpack_from(data, offset)
        records.append({
            "player_character_no": character_no,
            "pos_x": pos_x,
            "pos_y": pos_y,
            "pos_z": pos_z,
            "direction": direction,
            "action_ref": action_ref,
            "action_name": string_at(strings, action_ref),
            "class_type": class_type,
        })
    return records
