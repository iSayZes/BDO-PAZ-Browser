from __future__ import annotations

from typing import TypedDict

from _common.quest.reward_entry import RewardEntry


class FamilyStat(TypedDict):
    """One permanent Family-stat reward from a counted reward entry."""

    entry: int
    type: int
    label: str
    value: float | None


class QuestRecord(TypedDict):
    row: int
    offset: int
    size: int
    packed_quest_id: int
    accept_dialog_key: int
    complete_dialog_key: int
    quest_chain_id: int
    quest_id: int
    quest_category: int
    block_kind: int
    condition_script: str
    action_script: str
    objective_text_kr: str
    icon_path: str
    base_rewards: list[RewardEntry]
    select_rewards: list[RewardEntry]
    family_stats: list[FamilyStat]
    loc_texts_en: list[str]
