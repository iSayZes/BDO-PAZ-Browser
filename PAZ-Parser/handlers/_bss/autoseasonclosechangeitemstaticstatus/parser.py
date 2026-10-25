"""`autoseasonclosechangeitemstaticstatus.bss`: the Season gear that turns
into its normal version when a Season character graduates, and the season's
graduation settings.

    PABR | u32 row_count | row_count x row (16 bytes)
    | u32 count | count x season challenge (8 bytes)
    | u32 count | count x character type (2 bytes)
    | u32 count | count x u32 auto_graduation_quests
    | u32 count | count x u32 auto_graduation_items
    | bytes[4] unknown_auto_graduation_items_00
    | string table | u32 table_start | u32 0
    row: u32 index | u32 change_item_key | u32 before_item_key | u32 after_item_key
    season challenge: u16 challenge_key | u32 item_id | u8 unknown_06 | u8 unknown_07
    character type: u8 unknown_00 | u8 unknown_01

Layout 1 in docs/file-formats/bss/autoseasonclosechangeitemstaticstatus_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.counted_rows import read_counted_structs, read_counted_u32s
from _common.pabr_strings import HEADER_SIZE, U32_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "autoseasonclosechangeitemstaticstatus.bss"
KEY_FIELD = "index"

_ROW = struct.Struct("<IIII")
_ROW_FIELDS = (KEY_FIELD, "change_item_key", "before_item_key", "after_item_key")
_CHALLENGE = struct.Struct("<HIBB")
_CHALLENGE_FIELDS = ("challenge_key", "item_id", "unknown_06", "unknown_07")
_CHARACTER_TYPE = struct.Struct("<BB")
_CHARACTER_TYPE_FIELDS = ("unknown_00", "unknown_01")
_UNKNOWN_TAIL = struct.Struct("<4s")


class AutoSeasonCloseFile(NamedTuple):
    rows: list[dict]
    season_challenges: list[dict]
    auto_graduation_character_types: list[dict]
    # Packed quest IDs.
    auto_graduation_quests: list[int]
    # Item IDs.
    auto_graduation_items: list[int]
    # Four bytes as hex; they differ between clients.
    unknown_auto_graduation_items_00: str


def parse_autoseasonclose_file(data: bytes) -> AutoSeasonCloseFile:
    """The rows and the four lists after them.

    Raises ValueError on a bad magic or trailer, when a count runs past the
    string table, or when the lists do not end where it starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - U32_SIZE, end, FILE_NAME)
    parsed = AutoSeasonCloseFile(
        rows=read_counted_structs(reader, _ROW, _ROW_FIELDS, f"{FILE_NAME} row"),
        season_challenges=read_counted_structs(reader, _CHALLENGE, _CHALLENGE_FIELDS, f"{FILE_NAME} season challenge"),
        auto_graduation_character_types=read_counted_structs(
            reader, _CHARACTER_TYPE, _CHARACTER_TYPE_FIELDS, f"{FILE_NAME} character type",
        ),
        auto_graduation_quests=read_counted_u32s(reader, f"{FILE_NAME} graduation quest"),
        auto_graduation_items=read_counted_u32s(reader, f"{FILE_NAME} graduation item"),
        unknown_auto_graduation_items_00=reader.unpack(_UNKNOWN_TAIL)[0].hex(" "),
    )
    check_rows_end(data, reader.pos, f"{FILE_NAME} lists")
    return parsed
