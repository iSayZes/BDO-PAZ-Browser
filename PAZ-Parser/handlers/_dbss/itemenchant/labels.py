"""Display text for the coded itemenchant.dbss fields: classes, binding, trade, crystal group.

Each takes the handler's `values` strings from lang/<code>.json, so the labels
follow the app language. Meanings and evidence are in itemenchant_dbss.md.
"""

from __future__ import annotations

from _bss.jewelgroupstaticstatus.names import NO_LIMIT, JewelGroup
from _common.class_type import PLAYABLE_CLASSES_MASK, class_names, is_all_classes
from ui_text import fill_placeholders

# "All except Agent" reads better than 34 class names; above this many
# missing classes the names are listed instead.
_MAX_EXCEPTED_CLASSES = 3

_BIND_ON_OBTAIN = 1
_BIND_ON_EQUIP = 2

# trade_type values and the lang key of each; 4 is also sold to Trade
# Managers, but what sets it apart from 0 is open.
_TRADE_KEYS = {
    0: "tradeManager",
    1: "tradeKarma",
    3: "tradeImperialCrafting",
    4: "tradeManager",
    5: "tradeGuild",
}
def classes_label(class_mask: int, values: dict[str, str]) -> str:
    """'All', 'All except ...' or the class names; '' when no class may use it."""
    if is_all_classes(class_mask):
        return values["allClasses"]
    if not class_mask & PLAYABLE_CLASSES_MASK:
        return ""
    missing_mask = PLAYABLE_CLASSES_MASK & ~class_mask
    if missing_mask.bit_count() <= _MAX_EXCEPTED_CLASSES:
        return fill_placeholders(values["allExcept"], classes=", ".join(class_names(missing_mask)))
    return ", ".join(class_names(class_mask))


def binding_label(vested_type: int, family_bound: bool, values: dict[str, str]) -> str:
    """'On obtain (Family)' and the like; '' for an item that never binds."""
    if vested_type == _BIND_ON_OBTAIN:
        when = values["bindOnObtain"]
    elif vested_type == _BIND_ON_EQUIP:
        when = values["bindOnEquip"]
    else:
        return ""
    owner = values["family"] if family_bound else values["character"]
    return f"{when} ({owner})"


def trade_label(trade_type: int | None, values: dict[str, str]) -> str:
    """Where a trade good is sold or delivered; '' for other items."""
    if trade_type is None:
        return ""
    key = _TRADE_KEYS.get(trade_type)
    if key is None:
        return fill_placeholders(values["tradeType"], type=trade_type)
    return values[key]


def crystal_group_label(group: int | None, groups: dict[int, JewelGroup], values: dict[str, str]) -> str:
    """'Dawn (max 6)' as the item tooltip's crystal lines; the bare number when
    `groups` does not name it, '' for an item that is not a crystal."""
    if group is None:
        return ""
    known = groups.get(group)
    if known is None or not known.name:
        return str(group)
    if known.max_count == NO_LIMIT:
        return fill_placeholders(values["crystalGroupNoLimit"], name=known.name)
    return fill_placeholders(values["crystalGroup"], name=known.name, max_count=known.max_count)
