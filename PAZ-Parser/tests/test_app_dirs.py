"""Data Folder layout: the config, its pointer and one marked cache folder per PAZ folder."""
from __future__ import annotations

import os
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

from app_dirs import (
    APP_NAME,
    CONFIG_NAME,
    LOCATION_FILE,
    MAP_PINS_FILE,
    MARKER_FILE,
    PORTABLE_FOLDER,
    adopt_legacy_config,
    cache_root,
    client_cache_dir,
    client_id,
    config_file,
    copy_user_files,
    data_dir,
    default_data_dir,
    is_same_folder,
    move_out_of_game_folder,
    picked_data_dir,
    portable_data_dir,
    remove_cache_root,
    set_picked_data_dir,
)

_NAMES = ("a.cache", "b.sqlite")


@pytest.fixture
def local_app_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    local = tmp_path / "local"
    monkeypatch.setenv("LOCALAPPDATA", str(local))
    return local


# ── Data Folder ──────────────────────────────────────────────────────────────

def test_the_default_data_folder_is_under_local_app_data(local_app_data: Path) -> None:
    assert default_data_dir() == local_app_data / APP_NAME
    assert data_dir() == default_data_dir()
    assert config_file() == default_data_dir() / CONFIG_NAME
    assert picked_data_dir() is None


@pytest.fixture
def frozen_exe(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Path]:
    """Run as the Windows build, from an exe in `tmp_path/app`; returns the exe's folder."""
    app = tmp_path / "app"
    app.mkdir()
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "executable", str(app / "BDO-PAZ-Browser.exe"))
    portable_data_dir.cache_clear()
    yield app
    portable_data_dir.cache_clear()


def test_the_exe_keeps_its_data_folder_next_to_it(frozen_exe: Path, local_app_data: Path) -> None:
    assert default_data_dir() == frozen_exe / PORTABLE_FOLDER
    assert (frozen_exe / PORTABLE_FOLDER).is_dir()
    assert config_file() == frozen_exe / PORTABLE_FOLDER / CONFIG_NAME


def test_an_exe_that_cannot_write_its_folder_uses_local_app_data(frozen_exe: Path, local_app_data: Path) -> None:
    # A file where the folder should be: creating it fails like a read-only folder does.
    (frozen_exe / PORTABLE_FOLDER).write_text("", encoding="utf-8")

    assert default_data_dir() == local_app_data / APP_NAME


def test_a_picked_folder_is_used_while_it_exists(tmp_path: Path, local_app_data: Path) -> None:
    picked = tmp_path / "picked"
    picked.mkdir()

    set_picked_data_dir(picked)

    assert picked_data_dir() == picked
    assert data_dir() == picked
    assert config_file() == picked / CONFIG_NAME


def test_a_picked_folder_that_is_gone_reads_as_the_default(tmp_path: Path, local_app_data: Path) -> None:
    picked = tmp_path / "unplugged"
    picked.mkdir()
    set_picked_data_dir(picked)
    picked.rmdir()

    assert data_dir() == default_data_dir()
    # The pick is kept, so the folder is used again once it is back.
    assert picked_data_dir() == picked


def test_picking_the_default_folder_forgets_the_pick(tmp_path: Path, local_app_data: Path) -> None:
    picked = tmp_path / "picked"
    picked.mkdir()
    set_picked_data_dir(picked)

    set_picked_data_dir(default_data_dir())

    assert picked_data_dir() is None
    assert not (default_data_dir() / LOCATION_FILE).exists()


def test_an_unreadable_pointer_reads_as_the_default(local_app_data: Path) -> None:
    default_data_dir().mkdir(parents=True)
    (default_data_dir() / LOCATION_FILE).write_text("not json", encoding="utf-8")

    assert picked_data_dir() is None
    assert data_dir() == default_data_dir()


def test_a_legacy_config_moves_into_the_data_folder(tmp_path: Path, local_app_data: Path) -> None:
    legacy = tmp_path / "PAZ-Parser" / CONFIG_NAME
    legacy.parent.mkdir()
    legacy.write_text('{"language": "de"}', encoding="utf-8")

    adopt_legacy_config(legacy)

    assert config_file().read_text(encoding="utf-8") == '{"language": "de"}'
    assert not legacy.exists()


def test_a_config_already_in_the_data_folder_wins_over_the_legacy_one(tmp_path: Path, local_app_data: Path) -> None:
    legacy = tmp_path / CONFIG_NAME
    legacy.write_text('{"language": "de"}', encoding="utf-8")
    config_file().parent.mkdir(parents=True)
    config_file().write_text('{"language": "fr"}', encoding="utf-8")

    adopt_legacy_config(legacy)

    assert config_file().read_text(encoding="utf-8") == '{"language": "fr"}'
    assert legacy.exists()


def test_copying_the_user_files_replaces_the_target_and_keeps_the_source(tmp_path: Path) -> None:
    source = tmp_path / "old"
    target = tmp_path / "new"
    source.mkdir()
    target.mkdir()
    (source / CONFIG_NAME).write_text('{"language": "de"}', encoding="utf-8")
    (target / CONFIG_NAME).write_text('{"language": "fr"}', encoding="utf-8")
    (source / MAP_PINS_FILE).write_text('{"pins": []}', encoding="utf-8")

    copy_user_files(source, target)

    assert (target / CONFIG_NAME).read_text(encoding="utf-8") == '{"language": "de"}'
    assert (target / MAP_PINS_FILE).read_text(encoding="utf-8") == '{"pins": []}'
    assert (source / CONFIG_NAME).exists() and (source / MAP_PINS_FILE).exists()


