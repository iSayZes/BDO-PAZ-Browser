"""Layouts of the ocean siege (Blue Battlefield) tables that fit the PABR value tables.

`oceansiegereward.bss` and `oceansiegereviveposition.bss` nest their lists
and have their own handlers.
"""

from __future__ import annotations

from .fields import MAP_COLOR
from .layout import RowCount, ValueField, ValueTable, unknown_fields
from .oceansiege_names import siege_days_text
from .rosewar_names import region_text
from .siege_fields import limit_member_count_fields, stat_limit_fields, territory_key_field


# Where the limit block starts in the row, after the three territory keys.
_STAT_LIMITS_AT = 0x06


OCEAN_SIEGE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "oceansiegeinfo.bss",
        (
            MAP_COLOR,
            *unknown_fields((0x03, "B"), (0x04, "3s"), (0x07, "B")),
            ValueField("region_keys", "H", "regionKeys", display=region_text, is_counted_list=True),
            # The value the worldmapoceansiegeregionforconquest.bss grid cells store (worldmapgrid_bss.md).
            ValueField("area_number", "H", "areaNumber"),
        ),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    ValueTable(
        "oceansiegeterritoryoption.bss",
        (
            territory_key_field("territory_key_1", "territory1"),
            territory_key_field("territory_key_2", "territory2"),
            territory_key_field("console_territory_key", "consoleTerritory"),
            *stat_limit_fields(_STAT_LIMITS_AT),
            *unknown_fields(
                *((offset, "f") for offset in range(0x32, 0x3E, 4)),
                *((offset, "I") for offset in range(0x3E, 0x4E, 4)),
                (0x4E, "34s"),
                (0x70, "I"),
                (0x74, "I"),
                *((offset, "f") for offset in range(0x78, 0x88, 4)),
            ),
            *limit_member_count_fields(),
            ValueField("start_days", "I", "startDays", is_counted_list=True, list_display=siege_days_text),
        ),
        RowCount.COUNTED,
        count_key="oceanSiegeGroups",
    ),
)
