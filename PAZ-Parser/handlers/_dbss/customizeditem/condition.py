"""Readable text for the `customizeditem.dbss` condition scripts.

Two forms occur (Conditions in docs/file-formats/dbss/customizeditem_dbss.md):
`checkClass(N);` names class type `N` (LOC type 21) and
`clearquest(chain,quest);` a quest (LOC type 18 title). Any other script,
or a name LOC lacks, shows as the script itself.
"""

from __future__ import annotations

import re

from _common.class_type import class_name
from _common.quest.quest import quest_title

_CHECK_CLASS = re.compile(r"checkClass\((\d+)\);?")
_CLEAR_QUEST = re.compile(r"clearquest\((\d+),(\d+)\);?")


def condition_text(condition: str) -> str:
    """The class name or quest title a condition checks, else the script."""
    script = condition.strip()
    class_match = _CHECK_CLASS.fullmatch(script)
    if class_match:
        return class_name(int(class_match.group(1)))
    quest_match = _CLEAR_QUEST.fullmatch(script)
    if quest_match:
        return quest_title(int(quest_match.group(1)), int(quest_match.group(2))) or script
    return script
