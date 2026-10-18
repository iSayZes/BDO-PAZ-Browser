"""Display text of the quest reward entries read by `reward_entry.py`.

`panel_widget_questrewarditem.luac` names each reward type with a `GAME`
sheet key (`LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP`), an Amity reward as
`<NPC name> Amity <value>`, and fills `{mentalCardName}`, `{exp}`,
`{maxFeverPoint}` and `{addFeverPoint}` into the keys of the knowledge,
Contribution EXP and Agris Fever rewards. A key's text is LOC type 37 under
its `stringtable.bss` hash; the hashes are stored here, and a test checks
them against `stringtable.bss`.

The Family stat type (`12`) shows in the Family Stat column of `quest.dbss`,
so it has no text here.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_tagged, ui_key_text
from _common.character import character_name
from _common.html import e, html_list_cell, icon_html_label_cell
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.knowledge import knowledge_name
from _common.pa_text import pa_html, strip_pa_tags
from _dbss.lifeexp.labels import life_skill_name
from .reward_entry import (
    REWARD_EXP,
    REWARD_EXP_GRADE,
    REWARD_EXPLORE_EXP,
    REWARD_FEVER_POINT,
    REWARD_INTIMACY,
    REWARD_ITEM,
    REWARD_KNOWLEDGE,
    REWARD_LIFE_EXP,
    REWARD_SEASON_REWARD,
    REWARD_SKILL_EXP,
    REWARD_SKILL_EXP_GRADE,
    REWARD_TYPE_NAMES,
    RewardEntry,
)


# reward_type -> the GAME key the quest reward widget names it with.
_LABEL_KEYS = {
    REWARD_EXP: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP",
    REWARD_SKILL_EXP: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP",
    REWARD_LIFE_EXP: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_PRODUCTEXP",
    REWARD_INTIMACY: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_INTIMACY",
    REWARD_EXP_GRADE: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP_GRADE",
    REWARD_SKILL_EXP_GRADE: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP_GRADE",
    REWARD_SEASON_REWARD: "LUA_QUESTREWARD_SIMPLE_TOOLTIP_COMPLETE_SEASON",
}
# GAME keys with one `{param}` the widget fills: (key, param).
_KNOWLEDGE_KEY = ("LUA_REWARDITEM_KNOWLEDGE", "mentalCardName")
_EXPLORE_EXP_KEY = ("LUA_QUESTREWARD_EXPLOREEXP", "exp")
_MAX_FEVER_POINT_KEY = ("LUA_ACHIEVEMENT_REWARD_TYPE_MAXFEVERPOINT", "maxFeverPoint")
_ADD_FEVER_POINT_KEY = ("LUA_ACHIEVEMENT_REWARD_TYPE_ADDFEVERPOINT", "addFeverPoint")

KEY_HASHES = {
    GAME_SHEET: {
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP": 2472995372,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP": 4284641471,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_PRODUCTEXP": 1925150473,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_INTIMACY": 1556297376,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP_GRADE": 719304411,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP_GRADE": 1707267108,
        "LUA_QUESTREWARD_SIMPLE_TOOLTIP_COMPLETE_SEASON": 2918958536,
        "LUA_REWARDITEM_KNOWLEDGE": 544007691,
        "LUA_QUESTREWARD_EXPLOREEXP": 3088791961,
        "LUA_ACHIEVEMENT_REWARD_TYPE_MAXFEVERPOINT": 3666725375,
        "LUA_ACHIEVEMENT_REWARD_TYPE_ADDFEVERPOINT": 2092254369,
    }
}


def _label(reward_type: int) -> str:
    """The client's name of a reward type (`Skill EXP`), else the enum name."""
    text = ui_key_text(KEY_HASHES, GAME_SHEET, _LABEL_KEYS[reward_type])
    return text or REWARD_TYPE_NAMES[reward_type]


