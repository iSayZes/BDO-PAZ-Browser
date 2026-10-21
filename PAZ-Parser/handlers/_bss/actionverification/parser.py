"""`actionverification.bss`: action name hashes and `AbleCallTime` per character key.

    PABR | u32 count | count x (u16 character_key | u32 action_count
    | action_count x (u32 action_hash | u32 able_call_time))
    | string table (0 strings) | u32 string_table_start | u32 0

Layout in docs/file-formats/actionverification_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start


FILE_NAME = "actionverification.bss"

_COUNT_OFFSET = 4
_CHARACTER_HEAD = struct.Struct("<HI")
_ACTION = struct.Struct("<II")


def parse_actionverification_records(data: bytes) -> list[dict]:
    """One record per action, in file order, each with its character key.

    Raises ValueError on a missing magic or trailer, a character that runs
    past the string table, or characters that do not end where it starts.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    pos = HEADER_SIZE
    records: list[dict] = []
    for index in range(u32(data, _COUNT_OFFSET)):
        if pos + _CHARACTER_HEAD.size > rows_end:
            raise ValueError(f"{FILE_NAME}: character {index} at 0x{pos:X} runs past the characters")
        character_key, action_count = _CHARACTER_HEAD.unpack_from(data, pos)
        actions_start = pos + _CHARACTER_HEAD.size
        pos = actions_start + action_count * _ACTION.size
        if pos > rows_end:
            raise ValueError(
                f"{FILE_NAME}: character {character_key} has {action_count} actions, "
                "past the end of the characters"
            )
        records.extend(
            {"character_key": character_key, "action_hash": action_hash, "able_call_time": able_call_time}
            for action_hash, able_call_time in _ACTION.iter_unpack(data[actions_start:pos])
        )
    check_rows_end(data, pos, f"{FILE_NAME} characters")
    return records
