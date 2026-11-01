"""`petskill.dbss` and `petskilloffset.dbss`: pet skill levels keyed by pet skill ID.

    u32 count | count x (u16 key_prefix | payload)
    payload = u16 pet_skill_id | u8 skill_type | i32 | u32 | u32 level_count
              | level_count x 17-byte level entry | [u32 list_count | list_count x u8]

The trailing list is missing on older clients. Full layout in
docs/file-formats/dbss/petskill_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


_HEADER_SIZE = 4
_OFFSET_RECORD_SIZE = 10
_KEY_PREFIX_SIZE = 2

_OFFSET_ROW = struct.Struct("<HIHH")
_PAYLOAD_HEAD = struct.Struct("<HBiII")
# level_dup, skill_type, level, param_0, param_1
_LEVEL_ENTRY = struct.Struct("<iBiii")
_COUNT = struct.Struct("<I")


def parse_petskilloffset_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _HEADER_SIZE + index * _OFFSET_RECORD_SIZE
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break

        pet_skill_id, data_offset, data_size, unknown_08 = _OFFSET_ROW.unpack_from(data, pos)
        records.append({
            "pet_skill_id": pet_skill_id,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": data_offset - _KEY_PREFIX_SIZE,
            "unknown_08": unknown_08,
        })

    return records


def _read_level_entry(reader: RecordReader) -> dict:
    level_dup, skill_type, level, param_0, param_1 = reader.unpack(_LEVEL_ENTRY)
    if level_dup != level:
        raise ValueError(f"petskill level entry keyed {level_dup} holds level {level}")
    return {"skill_type": skill_type, "level": level, "param_0": param_0, "param_1": param_1}


def _read_unknown_list(reader: RecordReader) -> tuple[int, ...]:
    """The trailing u8 list; empty when the payload ends after the levels (older clients)."""
    if reader.at_end():
        return ()
    (list_count,) = reader.unpack(_COUNT)
    return reader.unpack(struct.Struct(f"<{list_count}B"))


def _read_payload(data: bytes, offset_record: dict, source_index: int) -> list[dict]:
    """The level records of one payload.

    Raises ValueError when the payload does not end where its offset row says,
    which means the layout has changed.
    """
    data_offset = offset_record["data_offset"]
    data_size = offset_record["data_size"]
    record_start = data_offset - _KEY_PREFIX_SIZE
    if record_start < _HEADER_SIZE:
        raise ValueError(f"petskill record {source_index} starts inside the header")

    label = f"petskill record {source_index}"
    reader = RecordReader(data, data_offset, data_offset + data_size, label)
    (key_prefix,) = struct.unpack_from("<H", data, record_start)
    pet_skill_id, skill_type, unknown_03, unknown_07, level_count = reader.unpack(_PAYLOAD_HEAD)
    levels = [_read_level_entry(reader) for _ in range(level_count)]
    unknown_list = _read_unknown_list(reader)
    if not reader.at_end():
        raise ValueError(f"{label} has {reader.remaining()} bytes after its levels")

    shared = {
        "source_index": source_index,
        "pet_skill_id": pet_skill_id,
        "unknown_03": unknown_03,
        "unknown_07": unknown_07,
        "unknown_list": unknown_list,
        "data_offset": data_offset,
        "data_size": data_size,
        "key_prefix": key_prefix,
        "offset_pet_skill_id": offset_record["pet_skill_id"],
        "pet_skill_id_match": key_prefix == pet_skill_id == offset_record["pet_skill_id"],
    }
    return [
        {**shared, **level, "skill_type_match": level["skill_type"] == skill_type}
        for level in levels
    ]


def parse_petskill_records(data: bytes, offset_data: bytes) -> list[dict]:
    """One record per skill level, sorted by pet skill ID and level."""
    if len(data) < _HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    offsets = parse_petskilloffset_records(offset_data)
    if len(offsets) != count:
        raise ValueError(
            f"petskill count mismatch: main has {count}, offset has {len(offsets)}"
        )

    records = [
        record
        for source_index, offset_record in enumerate(offsets)
        for record in _read_payload(data, offset_record, source_index)
    ]
    return sorted(records, key=lambda record: (record["pet_skill_id"], record["level"]))
