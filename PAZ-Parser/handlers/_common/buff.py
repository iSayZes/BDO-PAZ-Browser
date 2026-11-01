"""Buff icon paths and buff text shared by the buff tables.

`buff.dbss` and `buffsimply.bss` store the same icon paths, and every table
that names a buff (`buff.dbss`, `buffsimply.bss`, the `skill.dbss` and
`itemenchant.dbss` Buffs columns) reads its English text from LOC type 5,
keyed by buff ID. See docs/file-formats/dbss/buff_dbss.md.
"""

from __future__ import annotations

from collections.abc import Sequence

from _common.html import hidden_slice, icon_html_list_cell
from _common.icon_index import IconKind, clean_stored_icon_path, icon_path
from _common.loc import LOC_NULL, loc_lookup
from _common.pa_text import pa_html, strip_pa_tags
from _common.ui_texture import UI_TEXTURE_ICON_ROOT

LOC_BUFF_DESCRIPTION = 5

# Some records store this literal instead of leaving the path empty.
_ICON_PLACEHOLDER = "unknown"


def buff_icon_path(stored: str) -> str:
    """PAZ path for a stored buff icon, or an empty string when there is none."""
    path = clean_stored_icon_path(stored)
    if not path or path == _ICON_PLACEHOLDER:
        return ""
    # Stored paths start at "New_Icon/", which lives under ui_texture/icon/.
    return f"{UI_TEXTURE_ICON_ROOT}{path}"


def buff_loc_description(buff_id: int) -> str:
    """LOC type 5 text of a buff with PA tags intact, or '' on a miss or `<null>`."""
    text = loc_lookup(LOC_BUFF_DESCRIPTION, buff_id).strip()
    return "" if text == LOC_NULL else text


def _tagged_first_line(buff_id: int) -> str:
    """The first line of a buff's LOC type 5 text with its PA tags, or ''."""
    return buff_loc_description(buff_id).split("\n", 1)[0].strip()


def buff_first_line(buff_id: int) -> str:
    """The first line of a buff's LOC type 5 text without tags, or ''."""
    return strip_pa_tags(_tagged_first_line(buff_id)).strip()


def buff_label(buff_id: int) -> str:
    """Buff ID and the first line of its LOC type 5 text, for buff lists."""
    first_line = buff_first_line(buff_id)
    return f"{buff_id} {first_line}" if first_line else str(buff_id)


def buff_label_html(buff_id: int) -> str:
    """`buff_label` as HTML, the first line in its game colours."""
    tagged = _tagged_first_line(buff_id)
    if not strip_pa_tags(tagged).strip():
        return str(buff_id)
    return f"{buff_id} {pa_html(tagged)}"


def buff_list_cell(buff_ids: Sequence[int], max_items: int) -> str:
    """The first `max_items` buffs, each with its icon and coloured label, and a count of the rest."""
    shown = buff_ids[:max_items]
    entries = [(icon_path(IconKind.BUFF, buff_id), buff_label_html(buff_id)) for buff_id in shown]
    hidden = [buff_label(buff_id) for buff_id in hidden_slice(buff_ids, max_items)]
    return icon_html_list_cell(entries, len(buff_ids) - len(shown), hidden_names=hidden)
