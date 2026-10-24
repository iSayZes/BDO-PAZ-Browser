"""Cell text of the Magnus (`AbyssOne`) tables in `abyssone_tables.py`."""

from __future__ import annotations

from _common.class_type import class_name
from _common.item_key import item_name, split_item_key
from _dbss.itemenchant.slot_labels import slot_label
from .rosewar_names import region_text


# One entry of abyssoneequipmentpreset.bss: class type, equip slot copy,
# a u8, item key, an i32 and the Magnus coin price.
_PRESET_CLASS, _PRESET_ITEM_KEY, _PRESET_COIN = 0, 3, 5
# One entry of abyssmovecost.bss: cost, then two region keys.
_MOVE_COST, _MOVE_REGION_1, _MOVE_REGION_2 = 0, 1, 2


def equip_slot_text(equip_slot: int) -> str:
    """`12 Belt`: an equip slot and its tooltip label."""
    label = slot_label(equip_slot)
    return f"{equip_slot} {label}" if label and label != str(equip_slot) else str(equip_slot)


def preset_text(entry: list[int]) -> str:
    """`Warrior: Longsword of the Challenger (738501)`, with the coin price when it has one."""
    item_id, enchant_level = split_item_key(entry[_PRESET_ITEM_KEY])
    name = item_name(item_id) or str(item_id)
    level = f" +{enchant_level}" if enchant_level else ""
    coin = entry[_PRESET_COIN]
    price = f", {coin:,} coins" if coin else ""
    return f"{class_name(entry[_PRESET_CLASS])}: {name}{level} ({item_id}){price}"


def move_text(entry: list[int]) -> str:
    """`1733 Angavu Outpost / 1741 Radiant Lands: 0`: both regions and the cost."""
    return f"{region_text(entry[_MOVE_REGION_1])} / {region_text(entry[_MOVE_REGION_2])}: {entry[_MOVE_COST]:,}"
