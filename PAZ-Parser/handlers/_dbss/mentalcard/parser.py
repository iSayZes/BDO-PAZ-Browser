from __future__ import annotations

from _common.binary import u32 as read_u32
from _common.loc import loc_lookup
from .model import MentalCardRecord


def parse_mentalcard_records(
    mentalcard_data: bytes,
    offset_data: bytes,
) -> list[MentalCardRecord]:
    records: list[MentalCardRecord] = []

    start = 12
    record_size = 12

    if len(offset_data) < start:
        return records

    count = (len(offset_data) - start) // record_size

    for index in range(count):
        offset_record_pos = start + index * record_size

        mentalcard_offset = read_u32(offset_data, offset_record_pos)
        size = read_u32(offset_data, offset_record_pos + 4)
        internal_id = read_u32(offset_data, offset_record_pos + 8)

        if mentalcard_offset + 8 > len(mentalcard_data):
            continue

        entry_id = read_u32(mentalcard_data, mentalcard_offset)
        node_id = read_u32(mentalcard_data, mentalcard_offset + 4)

        records.append(MentalCardRecord(
            row=index,
            offset=mentalcard_offset,
            size=size,
            internal_id=internal_id,
            entry_id=entry_id,
            node_id=node_id,
            entry_name=loc_lookup(34, entry_id),
            node_name=loc_lookup(9, node_id),
        ))

    return records


def parse_mentalcard_offset_records(offset_data: bytes) -> list[tuple[int, int, int, int]]:
    records: list[tuple[int, int, int, int]] = []

    start = 12
    record_size = 12

    if len(offset_data) < start:
        return records

    count = (len(offset_data) - start) // record_size

    for index in range(count):
        pos = start + index * record_size
        records.append((
            index,
            read_u32(offset_data, pos),
            read_u32(offset_data, pos + 4),
            read_u32(offset_data, pos + 8),
        ))

    return records
