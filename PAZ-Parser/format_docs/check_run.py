"""Checks one format doc: the doc rules, then its layouts against a client's game files.

The game files come in through `read_file`, so the check runs the same on a
PAZ folder (check_docs.py) and on bytes a test builds.
"""
from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from .doc_checks import check_doc, read_layouts
from .doc_fit import fit_layouts
from .doc_index import doc_files
from .versions import merge_rows, read_rows, rows_from_fit, write_rows
from .walk_model import LayoutFit, Unwalkable

FileReader = Callable[[str], "bytes | None"]


class Status(Enum):
    OK = "ok"
    UPDATED = "Versions updated"
    PROBLEMS = "doc problems"
    NO_FIT = "fits no layout"
    SKIPPED = "game check skipped"

    @property
    def stops_commit(self) -> bool:
        return self in (Status.UPDATED, Status.PROBLEMS, Status.NO_FIT)


@dataclass(frozen=True)
class DocOutcome:
    doc: Path
    status: Status
    messages: tuple[str, ...] = ()


@dataclass(frozen=True)
class Client:
    """The client whose files `read_file` returns, by the number Versions names it with."""

    number: int
    read_file: FileReader


def check_doc_file(
    path: Path, rows: Mapping[str, list[tuple[str, str]]], client: Client | None, *, write: bool = True
) -> DocOutcome:
    """Check `path`; with a client, walk its files and rewrite Versions in place when they change (unless `write` is off)."""
    text = path.read_text(encoding="utf-8")
    folder = path.parent
    problems = check_doc(text, folder)
    if problems:
        return DocOutcome(path, Status.PROBLEMS, tuple(str(problem) for problem in problems))
    if client is None:
        return DocOutcome(path, Status.OK)
    layouts, _ = read_layouts(text, folder)
    files: dict[str, bytes] = {}
    missing: list[str] = []
    for name in doc_files(path.name, layouts, rows):
        data = client.read_file(name)
        if data is None:
            missing.append(name)
        else:
            files[name] = data
    if not files:
        return DocOutcome(path, Status.SKIPPED, (f"none of its files is in the PAZ folder ({', '.join(missing) or 'no files listed'})",))
    try:
        result = fit_layouts(layouts, files)
    except Unwalkable as reason:
        return DocOutcome(path, Status.SKIPPED, (f"a walk cannot follow it: {reason}",))
    if not isinstance(result, LayoutFit):
        newest = result[0]
        message = f"client {client.number} fits no layout of {newest.file}; Layout {newest.layout}: {newest.error}"
        return DocOutcome(path, Status.NO_FIT, (message,))
    notes = tuple(f"not in the PAZ folder: {name}" for name in missing)
    if not write:
        return DocOutcome(path, Status.OK, notes + (f"fits Layout {result.layout}",))
    updated = write_rows(text, merge_rows(read_rows(text), rows_from_fit(result, client.number)), layouts[0].number)
    if updated == text:
        return DocOutcome(path, Status.OK, notes)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(updated)
    return DocOutcome(path, Status.UPDATED, notes)
