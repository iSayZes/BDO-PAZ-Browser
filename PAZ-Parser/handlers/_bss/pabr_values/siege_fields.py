"""Fields the land and ocean siege tables share (`siege_tables.py`, `oceansiege_tables.py`)."""

from __future__ import annotations

from _common.rate import rate_percent
from _common.territory import territory_name
from .layout import NameLookup, ValueField, unknown_fields


# CppEnums.VillageSiegeType 0 to 5: the days getLimitMemberCount(day) takes,
# one u16 each (oceansiegeterritoryoption_bss.md, Field Names).
LIMIT_MEMBER_DAYS: tuple[str, ...] = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday")
# Where the two unnamed f32 (the AP+DP pair) and the three u32 after
# dr_rate_limit sit, from the start of the limit block.
_AP_DP_PAIR_AT = (0x0C, 0x10)
_AFTER_DR_RATE_AT = (0x20, 0x24, 0x28)


def territory_key_field(name: str, column: str) -> ValueField:
    """A u16 territory key and its LOC type 12 name, stored as `<role>_name`."""
    name_field = name.replace("_key", "_name")
    return ValueField(name, "H", f"{column}Key", NameLookup(name_field, column, territory_name))


def limit_member_count_fields() -> tuple[ValueField, ...]:
    """The six `limit_member_count_<day>` u16, Sunday to Friday."""
    return tuple(
        ValueField(f"limit_member_count_{day}", "H", f"limitMemberCount{day.capitalize()}") for day in LIMIT_MEMBER_DAYS
    )


def stat_limit_fields(start: int) -> tuple[ValueField, ...]:
    """The limit block from `start` (siegeterritoryoptionstaticstatus_bss.md, Stat Limits).

    The unnamed fields take their offsets from `start`, so each table keeps
    its doc's `unknown_<offset>` names.
    """
    return (
        ValueField("hp_limit", "f", "hpLimit"),
        ValueField("ap_limit", "f", "apLimit"),
        ValueField("dr_limit", "f", "drLimit"),
        *unknown_fields(*((start + offset, "f") for offset in _AP_DP_PAIR_AT)),
        ValueField("accuracy_limit", "f", "accuracyLimit"),
        ValueField("evasion_limit", "f", "evasionLimit"),
        ValueField("dr_rate_limit", "I", "drRateLimit", display=rate_percent),
        *unknown_fields(*((start + offset, "I") for offset in _AFTER_DR_RATE_AT)),
    )
