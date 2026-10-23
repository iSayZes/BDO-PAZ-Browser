"""The layout timeline at the top of a doc's Versions card, from `timeline_model`.

A layout band is a button that shows its layout (static/doc.js); a No
documented layout or No file band is a plain bar whose tooltip names its
clients. Ticks mark live, the oldest client and every change. The
Checked versions panel under the timeline (`checked_html`) lists every
client the doc check read.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from html import escape

from format_docs.versions import ClientCheck

from .checked_html import checked_panel
from .timeline_model import LAYOUT, NO_FILE, NO_LAYOUT, UNDATED, Band, Timeline, TimelineLayout, build_timeline

# The year under a tick: the date of the official Steam depot manifest of that client.
CLIENT_DATES: Mapping[int, str] = {
    794: "2018-06-20", 1230: "2019-10-16", 1485: "2021-01-06", 1784: "2021-12-29",
    2107: "2023-01-16", 2519: "2024-05-22", 3002: "2025-08-21", 3251: "2026-03-19",
}
_BAND_GAP_PX = 1


def timeline(layouts: Sequence[TimelineLayout], clients: Sequence[ClientCheck], axis: Sequence[int], shown: int) -> str:
    """The timeline for `layouts` (newest first); `shown` is the layout selected at load."""
    model = build_timeline(layouts, clients, axis)
    by_number = {layout.number: layout for layout in layouts}
    bands = "".join(_band(band, by_number, shown) for band in model.bands)
    ticks = "".join(_tick(client, model) for client in model.ticks)
    selected = by_number[shown]
    return (
        '<div class="tl"><div class="tl-track" role="group" aria-label="Layouts by client">'
        f'<div class="tl-base"></div>{bands}{ticks}</div>'
        f'<p class="tl-read" aria-live="polite"><b id="tlReadName">Layout {selected.number}</b>: '
        f'<span id="tlReadText">{escape(_read_text(selected))}</span></p>{checked_panel(clients)}</div>'
    )


def _band(band: Band, layouts: Mapping[int, TimelineLayout], shown: int) -> str:
    style = (
        f"left:calc({band.left * 100:.3f}% + {_BAND_GAP_PX}px);"
        f"width:calc({(band.right - band.left) * 100:.3f}% - {2 * _BAND_GAP_PX}px)"
    )
    if band.kind == NO_LAYOUT:
        verb = "has" if len(band.clients) == 1 else "have"
        tip = f"{_client_list(band.clients).capitalize()} {verb} the file; no documented layout reads it."
        return _bar("nolayout", style, tip, "No documented layout")
    if band.kind == NO_FILE:
        return _bar("absent", style, f"Not in {_client_list(band.clients)}.", "No file")
    layout = layouts[band.layout or 0]
    is_shown = layout.number == shown
    cls = "tl-band" + (" undated" if band.kind == UNDATED else "") + (" sel" if is_shown else "")
    attrs = (
        f'class="{cls}" data-layout="{layout.number}" aria-pressed="{"true" if is_shown else "false"}" '
        f'aria-label="Layout {layout.number}, {escape(layout.clients_text)}" '
        f'data-pill="{escape(layout.pill)}" data-read="{escape(_read_text(layout))}"'
    )
    return f'<button type="button" {attrs} style="{style}"><span class="tl-band-label">Layout {layout.number}</span></button>'


def _bar(cls: str, style: str, tip: str, label: str) -> str:
    """A band that only informs: no button, its clients in the tooltip."""
    return f'<div class="tl-band {cls}" title="{escape(tip)}" style="{style}"><span class="tl-band-label">{escape(label)}</span></div>'


def _tick(client: int, model: Timeline) -> str:
    sub = "live" if client == model.axis[-1] else CLIENT_DATES.get(client, "")[:4]
    result = model.results.get(client)
    cls = "" if result is not None and result[0] == LAYOUT else " unchecked"
    # The end ticks sit on the track's edges, so their labels align inward instead of centring.
    if len(model.axis) > 1:
        cls += " start" if client == model.axis[-1] else " end" if client == model.axis[0] else ""
    return f'<span class="tl-tick{cls}" style="left:{model.at[client] * 100:.3f}%">{client}<small>{sub}</small></span>'


def _read_text(layout: TimelineLayout) -> str:
    sizes = f", sizes from client {layout.checked}" if layout.checked is not None else ""
    return f"{layout.clients_text}{sizes}."


def _client_list(clients: Sequence[int]) -> str:
    """`client 794`, `clients 1230 and 794`, `clients 3474, 3473 and 1784`."""
    names = [str(client) for client in clients]
    if len(names) == 1:
        return f"client {names[0]}"
    return f"clients {', '.join(names[:-1])} and {names[-1]}"
