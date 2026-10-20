"""Names of `CppEnums.ServantKind` values, as listed in `global_define_cpp_enum.luac`.

Member names in value order from `0`, without the `Type_` prefix. The client
spells `RepairableCarrage` that way.
"""

from __future__ import annotations

from _common.enum_name import enum_name

SERVANT_KIND_NAMES: tuple[str, ...] = (
    "Horse",
    "Camel",
    "Donkey",
    "Elephant",
    "TwoWheelCarriage",
    "FourWheeledCarriage",
    "Ship",
    "Cat",
    "Dog",
    "MountainGoat",
    "Raft",
    "FishingBoat",
    "Tank",
    "BabyElephant",
    "GalleyShip",
    "PersonalTradeShip",
    "CampingTent",
    "PersonalBattleShip",
    "RepairableCarrage",
    "PersonalBoat",
    "FastShip",
    "CashPersonalTradeShip",
    "CashPersonalBattleShip",
    "Carrack",
    "GalleyShipSolo",
    "PersonalTradeShipSolo2",
    "PersonalBattleShipSolo2",
    "PersonalTradeShipSolo1",
    "PersonalBattleShipSolo1",
    "RaceHorse",
    "OceanTent",
    "Perica",
)


def servant_kind_name(servant_kind: int) -> str:
    """`Horse` for `0`, or the bare value outside the enum."""
    return enum_name(SERVANT_KIND_NAMES, servant_kind)
