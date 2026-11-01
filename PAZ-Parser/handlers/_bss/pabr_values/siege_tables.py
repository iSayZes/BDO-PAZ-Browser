"""Layouts of the land siege (Node War and Conquest War) tables that fit the PABR value tables.

`tax.bss` nests a fixed array per row and has its own handler.
"""

from __future__ import annotations

from .fields import MAP_COLOR
from .layout import RowCount, ValueField, ValueTable, unknown_fields
from .names import map_color_text
from .oceansiege_names import siege_days_text
from .rosewar_names import region_text
from .siege_fields import limit_member_count_fields, stat_limit_fields, territory_key_field
from .siege_names import territories_text, territory_text


# CppEnums.VillageSiegeType order, Sunday to Saturday (siegedayoption_bss.md).
_WEEK_DAYS: tuple[str, ...] = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
# Where the limit block starts in the row, after the three territory keys and unknown_06.
_STAT_LIMITS_AT = 0x08
# A row's fields after its start_days list, at start_days+0x11 to +0x48:
# twelve u32 in six pairs, then two more (siegeterritoryoptionstaticstatus_bss.md).
_TAIL_U32_AT = range(0x11, 0x49, 4)

# The colour the table is keyed by, then the struct's own pa::Color copy
# (siegeinfo_bss.md, Field Names).
_MAP_COLOR_FIELDS: tuple[ValueField, ...] = (
    MAP_COLOR,
    *unknown_fields((0x03, "B")),
    ValueField("map_color_dup", "3s"),
    *unknown_fields((0x07, "B")),
)


def _day_territories(day: str) -> ValueField:
    """One day's u64-counted list of territory keys."""
    return ValueField(
        f"{day}_territory_keys",
        "H",
        f"{day}Territories",
        is_counted_list=True,
        count_fmt="Q",
        list_display=territories_text,
    )


def _start_days_field(offset: int, fmt: str) -> ValueField:
    """An unnamed field after the start_days list, named by its offset from the list's end."""
    return ValueField(f"unknown_start_days_{offset:02x}", fmt)


SIEGE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "siegeinfo.bss",
        (
            *_MAP_COLOR_FIELDS,
            ValueField("is_siege", "B", "isSiege"),
            ValueField("territory_key", "h", "territoryKey", display=territory_text),
        ),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    ValueTable(
        "villagesiegeinfo.bss",
        (
            *_MAP_COLOR_FIELDS,
            ValueField("region_keys", "H", "regionKeys", display=region_text, is_counted_list=True),
            # The value the worldmapsiegeregionforconquest.bss grid cells store (worldmapgrid_bss.md).
            ValueField("area_number", "H", "areaNumber"),
        ),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    ValueTable(
        "siegedayoption.bss",
        tuple(_day_territories(day) for day in _WEEK_DAYS),
    ),
    ValueTable(
        "siegeterritoryoptionstaticstatus.bss",
        (
            territory_key_field("territory_key_1", "territory1"),
            territory_key_field("territory_key_2", "territory2"),
            territory_key_field("console_territory_key", "consoleTerritory"),
            *unknown_fields((0x06, "H")),
            *stat_limit_fields(_STAT_LIMITS_AT),
            *unknown_fields(
                *((offset, "f") for offset in range(0x34, 0x40, 4)),
                *((offset, "I") for offset in range(0x40, 0x50, 4)),
                *((offset, "H") for offset in range(0x50, 0x62, 2)),
                *((offset, "I") for offset in range(0x62, 0x72, 4)),
            ),
            *limit_member_count_fields(),
            ValueField("start_days", "I", "startDays", is_counted_list=True, list_display=siege_days_text),
            _start_days_field(0x00, "B"),
            ValueField("territory_1_icon_x", "f", "territory1IconX"),
            ValueField("territory_1_icon_y", "f", "territory1IconY"),
            ValueField("territory_2_icon_x", "f", "territory2IconX"),
            ValueField("territory_2_icon_y", "f", "territory2IconY"),
            *(_start_days_field(offset, "I") for offset in _TAIL_U32_AT),
            ValueField("hp_recovery_limit", "f", "hpRecoveryLimit"),
            _start_days_field(0x4D, "I"),
            _start_days_field(0x51, "I"),
            ValueField("stamina_limit", "I", "staminaLimit"),
            ValueField("unknown_skill_nos", "H", is_counted_list=True),
        ),
        RowCount.COUNTED,
        count_key="territoryGroups",
    ),
    ValueTable(
        "siegeoccupycolor.bss",
        (
            ValueField("index", "I", "index"),
            ValueField("color", "4s", "color", display=map_color_text),
        ),
        RowCount.COUNTED,
    ),
)
