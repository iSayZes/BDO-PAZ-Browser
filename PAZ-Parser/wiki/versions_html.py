"""The Versions card of a doc page, from the tables the doc check writes into `## Versions`."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from html import escape

from format_docs.versions import VersionRow, clients_text, read_rows


@dataclass(frozen=True)
class LayoutVersions:
    """The clients one layout fits and its bytes over every file, from the newest client checked."""

    layout: int
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
        first = own[0]
        found.append(LayoutVersions(
            layout, clients_text(first, newest_layout), max(row.checked for row in own),
            sum(row.known for row in own), sum(row.unknown for row in own), own,
        ))
    return tuple(found)


def versions_card(versions: Sequence[LayoutVersions], newest_layout: int) -> str:
    summaries = "".join(_summary(version, version.layout == newest_layout) for version in versions)
    rows = "".join(_table_row(version, row, newest_layout) for version in versions for row in version.rows)
    table = (
        '<div class="table-wrap"><table class="data-table"><thead><tr><th>Layout</th><th>Clients</th><th>File</th>'
        '<th class="num">Bytes</th><th>Records</th><th class="num">Row bytes</th><th class="num">Known</th>'
        f"</tr></thead><tbody>{rows}</tbody></table></div>"
    )
    return (
        '<section class="card" aria-labelledby="versions"><div class="card-head"><h2 id="versions">Versions</h2></div>'
        f'<div class="card-body ver-list">{summaries}{table}</div></section>'
    )


def _summary(version: LayoutVersions, is_current: bool) -> str:
    total = version.known + version.unknown
    current = '<span class="pill accent">Current</span>' if is_current else ""
    return (
        f'<div class="ver{" current" if is_current else ""}"><div class="ver-head">'
        f'<span class="ver-name">Layout {version.layout}</span>{current}'
        f'<span class="ver-clients">client {escape(version.clients)}, sizes from client {version.checked}</span></div>'
        f"{_bar(version.known, version.unknown)}"
        '<div class="cov-legend">'
        f'<span><i class="dot known"></i>Known <b>{version.known:,} B</b> {_percent(version.known, total)}</span>'
        f'<span><i class="dot unknown"></i>Unknown <b>{version.unknown:,} B</b> {_percent(version.unknown, total)}</span>'
        "</div></div>"
    )


def _table_row(version: LayoutVersions, row: VersionRow, newest_layout: int) -> str:
    pill = '<span class="pill accent row-pill">Current</span>' if version.layout == newest_layout else ""
    return (
        f"<tr><td>Layout {row.layout}{pill}</td><td class=\"mono\">{escape(version.clients)}</td>"
        f'<td class="mono">{escape(row.file)}</td><td class="num">{row.size:,}</td><td>{escape(row.records)}</td>'
        f'<td class="num">{escape(row.row_bytes)}</td><td class="num">{_percent(row.known, row.size)}</td></tr>'
    )


def _bar(known: int, unknown: int) -> str:
    total = known + unknown or 1
    return (
        f'<div class="covbar" aria-hidden="true"><span class="seg known" style="width:{known / total * 100:.2f}%"></span>'
        f'<span class="seg unknown" style="width:{unknown / total * 100:.2f}%"></span></div>'
    )


def _percent(part: int, whole: int) -> str:
    return f"{100 * part / whole:.1f}%" if whole else "-"
