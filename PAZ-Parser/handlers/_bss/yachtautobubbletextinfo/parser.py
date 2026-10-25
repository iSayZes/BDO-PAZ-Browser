"""`yachtautobubbletextinfo.bss`: the speech bubbles of a Yar! match.

    PABR | u32 pc_count | pc_count x row | u32 npc_count | npc_count x row
    | string table | u32 string_table_start | u32 0

    row (36 bytes): u32 bubble_text_key | u16 character_key | u32 hand_rank_key
                    | u32[6] text_kr_indexes | u8 condition | u8 unknown_23

The player's rows come first, then the NPCs' rows. Each text index points
into the string table; unused slots point at an empty string. Layout in
docs/file-formats/bss/yachtautobubbletextinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at


FILE_NAME = "yachtautobubbletextinfo.bss"

PC_GROUP = "pc"
NPC_GROUP = "npc"
# The groups in file order; each is a u32 count, then its rows.
GROUPS = (PC_GROUP, NPC_GROUP)
TEXT_SLOTS = 6

_COUNT_SIZE = 4
_ROW = struct.Struct(f"<IHI{TEXT_SLOTS}IBB")


def _parse_row(data: bytes, start: int, group: str, strings: list[str]) -> dict:
    key, character_key, hand_rank_key, *rest = _ROW.unpack_from(data, start)
    text_indexes, (condition, unknown_23) = rest[:TEXT_SLOTS], rest[TEXT_SLOTS:]
    return {
        "bubble_text_key": key,
        "group": group,
        "character_key": character_key,
        "hand_rank_key": hand_rank_key,
        "text_kr_indexes": text_indexes,
        # Every slot's text, empty ones included, so a slot keeps its LOC `str_id4`.
        "texts_kr": [string_at(strings, index) for index in text_indexes],
        "condition": condition,
        "unknown_23": unknown_23,
    }


def parse_yachtautobubbletextinfo_records(data: bytes) -> list[dict]:
    """Every row in file order, the player's group first.

    Raises ValueError on a bad magic, a group that runs past the string
    table, rows that do not end where the string table starts, or a string
    that runs past the table.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    pos = HEADER_SIZE - _COUNT_SIZE
    records: list[dict] = []
    for group in GROUPS:
        if pos + _COUNT_SIZE > end:
            raise ValueError(f"{FILE_NAME} {group} count at 0x{pos:X} runs past the string table")
        count = u32(data, pos)
        rows_start = pos + _COUNT_SIZE
        pos = rows_start + count * _ROW.size
        if pos > end:
            raise ValueError(f"{FILE_NAME} {count} {group} rows run past the string table")
        records.extend(_parse_row(data, rows_start + i * _ROW.size, group, strings) for i in range(count))
    check_rows_end(data, pos, f"{FILE_NAME} rows")
    return records
