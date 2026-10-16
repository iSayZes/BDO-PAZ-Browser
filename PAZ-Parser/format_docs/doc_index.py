"""docs/documented-formats.md: which game files each format doc covers."""
from __future__ import annotations

import re
from collections.abc import Mapping, Sequence

from .markdown import numbered_lines, tables
from .model import Layout

_FIRST_CODE = re.compile(r"`([^`]+)`")
_DOC_LINK = re.compile(r"\(file-formats/([^)#]+)")
_INDEX_COLUMNS = ("File", "Description", "Docs")
_COMPANION_HEADING = re.compile(r"^`(?P<file>[a-z0-9_.]+)`$")
# Index rows such as `*.ai` or `{a,b}stat.bss` name a family, not one file.
_PATTERN_CHARS = "*{"


def index_rows(documented_formats: str) -> dict[str, list[tuple[str, str]]]:
    """Per doc file name, the (file, description) rows of docs/documented-formats.md that link to it."""
    rows: dict[str, list[tuple[str, str]]] = {}
    for table in tables(numbered_lines(documented_formats)):
        if table.header[: len(_INDEX_COLUMNS)] != _INDEX_COLUMNS:
            continue
        for _, cells in table.rows:
            if len(cells) < len(_INDEX_COLUMNS):
                continue
            file_cell, description, docs_cell = cells[: len(_INDEX_COLUMNS)]
            file_match = _FIRST_CODE.search(file_cell)
            doc_match = _DOC_LINK.search(docs_cell)
            if file_match and doc_match:
                rows.setdefault(doc_match.group(1), []).append((file_match.group(1), description))
    return rows


def doc_files(doc_name: str, layouts: Sequence[Layout], rows: Mapping[str, list[tuple[str, str]]]) -> tuple[str, ...]:
    """The game files a doc covers: its index rows, and every file a ``### `file` `` heading names."""
    files = {file for file, _ in rows.get(doc_name, []) if not any(char in file for char in _PATTERN_CHARS)}
    for layout in layouts:
        for structure in layout.structures:
            match = _COMPANION_HEADING.match(structure.name)
            if match:
                files.add(match.group("file"))
    return tuple(sorted(files))
