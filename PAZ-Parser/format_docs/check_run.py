"""Checks one format doc: the doc rules, then its layouts against a client's game files.

The game files come in through `read_file`, so the check runs the same on a
PAZ folder (check_docs.py) and on bytes a test builds.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from .doc_checks import check_doc, is_converted, read_layouts
from .doc_fit import fit_layouts
from .doc_index import IndexRows, doc_files
from .versions import merge_rows, read_rows, rows_from_fit, write_rows
from .walk_model import LayoutFit, Unwalkable

FileReader = Callable[[str], "bytes | None"]


class Status(Enum):
    OK = "ok"
    UPDATED = "Versions updated"
    PROBLEMS = "doc problems"
    NO_FIT = "fits no layout"
    SKIPPED = "game check skipped"
    NOT_CONVERTED = "skipped (not converted)"

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
    path: Path, rows: IndexRows, client: Client | None, *, write: bool = True
) -> DocOutcome:
    """Check `path`; with a client, walk its files and rewrite Versions in place when they change (unless `write` is off).

    A doc not in the layout format yet is skipped: the doc rules do not apply to it.
    """
    text = path.read_text(encoding="utf-8")
    if not is_converted(text):
        return DocOutcome(path, Status.NOT_CONVERTED)
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
        broken = ", ".join(dict.fromkeys(miss.file for miss in result))
        breaks = tuple(f"Layout {miss.layout} breaks in {miss.file}: {miss.error}" for miss in result)
        return DocOutcome(path, Status.NO_FIT, (f"client {client.number} fits no layout of {broken}", *breaks))
    notes = tuple(f"not in the PAZ folder: {name}" for name in missing)
    if not write:
        return DocOutcome(path, Status.OK, notes + (f"fits Layout {result.layout}",))
    updated = write_rows(text, merge_rows(read_rows(text), rows_from_fit(result, client.number)), layouts[0].number)
    if updated == text:
        return DocOutcome(path, Status.OK, notes)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(updated)
    return DocOutcome(path, Status.UPDATED, notes)
