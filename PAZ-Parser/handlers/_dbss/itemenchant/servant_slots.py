"""Equipment slot labels of servant gear: mounts, wagons and ships.

Servant gear stores the character slot numbers with other meanings: a barding
goes in Chest (3), a wagon wheel in Glove (4). The item's `servant_kinds` mask
says which servants use it, bit `n` for `CppEnums.ServantKind` `n`.
`GetItemEquipServantType` (`panel_dialog_servantinfo_all_2.luac`) gives the
first group in `_GROUP_KINDS` whose kinds the mask holds, and
`_SERVANT_KIND_TYPESTRING` (`panel_dialog_servantinfo_all.luac`) labels the
slots of each group. That table swaps the horse costume saddle (15) and
stirrups (16) against the items, which are saddles in 15 and stirrups in 16,
so `SERVANT_SLOT_LABELS` follows the items there (itemenchant_dbss.md,
`equip_slot`). That function leaves out the camping tent (kind 16), which the
item tooltip handles as its own servant type; its slots take the labels of
the camp window (`panel_window_camp_all.luac`, `_menuStr`). The label keys' hashes
are stored here (`ui_key_labels.py`).
"""

from __future__ import annotations

from _bss.stringtable.parser import RESOURCE_SHEET
from .ui_key_labels import UiKeyLabel, key_hashes, label_text


_HORSE = "horse"
_WAGON = "wagon"
_ELEPHANT = "elephant"
_OCEAN_SHIP = "ocean_ship"
_BOAT = "boat"
_CAMPING_TENT = "camping_tent"


def _kinds_mask(*kinds: int) -> int:
    return sum(1 << kind for kind in set(kinds))


# Each group with its `CppEnums.ServantKind` values, in the order
# `GetItemEquipServantType` tests them; the first match wins.
_GROUP_KINDS: tuple[tuple[str, int], ...] = (
    # TwoWheelCarriage, FourWheeledCarriage, Tank, RepairableCarrage
    (_WAGON, _kinds_mask(4, 5, 12, 18)),
    # Horse, Camel, Donkey, MountainGoat, RaceHorse
    (_HORSE, _kinds_mask(0, 1, 2, 9, 29)),
    # Elephant, BabyElephant
    (_ELEPHANT, _kinds_mask(3, 13)),
    # Raft, GalleyShip, PersonalTradeShip, FastShip, the two Cash ships,
    # Carrack and the four Solo ships
    (_OCEAN_SHIP, _kinds_mask(10, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28)),
    # Ship (rowboat), FishingBoat
    (_BOAT, _kinds_mask(6, 11)),
    # CampingTent; not in GetItemEquipServantType
    (_CAMPING_TENT, _kinds_mask(16)),
)

_HULL = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_25", 3320948638)
_ORNAMENT = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_3", 4031778909)
_PROW = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_4", 2223442194)
_CARGO_CONTAINER = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_5", 1464560034)
_PLATING = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_17", 892450638)
_FIGUREHEAD = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_18", 3994716591)
_SAIL = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_19", 934221725)
_CANNON = UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_20", 4251385898)

