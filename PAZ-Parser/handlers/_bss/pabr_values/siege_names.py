"""Cell text of the land siege tables in `siege_tables.py`."""

from __future__ import annotations

from _common.territory import territory_name


_LIST_SEPARATOR = ", "
# siegeinfo.bss stores -1 where an area has no territory (its c8c8c8 row).
NO_TERRITORY = -1
_NO_TERRITORY_TEXT = "-"


def territory_text(territory_key: int) -> str:
    """`2 Calpheon`: a territory key and its LOC type 12 name; `-` for no territory."""
    if territory_key == NO_TERRITORY:
        return _NO_TERRITORY_TEXT
    name = territory_name(territory_key)
    return f"{territory_key} {name}" if name else str(territory_key)


def territories_text(territory_keys: list[int]) -> str:
    """`Balenos, Calpheon`: each territory's name in list order, or its key when LOC has none."""
    return _LIST_SEPARATOR.join(territory_name(key) or str(key) for key in territory_keys)
