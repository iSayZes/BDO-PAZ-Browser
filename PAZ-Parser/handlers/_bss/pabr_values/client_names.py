"""Cell text of the client, sound and web option tables (`client_tables.py`)."""

from __future__ import annotations


# `real_rgb` of a device with no colour (leddevice_bss.md, Row).
NO_RGB = -1
_EMPTY = "-"


def rgb_text(real_rgb: int) -> str:
    """A `0xRRGGBB` colour as `#RRGGBB`; the empty mark for `NO_RGB`."""
    if real_rgb == NO_RGB:
        return _EMPTY
    return f"#{real_rgb:06X}"
