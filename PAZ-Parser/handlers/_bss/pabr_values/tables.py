"""Layouts of the small PABR option tables, one entry per file.

Each file is the PABR magic, a few values where a table keeps its record
count, then an empty string table. The values are one set of fields, a u32
count and that many rows, or rows up to the string table. Each file's doc
is `docs/file-formats/<stem>_bss.md`; field names follow the doc, and
`unknown_*` fields get no column.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

from _common.character import character_name
from _common.loc import loc_text
from _common.skill import skill_name, split_skill_key
from _common.title import title_name
from _common.town import town_name
from _common.vehicle_skill import LOC_VEHICLE_SKILL


class RowCount(Enum):
    """How many times the fields repeat between the magic and the string table."""

    ONE = "one"
    # A u32 count at +0x04, then that many rows.
    COUNTED = "counted"
    # Rows from +0x04 up to the string table, no count.
    TO_TABLE_START = "to_table_start"


@dataclass(frozen=True)
class NameLookup:
    """A display name for a key field, stored on the record next to it."""

    field: str
    column: str
    name_of: Callable[[int], str]


@dataclass(frozen=True)
class ValueField:
    """One field: record key, `struct` format and its lang column key.

    `column` is None for an `unknown_*` field. An `s` format (`8s`) is a
    byte run, stored as hex text.
    """

    name: str
    fmt: str
    column: str | None = None
    lookup: NameLookup | None = None


@dataclass(frozen=True)
class ValueTable:
    """The layout of one file."""

    file_name: str
    fields: tuple[ValueField, ...]
    rows: RowCount = RowCount.ONE

    @property
    def has_named_field(self) -> bool:
        return any(field.column is not None for field in self.fields)


# The SiegeStage_0 to SiegeStage_6 columns of siegemercenarylimitcount.bss.
SIEGE_STAGE_COUNT = 7


def _vehicle_skill_name(key: int) -> str:
    return loc_text(LOC_VEHICLE_SKILL, key)


def _skill_key_name(key: int) -> str:
    skill_no, _level = split_skill_key(key)
    return skill_name(skill_no)


def _unknown_fields(*layout: tuple[int, str]) -> tuple[ValueField, ...]:
    """`unknown_<offset>` fields from (offset, format) pairs."""
    return tuple(ValueField(f"unknown_{offset:02x}", fmt) for offset, fmt in layout)


_CHARACTER_NAME = NameLookup("character_name", "character", character_name)
_CHARACTER_KEY = ValueField("character_key", "H", "characterId", _CHARACTER_NAME)


VALUE_TABLES: tuple[ValueTable, ...] = (
    ValueTable("cashproduct_newbieproduct.bss", (ValueField("product_id", "I", "productId"),)),
    ValueTable(
        "cultivationevent.bss",
        (ValueField("cultivation_event_type", "h", "cultivationEventType"),),
        RowCount.COUNTED,
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
        "musicoption.bss",
        (ValueField("playable_distance", "f", "playableDistance"), ValueField("unknown_08", "8s")),
    ),
    ValueTable("petfeedcount.bss", (ValueField("feed_item_count", "I", "feedItemCount"),)),
    ValueTable(
        "rosewarinfo.bss",
        _unknown_fields((0x00, "3s"), (0x03, "B"), (0x04, "3s"), (0x07, "B"), (0x08, "B")),
        RowCount.COUNTED,
    ),
    ValueTable(
        "servantchecktitle.bss",
        (
            ValueField("unknown_04", "H"),
            ValueField("title_id", "I", "titleId", NameLookup("title_name", "title", title_name)),
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
    ValueTable("timeattackranking.bss", (_CHARACTER_KEY,), RowCount.COUNTED),
    ValueTable(
        "vehicletrainingskill.bss",
        (ValueField("skill_key", "B", "skillId", NameLookup("skill_name", "skill", _vehicle_skill_name)),),
        RowCount.COUNTED,
    ),
    ValueTable(
        "voxelregionskillstaticstatusmanager.bss",
        (
            ValueField("unknown_00", "B"),
            ValueField("skill_key", "I", "skillId", NameLookup("skill_name", "skill", _skill_key_name)),
        ),
        RowCount.COUNTED,
    ),
)
