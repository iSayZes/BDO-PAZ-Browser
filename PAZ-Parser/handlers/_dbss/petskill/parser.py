from __future__ import annotations

import struct


_HEADER_SIZE = 4
_OFFSET_RECORD_SIZE = 10
_KEY_PREFIX_SIZE = 2
_EFFECT_ROW_SIZE = 17
_EFFECT_ROW_COUNT = 11
_BASE_PAYLOAD_SIZE = _KEY_PREFIX_SIZE + (_EFFECT_ROW_SIZE * _EFFECT_ROW_COUNT)
_EXTRA_PAYLOAD_SIZE = _BASE_PAYLOAD_SIZE + 1


def parse_petskilloffset_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _HEADER_SIZE + index * _OFFSET_RECORD_SIZE
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break

        pet_skill_id, data_offset, data_size, padding = struct.unpack_from("<HIHH", data, pos)
        records.append({
            "pet_skill_id": pet_skill_id,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": data_offset - _KEY_PREFIX_SIZE,
            "padding": padding,
        })

    return records


def _parse_effect_row(payload: bytes, row_index: int) -> dict:
    pos = _KEY_PREFIX_SIZE + row_index * _EFFECT_ROW_SIZE
    if pos + _EFFECT_ROW_SIZE > len(payload):
        raise ValueError(f"petskill effect row {row_index} exceeds payload size")

    skill_group = payload[pos]
    row_level = payload[pos + 1]
    padding = struct.unpack_from("<H", payload, pos + 2)[0]
    raw_value_a = struct.unpack_from("<I", payload, pos + 4)[0]
    raw_value_b = struct.unpack_from("<I", payload, pos + 8)[0]
    row_marker = struct.unpack_from("<I", payload, pos + 12)[0]
    row_padding = payload[pos + 16]

    return {
        "row_index": row_index,
        "skill_group": skill_group,
        "level": row_level,
        "row_padding": row_padding,
        "padding": padding,
        "raw_value_a": raw_value_a,
        "raw_value_b": raw_value_b,
        "row_marker": row_marker,
    }


def parse_petskill_records(data: bytes, offset_data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    offsets = parse_petskilloffset_records(offset_data)
    if len(offsets) != count:
        raise ValueError(
            f"petskill count mismatch: main has {count}, offset has {len(offsets)}"
        )

    records: list[dict] = []
    for source_index, offset_record in enumerate(offsets):
        data_offset = offset_record["data_offset"]
        data_size = offset_record["data_size"]
        record_start = data_offset - _KEY_PREFIX_SIZE

        if data_size not in (_BASE_PAYLOAD_SIZE, _EXTRA_PAYLOAD_SIZE):
            raise ValueError(f"petskill record {source_index} has unexpected size {data_size}")
        if record_start < _HEADER_SIZE or data_offset + data_size > len(data):
            raise ValueError(f"petskill record {source_index} exceeds file size")

        key_prefix = struct.unpack_from("<H", data, record_start)[0]
        payload = data[data_offset:data_offset + data_size]
        pet_skill_id = struct.unpack_from("<H", payload, 0)[0]
        extra_marker = payload[_BASE_PAYLOAD_SIZE] if data_size == _EXTRA_PAYLOAD_SIZE else None
        effect_rows = [_parse_effect_row(payload, row_index) for row_index in range(_EFFECT_ROW_COUNT)]
        baseline = effect_rows[0]

        for effect in effect_rows[1:]:
            records.append({
                "source_index": source_index,
                "pet_skill_id": pet_skill_id,
                "skill_group": effect["skill_group"],
                "level": effect["level"],
                "raw_value_a": effect["raw_value_a"],
                "raw_value_b": effect["raw_value_b"],
                "row_marker": effect["row_marker"],
                "extra_marker": extra_marker,
                "data_offset": data_offset,
                "data_size": data_size,
                "key_prefix": key_prefix,
                "offset_pet_skill_id": offset_record["pet_skill_id"],
                "pet_skill_id_match": (
                    key_prefix == pet_skill_id == offset_record["pet_skill_id"]
                ),
                "baseline_raw_value_a": baseline["raw_value_a"],
                "baseline_raw_value_b": baseline["raw_value_b"],
                "baseline_row_marker": baseline["row_marker"],
            })

    return sorted(records, key=lambda record: (record["pet_skill_id"], record["level"]))
