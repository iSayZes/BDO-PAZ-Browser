"""What each confirmed effect type's parameters mean, one entry per type.

Every entry drives both the Effect text and the labels of the Param columns,
so a type is described once. The types whose parameters are the key of
something LOC names are in `named.py`. The evidence for each type is in
docs/file-formats/buff_dbss.md (Enum Values and Effect text).
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field

from .units import CRAFT_SECONDS, FLAT, KEY, METRES, MINUTES, PERCENT, SECONDS, WEIGHT, Unit


@dataclass(frozen=True)
class EffectLine:
    """One effect a buff of a type can read as.

    The line applies when every parameter in `when` (parameter number to
    value) holds that value and the amount in `value_param` is not zero.
    `kind_labels` names those parameters for the Param columns, and
    `value_label` names the amount where nothing else tells what it is.
    """

    label: str
    value_param: int
    unit: Unit = FLAT
    when: Mapping[int, int] = field(default_factory=dict)
    kind_labels: Mapping[int, str] = field(default_factory=dict)
    value_label: str = ""
    # False for amounts the game prints without a sign: `Recover 10 Energy`.
    is_signed: bool = True
    # True for a reduction stored positive that the game prints negative:
    # `500000` reads `Fall Damage -50%`.
    is_negated: bool = False
    template: str = "{label} {amount}"


def recovery(label: str, value_param: int) -> EffectLine:
    """A one-off amount: `Recover 10 Energy`."""
    return EffectLine(label, value_param, is_signed=False, template="Recover {amount} {label}")


def kinds(
    kind_param: int,
    label: str,
    names: Mapping[int, str],
    value_param: int,
    unit: Unit = FLAT,
    template: str = "{label} {amount}",
) -> tuple[EffectLine, ...]:
    """One line per value of `kind_param`; `label` may hold `{kind}`.

    A template other than the default writes the amount without a sign:
    `Stun for 5 sec`, `Value Pack for 15 days`.
    """
    return tuple(
        EffectLine(
            label.format(kind=name),
            value_param,
            unit,
            when={kind_param: kind},
            kind_labels={kind_param: name},
            is_signed=template == "{label} {amount}",
            template=template,
        )
        for kind, name in names.items()
    )


@dataclass(frozen=True)
class FixedDamage:
    """`Retaliate 15 Fixed Damage when struck`."""

    verb: str
    trigger: str


@dataclass(frozen=True)
class OverTimeEffect:
    """HP or MP/WP/SP: `param_1` per tick (`tick_ms`), or per trigger.

    `recover_on` words a positive amount by `condition_type`, and
    `fixed_damage_on` a negative one; other conditions yield no text.
    `damage_kinds` names ticking damage by the buff's icon file, for the
    icons whose English text agrees.
    """

    resource: str
    recover_on: Mapping[int, str] = field(default_factory=dict)
    fixed_damage_on: Mapping[int, FixedDamage] = field(default_factory=dict)
    damage_kinds: Mapping[str, str] = field(default_factory=dict)


_LIFE_SKILLS = {
    0: "Gathering",
    1: "Fishing",
    2: "Hunting",
    3: "Cooking",
    4: "Alchemy",
    5: "Processing",
    6: "Training",
    7: "Trading",
    8: "Farming",
    9: "Sailing",
    11: "Barter",
}

# Type 149 `param_2` by life skill, the same on every buff with text. The
# [Life Skill Season] buffs pair Gathering and Processing with 2 to 7 for
# single tools (`Processing_Hoe Mastery`); those stay unlabelled.
_MASTERY_PARAM_2 = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 9: 1}
# Type 149 `param_1` for every life skill at once.
_ALL_LIFE_SKILLS = 15

# Type 187 `param_3`, the Land of the Morning Light attribute: the Korean names
# read 해 / 달 / 땅 and the English texts Morning Sun / Moon / Earth.
_MORNING_LIGHT_ATTRIBUTES = {0: "Sun", 1: "Moon", 2: "Earth"}

# Type 14 `param_1`, from the Korean buff names (`[액션제한] 넉다운`, "action
# limit: knockdown"); Flashbang's kind 4 reads "will be stunned" in game. The
# second set ignores the target's resistance (`저항 무시`). Kind 0 mixes
# resistances and stuns, 5 guard crush and knockback, 19 is groggy on two
# buffs: all three stay unlabelled.
_CROWD_CONTROL = {
    1: "Knockback",
    2: "Knockdown",
    4: "Stun",
    6: "Stiffness",
    7: "Bound",
    12: "Floating",
    13: "Air Smash",
    14: "Down Smash",
    22: "Freezing",
    15: "Bound (Ignores Resistance)",
    17: "Knockdown (Ignores Resistance)",
    20: "Stun (Ignores Resistance)",
    23: "Floating (Ignores Resistance)",
    24: "Freezing (Ignores Resistance)",
}

# Type 97 `param_1`, named after the items that apply each kind (Value Pack,
# Book of Training - Combat); a Value Pack applies kinds 1, 4 and 5. Kinds
# without an item of their own, or shared by unlike items (22: Premium Value
# Pack Plus and Blessing of Cron Stones), stay unlabelled.
_PACKAGES = {
    0: "Blessing of Kamasylve",
    1: "Value Pack",
    2: "Shining Pearl Blessing",
    4: "Unlimited Customization",
    5: "Unlimited Use of Merv's Palette",
    7: "Cliff's Skill Add-on Guide",
    8: "Armstrong's Skill Guide",
    10: "Book of Training - Combat",
    12: "Premium Value Pack",
    13: "Book of Training - Skill",
    14: "Artisan's Blessing",
    15: "Secret Book of Old Moon",
    18: "Viano's Guide to the Desert",
    20: "Millennial Wild Ginseng",
}

_RESISTANCES = {
    0: "Knockback/Floating",
    1: "Knockdown/Bound",
    2: "Grapple",
    3: "Stun/Stiffness/Freezing",
    8: "All",
}

# `param_1` of types 89 (flat) and 181 (per million). Kind 3 of type 181 is a
# single passive (`단련 경험치`, "training EXP") and stays unlabelled.
_BREATH_STRENGTH_HEALTH = {0: "Breath", 1: "Strength", 2: "Health"}

EFFECT_LINES: dict[int, tuple[EffectLine, ...]] = {
    2: (EffectLine("Max HP", 1),),
    # Removes the buffs of group param_1: "Remove Group 44812".
    16: (EffectLine("Remove Group", 1, KEY, value_label="Group"),),
    14: kinds(1, "{kind}", _CROWD_CONTROL, 2, SECONDS, template="{label} for {amount}"),
    # One-off EXP; the amount matches the number in all 47 item names that
    # carry one (`Guild EXP (200,000)`).
    24: kinds(2, "{kind} EXP", {0: "Combat", 1: "Guild", 2: "Skill"}, 1),
    # Endless Ocean Draught: "Sailor EXP +15%".
    19: (EffectLine("Sailor EXP", 1, PERCENT),),
    3: (EffectLine("HP Recovery", 1),),
    5: (EffectLine("Max MP/WP/SP", 1),),
    6: (EffectLine("MP/WP/SP Recovery", 1),),
    8: (EffectLine("Max Stamina", 1),),
    9: (EffectLine("Movement Speed", 1, PERCENT),),
    10: (EffectLine("Attack Speed", 1, PERCENT),),
    11: (EffectLine("Casting Speed", 1, PERCENT),),
    25: (
        *kinds(2, "{kind} EXP", {0: "Combat", 1: "Skill"}, 1, PERCENT),
        # Life EXP names its life skill in param_3, 15 for all of them.
        *(
            EffectLine(
                f"{name} EXP",
                1,
                PERCENT,
                when={2: 2, 3: skill},
                kind_labels={2: "Life", 3: name},
            )
            for skill, name in {**_LIFE_SKILLS, _ALL_LIFE_SKILLS: "Life"}.items()
        ),
    ),
    29: (EffectLine("Weight Limit", 1, WEIGHT),),
    30: (EffectLine("Critical Hit Rate", 1, PERCENT),),
    # param_1 3 is all targets. bdo-data-extractor reads 0 to 2 as melee,
    # ranged and magic; no buff with those has English text, so no label.
    39: kinds(1, "All AP", {3: "All"}, 2),
    40: kinds(1, "All Accuracy", {3: "All"}, 2),
    41: kinds(1, "All Evasion", {3: "All"}, 2),
    43: kinds(1, "All Damage Reduction", {3: "All"}, 2),
    # Summon, monster, siege and cannon damage as a share of attack; player
    # skills do not use it. param_1 may be the attack type (2 on magic).
    45: (EffectLine("Attack Damage", 4, PERCENT, is_signed=False),),
    # Kind 5 is unused ("Not in Use"); kind 6 mixes hunting effects whose
    # amounts do not follow param_2, so both stay unlabelled.
    46: kinds(
        1,
        "Extra AP Against {kind}",
        {
            0: "Humans",
            1: "Demihumans",
            2: "Beasts",
            3: "Kamasylvian Monsters",
            4: "Edanian Monsters",
        },
        2,
    ),
    # Kinds 3 and 5 are stun and stiffness in Korean but share one English
    # label; kind 6 (bound) reads "Not in Use" and stays unlabelled.
    49: kinds(
        1,
        "{kind} Resistance",
        {**_RESISTANCES, 5: "Stun/Stiffness/Freezing", 7: "Fear"},
        2,
        PERCENT,
    ),
    # [Event] Giddy-up Ghost Horsie!: "Horse Capture Rate +15%" (47) and
    # "Mount Skill EXP +15%" (51).
    47: (EffectLine("Horse Capture Rate", 1, PERCENT),),
    50: (EffectLine("Mount EXP", 1, PERCENT),),
    51: (EffectLine("Mount Skill EXP", 1, PERCENT),),
    52: (EffectLine("Fall Damage", 1, PERCENT, is_negated=True),),
    53: (EffectLine("Discovery Radius", 1, METRES),),
    # NPC amity gain, `친밀도 획득`: the villa and music buffs read `Amity +10%`.
    56: (EffectLine("Amity", 1, PERCENT),),
    57: (EffectLine("Item Drop Rate", 1, PERCENT),),
    59: (EffectLine("Jump Height", 1),),
    # One-off, like the `60 Contribution EXP` item that stores 60.
    60: kinds(1, "{kind} EXP", {0: "Contribution"}, 2),
    # `Skill Points (5)` stores 5; param_1 0 is combat (`전투`) on all.
    62: kinds(1, "Skill Points", {0: "Combat"}, 2),
    63: (recovery("Worker Stamina", 1),),
    # Natural energy regeneration, `기운 자연 회복량`.
    66: (EffectLine("Energy Recovery", 1),),
    # Stat limits, worded as the Breakthrough Crystals (15642 to 15648) read:
    # `Attack Speed Limit +1`, `Gathering Limit +1`. Kinds as in type 67.
    68: kinds(
        1,
        "{kind} Limit",
        {
            0: "Movement Speed",
            1: "Attack Speed",
            2: "Casting Speed",
            3: "Critical Hit Rate",
            4: "Luck",
            5: "Fishing",
            6: "Gathering",
        },
        2,
    ),
    # Inventory slots, like `Inventory +8 Expansion`. param_2 is 1 on the
    # time-limited variants (`- 기간`), which store no duration.
    71: (EffectLine("Inventory", 1),),
    # Karma, Guild Karma and Naval Fame, flat: `Karma Recovery Scroll` stores
    # 100000, Hans' Contract "Raises Naval Fame by 2,500" stores 2500.
    76: kinds(2, "{kind}", {0: "Karma", 1: "Guild Karma", 2: "Naval Fame"}, 1),
    67: kinds(
        1,
        "{kind}",
        {
            0: "Movement Speed",
            1: "Attack Speed",
            2: "Casting Speed",
            3: "Critical Hit",
            4: "Luck",
            5: "Fishing Speed",
            6: "Gathering Speed",
        },
        2,
    ),
    79: (recovery("Energy", 1),),
    80: kinds(1, "{kind} EXP", _LIFE_SKILLS, 2),
    89: kinds(1, "{kind} EXP", _BREATH_STRENGTH_HEALTH, 2),
    90: (EffectLine("Death Penalty Resistance", 1, PERCENT),),
    91: (EffectLine("Durability Reduction Resistance", 1, PERCENT),),
    93: kinds(
        1,
        "{kind} Extra Damage",
        {
            0: "All Special Attack",
            1: "Back Attack",
            2: "Down Attack",
            3: "Air Attack",
            4: "Critical Hit",
            5: "Speed Attack",
            6: "Counter Attack",
        },
        2,
        PERCENT,
    ),
    94: (EffectLine("Max Energy", 1),),
    95: (EffectLine("Underwater Breathing", 1, SECONDS),),
    97: kinds(1, "{kind}", _PACKAGES, 2, MINUTES, template="{label} for {amount}"),
    # Mount and ship stats, in the wording of their gear: horseshoes and
    # prows read `Movement Speed`, sails `Turn`, stirrups `Brake`. Speed is
    # marked `(Mount)` so it does not read like the player's type 9.
    98: kinds(
        1,
        "{kind}",
        {0: "Acceleration", 1: "Movement Speed (Mount)", 2: "Turn", 3: "Brake"},
        2,
        PERCENT,
    ),
    100: (EffectLine("Character Slots", 1),),
    105: kinds(1, "Ignore {kind} Resistance", _RESISTANCES, 2, PERCENT),
    # The rate counterpart of type 43, `모든 피해 감소율`; param_1 is 3 on all.
    106: kinds(1, "All Damage Reduction", {3: "All"}, 2, PERCENT),
    # param_2 1 and 2 do not change the English text, as on type 57.
    112: (EffectLine("Item Drop Amount", 1, PERCENT),),
    # param_2 2 to 7 limit it to one gathering tool (sap, hoe, pickaxe) on
    # single buffs that read only "Gathering Luck increases."; no label.
    107: (EffectLine("Gathering Item Drop Rate", 1, PERCENT, when={2: 0}),),
    108: (EffectLine("Knowledge Gain Chance", 1, PERCENT),),
    109: (EffectLine("Higher Grade Knowledge Gain Chance", 1, PERCENT),),
    # Kind 3 cuts farming time on two buffs whose names do not fit this
    # scale (400000 named -2 sec), so it stays unlabelled.
    111: (
        *(
            EffectLine(
                f"{name} Time",
                2,
                CRAFT_SECONDS,
                is_negated=True,
                when={1: kind},
                kind_labels={1: name},
            )
            for kind, name in {0: "Alchemy", 1: "Cooking"}.items()
        ),
        *kinds(1, "Processing Success Rate", {2: "Processing"}, 2, PERCENT),
    ),
    # Movement, attack and casting speed as rates, each in its own parameter:
    # `Attack/Casting Speed +10%` stores 100000 in param_2 and param_3.
    160: (
        EffectLine("Movement Speed", 1, PERCENT),
        EffectLine("Attack Speed", 2, PERCENT),
        EffectLine("Casting Speed", 3, PERCENT),
    ),
    # Kind 1 is yellow fish (`희귀`, "Rare Fish" in the fish descriptions),
    # kind 2 blue (`고급`, "High-quality Fish"), as the skills that apply them
    # read: `Increase chance to catch a high-quality fish (5%)`. The kind 2
    # buff texts say "Rare Fish" too, which is stale.
    126: kinds(
        1,
        "Chance to Catch {kind} Fish",
        {1: "Rare", 2: "High-quality"},
        2,
        PERCENT,
    ),
    # Healing reduction stored positive: "Target's Recovery -10%".
    169: (EffectLine("Target's Recovery", 1, PERCENT, is_negated=True),),
    # Test items A1_001 to A1_024, whose skills read "A1 Teleport": param_3
    # is the instancefield.dbss key (4001 is the field named `A1_001`).
    # param_1 is 17 on all 48 buffs, meaning unknown.
    176: (
        EffectLine(
            "Teleport to Instance Field", 3, KEY, when={1: 17}, value_label="Instance Field"
        ),
    ),
    # Token of Desert Trading (409) reads "Trade Goods Price Doubled" for
    # 1000000; item 408 reads "+50%" for 750000, which its Korean name gives.
    131: (EffectLine("Trade Item Price", 1, PERCENT),),
    134: (EffectLine("Swimming Speed", 1, PERCENT),),
    # Patrigio's Pocket Watch sets the character to level 61.
    196: (EffectLine("Set Level to", 1, is_signed=False),),
    # Oceanbound Otter Fishing Rod: "Prize Catch Fish Rate +3%".
    200: (EffectLine("Prize Catch Fish Rate", 1, PERCENT),),
    # A cut stored positive: "Auto-fishing Time -5%".
    121: (EffectLine("Auto-fishing Time", 1, PERCENT, is_negated=True),),
    # param_1 picks a rate (0) or a flat amount (2).
    120: (
        *kinds(1, "Monster Damage Reduction Rate", {0: "Rate"}, 2, PERCENT),
        *kinds(1, "Monster Damage Reduction", {2: "Flat"}, 2),
    ),
    128: kinds(1, "{kind} Resistance", {0: "Heatstroke", 1: "Hypothermia"}, 2, PERCENT),
    # One amount per target; no buff sets both.
    136: (
        EffectLine("Extra AP Against Monsters", 1, value_label="Monster AP"),
        EffectLine("Extra AP Against Adventurers", 2, value_label="Adventurer AP"),
    ),
    149: (
        *(
            EffectLine(
                f"{_LIFE_SKILLS[skill]} Mastery",
                3,
                when={1: skill, 2: param_2},
                kind_labels={1: _LIFE_SKILLS[skill]},
            )
            for skill, param_2 in _MASTERY_PARAM_2.items()
        ),
        EffectLine(
            "Life Skill Mastery",
            3,
            when={1: _ALL_LIFE_SKILLS, 2: 0},
            kind_labels={1: "All"},
        ),
    ),
    181: kinds(1, "{kind} EXP", _BREATH_STRENGTH_HEALTH, 2, PERCENT),
    # Black Shrine aura orbs: param_1 1 adds param_2 to the aura of param_3
    # (Sun Orb, red like the Sun Aura's orb), 0 to the aura the player picks
    # (Light Orb: "Selected Aura Stat +1"). The Sun and Moon Orb tooltips
    # name each other's aura.
    186: (
        *(
            EffectLine(
                f"{name} Aura Fixed Stat",
                2,
                when={1: 1, 3: attribute},
                kind_labels={1: "Fixed", 3: name},
            )
            for attribute, name in _MORNING_LIGHT_ATTRIBUTES.items()
        ),
        EffectLine("Selected Aura Stat", 2, when={1: 0}, kind_labels={1: "Selected"}),
    ),
    # Flat AP and DP from Land of the Morning Light buffs and bosses.
    187: tuple(
        EffectLine(stat, value_param, when={3: attribute}, kind_labels={3: name})
        for attribute, name in _MORNING_LIGHT_ATTRIBUTES.items()
        for stat, value_param in (("AP", 1), ("DP", 2))
    ),
}


# Types that store no amount and always read the same.
FIXED_TEXTS: dict[int, str] = {
    # Firecracker (Red): "Subjects within the range cannot hide their name";
    # Shai's Come Out, Come Out: "Reveals hidden enemies and names".
    84: "Reveal Hidden Names",
    # The English text of all 16 buffs, from Corsair skills such as Flow:
    # Raging Torrent.
    168: "No Guard Gauge recovery",
}

OVER_TIME_EFFECTS: dict[int, OverTimeEffect] = {
    1: OverTimeEffect(
        "HP",
        recover_on={1: "on Hits", 3: "when struck", 9: "on Critical Hits"},
        fixed_damage_on={
            4: FixedDamage("Retaliate", "when struck"),
            6: FixedDamage("Deal", "on Back Attack Hits"),
            10: FixedDamage("Deal", "on Critical Hits"),
        },
        # dot_bleeding.dds is left out: 201 of its texts say "burn".
        damage_kinds={
            "dot_poison.dds": "poison",
            "dot_burns.dds": "burn",
            "dot_pains.dds": "pain",
        },
    ),
    4: OverTimeEffect("MP/WP/SP", recover_on={1: "on Hits", 8: "when struck"}),
}
