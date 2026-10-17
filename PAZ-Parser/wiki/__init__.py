"""Builds the format docs wiki: a static site from docs/file-formats/.

`render_site` renders an index page, one page per doc and `formats.js` with
the list both page kinds show; `build_site` writes them with the static CSS
and JS and the app's favicon. See "Format Docs Wiki" in docs/format-docs.md.
"""
from __future__ import annotations

import posixpath
import shutil
from dataclasses import dataclass
from pathlib import Path

from format_docs import TEMPLATE_PREFIX
from format_docs.doc_index import index_rows

from .doc_page import doc_page
from .doc_source import read_doc
from .format_list import documented_counts, format_entry, formats_script, game_totals
from .index_page import index_page
from .page_shell import FAVICON, FORMATS_SCRIPT, INDEX_PAGE, REPO_URL, STATIC_DIR

__all__ = ["BuildResult", "RenderedSite", "build_site", "render_site"]

FORMATS_DIR = "file-formats"
DOCUMENTED_FORMATS = "documented-formats.md"
README = "README.md"
_STATIC_SOURCE = Path(__file__).parent / "static"
_FAVICON_SOURCE = Path(__file__).parent.parent / "ui" / FAVICON


@dataclass(frozen=True)
class BuildResult:
    out_dir: Path
    pages: int
    converted: int


@dataclass(frozen=True)
class RenderedSite:
    """The generated files by name: `index.html`, `formats.js` and one page per doc."""

    files: dict[str, str]
    doc_pages: int
    converted: int


def render_site(docs_dir: Path) -> RenderedSite:
    """Renders the wiki for `docs_dir` (the repo's docs/ folder) without writing it."""
    docs = [read_doc(path) for path in sorted((docs_dir / FORMATS_DIR).glob("*.md")) if not path.name.startswith(TEMPLATE_PREFIX)]
    documented = docs_dir / DOCUMENTED_FORMATS
    rows = index_rows(documented.read_text(encoding="utf-8")) if documented.exists() else {}
    entries = [format_entry(doc, rows.get(doc.path.name, [])) for doc in docs]
    readme = docs_dir.parent / README
    totals = game_totals(readme.read_text(encoding="utf-8")) if readme.exists() else {}
    links = _links({doc.path.name: doc.page for doc in docs})
    files = {
        FORMATS_SCRIPT: formats_script(entries, documented_counts(rows), totals),
        INDEX_PAGE: index_page(),
        **{doc.page: doc_page(doc, links) for doc in docs},
    }
    return RenderedSite(files, len(docs), sum(1 for doc in docs if doc.is_converted))


def build_site(docs_dir: Path, out_dir: Path) -> BuildResult:
    """Writes the wiki for `docs_dir` (the repo's docs/ folder) into `out_dir`."""
    site = render_site(docs_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(_STATIC_SOURCE, out_dir / STATIC_DIR, dirs_exist_ok=True)
    shutil.copy2(_FAVICON_SOURCE, out_dir / STATIC_DIR / FAVICON)
    for name, text in site.files.items():
        (out_dir / name).write_text(text, encoding="utf-8")
    return BuildResult(out_dir, site.doc_pages, site.converted)


def _links(pages: dict[str, str]):
    """Maps a link in a format doc: another doc goes to its page, other repo files to GitHub."""

    def resolve(url: str) -> str:
        if url.startswith(("http://", "https://", "#", "mailto:")):
            return url
        path, _, anchor = url.partition("#")
        suffix = f"#{anchor}" if anchor else ""
        if path in pages:
            return pages[path] + suffix
        repo_path = posixpath.normpath(posixpath.join("docs", FORMATS_DIR, path))
        return f"{REPO_URL}/blob/main/{repo_path}{suffix}"

    return resolve
