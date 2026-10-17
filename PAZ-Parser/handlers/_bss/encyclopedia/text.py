"""Fishing Encyclopedia descriptions from LOC type 30, by entry key.

`str_id1` is the `encyclopedia.bss` key and `str_id4` 0 the description, the
translation of the row's inline Korean text.
"""

from __future__ import annotations

from _common.loc import loc_tagged

LOC_ENCYCLOPEDIA = 30
_DESCRIPTION_FIELD = 0


def entry_description(key: int) -> str:
    """The description of one entry, or '' when LOC has none or is not loaded."""
    return loc_tagged(LOC_ENCYCLOPEDIA, key, _DESCRIPTION_FIELD)
