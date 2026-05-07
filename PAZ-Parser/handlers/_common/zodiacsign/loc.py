from __future__ import annotations

from _common.loc import loc_lookup, strip_pa_tags


def resolve_loc_type7(
    zodiac_ids: list[int],
) -> tuple[dict[int, str], dict[int, str]]:
    """Return (names, traits) keyed by zodiac_id from the loc index."""
    names:  dict[int, str] = {}
    traits: dict[int, str] = {}
    for zid in zodiac_ids:
        name  = loc_lookup(7, zid, 0, 0, 0)
        trait = loc_lookup(7, zid, 0, 0, 1)
        if name:
            names[zid]  = name
        if trait:
            traits[zid] = strip_pa_tags(trait)
    return names, traits
