from __future__ import annotations

from _common.binary import u16, u32


_HEADER_SIZE = 4
_GROUP_HEADER_SIZE = 4
_ENTRY_SIZE = 0x10


def parse_plantworkerselect_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    group_count = u32(data, 0)
    pos = _HEADER_SIZE
    records: list[dict] = []

    for group in range(group_count):
        if pos + _GROUP_HEADER_SIZE > len(data):
            break

        entry_count = u32(data, pos)
        pos += _GROUP_HEADER_SIZE

        for row in range(entry_count):
            if pos + _ENTRY_SIZE > len(data):
                return records

            records.append({
                "group": group,
                "row": row,
                "entry_count": entry_count,
                "selection_id": u16(data, pos),
                "worker_id": u16(data, pos + 0x02),
                "zero_a": u32(data, pos + 0x04),
                "hire_cost": u32(data, pos + 0x08),
                "zero_b": u32(data, pos + 0x0C),
            })
            pos += _ENTRY_SIZE

    return records
