"""Cell text of the PvP and matching tables in `pvp_tables.py`."""

from __future__ import annotations

from _common.instance_field import instance_field_name
from _common.skill import skill_name


def _value_and_name(value: int, name: str) -> str:
    return f"{value} {name}" if name else str(value)


def action_hash_text(action_hash: int) -> str:
    """An action name hash as `0x0E907704` (`ascii_key_hash("BS_START")`)."""
    return f"0x{action_hash:08X}"


def skill_text(skill_no: int) -> str:
    """`41292 <name>`: a skill number and its LOC type 10 or Korean name.

    A cell text, read when the page draws: the Korean names come from a
    lookup index the tests do not load.
    """
    return _value_and_name(skill_no, skill_name(skill_no))


def matching_condition_text(entry: list[int]) -> str:
    """An `[instance_field_key, min_ap, min_dp]` entry as `151 Atoraxion_Desert_EZ: 220 / 270`.

    The column label names the two numbers (AP / DP).
    """
    instance_field_key, min_ap, min_dp = entry
    field = _value_and_name(instance_field_key, instance_field_name(instance_field_key))
    return f"{field}: {min_ap} / {min_dp}"
