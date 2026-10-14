"""Names of `CppEnums.VehicleType` values, as listed in `global_define_cpp_enum.luac`.

The enum is sparse, so the names sit in a dict keyed by value, without the
`Type_` prefix. Six values the Lua enum leaves out take their member name
from the 2016 client's `gc::VehicleType` (`VehicleType_` prefix dropped),
because the characters that store them in `characterstatic.dbss` still fit
it: `6` GateCrank on cranks, `8` Haetae on Heuklang. Other values show as the
bare number.
"""

from __future__ import annotations

VEHICLE_TYPE_NAMES: dict[int, str] = {
    0: "Horse",
    1: "Cannon",
    2: "Camel",
    3: "Donkey",
    4: "Elephant",
    5: "Bomb",
    6: "GateCrank",  # 2016 name
    7: "Ladder",
    8: "Haetae",  # 2016 name
    9: "Carriage",
    10: "QuestObjectSheep",
    11: "QuestObjectCart",
    13: "QuestObjectOak",
    14: "QuestObjectBox",
    15: "QuestObjectSack",
    16: "QuestObjectBoat",
    17: "QuestObjectPumpkin",
    18: "Boat",
    19: "QuestObjectBrokenFrag",
    20: "QuestDonkey",  # 2016 name
    21: "Catapult",  # 2016 name
    22: "Ballista",
    23: "Catapult2",  # 2016 name
    24: "QuestObjectHerbalMachines",
    25: "QuestObjectExtractor",
    26: "Cow",
    27: "LumberVerticalSaw",  # 2016 name
    28: "CowCarriage",
    29: "Raft",
    30: "Cat",
    31: "Dog",
    32: "MountainGoat",
    33: "FishingBoat",
    34: "SailingBoat",
    35: "Train",
    36: "BabyElephant",
    37: "ThrowStone",
    38: "PracticeCannon",
    39: "ThrowFire",
    40: "RidableBabyElephant",
    41: "WoodenFence",
    42: "SiegeTower",
    43: "LargeSiegeTower",
    44: "PersonalBattleShip",
    46: "PersonTradeShip",
    47: "CampingTent",
    48: "RepairableCarriage",
    49: "Bungalow",
    50: "Summer",
    51: "Training",
    52: "PersonalBoat",
    53: "RaceHorse",
    54: "Perica",
    55: "FastShip",
    56: "CashPersonalTradeShip",
    57: "CashPersonalBattleShip",
    58: "BossMonster",
    59: "Airballoon",
    60: "Carrack",
    61: "OceanTent",
    63: "GuildDragon",
}


def vehicle_type_text(vehicle_type: int) -> str:
    """`30 Cat`, or the bare value when the enum does not name it."""
    name = VEHICLE_TYPE_NAMES.get(vehicle_type)
    return f"{vehicle_type} {name}" if name else str(vehicle_type)
