"""Class names of `pcgrowth.dbss` and `pcgrowthsimply.bss`."""

from __future__ import annotations

from _common.class_type import class_name


def class_display_name(class_type: int, name_kr: str) -> str:
    """LOC type 21 name of a class type, else the Korean name the table stores."""
    name = class_name(class_type)
    # class_name() falls back to the number when LOC has no name.
    return name_kr if name == str(class_type) else name
