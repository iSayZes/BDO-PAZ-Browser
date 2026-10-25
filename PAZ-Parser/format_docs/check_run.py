"""Checks one format doc: the doc rules, then its layouts against a client's game files.

The game files come in through `read_file`, so the check runs the same on a
PAZ folder (check_docs.py) and on bytes a test builds.
"""
from __future__ import annotations

import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from .doc_checks import check_doc, is_converted, read_layouts
from .doc_fit import fit_layouts
from .doc_index import IndexRows, doc_files
from .fingerprint import layouts_fingerprint
from .versions import (
    ClientCheck,
    VersionRow,
    current_rows,
    merge_clients,
    merge_rows,
    read_clients,
    read_rows,
    rows_from_fit,
    write_rows,
)
from .walk_model import LayoutFit, Unwalkable

FileReader = Callable[[str], "bytes | None"]
# Another program (a virus scanner, an editor) can hold a doc for a moment; wait for it this long at most.
_WRITE_ATTEMPTS = 40
_WRITE_WAIT_SECONDS = 0.25
NA_COPY_PREFIX = "#na#"


class UnreadableFile(Exception):
    """Raised by a `FileReader` that cannot pick or read a file, e.g. two PAZ paths share its name."""


class Status(Enum):
    OK = "ok"
    UPDATED = "Versions updated"
    PROBLEMS = "doc problems"
    NO_FIT = "fits no layout"
    SKIPPED = "game check skipped"
    NOT_CONVERTED = "skipped (not converted)"
    CHECKED_BEFORE = "checked before"

    @property
    def stops_commit(self) -> bool:
        return self in (Status.UPDATED, Status.PROBLEMS, Status.NO_FIT)


@dataclass(frozen=True)
class VersionsUpdate:
    """What one client adds to a doc's Versions: its Clients row and the size rows of the layout it fits."""

    newest_layout: int
    check: ClientCheck
    rows: tuple[VersionRow, ...] = ()

    def apply(self, text: str) -> str:
        """`text` with this update merged into its Versions section."""
        return apply_updates(text, (self,))


def apply_updates(text: str, updates: Sequence[VersionsUpdate]) -> str:
    """`text` with `updates` merged into its Versions section in order, parsed and written once."""
    if not updates:
        return text
    clients = merge_clients(read_clients(text), (update.check for update in updates))
    rows = merge_rows(current_rows(read_rows(text), clients), (row for update in updates for row in update.rows))
    return write_rows(text, rows, clients, updates[-1].newest_layout)


@dataclass(frozen=True)
class DocOutcome:
    """A doc's check; `update` is the Versions change when the caller merges and writes it (`defer_write`)."""

    doc: Path
    status: Status
    messages: tuple[str, ...] = ()
    update: VersionsUpdate | None = None


@dataclass(frozen=True)
class Client:
    """The client whose files `read_file` returns, by the number Versions names it with."""

    number: int
    read_file: FileReader

    def read_doc_file(self, name: str) -> bytes | None:
        """`name`, else its NA copy (`#na#eventmanagement.bss`), which some clients ship in its place."""
        data = self.read_file(name)
        return data if data is not None else self.read_file(na_copy_name(name))


def na_copy_name(name: str) -> str:
    """`name` with the NA prefix on its file name: `#na#x.bss`, `folder/#na#x.bss` for a full path.

    Clients 837 to 1246 ship some tables only under this name; client 1000 has
    244 `.bss` files outside `detaildialog/` with it.
    """
    folder, slash, file_name = name.rpartition("/")
    return f"{folder}{slash}{NA_COPY_PREFIX}{file_name}"


