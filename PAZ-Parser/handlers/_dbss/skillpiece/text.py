"""Set effect tier text from LOC type 52.

Keyed `(skill_no, level, 0, field)`: field 2 is the set title, 1 the
threshold label (`2 Parts`) and 0 the bonus lines, all with their `<PAColor>`
tags. The Korean strings of the record stand in where LOC has no row. See
"Type 52" in docs/file-formats/languagedata_loc.md.
"""

from __future__ import annotations

from dataclasses import dataclass

from _common.loc import loc_type_entries
from _common.pa_text import strip_pa_tags

LOC_SET_EFFECT = 52
_FIELD_DESC = 0
_FIELD_DESC_TITLE = 1
_FIELD_GROUP_TITLE = 2


@dataclass(frozen=True)
class TierText:
    """A tier's tagged set title, threshold label and bonus lines; "" when blank."""

    group_title: str
    desc_title: str
    desc: str


def tier_text(skill_no: int, level: int, korean: TierText) -> TierText:
    """The tier's LOC type 52 text in the user's language, else `korean`."""
    entries = loc_type_entries(LOC_SET_EFFECT)

    def pick(field: int, fallback: str) -> str:
        tagged = entries.get((LOC_SET_EFFECT, skill_no, level, 0, field), "")
        return tagged.strip() if strip_pa_tags(tagged).strip() else fallback.strip()

    return TierText(
        group_title=pick(_FIELD_GROUP_TITLE, korean.group_title),
        desc_title=pick(_FIELD_DESC_TITLE, korean.desc_title),
        desc=pick(_FIELD_DESC, korean.desc),
    )
