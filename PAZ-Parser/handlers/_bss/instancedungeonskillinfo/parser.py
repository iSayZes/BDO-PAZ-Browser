"""`instancedungeonskillinfo.bss`: per class type, 20 lists of skill keys, then a table keyed by skill.

    PABR | 97 x Class Row | u32 skill_entry_count | skill_entry_count x Skill Entry
    | string table | u32 table_start | u32 0
    Class Row: 20 x (u64 skill_key_count | skill_key_count x u32 skill_key)
    Skill Entry: u16 skill_no | u16 unknown_02 | u32 unknown_04 | unknown_04 x u8 unknown_08

The file stores no class row count; 97 is the count of the newest layout
(client 3482, the row count of `skillquickslotinfo.bss` too). Client 3482
ships every list empty and no entries. Full layout in
docs/file-formats/instancedungeonskillinfo_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "instancedungeonskillinfo.bss"
CLASS_ROW_COUNT = 97
LIST_COUNT = 20

_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_ENTRY_HEAD = struct.Struct("<HHI")
# Right after the PABR magic: the file has no row count.
_ROWS_AT = 4


@dataclass(frozen=True)
class SkillList:
    class_type: int
    list_index: int
    skill_keys: tuple[int, ...]


@dataclass(frozen=True)
class SkillEntry:
    skill_no: int
    unknown_02: int
    unknown_08: tuple[int, ...]


@dataclass(frozen=True)
class InstanceDungeonSkills:
    # The lists that hold keys, class row by class row.
    lists: tuple[SkillList, ...]
    entries: tuple[SkillEntry, ...]


def _read_keys(reader: RecordReader, what: str) -> tuple[int, ...]:
    (count,) = reader.unpack(_U64)
    if count * _U32.size > reader.remaining():
        raise ValueError(f"{what} count {count:,} at 0x{reader.pos - _U64.size:X} runs past the rows")
    return tuple(reader.unpack(struct.Struct(f"<{count}I")))


def _read_entry(reader: RecordReader) -> SkillEntry:
    skill_no, unknown_02, value_count = reader.unpack(_ENTRY_HEAD)
    if value_count > reader.remaining():
        raise ValueError(f"{FILE_NAME} skill {skill_no} value count {value_count:,} runs past the rows")
    return SkillEntry(skill_no, unknown_02, tuple(reader.unpack(struct.Struct(f"<{value_count}B"))))


def parse_instancedungeonskillinfo(data: bytes) -> InstanceDungeonSkills:
    """The filled skill lists and the skill entries, in file order.

    Raises ValueError on a bad magic, or when the class rows and entries run
    past or end before the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _ROWS_AT, rows_end, FILE_NAME)
    lists: list[SkillList] = []
    for class_type in range(CLASS_ROW_COUNT):
        for list_index in range(LIST_COUNT):
            keys = _read_keys(reader, f"{FILE_NAME} class {class_type} list {list_index}")
            if keys:
                lists.append(SkillList(class_type, list_index, keys))
    (entry_count,) = reader.unpack(_U32)
    entries = tuple(_read_entry(reader) for _ in range(entry_count))
    check_rows_end(data, reader.pos, f"{FILE_NAME} skill entries")
    return InstanceDungeonSkills(tuple(lists), entries)
