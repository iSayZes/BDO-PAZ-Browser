"""The text of a `tooltiptable.dbss` line in the user's language.

LOC type 46 holds each line under `(key_hash, 0, tooltip_type, 0)`. Kept out
of `handler.py` so tests can import it without loading the handler registry.
"""

from __future__ import annotations

from _common.loc import loc_lookup, resolve_text_binds

LOC_TOOLTIP = 46


def tooltip_text(key_hash: int, tooltip_type: int, format_kr: str) -> str:
    """The LOC type 46 line with its PA tags, else the Korean text with its TextBinds filled."""
    localized = loc_lookup(LOC_TOOLTIP, key_hash, 0, tooltip_type, 0).strip()
    return localized or resolve_text_binds(format_kr).strip()
