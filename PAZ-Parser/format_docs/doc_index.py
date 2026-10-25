"""docs/documented-formats.md: which game files each format doc covers."""
from __future__ import annotations

import re
from collections.abc import Mapping, Sequence

from .markdown import numbered_lines, tables
from .model import Layout
from .reader import COMPANION_HEADING

# What `index_rows` returns, as the readers of it take it.
IndexRows = Mapping[str, list[tuple[str, str]]]

_FIRST_CODE = re.compile(r"`([^`]+)`")
# The doc's file name, behind its group folder: `(file-formats/dbss/buff_dbss.md)`.
_DOC_LINK = re.compile(r"\(file-formats/(?:[^)#/]+/)*([^)#/]+)")
_INDEX_COLUMNS = ("File", "Description", "Docs")
# Index rows such as `*.ai` or `{a,b}stat.bss` name a family, not one file.
_PATTERN_CHARS = "*{"


def is_file_pattern(name: str) -> bool:
    """True for an index row that names a family of files, such as `*.ai` or `{a,b}stat.bss`."""
    return any(char in name for char in _PATTERN_CHARS)


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


def doc_files(doc_name: str, layouts: Sequence[Layout], rows: IndexRows) -> tuple[str, ...]:
    """The game files a doc covers: its index rows, and every file a ``### `file` `` heading names."""
    files = {file for file, _ in rows.get(doc_name, []) if not is_file_pattern(file)}
    for layout in layouts:
        for structure in layout.structures:
            match = COMPANION_HEADING.match(structure.name)
            if match:
                files.add(match.group("file"))
    return tuple(sorted(files))
