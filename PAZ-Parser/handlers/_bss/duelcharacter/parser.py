"""`duelcharacter.bss`: the Tag Characters (duel character) options, one fixed record.

    u32 item_copy_quest | u32 need_item_for_copy | u32 need_item_for_individual_copy
    | 11 x u32 unknown_0c .. unknown_34 | u16 unknown_38

58 bytes in all. Layout 1 in docs/file-formats/bss/duelcharacter_bss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "duelcharacter.bss"

_RECORD = struct.Struct("<14IH")
_FIELDS = (
    "item_copy_quest",
    "need_item_for_copy",
    "need_item_for_individual_copy",
    "unknown_0c",
    "unknown_10",
    "unknown_14",
    "unknown_18",
    "unknown_1c",
    "unknown_20",
    "unknown_24",
    "unknown_28",
    "unknown_2c",
    "unknown_30",
    "unknown_34",
    "unknown_38",
)


def parse_duelcharacter_records(data: bytes) -> list[dict]:
    """The one record. Raises ValueError when the file is not 58 bytes."""
    if len(data) != _RECORD.size:
        raise ValueError(f"{FILE_NAME} is {len(data):,} bytes, the record is {_RECORD.size}")
    return [dict(zip(_FIELDS, _RECORD.unpack(data), strict=True))]
