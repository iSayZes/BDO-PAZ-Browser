"""The effect text of a Skill Add-on ability index.

LOC type 33 holds the text in the loaded language, keyed by the ability
index in `str_id1`; `skillawakeningability.dbss` holds the Korean text
(`description_kr`). `skillawakeningability.dbss` and
`skillawakeningability2.bss` show the same text. Field Names in
docs/file-formats/skillawakeningability_dbss.md.
"""

from __future__ import annotations

from collections.abc import Mapping

from _common.loc import LOC_NULL, loc_tagged
from .parser import KEY_FIELD, parse_skillawakeningability_records


LOC_AWAKENING_ABILITY = 33


def ability_description_tagged(ability_index: int, description_kr: str) -> str:
    """The LOC type 33 text of the ability with its tags, else `description_kr`."""
    text = loc_tagged(LOC_AWAKENING_ABILITY, ability_index)
    if text and text != LOC_NULL:
        return text
    return description_kr.strip()


def korean_descriptions(data: bytes) -> Mapping[int, str]:
    """Ability index -> its Korean `description_kr`, from `skillawakeningability.dbss` bytes.

    Raises ValueError like `parse_skillawakeningability_records()`.
    """
    return {record[KEY_FIELD]: record["description_kr"] for record in parse_skillawakeningability_records(data)}
