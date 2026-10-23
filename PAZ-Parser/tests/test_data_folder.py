"""The "Data Folder" setting: where a folder load keeps its caches, and switching folders."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from api.bdo_api import Api
from api.bdo_config import config_file, load_config
from app_dirs import cache_root, client_id, data_dir, default_data_dir, picked_data_dir
from bdo_models import PazEntry
from paz.bdo_cache import CACHE_FILE, CachedEntries, load_cache

_VERSION = 3458
_ENTRIES = [PazEntry("pad00001.paz", "gamecommondata/binary/a.dbss", 0, 10, 20, 0, 0)]


@pytest.fixture(autouse=True)
def local_app_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A fresh default Data Folder, with no records store.

    The records store would install itself as the handlers' global records
    source, so the config turns it off.
    """
    local = tmp_path / "local"
    monkeypatch.setenv("LOCALAPPDATA", str(local))
    default_data_dir().mkdir(parents=True)
    config_file().write_text(json.dumps({"records_cache": "off"}))
    return local


def _loaded_api(paz_root: Path) -> Api:
    """An Api with `paz_root` loaded, as far as the caches need it."""
    paz_root.mkdir(exist_ok=True)
    api = Api()
    api._paz_root = paz_root
    api._meta_version = _VERSION
    api._entries = list(_ENTRIES)
    api._open_cache_dir(paz_root)
    return api


def _cache_dir(api: Api) -> Path:
    assert api.cache_dir is not None
    return api.cache_dir


def _save(api: Api, paz_root: Path, data_folder: str, language: str = "en") -> dict:
    return api.save_settings(str(paz_root), language, data_folder=data_folder)


def test_a_folder_load_keeps_its_caches_outside_the_game_folder(tmp_path: Path) -> None:
    paz_root = tmp_path / "Paz"
    paz_root.mkdir()
    (paz_root / CACHE_FILE).write_bytes(b"old")

    api = _loaded_api(paz_root)

    assert _cache_dir(api) == cache_root(default_data_dir()) / client_id(paz_root)
    assert (_cache_dir(api) / CACHE_FILE).read_bytes() == b"old"
    assert not (paz_root / CACHE_FILE).exists()


def test_a_new_data_folder_gets_the_settings_and_the_entry_list(tmp_path: Path) -> None:
    paz_root = tmp_path / "Paz"
    api = _loaded_api(paz_root)
    old_cache_root = cache_root(default_data_dir())
    new_folder = tmp_path / "elsewhere"

    result = _save(api, paz_root, str(new_folder), language="de")

    assert result["ok"] is True
    assert result["cache_error"] == ""
    assert data_dir() == new_folder
    assert load_config()["language"] == "de"
    assert api.get_settings()["data_folder"] == str(new_folder)
    assert api.cache_dir == cache_root(new_folder) / client_id(paz_root)
    assert load_cache(_cache_dir(api)) == CachedEntries(_VERSION, (), _ENTRIES)
    assert not old_cache_root.exists()


def test_the_old_folder_keeps_its_copy_of_the_settings(tmp_path: Path) -> None:
    paz_root = tmp_path / "Paz"
    api = _loaded_api(paz_root)
    old_config = config_file()

    _save(api, paz_root, str(tmp_path / "elsewhere"))

    assert old_config.exists()
    assert config_file() != old_config


def test_settings_already_in_the_new_folder_are_replaced(tmp_path: Path) -> None:
    paz_root = tmp_path / "Paz"
    api = _loaded_api(paz_root)
    new_folder = tmp_path / "synced"
    new_folder.mkdir()
    (new_folder / "paz_config.json").write_text(json.dumps({"language": "fr", "records_cache": "off"}))

    _save(api, paz_root, str(new_folder), language="en")

    assert load_config()["language"] == "en"


def test_switching_back_to_the_default_forgets_the_pick(tmp_path: Path) -> None:
    paz_root = tmp_path / "Paz"
    api = _loaded_api(paz_root)
    _save(api, paz_root, str(tmp_path / "elsewhere"))

    _save(api, paz_root, "")

    assert picked_data_dir() is None
    assert data_dir() == default_data_dir()
    assert api.cache_dir == cache_root(default_data_dir()) / client_id(paz_root)


def test_saving_the_same_data_folder_keeps_its_caches(tmp_path: Path) -> None:
    paz_root = tmp_path / "Paz"
    api = _loaded_api(paz_root)
    kept = _cache_dir(api) / "paz_browser_thumbnails.sqlite"
    kept.write_bytes(b"x")

    _save(api, paz_root, str(default_data_dir()))

    assert kept.exists()


def test_a_relative_data_folder_is_refused_before_anything_changes(tmp_path: Path) -> None:
    paz_root = tmp_path / "Paz"
    api = _loaded_api(paz_root)
    cache_dir = _cache_dir(api)

    result = _save(api, paz_root, "relative/data", language="de")

    assert result["ok"] is False
    assert data_dir() == default_data_dir()
    assert "language" not in load_config()
    assert api.cache_dir == cache_dir
