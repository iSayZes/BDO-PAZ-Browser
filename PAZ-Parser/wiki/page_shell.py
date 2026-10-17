"""The HTML document around every wiki page: head, top bar and scripts."""
from __future__ import annotations

from html import escape

REPO_URL = "https://github.com/iSayZes/BDO-PAZ-Browser"
INDEX_PAGE = "index.html"
STATIC_DIR = "static"
FORMATS_SCRIPT = "formats.js"
FAVICON = "favicon.ico"


def page(title: str, crumb: str, body_class: str, body: str, scripts: tuple[str, ...], inline_script: str = "") -> str:
    """A whole page. `crumb` is HTML after the "Format docs" link; `scripts` are paths relative to the page."""
    script_tags = "".join(f'<script src="{escape(src)}"></script>' for src in scripts)
    inline = f"<script>{inline_script}</script>" if inline_script else ""
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f"<title>{escape(title)}</title>"
        f'<link rel="icon" href="{STATIC_DIR}/{FAVICON}">'
        f'<link rel="stylesheet" href="{STATIC_DIR}/wiki.css"></head>'
        f'<body class="{body_class}">{_top_bar(crumb)}{body}{inline}{script_tags}</body></html>\n'
    )


def _top_bar(crumb: str) -> str:
    return (
        '<header class="tb"><div class="tb-inner">'
        f'<a class="tb-brand" href="{INDEX_PAGE}">BDO PAZ Browser</a>'
        f'<span class="tb-crumb"><a href="{INDEX_PAGE}">Format docs</a>{crumb}</span>'
        '<span class="tb-gap"></span>'
        f'<a class="tb-link" href="{REPO_URL}">GitHub ↗</a>'
        "</div></header>"
    )
