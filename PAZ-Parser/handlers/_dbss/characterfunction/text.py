"""Display text of a `characterfunction.dbss` record: its buttons, nodes and vehicle types.

Kept apart from handler.py so tests can import it without loading the handler
registry.
"""

from __future__ import annotations

from _common.loc import LOC_NULL, loc_text
from _common.node import full_node_name
from _common.vehicle_type import vehicle_type_text
from .parser import CharacterFunctionRecord, FunctionSlot

# Button text per character: str_id1 = character ID, str_id4 = slot loc_index.
LOC_FUNCTION_BUTTON = 32


def _is_blank(text: str) -> bool:
    return not text or text.lower() == LOC_NULL


def button_label(character_id: int, slot: FunctionSlot) -> str:
    """The slot's button in the loaded LOC language, else its inline Korean text."""
    if slot.loc_index is not None:
        text = loc_text(LOC_FUNCTION_BUTTON, character_id, slot.loc_index)
        if not _is_blank(text):
            return text
    return slot.name


def function_labels(record: CharacterFunctionRecord) -> list[str]:
    """Buttons of every slot with button text, in slot order.

    `<Null>` is a placeholder the file stores in the season gift slot of almost
    every record, not a button.
    """
    return [
        button_label(record.character_id, slot)
        for slot in record.slots
        if not _is_blank(slot.name)
    ]


def node_names(node_keys: tuple[int, ...]) -> list[str]:
    """Worldmap names of the nodes, or the bare key when LOC has none."""
    return [full_node_name(key) or str(key) for key in node_keys]


def vehicle_names(record: CharacterFunctionRecord) -> list[str]:
    """`0 Horse`-style text of each vehicle type the stable takes, once each, in stored order."""
    return [vehicle_type_text(value) for value in dict.fromkeys(record.vehicle_types)]
