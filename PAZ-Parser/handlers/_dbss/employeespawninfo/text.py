"""Display text of a sailor row: its name, lines, hire item and towns.

LOC type 70 holds each sailor's two lines, keyed by character key: `str_id4`
0 when the sailor agrees to be hired, 1 when it turns the player down. The
inline Korean lines of the row stand in when LOC has none.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence

from _common.character import character_name, character_title
from _common.item_key import item_key_text_tagged
from _common.loc import loc_tagged
from _common.pa_text import pa_fields
from _common.town import town_name
from _dbss.employeespawnposition.parser import parse_employeespawnposition_records
from .parser import parse_employeespawninfo_records

_LOC_SAILOR_LINE = 70
_ACCEPT_ID4 = 0
_REFUSE_ID4 = 1


def sailor_name(character_key: int) -> str:
    """`Sailor <Ambitious>`, as the name plate reads; '' when LOC has neither part."""
    parts = (character_name(character_key), character_title(character_key))
    return " ".join(part for part in parts if part)


def sailors_by_spawn_position(info_data: bytes, info_offset_data: bytes) -> dict[int, list[str]]:
    """Spawn position key -> the sailors that can appear on it, in file order.

    A sailor without a LOC name shows as its character key.
    """
    sailors: dict[int, list[str]] = {}
    for record in parse_employeespawninfo_records(info_data, info_offset_data):
        name = sailor_name(record["character_key"]) or str(record["character_key"])
        for key in record["spawn_position_keys"]:
            sailors.setdefault(key, []).append(name)
    return sailors


def sailor_text_fields(record: dict) -> dict[str, str]:
    """`accept_text` and `refuse_text` in the loaded LOC language, else the inline Korean, with tagged copies."""
    character_key = record["character_key"]
    accept = loc_tagged(_LOC_SAILOR_LINE, character_key, _ACCEPT_ID4) or record["accept_text_ko"]
    refuse = loc_tagged(_LOC_SAILOR_LINE, character_key, _REFUSE_ID4) or record["refuse_text_ko"]
    return {**pa_fields("accept_text", accept), **pa_fields("refuse_text", refuse)}


def hire_item_fields(item_key: int) -> dict[str, str]:
    """`hire_item`: the item name (its ID when LOC has none), with a grade-coloured copy."""
    return pa_fields("hire_item", item_key_text_tagged(item_key))


def spawn_towns(
    spawn_position_data: bytes | None,
    spawn_position_offset_data: bytes | None,
) -> Callable[[Sequence[int]], list[str]]:
    """A function from spawn position keys to the distinct towns they lie in, in key order.

    Without both `employeespawnposition.dbss` files it returns no towns.
    """
    region_of: dict[int, int] = {}
    if spawn_position_data is not None and spawn_position_offset_data is not None:
        region_of = {
            row["spawn_position_key"]: row["region_key"]
            for row in parse_employeespawnposition_records(spawn_position_data, spawn_position_offset_data)
        }

    def towns(spawn_position_keys: Sequence[int]) -> list[str]:
        regions = [region_of[key] for key in spawn_position_keys if key in region_of]
        return [town_name(region) or str(region) for region in dict.fromkeys(regions)]

    return towns
