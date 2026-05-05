from __future__ import annotations

from typing import TypedDict


class QuestRecord(TypedDict):
    row: int
    offset: int
    size: int
    quest_id: int
    condition_script: str
    action_script: str
    objective_text_kr: str
    icon_path: str
    loc_texts_en: list[str]
