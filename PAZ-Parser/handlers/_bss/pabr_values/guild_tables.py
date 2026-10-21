"""Layouts of the guild tables (`guild*.bss`) that fit the PABR value tables.

A grade list holds one u8 flag per guild member grade, in grade order; the
cell names the grades whose flag is set. A reward list holds
`(item_key, item_count)` entries.
"""

from __future__ import annotations

from _common.skill import skill_name
from .guild_names import grade_text, number_list_text, reward_item_text
from .layout import NameLookup, RowCount, ValueField, ValueTable, unknown_fields


_GRADE = ValueField("grade", "B", "grades", is_counted_list=True, list_display=grade_text)
_SKILL_NAME = NameLookup("skill_name", "skill", skill_name)


def _reward_items(name: str, column: str) -> ValueField:
    """A u32-counted list of (u32 item key, u64 item count)."""
    return ValueField(name, "IQ", column, display=reward_item_text, is_counted_list=True)


GUILD_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "guildgiveaway.bss",
        (ValueField("giveaway_key", "I", "giveawayKey"), _reward_items("items", "items")),
        RowCount.COUNTED,
    ),
    ValueTable(
        "guildmatchexp.bss",
        (ValueField("combat_exp", "I", "combatExp", is_counted_list=True, list_display=number_list_text),),
        RowCount.COUNTED,
    ),
    ValueTable(
        "guildmatchoption.bss",
        (
            *unknown_fields(
                (0x04, "H"),
                (0x06, "H"),
                (0x08, "H"),
                (0x0A, "H"),
                (0x0C, "H"),
                (0x0E, "B"),
                (0x0F, "B"),
                (0x10, "8s"),
                (0x18, "I"),
                (0x1C, "B"),
                (0x1D, "B"),
                (0x1E, "H"),
                (0x20, "B"),
                (0x21, "B"),
            ),
            _reward_items("victory_reward_items", "victoryRewards"),
            _reward_items("defeat_reward_items", "defeatRewards"),
            ValueField("unknown_item_ids", "I", is_counted_list=True),
        ),
    ),
    ValueTable(
        "guildmatchrank.bss",
        (
            ValueField("unknown_00", "H"),
            ValueField("rank", "I", "rank"),
            ValueField("unknown_06", "B"),
            ValueField("min_point", "H", "minPoint"),
            ValueField("max_point", "I", "maxPoint"),
            *unknown_fields((0x0D, "B"), (0x0E, "B"), (0x0F, "B"), (0x10, "B"), (0x11, "B")),
        ),
        RowCount.COUNTED,
    ),
    ValueTable("guildright.bss", (ValueField("index", "B", "rightIndex"), _GRADE), RowCount.COUNTED),
    ValueTable(
        "guildskill.bss",
        (ValueField("skill_level", "H", "skillLevel"), ValueField("skill_no", "H", "skillId", _SKILL_NAME)),
        RowCount.COUNTED,
        first_fields=("skill_no",),
    ),
    ValueTable(
        "guildspecialskillright.bss",
        (ValueField("guild_skill_no", "H", "skillId", _SKILL_NAME), _GRADE),
        RowCount.COUNTED,
    ),
)
