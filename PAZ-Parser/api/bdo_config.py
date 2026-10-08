"""User config in `paz_config.json` in the Data Folder: settings and per-file table sorts."""

from __future__ import annotations

import json
import logging
import os
from collections.abc import Collection
from pathlib import Path

import app_dirs
from table_sort import TableSort

from .config_migrations import VERSION_KEY, current_version, migrate, needs_migration

# Where the config lived before the Data Folder; `bdo_app.main()` moves it over.
LEGACY_CONFIG_FILE = Path(__file__).parent.parent / app_dirs.CONFIG_NAME
# Next to the config: the last config that could not be read or migrated.
BACKUP_NAME = "paz_config.backup.json"

# {"buff.dbss": {"field": "duration_ms", "dir": "desc"}, ...}
_TABLE_SORT_KEY = "table_sort"


def config_file() -> Path:
    """`paz_config.json` in the Data Folder in use (`app_dirs.py`)."""
    return app_dirs.config_file()


def load_config() -> dict:
    """The saved settings, brought to the current config version (`config_migrations.py`).

    A config that isn't a JSON object, or can't be migrated, is renamed to
    `paz_config.backup.json` and the app starts with default settings, so the
    next save can't overwrite it. A migrated config is saved right away.
    """
    path = config_file()
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}
    except OSError:
        logging.warning("Could not read the settings from %s", path, exc_info=True)
        return {}

    try:
        cfg = json.loads(text)
        if not isinstance(cfg, dict):
            raise ValueError(f"the settings are a JSON {type(cfg).__name__}, not an object")
        if not needs_migration(cfg):
            return cfg
        migrated = migrate(cfg)
    except Exception:
        # Any failure, a bug in a migration step included: the app must still start.
        logging.warning("Could not read the settings in %s, starting with defaults", path, exc_info=True)
        _back_up(path)
        return {}

    _write_config(path, migrated)
    return migrated


def show_pa_tags_setting(cfg: dict) -> bool:
    """The "Show game text tags" setting; off unless saved as true."""
    return cfg.get("show_pa_tags") is True


def handled_only_setting(cfg: dict) -> bool:
    """The "Show only handled tables" setting; off unless saved as true."""
    return cfg.get("handled_only") is True


def check_app_updates_setting(cfg: dict) -> bool:
    """The exe's "Check for updates on start" setting; on unless saved as false."""
    return cfg.get("check_app_updates") is not False


def update_handlers_setting(cfg: dict) -> bool:
    """The exe's "Update handlers on start" setting; on unless saved as false."""
    return cfg.get("update_handlers") is not False


# "Parsed table cache": never, when a table is opened, or every table in the background.
RECORDS_CACHE_MODES = ("off", "open", "all")
_DEFAULT_RECORDS_CACHE_MODE = "open"


def records_cache_setting(cfg: dict) -> str:
    """The "Parsed table cache" mode; "open" unless a valid mode is saved."""
    mode = cfg.get("records_cache")
    return mode if mode in RECORDS_CACHE_MODES else _DEFAULT_RECORDS_CACHE_MODE


def dismissed_loc_warnings(cfg: dict) -> frozenset[str]:
    """Languages whose missing-LOC corner warning was dismissed for good."""
    codes = cfg.get("loc_warning_dismissed")
    return frozenset(code for code in codes if isinstance(code, str)) if isinstance(codes, list) else frozenset()


def save_config(updates: dict) -> None:
    # A config from a newer app keeps its own version and keys.
    _write_config(config_file(), {VERSION_KEY: current_version(), **load_config(), **updates})


def _write_config(path: Path, cfg: dict) -> None:
    """Write through a temporary file, so a crash mid-write can't leave half a config."""
    temp = path.with_name(f"{path.name}.tmp")
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        temp.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
        os.replace(temp, path)
    except OSError:
        logging.warning("Could not save the settings to %s", path, exc_info=True)


def _back_up(path: Path) -> None:
    """Rename an unreadable config to `paz_config.backup.json`, replacing an older backup."""
    try:
        os.replace(path, path.with_name(BACKUP_NAME))
    except OSError:
        logging.warning("Could not rename %s to %s", path, BACKUP_NAME, exc_info=True)


def table_sort_file_key(internal_path: str) -> str:
    """Config key for a file's sort: its lowercased file name.

    Handlers are chosen by file name, so every file sharing a name shares its
    columns and can share a sort.
    """
    return internal_path.replace("\\", "/").rsplit("/", 1)[-1].lower()


def _saved_table_sorts() -> dict:
    sorts = load_config().get(_TABLE_SORT_KEY)
    return sorts if isinstance(sorts, dict) else {}


def load_table_sort(file_key: str, sortable_fields: Collection[str]) -> TableSort | None:
    """The saved sort for a file, if its field is still sortable.

    A malformed entry, or one whose field the handler no longer declares, is
    dropped from the config so the file opens in its default sort from then on.
    """
    if file_key not in _saved_table_sorts():
        return None

    sort = peek_table_sort(file_key, sortable_fields)
    if sort is None:
        forget_table_sort(file_key)
    return sort


def peek_table_sort(file_key: str, sortable_fields: Collection[str]) -> TableSort | None:
    """`load_table_sort()` without dropping a stale entry, so it never writes the config."""
    saved = _saved_table_sorts().get(file_key)
    sort = TableSort.parse(saved.get("field"), saved.get("dir")) if isinstance(saved, dict) else None
    return sort if sort is not None and sort.field in sortable_fields else None


def save_table_sort(file_key: str, sort: TableSort) -> None:
    """Remember a file's sort. Writes only when it changed."""
    sorts = _saved_table_sorts()
    if sorts.get(file_key) == sort.to_dict():
        return
    save_config({_TABLE_SORT_KEY: {**sorts, file_key: sort.to_dict()}})


def forget_table_sort(file_key: str) -> None:
    sorts = _saved_table_sorts()
    if file_key not in sorts:
        return
    save_config({_TABLE_SORT_KEY: {key: value for key, value in sorts.items() if key != file_key}})
