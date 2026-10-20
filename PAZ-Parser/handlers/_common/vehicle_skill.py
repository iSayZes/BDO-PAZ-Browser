"""Mount and ship skill names, shared by the tables that list `vehicleskill.dbss` keys.

LOC type 8 is keyed by the u8 skill key in `str_id1`; `str_id4` 0 is the
name. Without a LOC row the name falls back to the Korean `name_kr` of
`vehicleskill.dbss`, which callers load as an optional companion
(`vehicle_skill_names_kr()` in `_dbss/vehicleskill/parser.py`).
"""

from __future__ import annotations

from collections.abc import Mapping

from _common.loc import loc_text

LOC_VEHICLE_SKILL = 8
VEHICLE_SKILL_FILE = "vehicleskill.dbss"


def vehicle_skill_name(key: int, names_kr: Mapping[int, str]) -> str:
    """The skill's name in the loaded LOC language, else its Korean name, else the bare key."""
    return loc_text(LOC_VEHICLE_SKILL, key) or names_kr.get(key) or str(key)


def vehicle_skill_companion(internal_path: str) -> str:
    """The `vehicleskill.dbss` path next to a file in the same folder."""
    folder = internal_path.rsplit("/", 1)[0]
    return f"{folder}/{VEHICLE_SKILL_FILE}"
