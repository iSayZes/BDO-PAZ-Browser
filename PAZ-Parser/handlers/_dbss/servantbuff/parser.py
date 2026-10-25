"""`servantbuff.dbss`: Horse Communion actions, one variable-size record per key.

    u32 count | count x Record, back to back up to EOF
    Record: u32 key | u32 key_dup | str16 condition | str8 action_name
            | u32 action_hash | str8 servant_action_name
            | u32 servant_action_hash | u16 skill_no

Layout 2 in docs/file-formats/dbss/servantbuff_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "servantbuff.dbss"

_COUNT = struct.Struct("<I")
_KEYS = struct.Struct("<II")
_HASH = struct.Struct("<I")
_SKILL_NO = struct.Struct("<H")


def _parse_record(reader: RecordReader, index: int) -> dict:
    key, key_dup = reader.unpack(_KEYS)
    if key_dup != key:
        raise ValueError(f"{FILE_NAME} record {index} repeats key {key_dup}, expected {key}")
    condition = reader.text(wide=True)
    action_name = reader.text(wide=False)
    (action_hash,) = reader.unpack(_HASH)
    servant_action_name = reader.text(wide=False)
    (servant_action_hash,) = reader.unpack(_HASH)
    (skill_no,) = reader.unpack(_SKILL_NO)
    return {
        "key": key,
        "condition": condition,
        "action_name": action_name,
        "action_hash": action_hash,
        "servant_action_name": servant_action_name,
        "servant_action_hash": servant_action_hash,
        "skill_no": skill_no,
    }


def parse_servantbuff_records(data: bytes) -> list[dict]:
    """Every record in file order.

    Raises ValueError when a record runs past the file, a `key_dup` differs
    from its `key`, or bytes follow the last declared record.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (count,) = reader.unpack(_COUNT)
    records = [_parse_record(reader, index) for index in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes follow record {count}")
    return records


def servant_buff_skills(data: bytes | None) -> dict[int, int]:
    """Buff key -> `skill_no`, or an empty map without the file."""
    if data is None:
        return {}
    return {record["key"]: record["skill_no"] for record in parse_servantbuff_records(data)}
