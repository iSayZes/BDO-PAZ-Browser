"""The Versions card of a doc page, from the tables the doc check writes into `## Versions`.

The layout timeline comes first, then a known/unknown bar per layout; the
bar of the layout on show is highlighted.
"""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, replace
from html import escape

from format_docs.versions import ClientCheck, VersionRow, clients_text, read_rows

from .timeline_html import timeline
from .timeline_model import TimelineLayout


@dataclass(frozen=True)
class LayoutVersions:
    """The clients one layout fits and its bytes over every file, from the newest client checked."""

    layout: int
    first: int
    clients: str
    checked: int
    known: int
    unknown: int
    rows: tuple[VersionRow, ...]


def layout_versions(text: str, newest_layout: int) -> tuple[LayoutVersions, ...]:
    """Per layout with a Versions row, newest first."""
    rows = read_rows(text)
    found: list[LayoutVersions] = []
    for layout in sorted({row.layout for row in rows}, reverse=True):
        own = tuple(row for row in rows if row.layout == layout)
        checked = max(row.checked for row in own)
        first = min(row.first for row in own)
        # The range over every file of the layout, so a file added later does not narrow it.
        span = replace(own[0], first=first, checked=checked)
        found.append(LayoutVersions(
            layout, first, clients_text(span, newest_layout), checked,
            sum(row.known for row in own), sum(row.unknown for row in own), own,
        ))
    return tuple(found)


def timeline_layouts(numbers: Sequence[int], versions: Sequence[LayoutVersions]) -> tuple[TimelineLayout, ...]:
    """Every layout of the doc (newest first) with its clients; a layout without a Versions row has none."""
    by_layout = {version.layout: version for version in versions}
    newest = max(numbers)
    layouts: list[TimelineLayout] = []
    for number in numbers:
        version = by_layout.get(number)
        if version is None:
            layouts.append(TimelineLayout(number, None, None, False, None))
            continue
        is_open = number == newest
        layouts.append(TimelineLayout(number, version.first, None if is_open else version.checked, is_open, version.checked))
    return tuple(layouts)


def versions_card(
    versions: Sequence[LayoutVersions], layouts: Sequence[TimelineLayout], clients: Sequence[ClientCheck], axis: Sequence[int]
) -> str:
    shown = layouts[0].number
    summaries = "".join(_summary(version, version.layout == shown) for version in versions)
    return (
        '<section class="card" aria-labelledby="versions"><div class="card-head"><h2 id="versions">Versions</h2></div>'
        f'<div class="card-body ver-list">{timeline(layouts, clients, axis, shown)}{summaries}</div></section>'
    )


def _summary(version: LayoutVersions, is_shown: bool) -> str:
    total = version.known + version.unknown
    return (
        f'<div class="ver{" sel" if is_shown else ""}" data-layout="{version.layout}"><div class="ver-head">'
        f'<span class="ver-name">Layout {version.layout}</span>'
        f'<span class="ver-clients">client {escape(version.clients)}, sizes from client {version.checked}</span></div>'
        f"{_bar(version.known, version.unknown)}"
        '<div class="cov-legend">'
        f'<span><i class="dot known"></i>Known <b>{version.known:,} B</b> {_percent(version.known, total)}</span>'
        f'<span><i class="dot unknown"></i>Unknown <b>{version.unknown:,} B</b> {_percent(version.unknown, total)}</span>'
        "</div></div>"
    )


def _bar(known: int, unknown: int) -> str:
    total = known + unknown or 1
    return (
        f'<div class="covbar" aria-hidden="true"><span class="seg known" style="width:{known / total * 100:.2f}%"></span>'
        f'<span class="seg unknown" style="width:{unknown / total * 100:.2f}%"></span></div>'
    )


def _percent(part: int, whole: int) -> str:
    return f"{100 * part / whole:.1f}%" if whole else "-"
