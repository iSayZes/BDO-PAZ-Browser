"""Names of the trade categories (`enCommerceType`) of trade goods.

`panel_tooltip_item.luac` defines `enCommerceType` (1 Luxury_Miscellaneous to
9 RawMaterial, 10 Max) and names each value with `commerceStringTable`, a
`RESOURCE` sheet key of `stringtable.bss`; the item tooltip adds that name
after `Trade Item`. `panel_dialog_trade_marketitemlist_all.luac` uses the same
keys for the trade market tabs.

The key's text is LOC type 37 under its `stringtable.bss` hash. The hash
function is unknown but depends on the key string alone, so the hashes are
stored here, and a test checks them against `stringtable.bss`.
"""

from __future__ import annotations

from typing import NamedTuple

from _bss.stringtable.text import ui_key_text

RESOURCE_SHEET = "RESOURCE"


class CommerceLabel(NamedTuple):
    enum_name: str
    key: str
    key_hash: int


# enCommerceType value -> its enum name and label key, in the Lua's order.
COMMERCE_TYPES: dict[int, CommerceLabel] = {
    1: CommerceLabel("Luxury_Miscellaneous", "TRADEMARKET_GRAPH_BTN_MISCELL", 3544307266),
    2: CommerceLabel("Luxury", "TRADEMARKET_GRAPH_BTN_LUXURY", 1443131495),
    3: CommerceLabel("Grocery", "TRADEMARKET_GRAPH_BTN_GROCERY", 921122734),
    4: CommerceLabel("Medicine", "TRADEMARKET_GRAPH_BTN_MEDICINE", 2377007292),
    5: CommerceLabel("MilitarySupplies", "PANEL_TRADEMARKET_GRAPH_BTN_MILITARYSUPPLIES", 793668404),
    6: CommerceLabel("ObjectSaint", "TRADEMARKET_GRAPH_BTN_OBJECT", 4130299524),
    7: CommerceLabel("Cloth", "PANEL_TRADEMARKET_GRAPH_BTN_CLOTH", 1381072196),
    8: CommerceLabel("SeaFood", "TRADEMARKET_GRAPH_BTN_SEAFOOD", 2232966076),
    9: CommerceLabel("RawMaterial", "PANEL_TRADEMARKET_GRAPH_BTN_RAWMATERIAL", 2827763150),
}

KEY_HASHES = {RESOURCE_SHEET: {label.key: label.key_hash for label in COMMERCE_TYPES.values()}}


def commerce_type_name(commerce_type: int) -> str:
    """The LOC name of a trade category (`Food`), else its enum name, else its number."""
    label = COMMERCE_TYPES.get(commerce_type)
    if label is None:
        return str(commerce_type)
    return ui_key_text(KEY_HASHES, RESOURCE_SHEET, label.key) or label.enum_name