def _filled(reward_type: int, key_param: tuple[str, str], value: str) -> str:
    """The key's text with `value` in its `{param}`; else the enum name and the value."""
    key, param = key_param
    placeholder = f"{{{param}}}"
    tagged = ui_key_tagged(KEY_HASHES, GAME_SHEET, key)
    if placeholder not in tagged:
        return f"{REWARD_TYPE_NAMES[reward_type]} {value}"
    return strip_pa_tags(tagged.replace(placeholder, value)).strip()


def _item_text(reward: RewardEntry) -> str:
    return f"{item_key_text(reward['item_key'])} x{reward['item_count']:,}"


def _exp_text(reward: RewardEntry) -> str:
    return f"{_label(REWARD_EXP)} {reward['experience']:,}"


def _skill_exp_text(reward: RewardEntry) -> str:
    return f"{_label(REWARD_SKILL_EXP)} {reward['skill_experience']:,}"


def _life_exp_text(reward: RewardEntry) -> str:
    life_skill = life_skill_name(reward["life_experience_type"])
    return f"{_label(REWARD_LIFE_EXP)} {reward['life_experience']:,} ({life_skill})"


def _intimacy_text(reward: RewardEntry) -> str:
    character_key = reward["intimacy_character"]
    npc = character_name(character_key) or str(character_key)
    return f"{npc} {_label(REWARD_INTIMACY)} {reward['intimacy_value']:,}"


def _knowledge_text(reward: RewardEntry) -> str:
    card_key = reward["mental_card_key"]
    return _filled(REWARD_KNOWLEDGE, _KNOWLEDGE_KEY, knowledge_name(card_key) or str(card_key))


def _exp_grade_text(_reward: RewardEntry) -> str:
    # The widget shows the label alone; exp_grade stays on the entry.
    return _label(REWARD_EXP_GRADE)


def _skill_exp_grade_text(_reward: RewardEntry) -> str:
    # The entry stores no skillexpgrade() argument.
    return _label(REWARD_SKILL_EXP_GRADE)


def _explore_exp_text(reward: RewardEntry) -> str:
    return _filled(REWARD_EXPLORE_EXP, _EXPLORE_EXP_KEY, f"{reward['explore_exp']:,}")


def _fever_point_text(reward: RewardEntry) -> str | None:
    """Max points first, then recovery points, as the widget picks; None for neither."""
    if reward["max_fever_point"] > 0:
        return _filled(REWARD_FEVER_POINT, _MAX_FEVER_POINT_KEY, f"{reward['max_fever_point']:,}")
    if reward["add_fever_point"] > 0:
        return _filled(REWARD_FEVER_POINT, _ADD_FEVER_POINT_KEY, f"{reward['add_fever_point']:,}")
    return None


def _season_reward_text(_reward: RewardEntry) -> str:
    # The widget shows the label alone; season_no stays on the entry.
    return _label(REWARD_SEASON_REWARD)


_TEXTS: dict[int, Callable[[RewardEntry], str | None]] = {
    REWARD_EXP: _exp_text,
    REWARD_SKILL_EXP: _skill_exp_text,
    REWARD_LIFE_EXP: _life_exp_text,
    REWARD_ITEM: _item_text,
    REWARD_INTIMACY: _intimacy_text,
    REWARD_KNOWLEDGE: _knowledge_text,
    REWARD_EXP_GRADE: _exp_grade_text,
    REWARD_SKILL_EXP_GRADE: _skill_exp_grade_text,
    REWARD_EXPLORE_EXP: _explore_exp_text,
    REWARD_FEVER_POINT: _fever_point_text,
    REWARD_SEASON_REWARD: _season_reward_text,
}


def reward_text(reward: RewardEntry) -> str | None:
    """`EXP 5,000`, `Silver x1,000`, `[Knowledge] Pet - Dog`; None for a type without text."""
    text_of = _TEXTS.get(reward["reward_type"])
    return None if text_of is None else text_of(reward)


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
