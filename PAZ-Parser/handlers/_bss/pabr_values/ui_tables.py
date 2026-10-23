"""Layouts of the quiz, photo mode and world map option tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/<stem>_bss.md`. The quiz names follow
the `Social_Quiz` sheet of a private server's `DataSheets.bexcel` on client
1784, the photo mode name the client Lua of client 3482. No source names a
field of `worldmapoptionstaticstatusmanager.bss`, so its view shows the row
bytes. `classinputdata.bss` and `classcooltimeuilist.bss` of the same batch
have rows of their own size and their own handlers (`_bss/classinputdata/`,
`_bss/classcooltimeuilist/`).
"""

from __future__ import annotations

from _common.contents_group import contents_groups_text
from .layout import NameLookup, RowCount, TextRef, ValueField, ValueTable, unknown_fields
from .rosewar_names import game_key_text
from .ui_names import quiz_action_text, quiz_answer_text


# The world position of a worldmapoptionstaticstatusmanager.bss row: x, y, z.
_POSITION_AXES = 3


UI_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "quizactionstaticstatus.bss",
        (
            ValueField("answer_type", "B", "answerType", display=quiz_answer_text),
            ValueField("action_hashes", "I", "quizActions", display=quiz_action_text, is_counted_list=True),
            ValueField(
                "contents_group_hashes",
                "I",
                "contentsGroups",
                is_counted_list=True,
                list_display=contents_groups_text,
            ),
        ),
        RowCount.COUNTED,
        count_key="quizAnswers",
    ),
    ValueTable(
        "photomodestaticstatus.bss",
        (
            ValueField("unknown_00", "I"),
            ValueField(
                "weather_name_ref",
                "I",
                text=TextRef("weather_name", "weatherNameKey", NameLookup("weather", "weather", game_key_text)),
            ),
        ),
        RowCount.COUNTED,
        count_key="weatherPresets",
        index_column="weatherPreset",
    ),
    ValueTable(
        "worldmapoptionstaticstatusmanager.bss",
        (
            *unknown_fields((0x00, "H"), (0x02, "H")),
            ValueField("unknown_04", "f", fixed_count=_POSITION_AXES),
        ),
        RowCount.COUNTED,
    ),
)
