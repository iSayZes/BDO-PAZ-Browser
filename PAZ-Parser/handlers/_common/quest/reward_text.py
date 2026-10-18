"""Display text of the quest reward entries read by `reward_entry.py`.

`panel_widget_questrewarditem.luac` names the reward types of the 2016
`gc::RewardType` with `GAME` sheet keys (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP`)
and an Amity reward as `<NPC name> Amity <value>`. A key's text is LOC type
37 under its `stringtable.bss` hash; the hashes are stored here, and a test
checks them against `stringtable.bss`.

The later reward types (5 to 18) keep their values in the undecoded tail of
the entry, so they have no text here; the Family stat type shows in the
Family Stat column of `quest.dbss`.
"""

from __future__ import annotations

from collections.abc import Sequence

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_text
from _common.character import character_name
from _common.html import e, html_list_cell, icon_html_label_cell
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.pa_text import pa_html
from _dbss.lifeexp.labels import life_skill_name
from .reward_entry import (
    REWARD_EXP,
    REWARD_INTIMACY,
    REWARD_ITEM,
    REWARD_LIFE_EXP,
    REWARD_SKILL_EXP,
    REWARD_TYPE_NAMES,
    RewardEntry,
)


# reward_type -> the GAME key the quest reward widget names it with.
_LABEL_KEYS = {
    REWARD_EXP: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP",
    REWARD_SKILL_EXP: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP",
    REWARD_LIFE_EXP: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_PRODUCTEXP",
    REWARD_INTIMACY: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_INTIMACY",
}

KEY_HASHES = {
    GAME_SHEET: {
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP": 2472995372,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP": 4284641471,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_PRODUCTEXP": 1925150473,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_INTIMACY": 1556297376,
    }
}


def _label(reward_type: int) -> str:
    """The client's name of a reward type (`Skill EXP`), else the enum name."""
    text = ui_key_text(KEY_HASHES, GAME_SHEET, _LABEL_KEYS[reward_type])
    return text or REWARD_TYPE_NAMES[reward_type]


def reward_text(reward: RewardEntry) -> str | None:
    """`EXP 5,000`, `Silver x1,000`, `Merindora Amity 40`; None for a type without text."""
    reward_type = reward["reward_type"]
    if reward_type == REWARD_ITEM:
        return f"{item_key_text(reward['item_key'])} x{reward['item_count']:,}"
    if reward_type == REWARD_EXP:
        return f"{_label(reward_type)} {reward['experience']:,}"
    if reward_type == REWARD_SKILL_EXP:
        return f"{_label(reward_type)} {reward['skill_experience']:,}"
    if reward_type == REWARD_LIFE_EXP:
        life_skill = life_skill_name(reward["life_experience_type"])
        return f"{_label(reward_type)} {reward['life_experience']:,} ({life_skill})"
    if reward_type == REWARD_INTIMACY:
        character_key = reward["intimacy_character"]
        npc = character_name(character_key) or str(character_key)
        return f"{npc} {_label(reward_type)} {reward['intimacy_value']:,}"
    return None


def reward_texts(rewards: Sequence[RewardEntry]) -> list[str]:
    """The text of every reward that has one, in entry order."""
    return [text for text in map(reward_text, rewards) if text is not None]


def _reward_cell(reward: RewardEntry, text: str) -> str:
    """An item with its icon and grade colour, then its count; other rewards as text."""
    if reward["reward_type"] != REWARD_ITEM:
        return e(text)
    label = f"{pa_html(item_key_text_tagged(reward['item_key']))} x{reward['item_count']:,}"
    return icon_html_label_cell(item_key_icon_path(reward["item_key"]), label)


def rewards_cell(rewards: Sequence[RewardEntry]) -> str:
    """Every reward that has a text, comma-separated, or ''."""
    cells = [
        _reward_cell(reward, text)
        for reward in rewards
        if (text := reward_text(reward)) is not None
    ]
    return html_list_cell(cells)
