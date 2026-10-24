"""Cell text of the ocean siege tables in `oceansiege_tables.py`."""

from __future__ import annotations

from _bss.regioninfo.parser import NODE_WAR_DAY_NAMES


_LIST_SEPARATOR = ", "


def siege_day_name(day: int) -> str:
    """The `CppEnums.VillageSiegeType` name of a day (`0` Sunday), or the bare value outside it."""
    return NODE_WAR_DAY_NAMES[day] if 0 <= day < len(NODE_WAR_DAY_NAMES) else str(day)


def siege_days_text(days: list[int]) -> str:
    """`Sunday, Monday, ...`: the name of each day in a list, in list order."""
    return _LIST_SEPARATOR.join(siege_day_name(day) for day in days)
