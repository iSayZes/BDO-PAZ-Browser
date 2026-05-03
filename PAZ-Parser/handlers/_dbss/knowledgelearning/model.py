from __future__ import annotations

from typing import TypedDict


class KnowledgeLearningRecord(TypedDict):
    offset: int
    kind: int
    knowledge_id: int
    knowledge_name: str


class KnowledgeLearningOffsetRecord(TypedDict):
    offset: int
    kind: int
    idx_id: int