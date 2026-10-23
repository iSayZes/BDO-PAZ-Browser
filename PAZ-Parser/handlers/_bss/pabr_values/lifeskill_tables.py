"""Layouts of the fishing tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/<stem>_bss.md`. The names follow the
`IceFishing` and `DiscardFish` sheets of a private server's
`DataSheets.bexcel` on client 1784. `lifeequipitemstaticstatusmanager.bss`
of the same batch has a list per life skill and its own handler
(`_bss/lifeequipitemstaticstatusmanager/`).
"""

from __future__ import annotations

from .layout import RowCount, ValueField, ValueTable
from .lifeskill_names import discard_grade_text, fishing_level_text


ICE_FISHING_FIELDS: tuple[ValueField, ...] = (
    ValueField("mini_game_group", "H", "miniGameGroup"),
    ValueField("min_wait_time", "Q", "minWaitTime"),
    ValueField("max_wait_time", "Q", "maxWaitTime"),
    ValueField("game_total_time", "Q", "gameTotalTime"),
    ValueField("game_min_time", "Q", "gameMinTime"),
    ValueField("game_max_time", "Q", "gameMaxTime"),
    ValueField("fish_hp", "I", "fishHp"),
    ValueField("decrease_hp", "I", "decreaseHp"),
    ValueField("time_per_tick", "Q", "timePerTick"),
    ValueField("critical_percent", "I", "criticalPercent"),
    ValueField("critical_decrease_hp", "I", "criticalDecreaseHp"),
    ValueField("possible_percent", "I", "possiblePercent"),
    ValueField("total_block", "I", "totalBlock"),
    ValueField("minigame_time", "Q", "minigameTime"),
    ValueField("random_minigame_time", "Q", "randomMinigameTime"),
    ValueField("fish_speed", "I", "fishSpeed"),
    ValueField("random_fish_speed", "I", "randomFishSpeed"),
    ValueField("player_move_speed", "I", "playerMoveSpeed"),
    ValueField("endurance_decrease", "I", "enduranceDecrease"),
    ValueField("reward_drop_group", "I", "rewardDropGroup"),
)


LIFE_SKILL_TABLES: tuple[ValueTable, ...] = (
    ValueTable("icefisingstaticstatus.bss", ICE_FISHING_FIELDS, RowCount.COUNTED, count_key="miniGameGroups"),
    ValueTable(
        "discardfish.bss",
        (
            ValueField("index", "I", "index"),
            ValueField("fishing_level", "I", "fishingLevel", display=fishing_level_text),
            ValueField("grade", "B", "discardGrade", display=discard_grade_text),
        ),
        RowCount.COUNTED,
        count_key="discardSteps",
    ),
)
