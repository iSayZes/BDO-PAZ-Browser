"""The NPC dialog that gives or takes a quest, shared by `quest.dbss` and the
`acceptquest.bss` / `completequest.bss` view.

A dialog key is `dialog_index << 16 | npc_id`, the `detail_dialog.dbss` key.
`quest.dbss` stores one for accepting and one for completing each quest, and
the two `.bss` files index the same pairs by NPC. NPC `0` has dialogs too:
dialog `0` is the Black Spirit's. A key with a `detail_dialog.dbss` row (the
`DIALOG_KEYS` index) shows as a link to that row.
"""

from __future__ import annotations

from _common.character import character_name
from _common.html import e, record_link
from _common.loc import loc_lookup
from _common.lookup_builders import DETAIL_DIALOG
from _common.lookup_index import IndexKind, lookup
from _common.pa_text import strip_pa_tags

# base_dialog.dbss text, keyed (character_id, dialog_index, 0, 0) for the name
# the dialog shows, which can differ from the character's LOC type 6 name.
LOC_DIALOG_NAME = 38
_NPC_BITS = 16
_NPC_MASK = 0xFFFF


def split_dialog_key(key: int) -> tuple[int, int]:
    """(npc_id, dialog_index) of a `detail_dialog.dbss` key."""
    return key & _NPC_MASK, key >> _NPC_BITS


def dialog_key(npc_id: int, dialog_index: int) -> int:
    """The `detail_dialog.dbss` key of one NPC dialog."""
    return dialog_index << _NPC_BITS | npc_id


def dialog_name(npc_id: int, dialog_index: int) -> str:
    """Name the NPC shows in this dialog, or '' when LOC has none."""
    return strip_pa_tags(loc_lookup(LOC_DIALOG_NAME, npc_id, dialog_index, 0, 0)).strip()


def dialog_speaker(key: int) -> str:
    """Who speaks in a dialog: its dialog name, else the NPC's name, else ''.

    `Villager` 544 shows as `Dins` in the dialog that gives quest 1001 / 49.
    """
    npc_id, dialog_index = split_dialog_key(key)
    return dialog_name(npc_id, dialog_index) or (character_name(npc_id) if npc_id else "")


def dialog_cell(key: int, text: str) -> str:
    """`text` as a link to the dialog's `detail_dialog.dbss` row, or as plain text without one."""
    if lookup(IndexKind.DIALOG_KEYS, key) is None:
        return e(text)
    return record_link(text, DETAIL_DIALOG, "key", key, "record-link")
