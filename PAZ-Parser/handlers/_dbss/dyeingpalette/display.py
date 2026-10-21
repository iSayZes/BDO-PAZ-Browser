"""Palette names and colours as the dye tables show them.

`itempalette.dbss` shows the colour each dye item applies and
`dyeingpalette.dbss` every colour of a palette; both draw a colour as a
swatch and its `#RRGGBB` text, and a palette by the name of its tab in the
dye window.
"""

from __future__ import annotations

from collections.abc import Mapping

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.html import e
from _common.string_hash import key_hash
from .parser import parse_dyeingpalette_rows

_EMPTY = "-"
# The dye window's tab of palette type N is `LUA_PALETTE_TAB_MATERIAL_{N - 1}`
# (`panel_window_dyeingpalette_renew.luac`): Basic Dye for type 1, then the
# seven town dyes. Type 100 (lantern colours) has no tab.
_TAB_KEY = "LUA_PALETTE_TAB_MATERIAL_{index}"
_TABBED_TYPES = range(1, 9)


def palette_name(palette_type: int) -> str:
    """`Basic Dye`, `Olvian Dye` ...: the dye window's tab of a palette type, or ''."""
    if palette_type not in _TABBED_TYPES:
        return ""
    return ui_hash_text(GAME_SHEET, key_hash(_TAB_KEY.format(index=palette_type - 1)))


def color_hex(color: Mapping[str, object]) -> str:
    """`#867E7E` from a colour's `color_r`, `color_g` and `color_b`."""
    return f"#{color['color_r']:02X}{color['color_g']:02X}{color['color_b']:02X}"


def palette_color_hexes(data: bytes | None) -> dict[tuple[int, int], str]:
    """`(palette_type, palette_index) -> #RRGGBB` of every colour, empty without the file.

    Raises ValueError when `dyeingpalette.dbss` does not parse.
    """
    if data is None:
        return {}
    return {
        (row["palette_type"], index): color_hex(color)
        for row in parse_dyeingpalette_rows(data)
        for index, color in enumerate(row["colors"])
    }


def color_cell(hex_text: str | None) -> str:
    """A swatch of the colour and its `#RRGGBB` text, or a dash without one."""
    if not hex_text:
        return e(_EMPTY)
    return f'<span class="color-swatch" style="background:{e(hex_text)}"></span>{e(hex_text)}'
