"""Resolve one file name to its handler, payload and companions."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from api.bdo_api import Api
from api.bdo_api_helpers import _norm, path_matcher
from bdo_models import PazEntry
from bdo_preview import PreviewHandler, get_handler, has_parsed_view
from paz.na_copy import plain_name

from .errors import CliError

# Candidates listed when a name matches several files.
_MAX_LISTED_MATCHES = 10


@dataclass(frozen=True)
class ParsedFile:
    """Everything a handler call needs, loaded like the GUI loads a preview."""

    entry: PazEntry
    handler: PreviewHandler
    data: bytes
    companions: dict[str, bytes]

    def records(self) -> list[dict]:
        return self.handler.all_records(self.data, self.entry, self.companions)


def find_entry(entries: Sequence[PazEntry], name: str) -> PazEntry:
    """The single entry of `entries` that `name` refers to.

    Tried in order: an exact path, an exact file name, the plain path or
    file name of a table's NA copy (`paz/na_copy.py`), then the `--list`
    pattern rules (glob, else substring). Anything but one hit is an error, so
    a command never picks a file silently.
    """
    wanted = _norm(name).lower()
    exact = [e for e in entries if _norm(e.internal_path).lower() == wanted]
    if not exact:
        exact = [e for e in entries if _file_name(e) == wanted]
    if not exact:
        # `#` first: only an NA copy (`#na#x.bss`) has a plain name of its own.
        exact = [e for e in entries if "#" in e.internal_path and wanted in _plain_names(e)]
    if len(exact) == 1:
        return exact[0]
    if exact:
        raise CliError(_ambiguous(name, exact))

    is_hit = path_matcher(name)
    matches = [e for e in entries if is_hit(_norm(e.internal_path))]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise CliError(f"no file matches '{name}'.")
    raise CliError(_ambiguous(name, matches))


def load_parsed_file(api: Api, name: str) -> ParsedFile:
    """Load `name` (a PAZ file, or the LOC file on disk) with a parsed view."""
    disk = api.disk_entry(Path(name).name.lower())
    if disk is not None:
        entry, data = disk
        handler = _parsed_handler(entry)
        return ParsedFile(entry, handler, data, {})

    entry = find_entry(api.entries, name)
    handler = _parsed_handler(entry)
    try:
        data = api.read_entry(entry.internal_path)
    except Exception as ex:
        raise CliError(f"cannot read {entry.internal_path}: {ex}") from ex
    return ParsedFile(entry, handler, data, api.entry_companions(handler, entry))


def _parsed_handler(entry: PazEntry) -> PreviewHandler:
    path = Path(entry.internal_path)
    handler = get_handler(path.name, path.suffix)
    if not has_parsed_view(handler):
        raise CliError(f"{entry.internal_path} has no parsed view (no handler builds records for it).")
    return handler


def _file_name(entry: PazEntry) -> str:
    return _norm(entry.internal_path).rsplit("/", 1)[-1].lower()


def _plain_names(entry: PazEntry) -> tuple[str, str]:
    """The plain path and file name of an NA copy; for any other entry its own."""
    plain = plain_name(_norm(entry.internal_path).lower())
    return plain, plain.rsplit("/", 1)[-1]


def _ambiguous(name: str, matches: Sequence[PazEntry]) -> str:
    listed = "\n".join(f"  {e.internal_path}" for e in matches[:_MAX_LISTED_MATCHES])
    more = len(matches) - _MAX_LISTED_MATCHES
    tail = f"\n  … and {more:,} more" if more > 0 else ""
    return f"'{name}' matches {len(matches):,} files, give the full path:\n{listed}{tail}"
