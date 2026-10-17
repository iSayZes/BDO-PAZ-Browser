"""The special crystal preset slots and the equipment slot each belongs to.

The numbers and the equipment slots come from the crystal preset window
(`panel_window_jewelpreset_all*.luac`, `panel_window_jewelpreset_all.xml`);
jewelspecialslotsgroupstaticstatus_bss.md, Special Slots, has the evidence.
"""

from __future__ import annotations

from typing import NamedTuple

from _dbss.itemenchant.slot_labels import slot_label


class SpecialSlot(NamedTuple):
    enum_name: str
    # `equip_slot` value of itemenchant.dbss, or None for a slot with no item.
    equip_slot: int | None


# `__eJewelSpecialSlot*` value -> its name and equipment slot.
SPECIAL_SLOTS: dict[int, SpecialSlot] = {
    12: SpecialSlot("AwakenWeapon1", 29),
    13: SpecialSlot("AwakenWeapon2", 29),
    14: SpecialSlot("PearlAvatarChest", 14),
    15: SpecialSlot("1MorningLand", None),
    16: SpecialSlot("2MorningLand", None),
    17: SpecialSlot("Necklace", 7),
    18: SpecialSlot("Ring1", 8),
    19: SpecialSlot("Ring2", 9),
    20: SpecialSlot("Earing1", 10),
    21: SpecialSlot("Earing2", 11),
    22: SpecialSlot("Belt", 12),
}


def special_slot_label(slot: int) -> str:
    """The equipment slot's LOC text, else the special slot's enum name, else the number."""
    special = SPECIAL_SLOTS.get(slot)
    if special is None:
        return str(slot)
    if special.equip_slot is None:
        return special.enum_name
    return slot_label(special.equip_slot) or special.enum_name
