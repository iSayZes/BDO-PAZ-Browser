"""Game text tags in LOC and inline text, as plain text or as coloured HTML.

Two tag kinds occur: `<PAColor0xAARRGGBB>` opens a colour and `<PAOldColor>`
goes back to the previous one, so colours nest as a stack. A key binding,
`{KeyBind:NAME}` or `{StringTableBind(KeyBind:NAME)}`, names a player action
(`Attack2`) whose key the game fills from the player's settings; it shows as
the action name, `[Attack2]` in plain text and a key chip in HTML.

- `strip_pa_tags()` returns plain text, for records, search, sort and CSV.
- `pa_html()` returns safe HTML, for render time only. With the app's "Show
  game text tags" setting on (`set_show_pa_tags()`, off by default) it also
  shows every tag and key binding as dimmed text.
- `argb_css()` turns one ARGB value into a CSS colour, also for colours stored
  as u32s rather than in tag text (`dropuitaginfo.bss`).
- `pa_fields()` / `pa_list_fields()` / `pa_cell()` / `pa_line_cell()` are the record side: a plain field for search,
  sort and CSV next to its tagged copy (`_description_pa`) for the cell. See
  "Display-Only Fields" in docs/handler.md.

`_common/pa_color.py` is a different job: it finds colour markers in raw
UTF-16 bytes for `title.dbss`.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

from _common.html import e, hidden_slice, html_list_cell

# Every `<PA...>` tag and key binding; both functions split text on this one
# pattern. Group 1 or 2 is the action name of a key binding.
_TOKEN_RE = re.compile(
    r"<PA[^>]+>|\{KeyBind:([A-Za-z0-9_]+)\}|\{StringTableBind\(KeyBind:([A-Za-z0-9_]+)\)\}"
)
_TOKEN_MARKERS = ("<PA", "KeyBind:")
# The tag body after "<PA", with the colour as exactly eight hex digits.
_COLOR_BODY_RE = re.compile(r"Color0x([0-9A-Fa-f]{8})")
_COLOR_PREFIX = "<PAColor"
_OLD_COLOR_TAG = "<PAOldColor>"

_MAX_ARGB = 0xFFFFFFFF
_ALPHA_MAX = 255
_SPAN_CLOSE = "</span>"
_EMPTY = "-"
_ELLIPSIS = "…"
# Visible characters a one-line cell keeps of a long text.
LINE_PREVIEW_CHARS = 120

# The "Show game text tags" setting, applied by the app and the CLI at start
# and on save, like the LOC language.
_show_pa_tags = False


def set_show_pa_tags(show: bool) -> None:
    """Turn the tags `pa_html()` shows as text on or off, for every table."""
    global _show_pa_tags
    _show_pa_tags = show


def strip_pa_tags(raw: str) -> str:
    """`raw` with every `<PA...>` tag removed and each key binding as `[NAME]`.
    Whitespace is kept."""
    if not any(marker in raw for marker in _TOKEN_MARKERS):
        return raw
    return _TOKEN_RE.sub(_visible_text, raw)


def _key_name(match: re.Match[str]) -> str | None:
    """The action name of a key binding match, or None for a `<PA...>` tag."""
    return match.group(1) or match.group(2)


def _visible_text(match: re.Match[str]) -> str:
    """What a token reads as in plain text: nothing for a tag, `[NAME]` for a key binding."""
    name = _key_name(match)
    return "" if name is None else f"[{name}]"


def argb_css(argb: int, alpha_scale: float = 1.0) -> str:
    """CSS colour of an ARGB value: `0xffe9bd23` -> `rgba(233, 189, 35, 1)`.

    Alpha is kept, so the few non-opaque game colours draw partly transparent
    as in game. `alpha_scale` multiplies it, for a colour the game uses to tint
    a translucent texture. Raises ValueError outside 0 to 0xFFFFFFFF.
    """
    if isinstance(argb, bool) or not 0 <= argb <= _MAX_ARGB:
        raise ValueError(f"ARGB value out of range: {argb!r}")
    alpha = (argb >> 24) & 0xFF
    red = (argb >> 16) & 0xFF
    green = (argb >> 8) & 0xFF
    blue = argb & 0xFF
    return f"rgba({red}, {green}, {blue}, {alpha / _ALPHA_MAX * alpha_scale:.3g})"


def pa_html(raw: str, *, colors: bool = True, max_chars: int | None = None) -> str:
    """`raw` as escaped HTML, each colour drawn as a span.

    Colours nest; a stray `<PAOldColor>` is dropped and colours left open are
    closed at the end. A `<PAColor...>` tag with a malformed value still opens
    a level (an unstyled span), so its `<PAOldColor>` closes it and not the
    colour around it. Other `<PA...>` tags are dropped and newlines are left
    alone. A key binding becomes a `key-bind` chip with the action name.

    `max_chars` cuts the visible text like `truncate()`: past that many
    characters (tags not counted) it ends in an ellipsis.

    `colors=False` drops the colours too, giving `e(strip_pa_tags(raw))` with
    the tag setting off, so a cell can turn colour off without changing its
    call. With the setting on, each tag stays visible as a dimmed `pa-tag`
    span outside the colour it opens or closes.
    """
    cut = _cut_visible(raw, max_chars)
    body = raw if cut is None else cut
    parts: list[str] = []
    open_spans = 0
    pos = 0
    for match in _TOKEN_RE.finditer(body):
        parts.append(e(body[pos:match.start()]))
        pos = match.end()
        tag = match.group()
        shown_tag = f'<span class="pa-tag">{e(tag)}</span>' if _show_pa_tags else ""
        key_name = _key_name(match)
        if key_name is not None:
            parts.append(shown_tag + (_key_chip(key_name) if colors else e(_visible_text(match))))
        elif not colors:
            parts.append(shown_tag)
        elif tag.startswith(_COLOR_PREFIX):
            parts.append(shown_tag + _color_open(tag))
            open_spans += 1
        elif tag == _OLD_COLOR_TAG and open_spans:
            parts.append(_SPAN_CLOSE + shown_tag)
            open_spans -= 1
        else:
            parts.append(shown_tag)
    ellipsis = "" if cut is None else _ELLIPSIS
    return "".join(parts) + e(body[pos:]) + ellipsis + _SPAN_CLOSE * open_spans


def _cut_visible(raw: str, max_chars: int | None) -> str | None:
    """`raw` cut after `max_chars` visible characters (tags not counted, a key
    binding counted as `[NAME]` and kept whole or cut before), or None when it fits."""
    if max_chars is None or len(strip_pa_tags(raw)) <= max_chars:
        return None
    budget = max_chars
    pos = 0
    for match in _TOKEN_RE.finditer(raw):
        text_len = match.start() - pos
        if text_len >= budget:
            break
        budget -= text_len
        width = len(_visible_text(match))
        if width > budget:
            return raw[:match.start()]
        budget -= width
        pos = match.end()
    return raw[:pos + budget]


def pa_key(field: str) -> str:
    """Record key of the tagged copy of `field`: `description` -> `_description_pa`."""
    return f"_{field}_pa"


def pa_fields(field: str, raw: str) -> dict[str, str]:
    """`field` as plain text and its tagged copy for the cell, to merge into a record."""
    return {field: strip_pa_tags(raw).strip(), pa_key(field): raw}


def pa_list_fields(field: str, raws: Sequence[str]) -> dict[str, list[str]]:
    """`pa_fields` for a list: the plain texts under `field`, the tagged ones under `pa_key(field)`."""
    return {field: [strip_pa_tags(raw).strip() for raw in raws], pa_key(field): list(raws)}


def pa_cell(record: dict, field: str, max_chars: int | None = None) -> str:
    """The cell of a `pa_fields` text in its game colours, or a dash when blank.

    `max_chars` cuts long text, see `pa_html`.
    """
    return pa_html(record[pa_key(field)], max_chars=max_chars) if record[field] else _EMPTY


def pa_line_cell(record: dict, field: str, max_chars: int = LINE_PREVIEW_CHARS) -> str:
    """`pa_cell` on one line for long text: line breaks and runs of spaces
    become one space, then the text is cut after `max_chars`."""
    if not record[field]:
        return _EMPTY
    return pa_html(" ".join(record[pa_key(field)].split()), max_chars=max_chars)


def pa_list_cell(raws: Sequence[str], max_items: int) -> str:
    """Tagged texts in their game colours, the hidden ones named on hover, or a dash."""
    shown = [pa_html(raw) for raw in raws[:max_items]]
    hidden = [strip_pa_tags(raw).strip() for raw in hidden_slice(raws, max_items)]
    return html_list_cell(shown, len(raws) - max_items, hidden) or _EMPTY


def _key_chip(name: str) -> str:
    return f'<kbd class="key-bind">{e(name)}</kbd>'


def _color_open(tag: str) -> str:
    """The opening span of a `<PAColor...>` tag; unstyled when its value is malformed."""
    match = _COLOR_BODY_RE.fullmatch(tag, len("<PA"), len(tag) - 1)
    if match is None:
        return '<span class="pa-color">'
    return f'<span class="pa-color" style="color: {argb_css(int(match.group(1), 16))}">'
