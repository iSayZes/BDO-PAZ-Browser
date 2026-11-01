"""`yachtnpcdiceinfo.bss`: the NPC opponents of the Yacht Dice minigame.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0

    row: u32 npc_dice_info_key | u16 npc_key | u32 dice_preset_key
         | u64 hand_rank_count | hand_rank_count x u32 hand_rank_key
         | u32 knowledge_key | u8 deck_limit | u8 roll_count_max

The string table is empty. Layout in docs/file-formats/bss/yachtnpcdiceinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start


FILE_NAME = "yachtnpcdiceinfo.bss"

# u32 npc_dice_info_key | u16 npc_key | u32 dice_preset_key | u64 hand_rank_count
_ROW_HEAD = struct.Struct("<IHIQ")
_HAND_RANK_KEY_SIZE = 4
# u32 knowledge_key | u8 deck_limit | u8 roll_count_max
_ROW_TAIL = struct.Struct("<IBB")


def parse_yachtnpcdiceinfo_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic, a row that runs past the string table,
    or rows that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    count = u32(data, 4)
    pos = HEADER_SIZE
    records: list[dict] = []
    for index in range(count):
        if pos + _ROW_HEAD.size > end:
            raise ValueError(f"{FILE_NAME} row {index} at 0x{pos:X} runs past the string table")
        key, npc_key, dice_preset_key, hand_rank_count = _ROW_HEAD.unpack_from(data, pos)
        keys_start = pos + _ROW_HEAD.size
        tail_start = keys_start + hand_rank_count * _HAND_RANK_KEY_SIZE
        pos = tail_start + _ROW_TAIL.size
        if pos > end:
            raise ValueError(f"{FILE_NAME} row {key} lists {hand_rank_count} hand ranks past the string table")
        knowledge_key, deck_limit, roll_count_max = _ROW_TAIL.unpack_from(data, tail_start)
        records.append({
            "npc_dice_info_key": key,
            "npc_key": npc_key,
            "dice_preset_key": dice_preset_key,
            "hand_rank_count": hand_rank_count,
            "hand_rank_keys": list(struct.unpack_from(f"<{hand_rank_count}I", data, keys_start)),
            "knowledge_key": knowledge_key,
            "deck_limit": deck_limit,
            "roll_count_max": roll_count_max,
        })
    check_rows_end(data, pos, f"{FILE_NAME} rows")
    return records
