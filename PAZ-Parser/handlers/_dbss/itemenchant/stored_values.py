"""Stored values that both itemenchant.dbss layouts encode the same way, as record values.

None sorts last and exports empty, so the "none" values become None.
"""

from __future__ import annotations

# Highest character level that can use the item, when there is none.
_NO_MAX_LEVEL = 0x7FFF_FFFF
# Stored for items without durability.
_NO_DURABILITY = 32_767
# `family_inventory` of an item that can go in the Family Inventory; 0 when not.
_FAMILY_INVENTORY_ALLOWED = 2


def max_level_value(stored: int) -> int | None:
    return None if stored == _NO_MAX_LEVEL else stored


def expiration_value(stored_minutes: int) -> int | None:
    """Minutes until the item expires; None when it does not (stored `0`)."""
    return stored_minutes or None


def durability_value(stored: int) -> int | None:
    return None if stored == _NO_DURABILITY else stored


def trade_type_value(for_trade: int, trade_type: int) -> int | None:
    """The trade type of a trade good; None for other items."""
    return trade_type if for_trade else None


def family_inventory_value(stored: int) -> bool:
    return stored == _FAMILY_INVENTORY_ALLOWED