# group -> {equip_slot -> label key}
SERVANT_SLOT_LABELS: dict[str, dict[int, UiKeyLabel]] = {
    _HORSE: {
        3: UiKeyLabel("LUA_INGAMECASHSHOP_SETEQUIP_BARD", 4211289195),
        4: UiKeyLabel("LUA_INGAMECASHSHOP_SETEQUIP_SADDLE", 2006824947),
        5: UiKeyLabel("LUA_INGAMECASHSHOP_SETEQUIP_STIRRUP", 1895492399),
        6: UiKeyLabel("LUA_INGAMECASHSHOP_SETEQUIP_HORSEHEAD", 1138605558),
        12: UiKeyLabel("LUA_DYENEW_DYEPART_HORSE_FOOT", 4249035766),
        14: UiKeyLabel("LUA_DYENEW_DYEPART_HORSE_AVATAR_ARMOR", 2431354158),
        # The client table has these two the other way round; the items do not.
        15: UiKeyLabel("LUA_DYENEW_DYEPART_HORSE_AVATAR_SADDLE", 1225445909),
        16: UiKeyLabel("LUA_DYENEW_DYEPART_HORSE_AVATAR_STIRRUP", 540335476),
        17: UiKeyLabel("LUA_DYENEW_DYEPART_HORSE_AVATAR_FACE", 3589960464),
    },
    _WAGON: {
        3: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_BODY", 1655561166),
        4: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_TIRE", 4087938742),
        5: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_FLAG", 180804316),
        6: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_INSIGNIA", 3946446423),
        13: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_LAMP", 820987467),
        25: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_CORVER", 871045696),
        14: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_AVATAR_BODY", 2583297170),
        15: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_AVATAR_TIRE", 698167442),
        16: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_AVATAR_FLAG", 580372958),
        17: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_AVATAR_INSIGNIA", 4057323351),
        26: UiKeyLabel("LUA_DYENEW_DYEPART_CARRIAGE_AVATAR_CORVER", 2811496534),
    },
    _ELEPHANT: {
        3: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO3", 2452652230),
        4: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO4", 381117645),
        5: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO5", 1615930974),
        6: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO6", 607793039),
        12: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO12", 4093492105),
        14: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO14", 4211188224),
        15: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO15", 3869284301),
        16: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO16", 608926256),
        17: UiKeyLabel("LUA_VEHICLEINFO_ELEPHANT_SLOTNO17", 144183361),
    },
    _OCEAN_SHIP: {
        3: _PLATING,
        4: _FIGUREHEAD,
        5: _CANNON,
        6: _ORNAMENT,
        7: UiKeyLabel("LUA_LIFEEQUIP_TOOLTIP_07", 2927776078),
        12: UiKeyLabel("LUA_ITEMTOOLTIP_SHIPAMOR_STONE", 4239777129),
        25: _SAIL,
        14: _PLATING,
        15: _FIGUREHEAD,
        16: _CANNON,
        26: _SAIL,
    },
    _BOAT: {
        3: _HULL,
        4: _PROW,
        5: _CARGO_CONTAINER,
        6: UiKeyLabel("LUA_ITEMTOOLTIP_SHIPARMOR_6", 2940958350),
        25: _ORNAMENT,
        14: _HULL,
        15: _PROW,
        16: _CARGO_CONTAINER,
        26: _ORNAMENT,
    },
    _CAMPING_TENT: {
        3: UiKeyLabel("PANEL_CAMP_WAREHOUSETOOL", 3094154879, RESOURCE_SHEET),
        4: UiKeyLabel("PANEL_CAMP_REPAIRTOOL", 2983385083, RESOURCE_SHEET),
        5: UiKeyLabel("PANEL_CAMP_SHOPTOOL", 3742943360, RESOURCE_SHEET),
        6: UiKeyLabel("PANEL_CAMP_TENTLOOKTITLE", 2198100692, RESOURCE_SHEET),
        7: UiKeyLabel("PANEL_CAMP_TENTTELEPORTSTONE", 648966765, RESOURCE_SHEET),
    },
}

_KEY_HASHES = key_hashes(label for labels in SERVANT_SLOT_LABELS.values() for label in labels.values())


def servant_group(servant_kinds: int) -> str | None:
    """The slot label group of a `servant_kinds` mask; None when no group holds its kinds."""
    return next((group for group, mask in _GROUP_KINDS if servant_kinds & mask), None)


def servant_slot_label(servant_kinds: int, equip_slot: int) -> str:
    """The slot's LOC text for the item's servant group; '' when the client labels none."""
    labels = SERVANT_SLOT_LABELS.get(servant_group(servant_kinds) or "", {})
    label = labels.get(equip_slot)
    return "" if label is None else label_text(_KEY_HASHES, label)
