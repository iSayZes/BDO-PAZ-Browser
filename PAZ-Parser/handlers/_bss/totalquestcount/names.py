"""The name the quest window shows for a quest region or quest type value.

Shared by the quest count tables and the `quest.dbss` Quest Type column
(`quest_category` is the quest type).
"""

from __future__ import annotations

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import KeyHashes, ui_key_text
from .tables import QuestCountTable


def value_name(quest_table: QuestCountTable, hashes: KeyHashes, value: int) -> str:
    """The name the quest window shows, else the enum name, else ''."""
    key = quest_table.name_keys.get(value)
    text = ui_key_text(hashes, GAME_SHEET, key) if key else ""
    if text:
        return text
    return quest_table.enum_names[value] if 0 <= value < len(quest_table.enum_names) else ""
