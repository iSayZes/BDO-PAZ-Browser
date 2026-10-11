"""Where the app keeps its files: the Data Folder, with the config and the caches.

The Data Folder is `%LOCALAPPDATA%\\BDO-PAZ-Browser` from source, `data\\` next
to the exe in the Windows build (so the unzipped folder holds everything), or
the folder picked in the settings. An exe whose folder isn't writable, such as
one unzipped into Program Files, uses the `%LOCALAPPDATA%` folder too. It holds
`paz_config.json`, the saved map pins in `map_pins.json` and `cache\\`, with
one cache subfolder per client named after a hash of its PAZ path, so a test
client keeps caches of its own.

The config can't hold its own location, so a picked folder is remembered in
`location.json` in the default folder. A picked folder that is gone, such as
an unplugged drive, reads as the default until it is back.

The caches used to sit next to the PAZ files and the config next to the code.
A game folder under Program Files is not writable, the launcher's file repair
can trip over files it does not know, and an exe has no code folder to write
to. Both are moved here when found.

Each client cache folder holds a marker file naming its PAZ folder. Only
folders with that marker are ever deleted, so a picked folder can safely hold
other files.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import shutil
import sys
import tempfile
from collections.abc import Iterable
from functools import cache
from pathlib import Path

from app_version import is_frozen

APP_NAME = "BDO-PAZ-Browser"
CONFIG_NAME = "paz_config.json"
# The map pins placed with `save` (`map_pins_file.py`).
MAP_PINS_FILE = "map_pins.json"
# What the user made: copied when another Data Folder is picked.
USER_FILES = (CONFIG_NAME, MAP_PINS_FILE)
# In the default Data Folder: {"data_folder": "<picked folder>"}, only while one is picked.
LOCATION_FILE = "location.json"
# Next to the exe: the Data Folder of the Windows build.
PORTABLE_FOLDER = "data"
_CACHE_FOLDER = "cache"
# In every client folder: the PAZ folder it belongs to, and proof the app made it.
MARKER_FILE = "paz_folder.txt"
# While the app runs: its local server's port and token (`server_info_file`).
SERVER_INFO_FILE = "local_server.json"
# Hex digits of the path hash that name a client folder.
_CLIENT_ID_LENGTH = 16


# ── Data Folder ──────────────────────────────────────────────────────────────

def default_data_dir() -> Path:
    """`data\\` next to the exe when it can write there, else `local_app_data_dir()`."""
    portable = portable_data_dir() if is_frozen() else None
    return portable if portable is not None else local_app_data_dir()


def local_app_data_dir() -> Path:
    """`%LOCALAPPDATA%\\BDO-PAZ-Browser`: local to the machine, never roaming."""
    local = os.environ.get("LOCALAPPDATA")
    base = Path(local) if local else Path.home() / "AppData" / "Local"
    return base / APP_NAME


def server_info_file() -> Path:
    """`local_server.json` of the running app, always in `local_app_data_dir()`.

    Not in the Data Folder, which can be anywhere, so other programs know
    where to look for the local server's port and token.
    """
    return local_app_data_dir() / SERVER_INFO_FILE


@cache
def portable_data_dir() -> Path | None:
    """`data\\` next to the exe, created; None when the exe's folder can't be written.

    Checked once per run by writing a file, since Windows folder permissions
    (ACLs) don't show in `os.access()`.
    """
    folder = Path(sys.executable).parent / PORTABLE_FOLDER
    try:
        folder.mkdir(exist_ok=True)
        with tempfile.TemporaryFile(dir=folder):
            pass
    except OSError:
        logging.info("%s is not writable, using %s", folder, local_app_data_dir())
        return None
    return folder


def picked_data_dir() -> Path | None:
    """The Data Folder picked in the settings, or None for the default."""
    pointer = default_data_dir() / LOCATION_FILE
    try:
        saved = json.loads(pointer.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError):
        logging.warning("Ignoring unreadable %s", pointer, exc_info=True)
        return None
    folder = saved.get("data_folder") if isinstance(saved, dict) else None
    return Path(folder) if isinstance(folder, str) and Path(folder).is_absolute() else None


def data_dir() -> Path:
    """The Data Folder in use: the picked one while it exists, else the default."""
    picked = picked_data_dir()
    return picked if picked is not None and picked.is_dir() else default_data_dir()


def set_picked_data_dir(folder: Path | None) -> None:
    """Remember `folder` as the Data Folder; None, or the default folder, forgets the pick."""
    default = default_data_dir()
    pointer = default / LOCATION_FILE
    if folder is None or is_same_folder(folder, default):
        pointer.unlink(missing_ok=True)
        return
    default.mkdir(parents=True, exist_ok=True)
    pointer.write_text(json.dumps({"data_folder": str(folder)}, indent=2), encoding="utf-8")


def config_file() -> Path:
    """`paz_config.json` in the Data Folder in use."""
    return data_dir() / CONFIG_NAME


def map_pins_file() -> Path:
    """`map_pins.json` in the Data Folder in use."""
    return data_dir() / MAP_PINS_FILE


def adopt_legacy_config(legacy: Path) -> None:
    """Move a config an older version kept at `legacy` into the Data Folder.

    Only when the Data Folder has none yet; a config already there is newer.
    Not fatal: a config that cannot be moved stays, and the app starts with
    default settings.
    """
    target = config_file()
    if target.exists() or not legacy.is_file():
        return
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(legacy, target)
    except OSError:
        logging.warning("Could not move %s to %s", legacy, target, exc_info=True)


def copy_user_files(source: Path, target: Path) -> None:
    """Copy the config and saved map pins of Data Folder `source` into `target`, replacing any there.

    A file `source` doesn't have is left alone in `target`. The copies in
    `source` stay. Raises OSError when one cannot be copied.
    """
    for name in USER_FILES:
        file = source / name
        if file.is_file():
            target.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(file, target / name)


def cache_root(data: Path) -> Path:
    """The folder under `data` that holds one cache folder per client."""
    return data / _CACHE_FOLDER


# ── Client cache folders ─────────────────────────────────────────────────────


def normalized_path(path: Path) -> str:
    """`path` absolute, with links followed and, on Windows, case and separators folded.

    `C:\\Games\\Paz`, `c:/games/PAZ/` and a junction to it give the same text.
    """
    return os.path.normcase(str(path.resolve()))


def is_same_folder(a: Path, b: Path) -> bool:
    return normalized_path(a) == normalized_path(b)


def client_id(paz_root: Path) -> str:
    """The name of the cache folder of `paz_root`: a hash of its normalized path."""
    return hashlib.sha256(normalized_path(paz_root).encode("utf-8")).hexdigest()[:_CLIENT_ID_LENGTH]


def client_cache_dir(cache_root: Path, paz_root: Path) -> Path:
    """The cache folder of `paz_root` under `cache_root`, created with its marker file.

    Raises OSError when the folder cannot be created.
    """
    folder = cache_root / client_id(paz_root)
    folder.mkdir(parents=True, exist_ok=True)
    marker = folder / MARKER_FILE
    if not marker.is_file():
        marker.write_text(str(paz_root.resolve()), encoding="utf-8")
    return folder


def move_out_of_game_folder(
    paz_root: Path,
    cache_dir: Path,
    current: Iterable[str],
    obsolete: Iterable[str] = (),
) -> None:
    """Move the caches an older version wrote next to the PAZ files into `cache_dir`.

    A `current` file that `cache_dir` already has is the newer copy, so the one
    in the game folder is deleted instead. `obsolete` files are deleted. Not
    fatal: a file that cannot be moved stays where it is and its cache is
    rebuilt in `cache_dir`.
    """
    for name in current:
        old = paz_root / name
        if not old.is_file():
            continue
        new = cache_dir / name
        try:
            if new.exists():
                old.unlink()
            else:
                _move_unless_open(old, new)
        except OSError:
            logging.warning("Could not move %s out of the PAZ folder", old, exc_info=True)
    for name in obsolete:
        try:
            (paz_root / name).unlink(missing_ok=True)
        except OSError:
            logging.warning("Could not delete %s", paz_root / name, exc_info=True)


def _move_unless_open(old: Path, new: Path) -> None:
    """Move `old` to `new`; raises OSError, leaving `old` in place, while a process has it open.

    Across drives a move is a copy, and a copy of a SQLite file another app
    instance is writing can be torn. Windows refuses to rename an open file,
    so renaming `old` first proves nothing holds it.
    """
    staged = old.with_name(f"{old.name}.moving")
    old.rename(staged)
    try:
        shutil.move(staged, new)
    except OSError:
        staged.rename(old)
        raise


def remove_cache_root(cache_root: Path, names: Iterable[str], folders: Iterable[str] = ()) -> list[str]:
    """Delete the client folders the app made under `cache_root`, then the root if empty.

    Deletes the files `names`, the subfolders `folders` with what is in them,
    and the marker in every folder that has a marker, and the folder once
    nothing else is left in it. Other files and folders are kept. Returns one
    message per file or subfolder that could not be deleted.
    """
    if not cache_root.is_dir():
        return []
    names = tuple(names)
    folders = tuple(folders)
    errors: list[str] = []
    for folder in cache_root.iterdir():
        if not (folder / MARKER_FILE).is_file():
            continue
        for name in folders:
            try:
                shutil.rmtree(folder / name)
            except FileNotFoundError:
                pass
            except OSError as ex:
                errors.append(f"{folder.name}/{name}: {ex}")
        # The marker goes last, so a folder that kept a file is found again next time.
        for name in (*names, MARKER_FILE):
            try:
                (folder / name).unlink(missing_ok=True)
            except OSError as ex:
                errors.append(f"{folder.name}/{name}: {ex}")
        _remove_if_empty(folder)
    _remove_if_empty(cache_root)
    return errors


def _remove_if_empty(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        # Not empty, or in use: it stays.
        pass
