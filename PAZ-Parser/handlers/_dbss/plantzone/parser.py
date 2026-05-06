from __future__ import annotations

import struct

_OFFSET_ROW_SIZE = 12
_OFFSET_HEADER_SIZE = 4


def parse_offset_records(data: bytes) -> list[dict]:
    if len(data) < _OFFSET_HEADER_SIZE:
        return []

    count = struct.unpack_from("<I", data, 0)[0]
    records: list[dict] = []

    for i in range(count):
        pos = _OFFSET_HEADER_SIZE + i * _OFFSET_ROW_SIZE
        if pos + _OFFSET_ROW_SIZE > len(data):
            break
        record_id, _zero, data_offset, data_size = struct.unpack_from("<HHII", data, pos)
        records.append({
            "record_id": record_id,
            "data_offset": data_offset,
            "data_size": data_size,
        })

    return records


def parse_plantzone_records(data: bytes, offset_data: bytes) -> list[dict]:
    offset_records = parse_offset_records(offset_data)
    records: list[dict] = []

    for off in offset_records:
        start = off["data_offset"]
        size = off["data_size"]

        if start + size > len(data) or size < 32:
            continue

        payload = data[start : start + size]

        record_id = struct.unpack_from("<I", payload, 0x00)[0]
        variant = struct.unpack_from("<B", payload, 0x0E)[0]
        linked_id = struct.unpack_from("<I", payload, 0x17)[0]
        value_count = struct.unpack_from("<I", payload, 0x1B)[0]

        values_end = 0x1F + value_count
        values = list(payload[0x1F:values_end]) if values_end <= size else []

        records.append({
            "record_id": record_id,
            "variant": variant,
            "linked_id": linked_id,
            "values": values,
            "data_size": size,
        })

    return records