def check_doc_file(
    path: Path, rows: IndexRows, client: Client | None, *, write: bool = True, recheck: bool = False, defer_write: bool = False
) -> DocOutcome:
    """Check `path`; with a client, walk its files and rewrite Versions in place when they change (unless `write` is off).

    A doc not in the layout format yet is skipped: the doc rules do not apply to it. Each client
    goes into the Clients table: the layout its files fit, `No documented layout` when they fit
    none, or `No file` when none of the doc's files is in it, under its name or as its NA copy
    (`Client.read_doc_file`). A file the reader cannot pick
    skips the game check for this doc and client and leaves Versions as they are. A client the
    table already holds, read against the same layouts, is not read again unless `recheck` is set.
    With `defer_write` the change comes back in the outcome instead, for the caller to merge and
    write: a worker process must not rewrite a doc that another worker may be reading as a
    shared layout, and a run over many clients writes each doc once in a while, not per client.
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
    if not layouts:
        return DocOutcome(path, Status.SKIPPED, ("no layout to read its files by",))
    names = doc_files(path.name, layouts, rows)
    fingerprint = layouts_fingerprint(layouts, names)
    if not recheck and _is_checked_before(text, fingerprint, client.number):
        return DocOutcome(path, Status.CHECKED_BEFORE)
    files: dict[str, bytes] = {}
    missing: list[str] = []
    for name in names:
        try:
            data = client.read_doc_file(name)
        except UnreadableFile as error:
            return DocOutcome(path, Status.SKIPPED, (str(error),))
        if data is None:
            missing.append(name)
        else:
            files[name] = data
    newest = layouts[0].number
    if not files:
        reason = f"none of its files is in the PAZ folder ({', '.join(missing) or 'no files listed'})"
        if not missing or not write:
            return DocOutcome(path, Status.SKIPPED, (reason,))
        return _outcome(path, text, Status.SKIPPED, (reason,), VersionsUpdate(newest, ClientCheck(client.number, None, False, fingerprint)), defer_write)
    try:
        result = fit_layouts(layouts, files)
    except Unwalkable as reason:
        return DocOutcome(path, Status.SKIPPED, (f"a walk cannot follow it: {reason}",))
    if not isinstance(result, LayoutFit):
        broken = ", ".join(dict.fromkeys(miss.file for miss in result))
        breaks = tuple(f"Layout {miss.layout} breaks in {miss.file}: {miss.error}" for miss in result)
        messages = (f"client {client.number} fits no layout of {broken}", *breaks)
        if not write:
            return DocOutcome(path, Status.NO_FIT, messages)
        update = VersionsUpdate(newest, ClientCheck(client.number, None, True, fingerprint))
        return _outcome(path, text, Status.NO_FIT, messages, update, defer_write, always=Status.NO_FIT)
    notes = tuple(f"not in the PAZ folder: {name}" for name in missing)
    if not write:
        return DocOutcome(path, Status.OK, notes + (f"fits Layout {result.layout}",))
    update = VersionsUpdate(newest, ClientCheck(client.number, result.layout, True, fingerprint), rows_from_fit(result, client.number))
    return _outcome(path, text, Status.OK, notes, update, defer_write)


def _outcome(
    path: Path, text: str, unchanged: Status, messages: tuple[str, ...], update: VersionsUpdate, defer_write: bool,
    always: Status | None = None,
) -> DocOutcome:
    """The outcome of `update`: `unchanged` when it changes nothing, else UPDATED (or `always`), written now unless deferred."""
    updated = update.apply(text)
    if updated == text:
        return DocOutcome(path, always or unchanged, messages)
    if defer_write:
        return DocOutcome(path, always or Status.UPDATED, messages, update)
    write_doc(path, updated)
    return DocOutcome(path, always or Status.UPDATED, messages)


def _is_checked_before(text: str, fingerprint: str, client: int) -> bool:
    """True when the Clients table holds `client` with a row read against the layouts `fingerprint` stands for."""
    return any(check.client == client and check.fingerprint == fingerprint for check in read_clients(text))


def write_doc(path: Path, text: str) -> None:
    """Writes `text` to `path`, waiting a moment while another program (a virus scanner, an editor) holds the file."""
    for attempt in range(_WRITE_ATTEMPTS):
        try:
            with path.open("w", encoding="utf-8", newline="") as handle:
                handle.write(text)
            return
        except OSError:
            if attempt == _WRITE_ATTEMPTS - 1:
                raise
            time.sleep(_WRITE_WAIT_SECONDS)
