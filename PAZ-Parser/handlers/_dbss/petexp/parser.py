from __future__ import annotations

import struct


_OFFSET_HEADER_SIZE = 4
_OFFSET_RECORD_SIZE = 10
_PAYLOAD_SIZE = 406
_LEVEL_CAPACITY = 50


def parse_petexpoffset_records(data: bytes) -> list[dict]:
    if len(data) < _OFFSET_HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _OFFSET_HEADER_SIZE + index * _OFFSET_RECORD_SIZE
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break

        exp_table_id, data_offset, data_size = struct.unpack_from("<HII", data, pos)
        records.append({
            "exp_table_id": exp_table_id,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": data_offset - 2,
        })

    return records


def parse_petexp_records(data: bytes, offset_data: bytes) -> list[dict]:
    records: list[dict] = []
    offsets = parse_petexpoffset_records(offset_data)

    for row, offset_record in enumerate(offsets):
        record_start = offset_record["record_start"]
        data_offset = offset_record["data_offset"]
        data_size = offset_record["data_size"]
        if record_start < _OFFSET_HEADER_SIZE or data_offset + data_size > len(data):
            raise ValueError(f"pet exp record {row} exceeds file size")
        if data_size < _PAYLOAD_SIZE:
            raise ValueError(f"pet exp record {row} payload is too small")

        prefix_id = struct.unpack_from("<H", data, record_start)[0]
        exp_table_id, max_level = struct.unpack_from("<HI", data, data_offset)
        if max_level > _LEVEL_CAPACITY:
            raise ValueError(f"pet exp record {row} max_level exceeds capacity")

        level_exp = struct.unpack_from(f"<{_LEVEL_CAPACITY}Q", data, data_offset + 6)

        populated = level_exp[:max_level]
        for level, required_exp in enumerate(populated, start=1):
            records.append({
                "row": row,
                "exp_table_id": exp_table_id,
                "prefix_exp_table_id": prefix_id,
                "offset_exp_table_id": offset_record["exp_table_id"],
                "key_match": prefix_id == exp_table_id == offset_record["exp_table_id"],
                "max_level": max_level,
                "level": level,
                "required_exp": required_exp,
                "data_offset": data_offset,
                "data_size": data_size,
            })

    return records
