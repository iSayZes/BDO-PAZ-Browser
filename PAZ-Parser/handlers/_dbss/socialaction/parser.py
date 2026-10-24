"""`socialaction.dbss`: the social actions (emotes) a character can play.

    u32 count | count x (u16 social_action_key | row)
    row: u16 social_action_key_dup | str16 name_kr | str16 condition
         | str16 chatting_command_kr | u32 chatting_command_hash
         | str16 chatting_keywords_kr | str8 action_name | u32 action_hash
         | str16 icon_path | str16 condition_message_kr
         | u32 contents_group_count | contents_group_count x u32 contents_group_hash
         | u32 unknown_contents_group_hashes_00 | u8 unknown_contents_group_hashes_04

`socialactionoffset.dbss` (u32 count, then u16 key, u32 offset and u32 size
per row) points just past the u16 key, at `social_action_key_dup`, and its
size leaves the key out. Layout 1 in docs/file-formats/socialaction_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "socialaction.dbss"
OFFSET_FILE = "socialactionoffset.dbss"
KEY_FIELD = "social_action_key"

_KEYS = struct.Struct("<HH")
_U32 = struct.Struct("<I")
_TAIL = struct.Struct("<IB")


def _read_row(reader: RecordReader) -> dict:
    social_action_key, social_action_key_dup = reader.unpack(_KEYS)
    name_kr = reader.text(wide=True)
    condition = reader.text(wide=True)
    chatting_command_kr = reader.text(wide=True)
    (chatting_command_hash,) = reader.unpack(_U32)
    chatting_keywords_kr = reader.text(wide=True)
    action_name = reader.text(wide=False)
    (action_hash,) = reader.unpack(_U32)
    icon_path = reader.text(wide=True)
    condition_message_kr = reader.text(wide=True)
    (contents_group_count,) = reader.unpack(_U32)
    contents_group_hashes = [reader.unpack(_U32)[0] for _ in range(contents_group_count)]
    unknown_00, unknown_04 = reader.unpack(_TAIL)
    return {
        KEY_FIELD: social_action_key,
        "social_action_key_dup": social_action_key_dup,
        "name_kr": name_kr,
        "condition": condition,
        "chatting_command_kr": chatting_command_kr,
        "chatting_command_hash": chatting_command_hash,
        "chatting_keywords_kr": chatting_keywords_kr,
        "action_name": action_name,
        "action_hash": action_hash,
        "icon_path": icon_path,
        "condition_message_kr": condition_message_kr,
        "contents_group_hashes": contents_group_hashes,
        "unknown_contents_group_hashes_00": unknown_00,
        "unknown_contents_group_hashes_04": unknown_04,
    }


def parse_socialaction_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_socialactionoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
