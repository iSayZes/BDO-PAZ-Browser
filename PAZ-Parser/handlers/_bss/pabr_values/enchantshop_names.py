"""Cell text of the enchant and shop tables (`enchantshop_tables.py`)."""

from __future__ import annotations

from _common.challenge import challenge_name
from _common.item_key import item_count_text
from _common.rate import rate_percent
from .world_names import item_key_entry_text


# One stack entry of enchant_blackstonestack.bss: need_stack_item_count,
# stack, padding_0c (enchant_blackstonestack_bss.md, Stack).
_STACK_ITEM_COUNT, _STACK = 0, 1
# One level of reforgestonestaticstatusmanager.bss: item_enchant_key,
# unknown_04, material_item_enchant_key, padding_0c, material_item_count
# (reforgestonestaticstatusmanager_bss.md, Level).
_LEVEL_ITEM_KEY, _LEVEL_MATERIAL_KEY, _LEVEL_MATERIAL_COUNT = 0, 2, 4
# One entry of the two mansionrentaldiscount.bss lists: day, then a percent.
_DAY, _PERCENT = 0, 1


def stack_text(entry: list) -> str:
    """`x5: +5`: the item count a stack costs and the Enhancement Chance it gives."""
    return f"x{entry[_STACK_ITEM_COUNT]:,}: +{entry[_STACK]}"


def reforge_level_text(entry: list) -> str:
    """The level's item, then the material that upgrades a stone to it when the level has one."""
    item = item_key_entry_text(entry[_LEVEL_ITEM_KEY])
    material_key = entry[_LEVEL_MATERIAL_KEY]
    if not material_key:
        return item
    return f"{item} <- {item_count_text(material_key, entry[_LEVEL_MATERIAL_COUNT])}"


def challenge_text(challenge_key: int) -> str:
    """`2984 [Event] Use 20,000 Pearls`: a challenge key and its name, or the bare key."""
    name = challenge_name(challenge_key)
    return f"{challenge_key} {name}" if name else str(challenge_key)


def day_percent_text(entry: list) -> str:
    """`30: 5%`: a rental length in days and its percent on the 1,000,000 = 100% scale."""
    return f"{entry[_DAY]}: {rate_percent(entry[_PERCENT])}"
