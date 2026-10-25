"""`yachtgameboardinfo.bss`: the game boards (modes) of a Yar! match between two players.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0

    row: u32 game_board_key | u64 hand_rank_count | hand_rank_count x u32 hand_rank_key
         | u8 roll_count_max | u32 desc_kr_index | u32 icon_texture_index
         | u32 big_texture_index | u32 level | u8 is_use_matching

The three indexes point into the string table. Client 1784 rows have no
`is_use_matching` (Layout 1); this reads the live layout. Layouts in
docs/file-formats/bss/yachtgameboardinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at


FILE_NAME = "yachtgameboardinfo.bss"

# u32 game_board_key | u64 hand_rank_count
_ROW_HEAD = struct.Struct("<IQ")
_HAND_RANK_KEY_SIZE = 4
# u8 roll_count_max | u32 desc_kr_index | u32 icon_texture_index | u32 big_texture_index | u32 level | u8 is_use_matching
_ROW_TAIL = struct.Struct("<BIIIIB")


def parse_yachtgameboardinfo_records(data: bytes) -> list[dict]:
    """Every game board in file order, its strings read from the string table.

    Raises ValueError on a bad magic, a row that runs past the string table,
    rows that do not end where the string table starts, or a string that
    runs past the table.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    count = u32(data, 4)
    pos = HEADER_SIZE
    records: list[dict] = []
    for index in range(count):
        if pos + _ROW_HEAD.size > end:
            raise ValueError(f"{FILE_NAME} row {index} at 0x{pos:X} runs past the string table")
        key, hand_rank_count = _ROW_HEAD.unpack_from(data, pos)
        keys_start = pos + _ROW_HEAD.size
        tail_start = keys_start + hand_rank_count * _HAND_RANK_KEY_SIZE
        pos = tail_start + _ROW_TAIL.size
        if pos > end:
            raise ValueError(f"{FILE_NAME} row {key} lists {hand_rank_count} hand ranks past the string table")
        roll_count_max, desc_kr_index, icon_texture_index, big_texture_index, level, is_use_matching = (
            _ROW_TAIL.unpack_from(data, tail_start)
        )
        records.append({
            "game_board_key": key,
            "hand_rank_count": hand_rank_count,
            "hand_rank_keys": list(struct.unpack_from(f"<{hand_rank_count}I", data, keys_start)),
            "roll_count_max": roll_count_max,
            "desc_kr_index": desc_kr_index,
            "desc_kr": string_at(strings, desc_kr_index),
            "icon_texture_index": icon_texture_index,
            "icon_texture": string_at(strings, icon_texture_index),
            "big_texture_index": big_texture_index,
            "big_texture": string_at(strings, big_texture_index),
            "level": level,
            "is_use_matching": is_use_matching,
        })
    check_rows_end(data, pos, f"{FILE_NAME} rows")
    return records
