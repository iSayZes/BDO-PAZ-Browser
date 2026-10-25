"""`petchangelook.dbss`: the looks a pet can change to, per look key.

    u32 count | Record[count]
    Record: u16 key_prefix | Payload
    Payload: u16 change_look_key | u32 look_count | Look[look_count]
    Look: u32 action_index | str8 icon_path | str8 icon_path_1 | str8 icon_path_2
          | u16 skill_level | u16 skill_no | u8 unknown_icon_path_2_04
          | str16 skin_name_kr | u8 unknown_skin_name_kr_00 | bytes[3] unknown_skin_name_kr_01

`petchangelookoffset.dbss` is a bare u16-keyed offset table into it (u32
count, then u16 key, u32 offset, u32 size per row); each offset points at the
payload, past the key prefix. The parser reads Layout 2 (client 3474) of
docs/file-formats/dbss/petchangelook_dbss.md and walks the main file without the
offset table.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "petchangelook.dbss"
OFFSET_FILE = "petchangelookoffset.dbss"

_COUNT_SIZE = 4
KEY_PREFIX_SIZE = 2
_KEY = struct.Struct("<H")
_PAYLOAD_HEAD = struct.Struct("<HI")
_ACTION_INDEX = struct.Struct("<I")
# skill_level, skill_no, unknown_icon_path_2_04
_SKILL = struct.Struct("<HHB")
# unknown_skin_name_kr_00, then the 3 bytes of unknown_skin_name_kr_01
_TAIL = struct.Struct("<B3s")


def _read_look(reader: RecordReader, change_look_key: int, look_count: int, look_index: int) -> dict:
    (action_index,) = reader.unpack(_ACTION_INDEX)
    icon_path = reader.text(wide=False)
    icon_path_1 = reader.text(wide=False)
    icon_path_2 = reader.text(wide=False)
    skill_level, skill_no, unknown_icon_path_2_04 = reader.unpack(_SKILL)
    skin_name_kr = reader.text(wide=True)
    unknown_skin_name_kr_00, unknown_skin_name_kr_01 = reader.unpack(_TAIL)
    return {
        "change_look_key": change_look_key,
        "look_count": look_count,
        "look_index": look_index,
        "action_index": action_index,
        "icon_path": icon_path,
        "icon_path_1": icon_path_1,
        "icon_path_2": icon_path_2,
        "skill_level": skill_level,
        "skill_no": skill_no,
        "unknown_icon_path_2_04": unknown_icon_path_2_04,
        "skin_name_kr": skin_name_kr,
        "unknown_skin_name_kr_00": unknown_skin_name_kr_00,
        "unknown_skin_name_kr_01": unknown_skin_name_kr_01.hex(" "),
    }


def parse_petchangelook_records(data: bytes) -> list[dict]:
    """One record per look, in file order, each with its look key and its place in the key's list.

    Raises ValueError when a record runs past the file, its key prefix differs
    from its key, or bytes are left after the last record.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    looks: list[dict] = []
    for _ in range(u32(data, 0)):
        (key_prefix,) = reader.unpack(_KEY)
        change_look_key, look_count = reader.unpack(_PAYLOAD_HEAD)
        if change_look_key != key_prefix:
            raise ValueError(f"look key {change_look_key} at 0x{reader.pos:X} follows key prefix {key_prefix}")
        looks += [_read_look(reader, change_look_key, look_count, index) for index in range(look_count)]
    if not reader.at_end():
        raise ValueError(f"{reader.remaining():,} bytes left after the last record of {FILE_NAME}")
    return looks


def parse_petchangelookoffset_records(data: bytes) -> list[dict]:
    """Every index row: the look key, where its payload starts and its size.

    Raises ValueError on a count the file cannot hold.
    """
    return [
        {"change_look_key": row.entry_id, "offset": row.offset, "size": row.size}
        for row in parse_bare_offset_rows(data)
    ]
