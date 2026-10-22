"""Layouts of the ocean siege (Blue Battlefield) tables that fit the PABR value tables.

`oceansiegereward.bss` and `oceansiegereviveposition.bss` nest their lists
and have their own handlers.
"""

from __future__ import annotations

from _common.territory import territory_name
from .fields import MAP_COLOR
from .layout import NameLookup, RowCount, ValueField, ValueTable, unknown_fields
from .oceansiege_names import siege_days_text
from .rosewar_names import region_text


# CppEnums.VillageSiegeType 0 to 5: the days getLimitMemberCount(day) takes,
# one u16 each (oceansiegeterritoryoption_bss.md, Field Names).
_LIMIT_MEMBER_DAYS: tuple[str, ...] = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday")


def _territory(name: str, column: str) -> ValueField:
    """A u16 territory key and its LOC type 12 name, stored as `<role>_name`."""
    name_field = name.replace("_key", "_name")
    return ValueField(name, "H", f"{column}Key", NameLookup(name_field, column, territory_name))


def _limit_member_count(day: str) -> ValueField:
    return ValueField(f"limit_member_count_{day}", "H", f"limitMemberCount{day.capitalize()}")


OCEAN_SIEGE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "oceansiegeinfo.bss",
        (
            MAP_COLOR,
            *unknown_fields((0x03, "B"), (0x04, "3s"), (0x07, "B")),
            ValueField("region_keys", "H", "regionKeys", display=region_text, is_counted_list=True),
            ValueField("unknown_region_keys_00", "H"),
        ),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    ValueTable(
        "oceansiegeterritoryoption.bss",
        (
            _territory("territory_key_1", "territory1"),
            _territory("territory_key_2", "territory2"),
            _territory("console_territory_key", "consoleTerritory"),
            *unknown_fields(
                *((offset, "f") for offset in range(0x06, 0x22, 4)),
                *((offset, "I") for offset in range(0x22, 0x32, 4)),
                *((offset, "f") for offset in range(0x32, 0x3E, 4)),
                *((offset, "I") for offset in range(0x3E, 0x4E, 4)),
                (0x4E, "34s"),
                (0x70, "I"),
                (0x74, "I"),
                *((offset, "f") for offset in range(0x78, 0x88, 4)),
            ),
            *(_limit_member_count(day) for day in _LIMIT_MEMBER_DAYS),
            ValueField("start_days", "I", "startDays", is_counted_list=True, list_display=siege_days_text),
        ),
        RowCount.COUNTED,
        count_key="oceanSiegeGroups",
    ),
)
