"""The NPC dialog that gives or takes a quest, shared by `quest.dbss` and the
`acceptquest.bss` / `completequest.bss` view.

A dialog key is `dialog_index << 16 | npc_id`, the `detail_dialog.dbss` key.
`quest.dbss` stores one for accepting and one for completing each quest, and
the two `.bss` files index the same pairs by NPC. NPC `0` has dialogs too:
dialog `0` is the Black Spirit's.
"""

from __future__ import annotations

from _common.character import character_name
from _common.loc import loc_lookup
from _common.pa_text import strip_pa_tags

# base_dialog.dbss text, keyed (character_id, dialog_index, 0, 0) for the name
# the dialog shows, which can differ from the character's LOC type 6 name.
LOC_DIALOG_NAME = 38
_NPC_BITS = 16
_NPC_MASK = 0xFFFF


def split_dialog_key(key: int) -> tuple[int, int]:
    """(npc_id, dialog_index) of a `detail_dialog.dbss` key."""
    return key & _NPC_MASK, key >> _NPC_BITS


def dialog_name(npc_id: int, dialog_index: int) -> str:
    """Name the NPC shows in this dialog, or '' when LOC has none."""
    return strip_pa_tags(loc_lookup(LOC_DIALOG_NAME, npc_id, dialog_index, 0, 0)).strip()


def dialog_speaker(key: int) -> str:
    """Who speaks in a dialog: its dialog name, else the NPC's name, else ''.

    `Villager` 544 shows as `Dins` in the dialog that gives quest 1001 / 49.
    """
    npc_id, dialog_index = split_dialog_key(key)
    return dialog_name(npc_id, dialog_index) or (character_name(npc_id) if npc_id else "")
