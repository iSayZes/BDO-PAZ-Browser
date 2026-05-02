from __future__ import annotations

import zlib

from .model import MentalCardRecord


def read_u32(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 4 > len(data):
        return 0

    return int.from_bytes(data[offset:offset + 4], byteorder="little", signed=False)


def read_u64(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 8 > len(data):
        return 0

    return int.from_bytes(data[offset:offset + 8], byteorder="little", signed=False)


def parse_loc_entries(raw: bytes) -> dict[int, str]:
    try:
        data = zlib.decompress(raw[4:])
    except Exception:
        return {}

    entries: dict[int, str] = {}
    pos = 0

    while pos + 20 <= len(data):
        str_len = read_u32(data, pos)
        rec_id = read_u64(data, pos + 8)

        text_start = pos + 16
        text_end = text_start + str_len * 2

        if text_end + 4 > len(data):
            break

        text = data[text_start:text_end].decode("utf-16-le", errors="ignore")

        if text and text != "<null>":
            entries[rec_id] = text

        pos = text_end + 4

    return entries


def parse_mentalcard_records(
    mentalcard_data: bytes,
    offset_data: bytes,
    loc_entries: dict[int, str],
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
            entry_name=loc_entries.get(entry_id, ""),
            node_name=loc_entries.get(node_id, ""),
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