"""Drop item window tags drawn as the window draws them.

Each tag is a pill: the `Combine_Etc_DropItem_Tag_BG` texture (white at alpha
51 in `combine/etc/combine_etc_dropitem.dds`) tinted with the tag's
`texture_color`, and its name in `font_color` (`tagControl:SetColor` /
`SetFontColor` in the window Lua). See the `dropuitaginfo.bss` section of
docs/file-formats/dropuihuntinggroundinfo_bss.md.
"""

from __future__ import annotations

from collections.abc import Sequence

from _common.html import e, hidden_slice, html_list_cell
from _common.pa_text import argb_css
from .parser import TagColors

# The alpha of the white tag texture the game tints, as a share of opaque.
_TAG_TEXTURE_ALPHA = 51 / 255
_CHIP_SEPARATOR = " "
_EMPTY = "-"


def tag_chip(name: str, colors: TagColors | None) -> str:
    """One tag in its colours; the plain name when `dropuitaginfo.bss` has none."""
    if colors is None:
        return e(name)
    style = f"background: {argb_css(colors.texture, _TAG_TEXTURE_ALPHA)}; color: {argb_css(colors.font)}"
    return f'<span class="tag-chip" style="{style}">{e(name)}</span>'


def tag_chips_cell(names: Sequence[str], colors: Sequence[TagColors | None], max_items: int) -> str:
    """The tags in their colours, space-separated as in game, or a dash."""
    chips = [tag_chip(name, tag_colors) for name, tag_colors in zip(names, colors)][:max_items]
    hidden = hidden_slice(names, max_items)
    return html_list_cell(chips, len(names) - max_items, hidden, _CHIP_SEPARATOR) or _EMPTY
