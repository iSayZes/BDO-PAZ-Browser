"""`experience.bss`: character level rules per class type and level.

    PABR | class_group* | byte[200] 0 | string table | u32 string_table_start | u32 0
    class_group = u32 level_count | level_count x 236-byte level record

There is no group count: the groups fill the space up to 200 zero bytes (one
stat body) before the string table. Full layout in
docs/file-formats/experience_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader
from .stat_body import STAT_BODY, STAT_BODY_SIZE, stat_fields


FILE_NAME = "experience.bss"
_FIRST_GROUP = 0x04
# The zero run between the last group and the string table, one stat body long.
_PADDING_SIZE = STAT_BODY_SIZE
_COUNT = struct.Struct("<I")

# class_type, level, then 28 zero bytes before the stat body.
_RECORD_HEAD = struct.Struct("<II28x")


def _read_record(reader: RecordReader) -> dict:
    class_type, level = reader.unpack(_RECORD_HEAD)
    return {"class_type": class_type, "level": level, **stat_fields(reader.unpack(STAT_BODY))}


def _read_group(reader: RecordReader, class_type: int) -> list[dict]:
    """The level records of one class group, level 0 first.

    Raises ValueError when a record names another class or level than its
    place, which means the record size or the group layout has changed.
    """
    (level_count,) = reader.unpack(_COUNT)
    records = [_read_record(reader) for _ in range(level_count)]
    for level, record in enumerate(records):
        if (record["class_type"], record["level"]) != (class_type, level):
            raise ValueError(
                f"{FILE_NAME} group {class_type} record {level} holds class "
                f"{record['class_type']} level {record['level']}"
            )
    return records


def parse_experience_records(data: bytes) -> list[dict]:
    """Every level record in file order, class type 0 first.

    Raises ValueError on a missing magic, a group that runs into the zero run
    before the string table, or groups that stop short of it.
    """
    groups_end = checked_string_table_start(data, FILE_NAME) - _PADDING_SIZE
    if groups_end < _FIRST_GROUP:
        raise ValueError(f"{FILE_NAME} is too short for its {_PADDING_SIZE}-byte zero run")
    reader = RecordReader(data, _FIRST_GROUP, groups_end, FILE_NAME)
    records: list[dict] = []
    class_type = 0
    while not reader.at_end():
        records.extend(_read_group(reader, class_type))
        class_type += 1
    if any(data[groups_end:groups_end + _PADDING_SIZE]):
        raise ValueError(f"{FILE_NAME} has data in the {_PADDING_SIZE} bytes before its string table")
    return records
