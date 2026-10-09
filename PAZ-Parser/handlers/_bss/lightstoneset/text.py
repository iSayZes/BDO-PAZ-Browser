"""Lightstone set name and effect lines, from LOC type 113 by set ID.

The text is the coloured name in brackets on the first line, then one effect
per line (`[Well-prepared]`, `Combat EXP +50%`, ...). The Korean row text of
`lightstoneset.bss` is its source and stands in when LOC has no row.
"""

from __future__ import annotations

from typing import NamedTuple

from _common.loc import loc_tagged
from _common.pa_text import strip_pa_tags

LOC_LIGHTSTONE_SET = 113


class SetText(NamedTuple):
    """The tagged name line and the tagged effect lines of one set."""

    name: str
    effects: list[str]


def split_set_text(text: str) -> SetText:
    """The first line as the name, every further non-blank line as one effect."""
    name, *effects = text.strip().split("\n")
    return SetText(name.strip(), [line.strip() for line in effects if line.strip()])


def set_text(set_id: int, text_kr: str) -> SetText:
    """The set's LOC type 113 text in the user's language, else its Korean text."""
    tagged = loc_tagged(LOC_LIGHTSTONE_SET, set_id)
    return split_set_text(tagged if strip_pa_tags(tagged).strip() else text_kr)
