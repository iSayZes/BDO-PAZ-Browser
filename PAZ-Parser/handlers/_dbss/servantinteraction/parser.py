"""`servantinteraction.dbss`: the Horse Communion actions each servant offers.

    u32 count | count x Record, back to back up to EOF
    Record: u16 character_id | u16 character_id_dup | u64 cool_time
            | u64 buff_count | u32 buff_keys x buff_count

`buff_keys` are `servantbuff.dbss` keys. Layout 2 in
docs/file-formats/dbss/servantinteraction_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "servantinteraction.dbss"

_COUNT = struct.Struct("<I")
# u16 character_id | u16 character_id_dup | u64 cool_time | u64 buff_count
_HEAD = struct.Struct("<HHQQ")


def _parse_record(reader: RecordReader, index: int) -> dict:
    character_id, character_id_dup, cool_time, buff_count = reader.unpack(_HEAD)
    if character_id_dup != character_id:
        raise ValueError(
            f"{FILE_NAME} record {index} at 0x{reader.pos - _HEAD.size:X} repeats "
            f"character {character_id_dup}, expected {character_id}"
        )
    buff_keys = reader.unpack(struct.Struct(f"<{buff_count}I"))
    return {
        "character_id": character_id,
        "cool_time": cool_time,
        "buff_keys": list(buff_keys),
    }


def parse_servantinteraction_records(data: bytes) -> list[dict]:
    """Every record in file order.

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
