from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import parse_bare_u32_offset_rows


def parse_employeenameoffset_records(data: bytes) -> list[dict]:
    return [
        {"employee_name_id": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]


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
        employee_name_id, char_count, unknown_08 = struct.unpack_from("<III", block, 0)
        name_end = 12 + char_count * 2
        terminator_offset = name_end

        if terminator_offset + 4 > len(block):
            continue

        name = block[12:name_end].decode("utf-16-le", errors="replace")
        terminator = u32(block, terminator_offset)

        records.append({
            "employee_name_id": employee_name_id,
            "name_kr": name,
            "char_count": char_count,
            "unknown_08": unknown_08,
            "terminator": terminator,
            "data_offset": start,
            "data_size": size,
            "offset_employee_name_id": expected_id,
            "count": count,
        })

    return records
