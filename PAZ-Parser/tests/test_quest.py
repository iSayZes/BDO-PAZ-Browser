from __future__ import annotations

from _common.quest.quest import split_packed_quest_id


def test_split_packed_quest_id() -> None:
    # Quest 1 of the first Growth Pass chain: (1 << 16) | 4464.
    assert split_packed_quest_id(1 << 16 | 4464) == (4464, 1)
    assert split_packed_quest_id(0xFFFF << 16 | 0xFFFF) == (0xFFFF, 0xFFFF)
