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

from _common.loc import loc_text
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


def _vehicle_skill_name(key: int) -> str:
    return loc_text(LOC_VEHICLE_SKILL, key)


VALUE_TABLES: tuple[ValueTable, ...] = (
    ValueTable("cashproduct_newbieproduct.bss", (ValueField("product_id", "I", "productId"),)),
    ValueTable(
        "icefisingregionstaticstatus.bss",
        (
            ValueField("region_key", "H", "regionKey", NameLookup("region_name", "region", town_name)),
            ValueField("mini_game_group_index", "H", "miniGameGroup"),
        ),
        RowCount.TO_TABLE_START,
    ),
    ValueTable("instanceetcoption.bss", (ValueField("unknown_04", "I"), ValueField("unknown_08", "I"))),
    ValueTable("maidactoroption.bss", (ValueField("unknown_04", "B"), ValueField("unknown_05", "B"))),
    ValueTable(
        "musicoption.bss",
        (ValueField("playable_distance", "f", "playableDistance"), ValueField("unknown_08", "8s")),
    ),
    ValueTable("petfeedcount.bss", (ValueField("feed_item_count", "I", "feedItemCount"),)),
    ValueTable("servantwhistledistance.bss", (ValueField("unknown_04", "2s"),)),
    ValueTable(
        "vehicletrainingskill.bss",
        (ValueField("skill_key", "B", "skillId", NameLookup("skill_name", "skill", _vehicle_skill_name)),),
        RowCount.COUNTED,
    ),
)
