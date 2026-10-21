"""Layouts of the Hardcore channel tables (`hardcore*.bss`) that fit the PABR value tables.

`hardcorerandomspawncharacterstaticstatusmanager.bss` stores lists after its
rows and has its own handler; `hardcorecharacterstatstaticstatus.bss` too.
"""

from __future__ import annotations

from .fields import MAP_COLOR
from .hardcore_names import class_list_text, grade_name
from .layout import NameLookup, RowCount, TextRef, ValueField, ValueTable, unknown_fields
from .rosewar_names import argb_hex


HARDCORE_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "hardcorechanneletcoptionstaticstatus.bss",
        (
            *unknown_fields(
                (0x04, "I"),
                (0x08, "I"),
                (0x0C, "H"),
                (0x0E, "B"),
                *((offset, "I") for offset in range(0x0F, 0x3B, 4)),
                (0x3B, "i"),
                (0x3F, "Q"),
                (0x47, "Q"),
                (0x4F, "Q"),
            ),
            # (u8, f32, u16) entries; hardcorechanneletcoptionstaticstatus_bss.md, Open Questions.
            ValueField("unknown_entries", "BfH", is_counted_list=True),
            ValueField("unknown_entries_00", "f"),
            ValueField(
                "possible_class_types",
                "B",
                "possibleClasses",
                is_counted_list=True,
                list_display=class_list_text,
            ),
        ),
    ),
    ValueTable(
        "hardcorechannelinfo.bss",
        (
            MAP_COLOR,
            *unknown_fields((0x03, "B"), (0x04, "3s"), (0x07, "B"), (0x08, "B")),
        ),
        RowCount.COUNTED,
        count_key="mapColors",
    ),
    ValueTable(
        "hardcorechanneltitlestaticstatusmanager.bss",
        (
            ValueField("title_key", "H", "hardcoreTitleKey"),
            *unknown_fields((0x02, "B"), (0x03, "I")),
            ValueField("kill_count", "I", "killCount"),
            *unknown_fields((0x0B, "I"), (0x0F, "I"), (0x13, "I"), (0x17, "I")),
            ValueField("name_ref", "I", text=TextRef("name_kr", "hardcoreTitle")),
            ValueField("description_ref", "I", text=TextRef("description_kr", "description")),
            ValueField("condition_ref", "I", text=TextRef("condition_kr", "condition")),
            ValueField("unknown_27", "I"),
            ValueField("grade_color", "I", "gradeColor", display=argb_hex),
        ),
        RowCount.COUNTED,
        count_key="hardcoreTitles",
        first_fields=("title_key", "name_ref", "description_ref", "condition_ref"),
    ),
    ValueTable(
        "hardcorechanneltotalrankgradestaticstatusmanager.bss",
        (
            ValueField("grade_key", "H", "gradeKey", NameLookup("grade_name", "grade", grade_name)),
            ValueField("rank", "I", "rank"),
            ValueField("percent", "f", "topPercent"),
        ),
        RowCount.COUNTED,
        count_key="hardcoreGrades",
        head=(ValueField("rank_threshold", "I", "rankThreshold"), ValueField("unknown_08", "I")),
    ),
)
