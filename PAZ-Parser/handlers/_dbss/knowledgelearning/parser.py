from __future__ import annotations

from _common.binary import u32 as read_u32
from _common.loc import loc_lookup
from .model import KnowledgeLearningOffsetRecord, KnowledgeLearningRecord


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
            offset=read_u32(offset_data, pos),
            kind=read_u32(offset_data, pos + 4),
            idx_id=read_u32(offset_data, pos + 8),
        ))

    return records


def parse_knowledgelearning_records(
    dbss_data: bytes,
    offset_data: bytes,
) -> list[KnowledgeLearningRecord]:
    records: list[KnowledgeLearningRecord] = []

    offset_records = parse_knowledgelearning_offset_records(offset_data)

    for offset_record in offset_records:
        dbss_offset = offset_record["offset"]
        kind = offset_record["kind"]

        if dbss_offset >= len(dbss_data):
            continue

        knowledge_id = read_u32(dbss_data, dbss_offset + 9)

        records.append(KnowledgeLearningRecord(
            offset=dbss_offset,
            kind=kind,
            knowledge_id=knowledge_id,
            knowledge_name=loc_lookup(34, knowledge_id),
        ))

    return records
