"""Checks the format docs in docs/file-formats/ against docs/format-docs.md.

`check_doc` reads one doc's text and returns its problems; `converted_docs`
lists the docs in the layout format, the ones the checks apply to.
"""
from __future__ import annotations

from pathlib import Path

from .doc_checks import check_doc, is_converted, read_layouts, structure_sizes
from .model import Problem

__all__ = ["Problem", "check_doc", "converted_docs", "is_converted", "read_layouts", "structure_sizes"]

TEMPLATE_PREFIX = "_"


def converted_docs(folder: Path) -> tuple[Path, ...]:
    """The format docs in `folder` that use `## Layout N`, the template left out."""
    return tuple(
        path
        for path in sorted(folder.glob("*.md"))
        if not path.name.startswith(TEMPLATE_PREFIX) and is_converted(path.read_text(encoding="utf-8"))
    )
