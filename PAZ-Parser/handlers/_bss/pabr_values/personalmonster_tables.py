"""Layout of the Dark Rift world map table that fits the PABR value tables.

`personalmonsteretc.bss` is one value set; its doc is
`docs/file-formats/personalmonsteretc_bss.md`. The field names follow the
`PersonalMonsterOption_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784. `personalmonster.dbss` and `personalmonsterposition.dbss`
have offset files and are not value tables.
"""

from __future__ import annotations

from .layout import ValueField, ValueTable
from .personalmonster_names import icon_region_text, icon_size_text


# The `UV Difficulty1` to `UV Difficulty3` and `UV Level1` to `UV Level5` columns.
DIFFICULTY_COUNT = 3
LEVEL_COUNT = 5
# The `IconSize` column: width and height.
ICON_SIZE_VALUES = 2
# One region: x1, y1, x2, y2.
_REGION = "4f"


PERSONAL_MONSTER_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "personalmonsteretc.bss",
        (
            ValueField("unknown_04", "I"),
            ValueField("detect_range", "f", "detectRange"),
            ValueField("max_level", "I", "maxLevel"),
            ValueField("icon_size", "f", "iconSize", fixed_count=ICON_SIZE_VALUES, list_display=icon_size_text),
            ValueField(
                "difficulty_icon_uvs", _REGION, "difficultyIconUvs", fixed_count=DIFFICULTY_COUNT, display=icon_region_text
            ),
            ValueField("level_icon_uvs", _REGION, "levelIconUvs", fixed_count=LEVEL_COUNT, display=icon_region_text),
            ValueField("unknown_98", "I"),
        ),
    ),
)
