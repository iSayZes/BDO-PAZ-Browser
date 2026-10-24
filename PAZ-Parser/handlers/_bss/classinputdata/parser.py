"""`classinputdata.bss`: key commands by index and `ClassNo`.

    PABR | u32 index_count | index_count x Index Row | u32 string_count | strings
    | u32 table_start | u32 0
    Index Row: u32 index | u32 class_count | class_count x Class Entry
    Class Entry: u8 class_no | u64 command_count | command_count x u32 command

Each command is a `CppEnums.ActionInputType` value (`ACTION_INPUT_TYPES`).
The string table holds no strings. Layout 1 in
docs/file-formats/classinputdata_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "classinputdata.bss"
# CppEnums.ActionInputType in value order from 0, without the prefix
# (global_define_cpp_enum.luac, client 3482).
ACTION_INPUT_TYPES: tuple[str, ...] = (
    "MoveFront", "MoveBack", "MoveLeft", "MoveRight", "Attack1", "Attack2", "Dash", "Jump",
    "Interaction", "AutoRun", "WeaponInOut", "CameraReset", "CrouchOrSkill", "GrabOrGuard", "Kick",
    "ServantOrder1", "ServantOrder2", "ServantOrder3", "ServantOrder4",
    "QuickSlot1", "QuickSlot2", "QuickSlot3", "QuickSlot4", "QuickSlot5", "QuickSlot6", "QuickSlot7",
    "QuickSlot8", "QuickSlot9", "QuickSlot10", "QuickSlot11", "QuickSlot12", "QuickSlot13",
    "QuickSlot14", "QuickSlot15", "QuickSlot16", "QuickSlot17", "QuickSlot18", "QuickSlot19",
    "QuickSlot20", "Complicated0", "Complicated1", "Complicated2", "Complicated3", "AutoMoveWalkMode",
    "CameraUp", "CameraDown", "CameraLeft", "CameraRight", "CameraRotateGameMode", "PushToTalk",
    "WalkMove", "KBAction1", "KBAction2", "KBAction3", "CameraReflect", "Grenade",
    "SocialAction0", "SocialAction1", "SocialAction2", "SocialAction3", "SocialAction4",
    "SocialAction5", "Esc", "SocialAction6", "Undefined",
)

# The index rows follow the PABR magic and their count.
_COUNT_AT = 4
_U32 = struct.Struct("<I")
_INDEX_HEAD = struct.Struct("<II")
_CLASS_HEAD = struct.Struct("<BQ")


def _read_class_entry(reader: RecordReader, index: int) -> dict:
    class_no, command_count = reader.unpack(_CLASS_HEAD)
    if command_count * _U32.size > reader.remaining():
        raise ValueError(
            f"{FILE_NAME} index {index} class {class_no} command count {command_count:,} runs past the string table"
        )
    commands = list(reader.unpack(struct.Struct(f"<{command_count}I")))
    return {"index": index, "class_no": class_no, "commands": commands}


def parse_classinput_records(data: bytes) -> list[dict]:
    """One record per class entry, index row by index row, in file order.

    Raises ValueError on a bad PABR magic or trailer, or when a count runs
    past the string table or the rows do not end where it starts.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _COUNT_AT, table_start, FILE_NAME)
    (index_count,) = reader.unpack(_U32)
    records: list[dict] = []
    for _ in range(index_count):
        index, class_count = reader.unpack(_INDEX_HEAD)
        records += [_read_class_entry(reader, index) for _ in range(class_count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X}, the string table starts at 0x{table_start:X}")
    return records
