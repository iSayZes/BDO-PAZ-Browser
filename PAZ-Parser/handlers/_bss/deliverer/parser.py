"""`deliverer.bss`: the wagons and ships that carry the Transport (delivery) window's goods.

    PABR | u32 row_count | row_count x row (106 bytes) | string table
    | u32 table_start | u32 0
    row: u16 character_key | u16 character_key_dup | u32 delivery_route
         | u32 load_age | i64 fee | u32 object_file_index
         | u32[20] waypoint_name_indexes | u8 deliverer_type | u8 unknown_69

The object file and waypoint names are indexes into the PABR string table
at the end of the file; an unused waypoint slot points at an empty string.
Layout 1 in docs/file-formats/bss/deliverer_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "deliverer.bss"
KEY_FIELD = "character_key"
WAYPOINT_SLOTS = 20

_ROW = struct.Struct(f"<HHIIqI{WAYPOINT_SLOTS}IBB")


def parse_deliverer_records(data: bytes) -> list[dict]:
    """Every row in file order, with its strings read from the string table.

    Raises ValueError on a bad magic, rows that do not end where the string
    table starts, or a string that runs past it.
    """
    starts = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records = []
    for start in starts:
        values = _ROW.unpack_from(data, start)
        character_key, character_key_dup, delivery_route, load_age, fee, object_file_index = values[:6]
        waypoint_indexes = list(values[6 : 6 + WAYPOINT_SLOTS])
        deliverer_type, unknown_69 = values[6 + WAYPOINT_SLOTS :]
        records.append(
            {
                KEY_FIELD: character_key,
                "character_key_dup": character_key_dup,
                "delivery_route": delivery_route,
                "load_age": load_age,
                "fee": fee,
                "object_file_index": object_file_index,
                "object_file": string_at(strings, object_file_index),
                "waypoint_name_indexes": waypoint_indexes,
                # Unused slots point at an empty string; the names keep slot order.
                "waypoint_names": [name for name in (string_at(strings, index) for index in waypoint_indexes) if name],
                "deliverer_type": deliverer_type,
                "unknown_69": unknown_69,
            }
        )
    return records
