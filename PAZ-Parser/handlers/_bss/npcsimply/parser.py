"""`npcsimply.bss`: compact identity table for service and story NPCs.

    PABR | u32 count | count x 33-byte row | string table | u32 string_table_start | u32 0

Each row maps a character ID to its primary SpawnType role and string-table
indexes for the action script, Korean name and Korean role text. Full layout in
docs/file-formats/bss/npcsimply_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.knowledge_script import knowledge_id_of
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at, string_table_start


# u16 character_id | u8 unknown_02 | u8 zero | u32 kind | u32 script_ref
# | u32 lease_item_id | u16 lease_cost | u16 unknown_12 | u8 has_lease_condition
# | u32 name_ref | u32 role_ref | u32 padding
_RECORD = struct.Struct("<HBBIIIHHBIII")
_RECORD_SIZE = 33
assert _RECORD.size == _RECORD_SIZE


def parse_npcsimply_records(data: bytes) -> list[dict]:
    """Every NPC row in file order, with its strings resolved.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = fixed_row_offsets(data, _RECORD_SIZE, "npcsimply.bss")
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        (
            character_id, unknown_02, _zero, kind, script_ref,
            lease_item_id, lease_cost, unknown_12, has_lease_condition,
            name_ref, role_ref, _padding,
        ) = _RECORD.unpack_from(data, offset)
        script = string_at(strings, script_ref)
        records.append({
            "character_id": character_id,
            "unknown_02": unknown_02,
            "kind": kind,
            "name_kr": string_at(strings, name_ref),
            "role_kr": string_at(strings, role_ref),
            "script": script,
            "knowledge_id": knowledge_id_of(script),
            "lease_item_id": lease_item_id,
            "lease_cost": lease_cost,
            "unknown_12": unknown_12,
            "has_lease_condition": has_lease_condition,
        })
    return records
