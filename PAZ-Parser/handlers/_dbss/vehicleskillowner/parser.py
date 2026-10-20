"""`vehicleskillowner.dbss`: the vehicle skills each servant can learn.

    u32 count | count x Record, back to back up to EOF
    Record: u16 character_id | u16 character_id_dup | u32 cant_learnable_rate
            | u32 skill_count | skill_count x 16-byte Skill

Each skill is a `vehicleskill.dbss` key with its learn weight (`able`), EXP
value and learn flag. Layout 2 in docs/file-formats/vehicleskillowner_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "vehicleskillowner.dbss"

_COUNT = struct.Struct("<I")
# u16 character_id | u16 character_id_dup | u32 cant_learnable_rate | u32 skill_count
_HEAD = struct.Struct("<HHII")
# u32 skill_key | u32 able | u32 add_exp | u8 is_learn | u8 unknown_0d | u16 unknown_0e
_SKILL = struct.Struct("<IIIBBH")


def _parse_skill(reader: RecordReader) -> dict:
    skill_key, able, add_exp, is_learn, unknown_0d, unknown_0e = reader.unpack(_SKILL)
    return {
        "skill_key": skill_key,
        "able": able,
        "add_exp": add_exp,
        "is_learn": is_learn,
        "unknown_0d": unknown_0d,
        "unknown_0e": unknown_0e,
    }


def _parse_record(reader: RecordReader, index: int) -> dict:
    character_id, character_id_dup, cant_learnable_rate, skill_count = reader.unpack(_HEAD)
    if character_id_dup != character_id:
        raise ValueError(
            f"{FILE_NAME} record {index} at 0x{reader.pos - _HEAD.size:X} repeats "
            f"character {character_id_dup}, expected {character_id}"
        )
    return {
        "character_id": character_id,
        "cant_learnable_rate": cant_learnable_rate,
        "skills": [_parse_skill(reader) for _ in range(skill_count)],
    }


def parse_vehicleskillowner_records(data: bytes) -> list[dict]:
    """Every servant in file order, each with its `skills` list.

    Raises ValueError when a record runs past the file, a record's
    `character_id_dup` differs from its `character_id`, or bytes follow the
    last declared record.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (count,) = reader.unpack(_COUNT)
    records = [_parse_record(reader, index) for index in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes follow record {count}")
    return records
