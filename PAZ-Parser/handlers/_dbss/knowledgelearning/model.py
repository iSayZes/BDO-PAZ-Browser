from __future__ import annotations

from typing import TypedDict


class KnowledgeLearningRecord(TypedDict):
    row: int
    offset: int
    kind: int
    mob_id: int
    size: int
    knowledge_id: int
    mob_name: str
    knowledge_name: str


class KnowledgeLearningOffsetRecord(TypedDict):
    row: int
    offset: int
    kind: int
    idx_id: int