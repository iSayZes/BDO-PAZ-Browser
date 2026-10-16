"""Read game files by name from a PAZ folder, for checks that need raw bytes."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from api.bdo_api import Api
from api.bdo_api_helpers import _norm
from bdo_models import PazEntry
from paz.bdo_cache import read_meta_version
from paz.bdo_paz_extract import find_single_meta_file

from .errors import CliError
from .session import open_session, resolve_paz_root


@dataclass(frozen=True)
class GameFiles:
    """A loaded PAZ folder and the client number its `.meta` holds."""

    root: Path
    client: int
    api: Api
    # Lower-case file name to its entries; only an exact name reads a file.
    by_name: dict[str, list[PazEntry]] = field(default_factory=dict)

    @classmethod
    def open(cls, paz_folder: str | None) -> GameFiles:
        root = resolve_paz_root(paz_folder)
        try:
            client = read_meta_version(find_single_meta_file(root))
        except (OSError, ValueError) as ex:
            raise CliError(f"cannot read the client number of {root}: {ex}") from ex
        api = open_session(str(root), load_loc=False, load_indexes=False)
        by_name: dict[str, list[PazEntry]] = {}
        for entry in api.entries:
            by_name.setdefault(_norm(entry.internal_path).rsplit("/", 1)[-1].lower(), []).append(entry)
        return cls(root, client, api, by_name)

    def read(self, name: str) -> bytes | None:
        """The decompressed bytes of the one file called `name`, or None when the folder has none."""
        entries = self.by_name.get(name.lower(), [])
        if not entries:
            return None
        if len(entries) > 1:
            raise CliError(f"{len(entries)} files are called {name}: {', '.join(entry.internal_path for entry in entries)}")
        entry = entries[0]
        try:
            return self.api.read_entry(entry.internal_path)
        except (OSError, ValueError) as ex:
            raise CliError(f"cannot read {entry.internal_path}: {ex}") from ex
