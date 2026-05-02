from __future__ import annotations

from typing import TypedDict


class MentalCardRecord(TypedDict):
    row: int
    offset: int
    size: int
    internal_id: int
    entry_id: int
    node_id: int
    entry_name: str
    node_name: str