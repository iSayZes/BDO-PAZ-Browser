"""Text helpers the Yar! table views share."""

from __future__ import annotations

from collections.abc import Iterable


def keys_text(keys: Iterable[int]) -> str:
    """Keys in list order as `1, 6, 12`, for list cells, search and export."""
    return ", ".join(str(key) for key in keys)
