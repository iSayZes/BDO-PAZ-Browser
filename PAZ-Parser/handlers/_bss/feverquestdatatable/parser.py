"""`feverquestdatatable.bss`: the Agris Fever quests and their point cost.

    PABR | u32 count | count x 8-byte row | string table | u32 string_table_start | u32 0

    row: u16 quest_chain_id | u16 quest_id | u32 consumption_fever_point

The string table is empty. Layout in docs/file-formats/feverquestdatatable_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "feverquestdatatable.bss"

_ROW = struct.Struct("<HHI")


def parse_feverquestdatatable_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    records: list[dict] = []
    for offset in fixed_row_offsets(data, _ROW.size, FILE_NAME):
        quest_chain_id, quest_id, consumption_fever_point = _ROW.unpack_from(data, offset)
        records.append({
            "quest_chain_id": quest_chain_id,
            "quest_id": quest_id,
            "packed_quest_id": quest_id << 16 | quest_chain_id,
            "consumption_fever_point": consumption_fever_point,
        })
    return records
