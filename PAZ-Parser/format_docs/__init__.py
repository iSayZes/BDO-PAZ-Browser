"""Checks the format docs in docs/file-formats/<group>/ against docs/format-docs.md.

`check_doc` reads one doc's text and returns its problems; `converted_docs`
lists the docs in the layout format, the ones the checks apply to.
"""
from __future__ import annotations

from pathlib import Path

from .doc_checks import check_doc, is_converted, read_layouts, shared_layout_path, structure_sizes
from .doc_paths import TEMPLATE_PREFIX, doc_group, doc_path, format_doc_paths
from .model import Problem

__all__ = [
    "TEMPLATE_PREFIX", "Problem", "check_doc", "converted_docs", "doc_group", "doc_path", "format_doc_paths", "is_converted",
    "read_layouts", "shared_layout_path", "structure_sizes",
]


def converted_docs(folder: Path) -> tuple[Path, ...]:
    """The format docs under `folder` (docs/file-formats/) that use `## Layout N` or share another doc's."""
    return tuple(path for path in format_doc_paths(folder) if is_converted(path.read_text(encoding="utf-8")))
