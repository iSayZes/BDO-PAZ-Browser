"""`knowledgelearning.dbss`: which character or item teaches which knowledge card.

The offset file holds `table_count` index tables, each `u32 count` plus
12-byte rows (`source_id`, `data_offset`, `size`). Each row points at a
13-byte record:

    u32 source_id | u32 source_type | u8 0 | u32 card_id

Table 0 is characters (`source_type` 0), table 1 items (`source_type` 1).
Full layout in docs/file-formats/dbss/knowledgelearning_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32

_RECORD = struct.Struct("<IIBI")
_INDEX_ROW = struct.Struct("<III")

SOURCE_CHARACTER = 0
SOURCE_ITEM = 1


@dataclass(frozen=True)
class KnowledgeIndexRow:
    table: int
    source_id: int
    offset: int
    size: int


@dataclass(frozen=True)
class KnowledgeLearningRecord:
    table: int
    source_id: int
    source_type: int
    card_id: int


def parse_knowledgelearning_offset_records(data: bytes) -> list[KnowledgeIndexRow]:
    """Every index row of every table, in file order.

    Raises ValueError when a table runs past the end, or when the tables do
    not end exactly at the end of the file.
    """
    if len(data) < 4:
        raise ValueError("knowledgelearningoffset.dbss is too short for its table count")

    rows: list[KnowledgeIndexRow] = []
    pos = 4
    for table in range(u32(data, 0)):
        count = u32(data, pos)
        end = pos + 4 + count * _INDEX_ROW.size
        if end > len(data):
            raise ValueError(f"knowledgelearningoffset.dbss table {table} runs past the end")
        rows.extend(
            KnowledgeIndexRow(table, source_id, offset, size)
            for source_id, offset, size in _INDEX_ROW.iter_unpack(data[pos + 4:end])
        )
        pos = end

    if pos != len(data):
        raise ValueError("knowledgelearningoffset.dbss has bytes after its last table")
    return rows


def parse_knowledgelearning_records(data: bytes, offset_data: bytes) -> list[KnowledgeLearningRecord]:
    """One record per index row. Raises ValueError on a row that does not fit."""
    records: list[KnowledgeLearningRecord] = []
    for row in parse_knowledgelearning_offset_records(offset_data):
        if row.size != _RECORD.size or row.offset + _RECORD.size > len(data):
            raise ValueError(f"knowledgelearning row for source {row.source_id} does not fit a record")
        source_id, source_type, _reserved, card_id = _RECORD.unpack_from(data, row.offset)
        if source_id != row.source_id:
            raise ValueError(f"knowledgelearning record at 0x{row.offset:X} does not repeat its source ID")
        records.append(KnowledgeLearningRecord(row.table, source_id, source_type, card_id))
    return records


def _sources_by_card(data: bytes, offset_data: bytes, source_type: int) -> dict[int, tuple[int, ...]]:
    """Map each knowledge card to the sources of one type that teach it, in ascending ID order."""
    sources: dict[int, list[int]] = {}
    for record in parse_knowledgelearning_records(data, offset_data):
        if record.source_type == source_type:
            sources.setdefault(record.card_id, []).append(record.source_id)

    return {card_id: tuple(sorted(ids)) for card_id, ids in sources.items()}


def build_knowledge_learning_character_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map each knowledge card to the characters that teach it, in ascending ID order.

    Monsters, NPCs and gathering nodes. The same pairs are stored grouped by
    card in `knowledgelearningcharacterkey.bss`.
    """
    return _sources_by_card(data, offset_data, SOURCE_CHARACTER)


def build_knowledge_learning_item_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map each knowledge card to the items that teach it, in ascending ID order."""
    return _sources_by_card(data, offset_data, SOURCE_ITEM)
