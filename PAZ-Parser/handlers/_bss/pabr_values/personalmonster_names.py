"""Cell text of the Dark Rift world map table (`personalmonster_tables.py`)."""

from __future__ import annotations

from _common.binary import whole_float


def icon_size_text(size: list[float]) -> str:
    """A width and height as `119 x 119`."""
    return " x ".join(str(whole_float(value)) for value in size)


def icon_region_text(region: list[float]) -> str:
    """An icon sheet region `x1, y1, x2, y2` in pixels: `1, 1, 120, 120`."""
    return ", ".join(str(whole_float(value)) for value in region)
