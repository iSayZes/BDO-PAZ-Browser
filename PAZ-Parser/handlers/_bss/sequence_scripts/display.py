"""Plain-text cells the sequence and cutscene script views share."""

from __future__ import annotations

from collections.abc import Sequence


EMPTY = "-"


def position_text(position: Sequence[float]) -> str:
    """`4067, -6470, 69602`: a world position rounded to whole units."""
    return ", ".join(f"{value:.0f}" for value in position)


def contents_group_key(text: str) -> int | None:
    """The contents group key a trigger stores as decimal text (`2186`), or None when empty."""
    return int(text) if text.isdigit() else None


def radius_text(radius: float) -> str:
    """`2000` or `49.67`: a radius without trailing zeros."""
    return f"{radius:g}"
