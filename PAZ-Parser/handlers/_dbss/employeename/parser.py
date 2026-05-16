from __future__ import annotations

import struct

from _common.binary import u32


_OFFSET_ROW_SIZE = 12
_OFFSET_HEADER_SIZE = 4


def parse_employeenameoffset_records(data: bytes) -> list[dict]:
    count = u32(data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _OFFSET_HEADER_SIZE + index * _OFFSET_ROW_SIZE
        if pos + _OFFSET_ROW_SIZE > len(data):
            break

        employee_name_id, offset, size = struct.unpack_from("<III", data, pos)
        records.append({
            "employee_name_id": employee_name_id,
            "data_offset": offset,
            "data_size": size,
        })

    return records


def parse_employeename_records(data: bytes, offset_data: bytes) -> list[dict]:
    count = u32(data, 0)
    offset_records = parse_employeenameoffset_records(offset_data)
    records: list[dict] = []

    for offset_record in offset_records:
        expected_id = offset_record["employee_name_id"]
        start = offset_record["data_offset"]
        size = offset_record["data_size"]
        end = start + size

        if start < 4 or end > len(data) or size < 16:
            continue

        block = data[start:end]
        employee_name_id, char_count, unknown_0 = struct.unpack_from("<III", block, 0)
        name_end = 12 + char_count * 2
        terminator_offset = name_end

        if terminator_offset + 4 > len(block):
            continue

        name = block[12:name_end].decode("utf-16-le", errors="replace")
        terminator = u32(block, terminator_offset)

        records.append({
            "employee_name_id": employee_name_id,
            "name_ko": name,
            "char_count": char_count,
            "unknown_0": unknown_0,
            "terminator": terminator,
            "data_offset": start,
            "data_size": size,
            "offset_employee_name_id": expected_id,
            "count": count,
        })

    return records
