"""The version of the handler that reads a file, in the pack this process runs.

The GUI footer, `--records --json` and `--handler-version` read it here.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from app_version import source_commit_of
from bdo_preview import get_binary_handlers, handler_key

from .handler_packs import Pack, active_pack
from .handler_sets import handler_files


@dataclass(frozen=True)
class ActiveHandlerVersion:
    key: str
    # None from source without git, or for a key the pack manifest lacks.
    version: str | None


def handler_version(name: str) -> ActiveHandlerVersion | None:
    """The key and version of the handler that reads `name`; None when no handler does.

    `name` is a PAZ path, a file name or a registry key (`.loc`). The version
    is the running pack's, from its manifest. From source it is the commit
    that last changed the handler's files, with a `+` for uncommitted edits
    (`app_version.source_commit_of`).
    """
    path = Path(name)
    key = handler_key(path.name, path.suffix)
    return _version_of(active_pack(), key) if key is not None else None


def all_handler_versions() -> list[ActiveHandlerVersion]:
    """Every registered handler with its version, sorted by key."""
    pack = active_pack()
    return [_version_of(pack, key) for key in get_binary_handlers()]


def _version_of(pack: Pack, key: str) -> ActiveHandlerVersion:
    if pack.manifest is not None:
        entry = pack.manifest.handlers.get(key)
        return ActiveHandlerVersion(key, entry.version if entry is not None else None)
    files = [pack.folder / file for file in handler_files(pack.folder, key)]
    return ActiveHandlerVersion(key, source_commit_of(files))
