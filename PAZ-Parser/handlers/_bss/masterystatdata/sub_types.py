"""Names of the gathering and processing types that split two mastery tables.

`collectingstatdata.bss` and `manufacturingstat.bss` hold one row group per
type. The group index is the `subType` that
`panel_characterinfo_life_all_1.luac` passes to
`ToClient_LoadCollectingStatData` and `ToClient_getManufacturingStatCountRate`,
and it names the type with `_SUBLIFE_COLLECT_STRING[subType]` or
`_SUBLIFE_MANUFACTURE[subType]`: `RESOURCE` sheet keys of `stringtable.bss`.

The key's text is LOC type 37 under its `stringtable.bss` hash. The hash
function is unknown but depends on the key string alone, so the hashes are
stored here, and a test checks them against `stringtable.bss`.
"""

from __future__ import annotations

from typing import NamedTuple

from _bss.stringtable.text import ui_key_text

RESOURCE_SHEET = "RESOURCE"


class SubTypeLabel(NamedTuple):
    key: str
    key_hash: int


# Group index -> name key, as `_SUBLIFE_COLLECT_STRING` lists them. The index
# is also the `CollectToolType` (1 EmptyBottle ... 7 Pickax).
GATHERING_TYPES: dict[int, SubTypeLabel] = {
    1: SubTypeLabel("PANEL_CHARACTERINFO_RENEW_WATERING_TITLE", 2694735218),
    2: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_FELLING", 4287296960),
    3: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SAP", 1774998101),
    4: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_HOMMY", 3764073750),
    5: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SLAUGHTER", 3190642244),
    6: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_TANNING", 711475432),
    7: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_MINING", 4075807378),
}

# Group index -> name key, as `_SUBLIFE_MANUFACTURE` lists them.
PROCESSING_TYPES: dict[int, SubTypeLabel] = {
    1: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_SHAKING", 2418195621),
    2: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_GRIDING", 3008146878),
    3: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_FIREWOOD", 3832705241),
    4: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_DRYING", 3951843248),
    5: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_THINOUT", 1480449056),
    6: SubTypeLabel("PANEL_CHARACTERINFO_LIFEINFO_CRAFTTYPE_HEATING", 3795494190),
}

KEY_HASHES = {
    RESOURCE_SHEET: {
        label.key: label.key_hash
        for labels in (GATHERING_TYPES, PROCESSING_TYPES)
        for label in labels.values()
    }
}


def sub_type_name(labels: dict[int, SubTypeLabel], sub_type: int) -> str:
    """The LOC name of a type (`Lumbering`), else its number."""
    label = labels.get(sub_type)
    text = ui_key_text(KEY_HASHES, RESOURCE_SHEET, label.key) if label else ""
    return text or str(sub_type)
