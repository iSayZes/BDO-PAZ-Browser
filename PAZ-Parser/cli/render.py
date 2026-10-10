"""`browser.py --render <file> --page N > page.html`: one parsed page as HTML.

The page is the handler's `render_data_page()` output in file order, wrapped
with the app's stylesheets, so a handler's cells can be checked in a browser
without the GUI. Icons the GUI loads with JavaScript are inlined as data URLs.
"""
from __future__ import annotations

import argparse
import html
import re
from collections.abc import Callable
from pathlib import Path

from bdo_preview import PARSED_RECORDS_PER_PAGE

from _common.html import (
    PENDING_ICON_CELL_RE,
    PENDING_ICON_LABEL_RE,
    icon_cell,
    missing_icon_cell,
    resolved_icon_label_head,
)

from .errors import CliError
from .parsed_file import ParsedFile, load_parsed_file
from .session import open_session
from .stdio import error, progress, write_raw

_UI_DIR = Path(__file__).parent.parent / "ui"
_STYLE_ENTRY = _UI_DIR / "style.css"
_IMPORT_RE = re.compile(r'@import\s+url\("\./([^"]+)"\);')

# The app's page is a fixed, unscrollable window; a standalone page scrolls.
_PAGE_OVERRIDES = """
html, body { height: auto; overflow: auto; user-select: text; }
body { padding: 12px; }
.render-note { color: var(--color-text-3); font-size: 11px; margin-bottom: 8px; }
"""


def app_stylesheet() -> str:
    """Every CSS module `ui/style.css` imports, in its order."""
    names = _IMPORT_RE.findall(_STYLE_ENTRY.read_text(encoding="utf-8"))
    if not names:
        raise CliError(f"no @import rules found in {_STYLE_ENTRY}.")
    return "\n".join((_UI_DIR / name).read_text(encoding="utf-8") for name in names)


def inline_icons(body: str, icon_url: Callable[[str], str | None]) -> str:
    """Swap each pending icon cell for its image, or a dash when not shipped.

    A list entry keeps its label, markup included, and loses only the swatch
    when not shipped. `icon_url` returns a data URL for an icon path, or None
    when not shipped.
    """
    def replace_cell(match: re.Match[str]) -> str:
        path = html.unescape(match.group(1))
        url = icon_url(path)
        return icon_cell(path, url) if url else missing_icon_cell(path)

    def replace_label_head(match: re.Match[str]) -> str:
        title, path = (html.unescape(match.group(n)) for n in (1, 2))
        # The title is the path unless the handler gave the entry its own tooltip.
        tooltip = title if title != path else None
        return resolved_icon_label_head(path, tooltip, icon_url(path))

    body = PENDING_ICON_CELL_RE.sub(replace_cell, body)
    return PENDING_ICON_LABEL_RE.sub(replace_label_head, body)


def standalone_page(title: str, note: str, body: str, css: str) -> str:
    return (
        "<!doctype html>\n"
        '<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        f"<title>{html.escape(title)}</title>\n"
        f"<style>\n{css}\n{_PAGE_OVERRIDES}</style>\n"
        "</head>\n<body>\n"
        f'<div class="render-note">{html.escape(note)}</div>\n'
        f'<div id="preview-content">{body}</div>\n'
        "</body>\n</html>\n"
    )


def page_count(parsed: ParsedFile) -> int:
    count = parsed.handler.get_record_count(parsed.data, parsed.entry, parsed.companions)
    return max(1, -(-count // PARSED_RECORDS_PER_PAGE))


def run_render(args: argparse.Namespace) -> int:
    page = args.page
    try:
        if page < 1:
            raise CliError("--page starts at 1.")
        css = app_stylesheet()

        api = open_session(args.paz_folder, load_loc=not args.no_loc)
        parsed = load_parsed_file(api, args.render)
        progress(f"Rendering {parsed.entry.internal_path}…")
        total_pages = page_count(parsed)
        if page > total_pages:
            raise CliError(f"--page {page} is past the last page ({total_pages}).")
    except CliError as ex:
        error(str(ex))
        return 1

    body = parsed.handler.render_data_page(
        parsed.data, parsed.entry, parsed.companions, page - 1, PARSED_RECORDS_PER_PAGE
    )
    body = inline_icons(body, lambda path: api.get_icon_data_url(path).get("url"))
    note = f"{parsed.entry.internal_path}, page {page} of {total_pages}, file order"
    write_raw(standalone_page(Path(parsed.entry.internal_path).name, note, body, css))
    progress(f"Page {page} of {total_pages} written.")
    return 0
