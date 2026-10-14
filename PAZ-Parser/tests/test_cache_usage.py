"""Cache sizes and deletes per settings tab (`api/bdo_api_cache_usage.py`)."""
from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import pytest

import api.bdo_api_cache_usage as usage
import api.bdo_api_caches as caches
from api.bdo_api import Api
from api.bdo_api_cache_usage import CACHE_KINDS
from api.bdo_api_caches import CACHE_FILES
from app_dirs import MARKER_FILE, cache_root, client_cache_dir
from paz import bdo_cache, bdo_index_cache, bdo_records_cache
from world_map_build import MAP_FOLDER


@pytest.fixture
def data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """An empty Data Folder the API reads as the one in use."""
    folder = tmp_path / "data"
    monkeypatch.setattr(usage, "data_dir", lambda: folder)
    return folder


@pytest.fixture
def api(data: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Api]:
    """An API with a loaded folder whose cache folder holds every cache."""
    monkeypatch.setattr(caches, "records_cache_setting", lambda cfg: "open")
    api = Api()
    api._paz_root = tmp_path / "Paz"
    api._cache_dir = client_cache_dir(cache_root(data), api._paz_root)
    _fill_client(api._cache_dir)
    yield api
    api._close_records_cache()
    api._close_thumbnail_cache()


def _fill_client(folder: Path) -> None:
    for name in CACHE_FILES:
        (folder / name).write_bytes(b"x" * 10)
    tiles = folder / MAP_FOLDER / "1" / "7"
    tiles.mkdir(parents=True)
    (tiles / "0.jpg").write_bytes(b"x" * 10)


def _other_client(data: Path, paz_root: Path) -> Path:
    folder = client_cache_dir(cache_root(data), paz_root)
    _fill_client(folder)
    return folder


def test_every_cache_file_belongs_to_one_kind() -> None:
    files = [name for kind in CACHE_KINDS for name in kind.files]

    assert sorted(files) == sorted(CACHE_FILES)
    assert len({kind.id for kind in CACHE_KINDS}) == len(CACHE_KINDS)


def test_delete_all_keeps_the_paz_index() -> None:
    kept = [kind.id for kind in CACHE_KINDS if not kind.in_delete_all]

    assert kept == ["pazIndex"]


def test_usage_lists_every_kind_with_its_tab_and_size(api: Api) -> None:
    caches = api.get_cache_usage()["caches"]

    assert [cache["id"] for cache in caches] == [kind.id for kind in CACHE_KINDS]
    assert {cache["id"]: cache["tab"] for cache in caches}["records"] == "files"
    assert all(cache["bytes"] > 0 for cache in caches)


def test_usage_without_a_loaded_folder_lists_no_caches(data: Path) -> None:
    assert Api().get_cache_usage() == {"caches": [], "other_clients": []}


def test_deleting_one_cache_leaves_the_others(api: Api) -> None:
    assert api._cache_dir is not None

    result = api.delete_cache("records")

    assert result["ok"]
    assert result["freed"] > 0
    assert (api._cache_dir / bdo_index_cache.CACHE_FILE).is_file()
    assert (api._cache_dir / MAP_FOLDER).is_dir()


def test_deleting_the_map_removes_its_folder(api: Api) -> None:
    assert api._cache_dir is not None

    assert api.delete_cache("map")["ok"]

    assert not (api._cache_dir / MAP_FOLDER).exists()


def test_an_unknown_cache_is_refused(api: Api) -> None:
    assert not api.delete_cache("nope")["ok"]


def test_delete_all_deletes_all_but_the_paz_index(api: Api) -> None:
    assert api._cache_dir is not None

    assert api.delete_caches()["ok"]

    assert (api._cache_dir / bdo_cache.CACHE_FILE).is_file()
    assert not (api._cache_dir / bdo_index_cache.CACHE_FILE).exists()
    assert not (api._cache_dir / MAP_FOLDER).exists()


def test_other_clients_are_listed_with_their_folder(api: Api, data: Path, tmp_path: Path) -> None:
    gone = _other_client(data, tmp_path / "Uninstalled")
    present_root = tmp_path / "Test client"
    present_root.mkdir()
    present = _other_client(data, present_root)

    clients = {client["id"]: client for client in api.get_cache_usage()["other_clients"]}

    assert set(clients) == {gone.name, present.name}
    assert clients[present.name]["exists"]
    assert not clients[gone.name]["exists"]
    assert clients[gone.name]["folder"] == str((tmp_path / "Uninstalled").resolve())
    assert clients[gone.name]["bytes"] > 0


def test_deleting_another_client_removes_its_folder(api: Api, data: Path, tmp_path: Path) -> None:
    other = _other_client(data, tmp_path / "Uninstalled")

    result = api.delete_other_client_cache(other.name)

    assert result["ok"]
    assert not other.exists()


def test_the_loaded_folder_is_not_another_client(api: Api) -> None:
    assert api._cache_dir is not None

    result = api.delete_other_client_cache(api._cache_dir.name)

    assert not result["ok"]
    assert (api._cache_dir / MARKER_FILE).is_file()
    assert (api._cache_dir / bdo_records_cache.CACHE_FILE).is_file()
