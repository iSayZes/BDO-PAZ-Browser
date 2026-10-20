"""Layouts of the small option tables, one entry per file.

A PABR file is the PABR magic, the values, then an empty string table and
the trailer. A bare file is the values alone, with no magic, string table or
trailer. The values are one set of fields, a u32 count and that many rows,
or rows up to the string table or the end of a bare file. A field can be a
counted list: a u32 count, then that many values. Each file's doc is
`docs/file-formats/<stem>_bss.md`; field names follow the doc, and
`unknown_*` fields get no column.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

from _common.character import character_name
from _common.item_key import item_name_tagged
from _common.rate import rate_percent
from _common.title import title_name
from _common.town import town_name
from .names import (
    aura_name,
    calamity_number,
    cooldown_cut,
    duration_seconds,
    item_icon_path,
    packed_quest_text,
    packed_quest_title,
    rate_bonus,
    skill_key_name,
    utc_time,
    vehicle_skill_name,
)


class Framing(Enum):
    """What surrounds the values."""

    # PABR magic at +0x00, the values from +0x04, then the string table and the trailer.
    PABR = "pabr"
    # The values alone, from +0x00 to the end of the file.
    BARE = "bare"


class RowCount(Enum):
    """How many times the fields repeat in the values."""

    ONE = "one"
    # A u32 count where the values start, then that many rows.
    COUNTED = "counted"
    # Rows from where the values start up to the string table (PABR) or the
    # end of the file (BARE), no count.
    TO_TABLE_START = "to_table_start"


@dataclass(frozen=True)
class NameLookup:
    """A display name for a key field, stored on the record next to it.

    With `is_tagged`, `name_of` returns game text with `<PAColor>` tags: the
    record keeps the plain text under `field` and the tagged copy under
    `pa_key(field)`, and the cell draws the colours.
    """

    field: str
    column: str
    name_of: Callable[[int], str]
    is_tagged: bool = False


@dataclass(frozen=True)
class IconLookup:
    """An icon path for a key field, stored on the record; its column sits after the key."""

    field: str
    column: str
    path_of: Callable[[int], str]


@dataclass(frozen=True)
class ValueField:
    """One field: record key, `struct` format and its lang column key.

    `column` is None for a field with no column (`unknown_*`, or a copy of
    another field). An `s` format (`8s`) is a byte run, stored as hex text.
    `display` turns the value into its cell text; the record keeps the value.
    With `is_counted_list` the field is a u32 count, then that many values,
    stored as a list.
    """

    name: str
    fmt: str
    column: str | None = None
    lookup: NameLookup | None = None
    icon: IconLookup | None = None
    display: Callable[[int], str] | None = None
    is_counted_list: bool = False

    def __post_init__(self) -> None:
        if self.is_counted_list and (self.lookup is not None or self.icon is not None):
            raise ValueError(f"{self.name}: a counted list takes no name or icon lookup")


@dataclass(frozen=True)
class ValueTable:
    """The layout of one file; `count_key` is the lang `meta` key of its count line."""

    file_name: str
    fields: tuple[ValueField, ...]
    rows: RowCount = RowCount.ONE
    framing: Framing = Framing.PABR
    count_key: str = "count"

    def __post_init__(self) -> None:
        if self.rows is RowCount.TO_TABLE_START and any(field.is_counted_list for field in self.fields):
            raise ValueError(f"{self.file_name}: rows up to the string table need a fixed row size")

    @property
    def has_named_field(self) -> bool:
        return any(field.column is not None for field in self.fields)


# The SiegeStage_0 to SiegeStage_6 columns of siegemercenarylimitcount.bss.
SIEGE_STAGE_COUNT = 7


def _unknown_fields(*layout: tuple[int, str]) -> tuple[ValueField, ...]:
    """`unknown_<offset>` fields from (offset, format) pairs."""
    return tuple(ValueField(f"unknown_{offset:02x}", fmt) for offset, fmt in layout)


_CHARACTER_NAME = NameLookup("character_name", "character", character_name)
_CHARACTER_KEY = ValueField("character_key", "H", "characterId", _CHARACTER_NAME)
_ITEM_ID = ValueField(
    "item_id",
    "I",
    "itemId",
    NameLookup("item_name", "item", item_name_tagged, is_tagged=True),
    IconLookup("icon_path", "icon", item_icon_path),
)
_TITLE_ID = ValueField("title_id", "I", "titleId", NameLookup("title_name", "title", title_name))


VALUE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "barterresetoption.bss",
        (
            ValueField("general_barter", "I", "generalBarter", is_counted_list=True),
            ValueField("material_barter", "I", "materialBarter", is_counted_list=True),
        ),
    ),
    ValueTable("cashproduct_newbieproduct.bss", (ValueField("product_id", "I", "productId"),)),
    ValueTable(
        "cultivationevent.bss",
        (ValueField("cultivation_event_type", "h", "cultivationEventType"),),
        RowCount.COUNTED,
    ),
    ValueTable(
        "elementalstat.bss",
        (
            ValueField("element_type", "B", "elementType", NameLookup("aura", "aura", aura_name)),
            ValueField("ap_per_orb", "I", "apPerOrb"),
            ValueField("dp_per_orb", "I", "dpPerOrb"),
            ValueField("stat_points_per_orb", "I", "statPointsPerOrb"),
            ValueField("element_type_dup", "B"),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "blackShrineAuras",
    ),
    ValueTable("employeeloyalismitemetc.bss", _unknown_fields((0x04, "I"), (0x08, "I"), (0x0C, "I"), (0x10, "I"))),
    ValueTable(
        "icefisingregionstaticstatus.bss",
        (
            ValueField("region_key", "H", "regionKey", NameLookup("region_name", "region", town_name)),
            ValueField("mini_game_group_index", "H", "miniGameGroup"),
        ),
        RowCount.TO_TABLE_START,
    ),
    ValueTable("instanceetcoption.bss", (ValueField("unknown_04", "I"), ValueField("unknown_08", "I"))),
    ValueTable(
        "interaction.bss",
        (
            ValueField("interaction_type", "I", "interactionType"),
            ValueField("unknown_04", "B"),
            ValueField("execute", "I", "execute"),
            _CHARACTER_KEY,
        ),
        RowCount.COUNTED,
    ),
    ValueTable("maidactoroption.bss", (ValueField("unknown_04", "B"), ValueField("unknown_05", "B"))),
    ValueTable(
        "morninglandoption.bss",
        (
            ValueField("stat_reset_cost", "Q", "statResetCost"),
            ValueField("light_orb_reset_cost", "Q", "lightOrbResetCost"),
            ValueField("weekly_clear_limit", "B", "weeklyClearLimit"),
        ),
        framing=Framing.BARE,
    ),
    ValueTable(
        "musicoption.bss",
        (ValueField("playable_distance", "f", "playableDistance"), ValueField("unknown_08", "8s")),
    ),
    ValueTable(
        "othertownnotmovableitem.bss",
        (
            _ITEM_ID,
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "notMovableItems",
    ),
    ValueTable("petfeedcount.bss", (ValueField("feed_item_count", "I", "feedItemCount"),)),
    ValueTable(
        "petleaderbuff.bss",
        (
            ValueField("pet_tier", "B", "petTier"),
            ValueField("unknown_01", "B"),
            ValueField("leader_buff_rate", "I", "lootCooldown", display=cooldown_cut),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "petTiers",
    ),
    ValueTable(
        "rosewarinfo.bss",
        _unknown_fields((0x00, "3s"), (0x03, "B"), (0x04, "3s"), (0x07, "B"), (0x08, "B")),
        RowCount.COUNTED,
    ),
    ValueTable(
        "servantchecktitle.bss",
        (
            ValueField("unknown_04", "H"),
            _TITLE_ID,
            _CHARACTER_KEY,
        ),
    ),
    ValueTable("servantwhistledistance.bss", (ValueField("unknown_04", "2s"),)),
    ValueTable(
        "siegemercenarylimitcount.bss",
        tuple(ValueField(f"siege_stage_{stage}", "I", f"siegeStage{stage}") for stage in range(SIEGE_STAGE_COUNT)),
    ),
    ValueTable(
        "snowboardcourseinfo.bss",
        _unknown_fields((0x00, "3s"), (0x03, "B"), (0x04, "B"), (0x05, "3s"), (0x08, "B")),
        RowCount.COUNTED,
    ),
    ValueTable(
        "solareetcoptionstaticstatus.bss",
        _unknown_fields((0x00, "f"), (0x04, "f"), (0x08, "f"), (0x0C, "f"), (0x10, "f")),
        framing=Framing.BARE,
    ),
    ValueTable("timeattackranking.bss", (_CHARACTER_KEY,), RowCount.COUNTED),
    ValueTable(
        "vehicletrainingskill.bss",
        (ValueField("skill_key", "B", "skillId", NameLookup("skill_name", "skill", vehicle_skill_name)),),
        RowCount.COUNTED,
    ),
    ValueTable(
        "voxelregionskillstaticstatusmanager.bss",
        (
            ValueField("unknown_00", "B"),
            ValueField("skill_key", "I", "skillId", NameLookup("skill_name", "skill", skill_key_name)),
        ),
        RowCount.COUNTED,
    ),
    ValueTable(
        "elementalserverbuff.bss",
        (
            ValueField("calamity_level", "B", "calamity", display=calamity_number),
            ValueField("calamity_level_dup", "B"),
            ValueField("sun_blessing_ap", "f", "sunBlessingAp"),
            ValueField("moon_blessing_dp", "f", "moonBlessingDp"),
            ValueField("earth_blessing_drop_rate", "I", "earthBlessingDropRate", display=rate_bonus),
            ValueField("buff_duration", "I", "buffDuration", display=duration_seconds),
            ValueField("unknown_12", "I"),
        ),
        RowCount.COUNTED,
        Framing.BARE,
    ),
    ValueTable(
        "olviaacademyseasonss.bss",
        (
            ValueField("season_no", "I", "academyClass"),
            ValueField("start_time", "Q", "startTime", display=utc_time),
            ValueField("graduation_time", "Q", "graduationTime", display=utc_time),
            ValueField("close_time", "Q", "closeTime", display=utc_time),
            ValueField("end_time", "Q", "endTime", display=utc_time),
            ValueField(
                "enter_quest",
                "I",
                "enterQuestId",
                NameLookup("enter_quest_title", "enterQuest", packed_quest_title),
                display=packed_quest_text,
            ),
            ValueField(
                "graduation_quest",
                "I",
                "graduationQuestId",
                NameLookup("graduation_quest_title", "graduationQuest", packed_quest_title),
                display=packed_quest_text,
            ),
            _TITLE_ID,
        ),
        framing=Framing.BARE,
        count_key="academyClasses",
    ),
    ValueTable(
        "petupgrade.bss",
        (
            ValueField("pet_tier", "B", "petTier"),
            _ITEM_ID,
            ValueField("item_count", "Q", "itemCount"),
            ValueField("success_rate", "I", "successRate", display=rate_percent),
            ValueField("unknown_11", "I"),
            ValueField("pet_tier_dup", "B"),
        ),
        RowCount.COUNTED,
        Framing.BARE,
        "petTiers",
    ),
)
