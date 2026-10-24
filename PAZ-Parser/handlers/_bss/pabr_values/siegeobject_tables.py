"""Layouts of the siege object tables: object kinds, anger skills, revive options and the supply wagon."""

from __future__ import annotations

from _common.item_key import item_name_tagged
from _common.rate import rate_percent
from _common.skill import skill_name
from .fields import CHARACTER_KEY
from .layout import IconLookup, NameLookup, RowCount, ValueField, ValueTable, unknown_fields
from .names import item_icon_path
from .siege_names import territory_text


# A u16 territory key shown with its LOC type 12 name, as in siegeinfo.bss.
_TERRITORY_KEY = ValueField("territory_key", "H", "territoryKey", display=territory_text)
# A world position, three f32 (siegegovernorcarriagespawnposition_bss.md).
_POSITION: tuple[ValueField, ...] = (
    ValueField("position_x", "f", "x"),
    ValueField("position_y", "f", "y"),
    ValueField("position_z", "f", "z"),
)

# The SiegeAngerPoint values stored once after the skill rows, in the order
# the client 1784 server dump checks them (siegeangerskill_bss.md, Field Names).
_ANGER_POINT: tuple[ValueField, ...] = (
    ValueField("anger_point_per_death", "I", "angerPointPerDeath"),
    ValueField("max_anger_point", "I", "maxAngerPoint"),
    ValueField("anger_point_per_kill", "I", "angerPointPerKill"),
    ValueField("increase_point", "I", "increasePoint"),
    ValueField("decrease_survival_percent", "I", "decreaseSurvivalPercent", display=rate_percent),
    ValueField("decrease_survival_point", "I", "decreaseSurvivalPoint"),
    ValueField("increase_survival_percent", "I", "increaseSurvivalPercent", display=rate_percent),
    ValueField("increase_survival_point", "I", "increaseSurvivalPoint"),
)

# The SiegeOption columns of siegerevivevalue.bss, in sheet order, then two
# newer fields named by their file offset (siegerevivevalue_bss.md).
_REVIVE_VALUES: tuple[ValueField, ...] = (
    ValueField("siege_revival_time", "Q", "siegeRevivalTime"),
    ValueField("siege_death_revival_time", "Q", "siegeDeathRevivalTime"),
    ValueField("siege_recovery_revival_time", "Q", "siegeRecoveryRevivalTime"),
    ValueField("major_siege_recovery_revival_time", "Q", "majorSiegeRecoveryRevivalTime"),
    ValueField("siege_resource_revival_time", "Q", "siegeResourceRevivalTime"),
    ValueField("major_siege_liberation_fortress_point", "I", "liberationFortressPoint"),
    ValueField("major_siege_liberation_kill_point", "I", "liberationKillPoint"),
    ValueField("major_siege_liberation_death_point", "I", "liberationDeathPoint"),
    ValueField("major_siege_liberation_reward_time", "Q", "liberationRewardTime"),
    ValueField(
        "major_siege_enter_clothes_item_key",
        "I",
        "enterClothesItemId",
        NameLookup("enter_clothes_item_name", "enterClothesItem", item_name_tagged, is_tagged=True),
        IconLookup("icon_path", "icon", item_icon_path),
    ),
    ValueField("siege_fortress_short_distance_revival", "f", "fortressShortDistanceRevival"),
    ValueField("siege_short_distance_revival_avoid", "Q", "shortDistanceRevivalAvoid"),
    *unknown_fields((0x50, "B"), (0x51, "I")),
)


SIEGE_OBJECT_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "siegeobjectkindlistcache.bss",
        (ValueField("object_kind", "B", "objectKind"), CHARACTER_KEY),
        RowCount.COUNTED,
    ),
    ValueTable(
        "siegegravity.bss",
        (_TERRITORY_KEY, *_POSITION, *unknown_fields((0x0E, "f"))),
        RowCount.COUNTED,
    ),
    ValueTable("siegerevivevalue.bss", _REVIVE_VALUES),
    ValueTable(
        "siegeangerskill.bss",
        (
            ValueField("skill_no", "H", "skillId", NameLookup("skill_name", "skill", skill_name)),
            ValueField("resource_point", "I", "resourcePoint"),
            ValueField("siege_anger_skill_type", "B", "angerSkillType"),
            ValueField("siege_skill_resource_type", "B", "resourceType"),
        ),
        RowCount.COUNTED,
        tail=_ANGER_POINT,
    ),
    ValueTable(
        "siegegovernorcarriagespawn.bss",
        (
            CHARACTER_KEY,
            _TERRITORY_KEY,
            ValueField("start_time", "Q", "carriageStartTime"),
            ValueField("action_index", "I", "actionIndex"),
            *unknown_fields((0x10, "I")),
            ValueField("max_term", "Q", "maxTerm"),
            ValueField("spawn_position_list", "I", "spawnPositions", is_counted_list=True),
        ),
        RowCount.COUNTED,
        first_fields=("territory_key",),
    ),
    ValueTable(
        "siegegovernorcarriagespawnposition.bss",
        (ValueField("index", "I", "index"), *_POSITION),
        RowCount.COUNTED,
    ),
)
