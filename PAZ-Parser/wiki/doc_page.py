"""One wiki page per format doc.

A converted doc gets its Versions, Companion Files and Layouts cards; every
other section, and every section of a doc not converted yet, is a prose card.
"""
from __future__ import annotations

import json
import re
from html import escape

from .doc_source import DocSection, DocSource
from .layout_html import layouts_card
from .layout_view import layout_views
from .markdown_html import LinkMap, render_markdown, slug
from .page_shell import FORMATS_SCRIPT, STATIC_DIR, page

_HEAD_SECTIONS = ("Purpose",)
_CONVERTED_CARDS = ("Versions", "Companion Files")
_COUNTED_SECTIONS = ("Open Questions", "In-Game Checks")
_LAYOUT_SECTION = re.compile(r"^Layout \d+$")
_VERSIONS_EMPTY = (
    '<p class="muted">No client checked yet. The doc check writes the clients, file sizes and coverage of each '
    "layout here once it reads a PAZ folder.</p>"
)
_SIDEBAR = """<aside class="side" aria-label="Formats">
  <label class="input-box" for="fmtFilter"><span aria-hidden="true">⌕</span>
    <input id="fmtFilter" type="search" placeholder="Filter formats" autocomplete="off" spellcheck="false"></label>
  <span class="side-label">Formats · known share</span>
  <p class="side-legend"><span><span class="cnt q" aria-hidden="true">?</span> Open questions</span>
    <span><span class="cnt ig" aria-hidden="true">⌖</span> In-game checks</span></p>
  <ul class="fmt-list" id="fmtList"></ul>
  <p class="side-foot" id="fmtEmpty" hidden>No format matches.</p>
</aside>"""


def doc_page(doc: DocSource, links: LinkMap) -> str:
    views = layout_views(doc) if doc.is_converted else ()
    cards: list[str] = []
    if views:
        cards.append(f'<div class="row-2 cv">{_versions_card(doc, links)}{_section_card(doc.section("Companion Files"), links)}</div>')
        cards.append(layouts_card(views, links))
    else:
        cards.append(
            '<section class="card"><div class="card-body"><p class="muted">This doc is not in the layout format yet, '
            "so it shows as written and has no coverage.</p></div></section>"
        )
    cards.extend(_section_card(section, links) for section in doc.sections if _is_prose_card(section, doc.is_converted))
    main = (
        f'<main class="content" id="content">{_doc_head(doc, len(views), links)}{"".join(cards)}'
        f'<p class="foot">Built from <code>docs/file-formats/{escape(doc.path.name)}</code>.</p></main>'
    )
    body = f'<div class="shell">{_SIDEBAR}{main}</div>'
    current = f"var CURRENT_PAGE = {json.dumps(doc.page)};"
    scripts = (FORMATS_SCRIPT, f"{STATIC_DIR}/common.js", f"{STATIC_DIR}/doc.js")
    return page(f"{doc.name} · PAZ Format Docs", f" / <b>{escape(doc.name)}</b>", "doc-page", body, scripts, current)


def _doc_head(doc: DocSource, layout_count: int, links: LinkMap) -> str:
    purpose = doc.section("Purpose")
    lead = f'<div class="lead prose">{render_markdown(purpose.markdown, links)}</div>' if purpose else ""
    chips = [f'<span class="pill">{escape(doc.name.rsplit(".", 1)[-1])}</span>']
    if layout_count:
        chips.append(f'<span class="pill">{layout_count} layout{"s" if layout_count != 1 else ""}</span>')
        chips.append(f'<span class="pill accent">Current: Layout {layout_count}</span>')
    else:
        chips.append('<span class="pill">Not converted</span>')
    return (
        f'<section class="doc-head"><span class="eyebrow">docs/file-formats/{escape(doc.path.name)}</span>'
        f'<h1>{escape(doc.name)}</h1>{lead}<div class="chips">{"".join(chips)}</div></section>'
    )


def _versions_card(doc: DocSource, links: LinkMap) -> str:
    section = doc.section("Versions")
    content = render_markdown(section.markdown, links) if section else ""
    return (
        '<section class="card" aria-labelledby="versions"><div class="card-head"><h2 id="versions">Versions</h2></div>'
        f'<div class="card-body">{content or _VERSIONS_EMPTY}</div></section>'
    )


def _section_card(section: DocSection | None, links: LinkMap) -> str:
    if section is None:
        return ""
    heading_id = slug(section.title)
    pill = ""
    if section.title in _COUNTED_SECTIONS:
        count = sum(1 for line in section.markdown.splitlines() if line.startswith("### "))
        pill = f'<span class="pill">{count}</span>'
    return (
        f'<section class="card prose" aria-labelledby="{heading_id}"><div class="card-head">'
        f'<h2 id="{heading_id}">{escape(section.title)}</h2>{pill}</div>'
        f'<div class="card-body">{render_markdown(section.markdown, links)}</div></section>'
    )


def _is_prose_card(section: DocSection, is_converted: bool) -> bool:
    if section.title in _HEAD_SECTIONS:
        return False
    if is_converted:
        return section.title not in _CONVERTED_CARDS and not _LAYOUT_SECTION.match(section.title)
    return True
