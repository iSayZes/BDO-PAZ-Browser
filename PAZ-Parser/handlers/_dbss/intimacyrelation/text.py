"""The texts of an `intimacyrelation.dbss` row in the user's language.

LOC type 23 holds every text under `(npc_key, 0, 0, slot)`: slot 0 is
`covered_dialog_kr`, 1 is `discover_dialog_kr`, 2 to 6 are the five
`discover_dialogs_kr`. Kept out of `handler.py` so tests can import it
without loading the handler registry.
"""

from __future__ import annotations

from _common.loc import loc_tagged
from _dbss.dialogtext.text import tagged_text

LOC_NPC_DIALOG = 23
COVERED_SLOT = 0
DISCOVER_SLOT = 1
FIRST_LINE_SLOT = 2


def dialog_text(npc_key: int, slot: int, text_kr: str) -> str:
    """The LOC text of one slot with its PA tags, else the Korean, without client tags; '' when both are empty."""
    if not text_kr:
        return ""
    return tagged_text(loc_tagged(LOC_NPC_DIALOG, npc_key, slot) or text_kr)


def dialog_lines(npc_key: int, lines_kr: list[str]) -> list[str]:
    """The set `discover_dialogs_kr` lines, each as `dialog_text()`."""
    return [
        dialog_text(npc_key, FIRST_LINE_SLOT + index, line)
        for index, line in enumerate(lines_kr)
        if line
    ]
