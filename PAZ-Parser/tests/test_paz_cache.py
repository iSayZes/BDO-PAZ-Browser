"""The PAZ index cache: columns on disk, entries back, anything else a miss; `archive_files`."""
from __future__ import annotations

import pickle
from pathlib import Path

from bdo_models import PazEntry
from paz.bdo_cache import CACHE_FILE, CACHE_FORMAT, CachedEntries, archive_files, load_cache, save_cache

_ENTRIES = [
    PazEntry("PAD00001.PAZ", "gamecommondata/binary/quest.dbss", 12, 400, 900, 0, 0),
    PazEntry("PAD00002.PAZ", "ui_texture/icon/Old/Pet.dds", 0, 4_294_967_295, 16, 0, 0),
    PazEntry("PAD00001.PAZ", "readme.txt", 412, 8, 8, 0, 0),
]
_FILES = ("pad00001.paz", "pad00002.paz")
_CACHED = CachedEntries(3458, _FILES, _ENTRIES)


def _saved_columns(tmp_path: Path) -> dict:
    save_cache(tmp_path, _CACHED)
    with (tmp_path / CACHE_FILE).open("rb") as f:
        return pickle.load(f)


def _write(tmp_path: Path, data: object) -> None:
    (tmp_path / CACHE_FILE).write_bytes(pickle.dumps(data))


def test_saved_entries_load_back_in_order(tmp_path: Path) -> None:
    save_cache(tmp_path, _CACHED)

    loaded = load_cache(tmp_path)

    assert loaded == _CACHED
    assert loaded is not None and all(type(entry) is PazEntry for entry in loaded.entries)


def test_an_empty_client_round_trips(tmp_path: Path) -> None:
    save_cache(tmp_path, CachedEntries(1, (), []))

    assert load_cache(tmp_path) == CachedEntries(1, (), [])


def test_a_missing_cache_is_a_miss(tmp_path: Path) -> None:
    assert load_cache(tmp_path) is None


def test_the_old_pickled_list_format_is_a_miss(tmp_path: Path) -> None:
    _write(tmp_path, {"version": 3458, "entries": list(_ENTRIES)})

    assert load_cache(tmp_path) is None


def test_a_cache_without_the_archive_file_list_is_a_miss(tmp_path: Path) -> None:
    columns = _saved_columns(tmp_path)
    del columns["archive_files"]
    _write(tmp_path, {**columns, "format": 2})

    assert load_cache(tmp_path) is None


def test_another_format_number_is_a_miss(tmp_path: Path) -> None:
    columns = _saved_columns(tmp_path)
    _write(tmp_path, {**columns, "format": CACHE_FORMAT + 1})

    assert load_cache(tmp_path) is None


def test_columns_of_different_lengths_are_a_miss(tmp_path: Path) -> None:
    columns = _saved_columns(tmp_path)
    _write(tmp_path, {**columns, "paths": columns["paths"][:-1]})

    assert load_cache(tmp_path) is None


def test_an_archive_index_out_of_range_is_a_miss(tmp_path: Path) -> None:
    columns = _saved_columns(tmp_path)
    _write(tmp_path, {**columns, "archives": columns["archives"][:1]})

    assert load_cache(tmp_path) is None


def test_a_file_that_is_not_a_pickle_is_a_miss(tmp_path: Path) -> None:
    (tmp_path / CACHE_FILE).write_bytes(b"not a cache")

    assert load_cache(tmp_path) is None


def test_archive_files_lists_only_the_archives_in_lower_case(tmp_path: Path) -> None:
    for name in ("PAD00002.PAZ", "pad00001.paz", "pad00000.meta", "PAD00003.PAZ.part", "notes.txt"):
        (tmp_path / name).write_bytes(b"")

    assert archive_files(tmp_path) == ("pad00001.paz", "pad00002.paz")
