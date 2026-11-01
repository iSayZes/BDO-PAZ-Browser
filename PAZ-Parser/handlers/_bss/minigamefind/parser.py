"""`minigamefind.bss`: the game types and Lakiaro rows of the Lakiaro digging minigame.

    PABR | u32 type_count | type_count x 92-byte Type Row
    | u32 collect_rate_count | collect_rate_count x 26-byte Collect Rate Row
    | string table | u32 string_table_start | u32 0

A Collect Rate Row names its image by string table index. Layout 1 in
docs/file-formats/bss/minigamefind_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Sequence
from typing import NamedTuple

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_pabr, check_rows_end, read_string_table, string_at


FILE_NAME = "minigamefind.bss"

# `next_game` of the last game type in a chain.
NO_NEXT_GAME = 0xFF

_COUNT_SIZE = 4

# (field, struct code, array length); length 0 is a single value. Doc order.
FieldSpec = tuple[str, str, int]

_TYPE_FIELDS: tuple[FieldSpec, ...] = (
    ("game_type", "B", 0),
    ("game_type_dup", "B", 0),
    ("next_game", "B", 0),
    ("min_damage_rate", "I", 0),
    ("next_rate", "I", 0),
    ("life_type", "B", 0),
    ("life_rate", "I", 0),
    ("tool_item_keys", "I", 5),
    ("tool_rate", "I", 0),
    ("stone_rate", "I", 0),
    ("stone_drop_item_key", "I", 0),
    ("col", "B", 0),
    ("row", "B", 0),
    ("start_pos", "B", 4),
    ("min_root_count", "B", 6),
    # Left, Right, Top, Bottom.
    ("begin_root_count", "B", 4),
    ("use_slot_indexes", "B", 4),
    ("reward_item_keys", "I", 6),
)

_COLLECT_RATE_FIELDS: tuple[FieldSpec, ...] = (
    ("character_key", "H", 0),
    ("unknown_02", "I", 0),
    # x1, y1, x2, y2 in the image.
    ("slot_coordinate", "H", 4),
    ("image_ref", "I", 0),
    ("main_game_type", "B", 0),
    ("collect_rate", "I", 0),
    ("depth", "B", 0),
    ("vary_wp", "H", 0),
)


def _row_struct(fields: Sequence[FieldSpec]) -> struct.Struct:
    return struct.Struct("<" + "".join(f"{length or ''}{code}" for _, code, length in fields))


_TYPE_ROW = _row_struct(_TYPE_FIELDS)
_COLLECT_RATE_ROW = _row_struct(_COLLECT_RATE_FIELDS)


class MiniGameFindTables(NamedTuple):
    types: list[dict]
    collect_rates: list[dict]


def parse_minigamefind(data: bytes) -> MiniGameFindTables:
    """Both tables in file order, with `next_game` None on the last game of a chain and image paths resolved.

    Raises ValueError on a bad magic, a count the file cannot hold, or rows
    that do not end where the string table starts.
    """
    check_pabr(data, FILE_NAME)
    type_values, cursor = _rows(data, HEADER_SIZE - _COUNT_SIZE, _TYPE_ROW, "type rows")
    rate_values, cursor = _rows(data, cursor, _COLLECT_RATE_ROW, "collect rate rows")
    check_rows_end(data, cursor, f"{FILE_NAME} rows")
    strings = read_string_table(data)

    types = [_type_record(_named(values, _TYPE_FIELDS)) for values in type_values]
    collect_rates = [_collect_rate_record(_named(values, _COLLECT_RATE_FIELDS), strings) for values in rate_values]
    return MiniGameFindTables(types, collect_rates)


def _rows(data: bytes, count_at: int, row: struct.Struct, what: str) -> tuple[list[tuple], int]:
    """The rows after the u32 count at `count_at`, and the offset where they end."""
    if count_at + _COUNT_SIZE > len(data):
        raise ValueError(f"{FILE_NAME}: the {what} count at 0x{count_at:X} runs past the file")
    start = count_at + _COUNT_SIZE
    end = start + u32(data, count_at) * row.size
    if end > len(data):
        raise ValueError(f"{FILE_NAME}: the {what} run past the end of the file")
    return list(row.iter_unpack(data[start:end])), end


def _named(values: Sequence[int], fields: Sequence[FieldSpec]) -> dict:
    """`values` of one row as field -> value, arrays as lists."""
    record: dict = {}
    pos = 0
    for name, _code, length in fields:
        if length:
            record[name] = list(values[pos : pos + length])
            pos += length
        else:
            record[name] = values[pos]
            pos += 1
    return record


def _type_record(record: dict) -> dict:
    next_game = record["next_game"]
    return {**record, "next_game": None if next_game == NO_NEXT_GAME else next_game}


def _collect_rate_record(record: dict, strings: list[str]) -> dict:
    return {**record, "image_file": string_at(strings, record["image_ref"])}
