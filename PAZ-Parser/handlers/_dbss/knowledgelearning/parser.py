from __future__ import annotations

import zlib

from .model import KnowledgeLearningOffsetRecord, KnowledgeLearningRecord

KNOWLEDGE_RECORD_KIND = 13


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


def parse_knowledgelearning_offset_records(
    offset_data: bytes,
) -> list[KnowledgeLearningOffsetRecord]:
    records: list[KnowledgeLearningOffsetRecord] = []

    start = 12
    record_size = 12

    if len(offset_data) < start:
        return records

    count = (len(offset_data) - start) // record_size

    for index in range(count):
        pos = start + index * record_size

        records.append(KnowledgeLearningOffsetRecord(
            row=index,
            offset=read_u32(offset_data, pos),
            kind=read_u32(offset_data, pos + 4),
            idx_id=read_u32(offset_data, pos + 8),
        ))

    return records


def parse_knowledgelearning_records(
    dbss_data: bytes,
    offset_data: bytes,
    loc_entries: dict[int, str],
) -> list[KnowledgeLearningRecord]:
    records: list[KnowledgeLearningRecord] = []

    offset_records = parse_knowledgelearning_offset_records(offset_data)

    for offset_record in offset_records:
        dbss_offset = offset_record["offset"]
        kind = offset_record["kind"]
        mob_id = offset_record["idx_id"]

        if dbss_offset >= len(dbss_data):
            continue

        # Observed from build_knowledge.py:
        # field_a (+0) = mob_id
        # field_b (+9) = knowledge entry ID
        record_mob_id = read_u32(dbss_data, dbss_offset)
        knowledge_id = read_u32(dbss_data, dbss_offset + 9)

        if not record_mob_id:
            record_mob_id = mob_id

        records.append(KnowledgeLearningRecord(
            row=offset_record["row"],
            offset=dbss_offset,
            kind=kind,
            mob_id=record_mob_id,
            size=0,
            knowledge_id=knowledge_id,
            mob_name=loc_entries.get(record_mob_id, ""),
            knowledge_name=loc_entries.get(knowledge_id, ""),
        ))

    return records