def test_a_user_file_the_source_lacks_stays_in_the_target(tmp_path: Path) -> None:
    source = tmp_path / "old"
    target = tmp_path / "new"
    source.mkdir()
    target.mkdir()
    (target / MAP_PINS_FILE).write_text('{"pins": []}', encoding="utf-8")

    copy_user_files(source, target)

    assert (target / MAP_PINS_FILE).read_text(encoding="utf-8") == '{"pins": []}'


def test_caches_live_in_the_cache_folder_of_the_data_folder(tmp_path: Path) -> None:
    assert cache_root(tmp_path) == tmp_path / "cache"


# ── Client cache folders ─────────────────────────────────────────────────────


def test_each_paz_folder_gets_its_own_id(tmp_path: Path) -> None:
    assert client_id(tmp_path / "live" / "Paz") != client_id(tmp_path / "test" / "Paz")


def test_a_trailing_separator_keeps_the_id(tmp_path: Path) -> None:
    paz = tmp_path / "Paz"

    assert client_id(Path(f"{paz}{os.sep}")) == client_id(paz)


@pytest.mark.skipif(os.name != "nt", reason="Windows paths ignore case")
def test_letter_case_keeps_the_id_on_windows(tmp_path: Path) -> None:
    paz = tmp_path / "Paz"

    assert client_id(Path(str(paz).upper())) == client_id(paz)
    assert is_same_folder(Path(str(paz).lower()), paz)


def test_client_folder_is_created_with_a_marker_naming_the_paz_folder(tmp_path: Path) -> None:
    paz = tmp_path / "Paz"

    folder = client_cache_dir(tmp_path / "cache", paz)

    assert folder.parent == tmp_path / "cache"
    assert (folder / MARKER_FILE).read_text(encoding="utf-8") == str(paz.resolve())


def test_old_caches_move_out_of_the_game_folder(tmp_path: Path) -> None:
    paz = tmp_path / "Paz"
    paz.mkdir()
    (paz / "a.cache").write_bytes(b"old")
    (paz / "legacy.cache").write_bytes(b"old")
    cache_dir = client_cache_dir(tmp_path / "cache", paz)

    move_out_of_game_folder(paz, cache_dir, _NAMES, ("legacy.cache",))

    assert (cache_dir / "a.cache").read_bytes() == b"old"
    assert not (paz / "a.cache").exists()
    assert not (paz / "legacy.cache").exists()
    assert not (cache_dir / "legacy.cache").exists()


def test_a_cache_already_moved_wins_over_the_game_folder_copy(tmp_path: Path) -> None:
    paz = tmp_path / "Paz"
    paz.mkdir()
    (paz / "a.cache").write_bytes(b"old")
    cache_dir = client_cache_dir(tmp_path / "cache", paz)
    (cache_dir / "a.cache").write_bytes(b"new")

    move_out_of_game_folder(paz, cache_dir, _NAMES)

    assert (cache_dir / "a.cache").read_bytes() == b"new"
    assert not (paz / "a.cache").exists()


@pytest.mark.skipif(os.name != "nt", reason="Windows refuses to rename an open file")
def test_a_cache_another_process_has_open_stays_in_the_game_folder(tmp_path: Path) -> None:
    paz = tmp_path / "Paz"
    paz.mkdir()
    (paz / "a.cache").write_bytes(b"old")
    cache_dir = client_cache_dir(tmp_path / "cache", paz)

    with (paz / "a.cache").open("rb"):
        move_out_of_game_folder(paz, cache_dir, _NAMES)

    assert (paz / "a.cache").read_bytes() == b"old"
    assert not (cache_dir / "a.cache").exists()


def test_removing_a_root_deletes_only_marked_client_folders(tmp_path: Path) -> None:
    root = tmp_path / "cache"
    client = client_cache_dir(root, tmp_path / "Paz")
    for name in _NAMES:
        (client / name).write_bytes(b"x")
    foreign = root / "not ours"
    foreign.mkdir()
    (foreign / "a.cache").write_bytes(b"keep")

    errors = remove_cache_root(root, _NAMES)

    assert errors == []
    assert not client.exists()
    assert (foreign / "a.cache").read_bytes() == b"keep"


def test_removing_a_root_deletes_the_named_subfolders_of_client_folders(tmp_path: Path) -> None:
    root = tmp_path / "cache"
    client = client_cache_dir(root, tmp_path / "Paz")
    tiles = client / "map" / "3464" / "7"
    tiles.mkdir(parents=True)
    (tiles / "0.jpg").write_bytes(b"x")

    errors = remove_cache_root(root, _NAMES, ("map",))

    assert errors == []
    assert not client.exists()


def test_a_client_folder_with_other_files_is_kept_without_its_caches(tmp_path: Path) -> None:
    root = tmp_path / "cache"
    client = client_cache_dir(root, tmp_path / "Paz")
    (client / "a.cache").write_bytes(b"x")
    (client / "notes.txt").write_text("mine")

    remove_cache_root(root, _NAMES)

    assert not (client / "a.cache").exists()
    assert (client / "notes.txt").exists()


def test_an_emptied_root_is_removed(tmp_path: Path) -> None:
    root = tmp_path / "cache"
    client_cache_dir(root, tmp_path / "Paz")

    remove_cache_root(root, _NAMES)

    assert not root.exists()


def test_removing_a_missing_root_does_nothing(tmp_path: Path) -> None:
    assert remove_cache_root(tmp_path / "missing", _NAMES) == []
