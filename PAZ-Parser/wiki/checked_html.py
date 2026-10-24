"""The Checked versions panel under a doc's layout timeline: every client the doc check read, by region.

The doc check has no region yet, so every client lists under NA / EU / OC, the
first region, and the others list none. A chip's tooltip names the client's
result; clicking a chip with a layout shows that layout. static/doc.js opens
the panel, switches the region, filters the chips and remembers the open
state and region per viewer.
"""
from __future__ import annotations

from collections.abc import Sequence
from html import escape

from format_docs.versions import ClientCheck

# (key, name) per region, in the order of the region picker.
REGIONS: tuple[tuple[str, str], ...] = (
    ("naeu", "NA / EU / OC"),
    ("kr", "Korea"),
    ("jp", "Japan"),
    ("tw", "Taiwan / Hong Kong / Macau"),
    ("mena", "Turkey / MENA"),
    ("ru", "Russian-speaking Region"),
    ("sa", "South America"),
    ("sea", "Asia (TH/SEA)"),
)
CHECKED_REGION = "naeu"

_CHECK_ICON = (
    '<svg class="cv-icon" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5"/>'
    '<path d="M5.2 8.2l1.9 1.9 3.7-3.9"/></svg>'
)
_CHEVRON = '<svg class="cv-chevron" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6l4 4 4-4"/></svg>'


def checked_panel(clients: Sequence[ClientCheck]) -> str:
    """The panel for `clients`, newest first; empty when the doc check read no client."""
    if not clients:
        return ""
    checks = sorted(clients, key=lambda check: check.client, reverse=True)
    options = "".join(
        f'<option value="{key}"{" selected" if key == CHECKED_REGION else ""}>{escape(name)}</option>' for key, name in REGIONS
    )
    regions = "".join(_region(key, name, checks if key == CHECKED_REGION else ()) for key, name in REGIONS)
    total = len(checks)
    return (
        '<div class="cv" id="checkedVersions"><div class="cv-head">'
        f'<span class="cv-title">{_CHECK_ICON}Checked versions<span class="cv-count" id="cvCount">{total}</span></span>'
        f'<select class="cv-select" id="cvRegion" aria-label="Region">{options}</select>'
        '<button type="button" class="cv-toggle" id="cvToggle" aria-expanded="false" aria-controls="cvBody">'
        f'{_CHEVRON}<span id="cvToggleText">View</span></button></div>'
        '<div class="cv-body" id="cvBody" hidden>'
        '<label class="input-box" for="cvSearch"><span aria-hidden="true">⌕</span>'
        '<input id="cvSearch" type="search" placeholder="Search client version" inputmode="numeric" '
        'autocomplete="off" spellcheck="false"></label>'
        f'{regions}<p class="cv-empty" id="cvEmpty" hidden></p>'
        f'<p class="cv-foot" id="cvShown" aria-live="polite">Showing {total} of {total} versions</p></div></div>'
    )


def _region(key: str, name: str, checks: Sequence[ClientCheck]) -> str:
    hidden = "" if key == CHECKED_REGION else " hidden"
    chips = "".join(_chip(check) for check in checks)
    return f'<ul class="cv-grid" data-region="{key}" data-name="{escape(name)}" aria-label="{escape(name)} clients"{hidden}>{chips}</ul>'


def _chip(check: ClientCheck) -> str:
    """A client; a chip with a layout is a button that shows it, the other two only inform."""
    title = escape(check.result)
    if check.layout is not None:
        return (
            f'<li><button type="button" class="cv-chip" data-layout="{check.layout}" title="{title}" '
            f'aria-label="Client {check.client}, show layout {check.layout}">{check.client}</button></li>'
        )
    state = "nolayout" if check.has_file else "absent"
    return f'<li><span class="cv-chip {state}" title="{title}">{check.client}</span></li>'
