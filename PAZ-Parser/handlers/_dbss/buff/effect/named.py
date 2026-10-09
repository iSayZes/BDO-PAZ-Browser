"""Effect types whose parameters are the key of something LOC names.

`Summon Rock Golem`, `Learn Skill: Lightning Chain`, `Velia Storage +8`: one
or more entries per type, read by `render.py` for both the Effect text and the
Param labels. The evidence for each type is in docs/file-formats/buff_dbss.md
(Enum Values and Effect text).
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field

from _common.character import character_name
from _common.instance_field import instance_field_name
from _common.knowledge import knowledge_name, theme_name
from _common.node import full_node_name
from _common.quest.quest import quest_title
from _common.skill import skill_name
from _common.teleport import teleport_point_place
from _common.title import title_name
from _common.town import town_name


@dataclass(frozen=True)
class NamedEffect:
    """An effect whose parameters are the key of something LOC names.

    `name_of` receives the values of `key_params`. A template may hold
    `{name}`, `{key}` (`244/1`) and `{param_1}` to `{param_10}`; without a
    name, `unnamed_template` is used when given, else `template` with the key
    in place of the name, unless `is_key_shown` is False: then there is no
    text, for keys whose names are a fixed list with gaps. A type may have
    several entries; the first whose `when` (parameter number to value) holds
    applies.
    """

    template: str
    name_of: Callable[..., str]
    key_params: tuple[int, ...] = (1,)
    unnamed_template: str = ""
    when: Mapping[int, int] = field(default_factory=dict)
    is_key_shown: bool = True


# Type 72 `param_4`, from the expansion coupons (`Trent Stable +1 Expansion
# Coupon`); `param_1` is the town, `0` all towns (`모든 지역`).
_STORAGE_KINDS = {0: "Storage", 1: "Stable", 2: "Wharf", 3: "Worker's Lodging"}
_ALL_TOWNS = 0

# Type 73 `param_2` under `param_1` 0, from the Trade Pass descriptions
# (`Restocks the trading items ... in trading shops of Balenos`). Their
# English texts for 2 to 4 contradict the Korean names, so those stay
# unlabelled.
_TRADE_TERRITORIES = {
    0: "Balenos",
    1: "Serendia",
    5: "Southwestern Calpheon",
    6: "Southeastern Calpheon",
}
_TRADE_BY_TERRITORY = 0
_TRADE_BY_MANAGER = 1


def _worker_contract(worker_id: int, town_key: int) -> str:
    """`Giant Worker (Velia)`, the way the contract items name it."""
    worker = character_name(worker_id)
    if not worker:
        return ""
    town = town_name(town_key)
    return f"{worker} ({town})" if town else worker


def _storage_town(town_key: int) -> str:
    """`Velia`, or `All Towns` for 0."""
    return "All Towns" if town_key == _ALL_TOWNS else town_name(town_key)


def _trade_territory(territory: int) -> str:
    return _TRADE_TERRITORIES.get(territory, "")


NAMED_EFFECTS: dict[int, tuple[NamedEffect, ...]] = {
    # Secret Books: `Wizard/Witch Secret Book - Lightning Chain` applies the
    # skill of param_1.
    17: (NamedEffect("Learn Skill: {name}", skill_name),),
    # The summoned character. Siege objects and placed objects are characters too.
    18: (NamedEffect("Summon {name}", character_name),),
    # A teleport.dbss point: param_1 is its section, param_2 its key within
    # the section. Points have no name, so the nearest worldmap node places it.
    23: (
        NamedEffect(
            "Teleport to point {key}, near {name}",
            teleport_point_place,
            key_params=(1, 2),
            unnamed_template="Teleport to point {key}",
        ),
    ),
    # The node a Node Registration item registers.
    37: (NamedEffect("Register Node: {name}", full_node_name),),
    # Hidden buffs that items used on pickup apply to unlock a knowledge entry.
    38: (NamedEffect("Learn Knowledge: {name}", knowledge_name),),
    # Each piece of a set adds param_2 points to the set skill of param_1,
    # whose level per point total holds the set effects (Korean names
    # `세트 효과 2포인트`, "set effect 2 points", store 2).
    48: (NamedEffect("Set Effect Points +{param_2}: {name}", skill_name),),
    # Accepts quest `param_2` of chain `param_1`: Cartian Spell's "[Co-op]
    # Eliminating the Threats to Mediah will automatically be accepted".
    69: (NamedEffect("Accept Quest: {name}", quest_title, key_params=(1, 2)),),
    # Storage, stable, wharf and lodging slots in the town of param_1.
    72: tuple(
        NamedEffect(
            f"{{name}} {kind} +{{param_2}}",
            _storage_town,
            when={4: kind_id},
            unnamed_template=f"{kind} +{{param_2}} in town {{key}}",
        )
        for kind_id, kind in _STORAGE_KINDS.items()
    ),
    # Restocks the trade items of a territory, or of one trade manager.
    73: (
        NamedEffect(
            "Trade Refresh: {name}",
            _trade_territory,
            key_params=(2,),
            when={1: _TRADE_BY_TERRITORY},
            is_key_shown=False,
        ),
        NamedEffect(
            "Trade Refresh: {name}",
            character_name,
            key_params=(2,),
            when={1: _TRADE_BY_MANAGER},
        ),
    ),
    # Bookshelves: "There is a chance you may obtain Knowledge", worded
    # `Gain Cooking Knowledge` on their tooltips.
    101: (
        NamedEffect(
            "Gain {name} Knowledge",
            theme_name,
            unnamed_template="Gain Knowledge of theme {key}",
        ),
    ),
    # Worker contracts: the worker of param_1 in the town of param_2, as the
    # item reads `Employment Contract: Goblin Worker`, `Affiliation: Calpheon City`.
    103: (NamedEffect("Employment Contract: {name}", _worker_contract, key_params=(1, 2)),),
    # [Title] items: "Obtain the Linked Up Morning Light title".
    142: (NamedEffect("Obtain Title: {name}", title_name),),
    # Test items A1_001 to A1_024, whose skills read "A1 Teleport": param_3
    # is the instancefield.dbss key, and the field shares the item's name
    # (4001 is `A1_001`). param_1 is 17 on all 48 buffs, meaning unknown.
    176: (
        NamedEffect(
            "Teleport to Instance Field {name}",
            instance_field_name,
            key_params=(3,),
            when={1: 17},
        ),
    ),
}
