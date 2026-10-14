from __future__ import annotations

from _common.loc import loc_lookup
from _common.pa_text import strip_pa_tags
from _common.text_bind import resolve_text_binds

LOC_QUEST = 18


def quest_text_tagged(str_id1: int, str_id2: int, str_id4: int = 0) -> str:
    """One LOC type 18 text with its PA tags and TextBind placeholders filled, or ''.

    Quests key it (`quest_chain_id`, `quest_id`), journal pages
    (`journal_cat_id`, `page_no`); `str_id4` picks the field.
    """
    return resolve_text_binds(loc_lookup(LOC_QUEST, str_id1, str_id2, 0, str_id4).strip())


def quest_title_tagged(quest_chain_id: int, quest_id: int) -> str:
    """LOC type 18 title of a quest with its PA tags, for `pa_fields`, or ''."""
    return quest_text_tagged(quest_chain_id, quest_id)


def quest_title(quest_chain_id: int, quest_id: int) -> str:
    return strip_pa_tags(quest_title_tagged(quest_chain_id, quest_id)).strip()
