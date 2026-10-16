"""Territory and nation names, shared by the tables that link a territory.

LOC type 12 is keyed by the `territoryinfo.bss` territory key: str_id4 1 holds
the territory name, 0 the nation or realm. `2` is Calpheon, `4` Valencia.
"""

from __future__ import annotations

from _common.loc import loc_text

LOC_TERRITORY = 12
_TERRITORY_NAME = 1
_NATION_NAME = 0


def territory_name(territory_key: int) -> str:
    """Name of a territory in the loaded language, or '' when LOC has none."""
    return loc_text(LOC_TERRITORY, territory_key, _TERRITORY_NAME)


def nation_name(territory_key: int) -> str:
    """Name of the territory's nation or realm, or '' when LOC has none."""
    return loc_text(LOC_TERRITORY, territory_key, _NATION_NAME)
