"""The "Show only handled tables" setting: registry check, tree, searches, extraction."""
from __future__ import annotations

import json
import threading
from pathlib import Path

import pytest

import api.bdo_api as bdo_api
import api.bdo_config as bdo_config
from api.bdo_api import Api
from api.bdo_api_helpers import _file_icon
from api.bdo_tree import build_tree
from bdo_models import PazEntry
from bdo_preview import is_handled_file

_HANDLED_TABLE = "gamecommondata/binary/buff.dbss"
_HANDLED_WAYPOINT = "gamecommondata/waypoint_binary/patrol.bwp"
_UNHANDLED_TABLE = "gamecommondata/binary/no_handler_for_this.dbss"
_TEXTURE = "ui_texture/icon/new_icon.dds"
_PATHS = (_HANDLED_TABLE, _HANDLED_WAYPOINT, _UNHANDLED_TABLE, _TEXTURE)


@pytest.fixture
def config_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "paz_config.json"
    monkeypatch.setattr(bdo_config, "config_file", lambda: path)
    return path


def _entry(path: str) -> PazEntry:
    return PazEntry(
        archive_name="test.paz",
        internal_path=path,
        offset=0,
        compressed_size=10,
        uncompressed_size=10,
        compression_type=0,
        encryption_type=0,
    )


def _api(*, handled_only: bool) -> Api:
    api = Api()
    api._paz_root = Path("paz")
    api._entries = [_entry(path) for path in _PATHS]
    api._entry_map = {entry.internal_path: entry for entry in api._entries}
    api._tree_data = build_tree(api._entries)
    api._handled_only = handled_only
    return api


def _ids(items: list[dict]) -> set[str]:
    return {item["id"] for item in items}


# ── is_handled_file ──────────────────────────────────────────────────────────

def test_named_handler_is_handled() -> None:
    assert is_handled_file("buff.dbss")
    assert is_handled_file("Buff.DBSS")


def test_extension_handler_is_handled() -> None:
    assert is_handled_file("patrol.bwp")
    assert is_handled_file("languagedata_en.loc")


def test_builtin_views_and_unknown_tables_are_not_handled() -> None:
    assert not is_handled_file("new_icon.dds")
    assert not is_handled_file("readme.txt")
    assert not is_handled_file("no_handler_for_this.dbss")
    assert not is_handled_file("no_extension")


# ── Tree and file search ─────────────────────────────────────────────────────

def test_setting_off_shows_every_file() -> None:
    api = _api(handled_only=False)

    assert _ids(api.get_children("")) == {"gamecommondata", "ui_texture"}
    assert _ids(api.search("*")) == set(_PATHS)


def test_setting_on_hides_unhandled_files_and_empty_folders() -> None:
    api = _api(handled_only=True)

    assert _ids(api.get_children("")) == {"gamecommondata"}
    assert _ids(api.get_children("gamecommondata/binary")) == {_HANDLED_TABLE}
    assert api.get_children("ui_texture") == []


def test_setting_on_counts_only_handled_files() -> None:
    api = _api(handled_only=True)

    [root_dir] = api.get_children("")
    [binary_dir] = [d for d in api.get_children("gamecommondata") if d["name"] == "binary"]

    assert root_dir["count"] == 2
    assert binary_dir["count"] == 1


def test_setting_on_limits_file_search() -> None:
    api = _api(handled_only=True)

    assert _ids(api.search("*")) == {_HANDLED_TABLE, _HANDLED_WAYPOINT}


def test_disk_loc_stays_at_root() -> None:
    api = _api(handled_only=True)
    api._disk_companions = {"languagedata_en.loc": b""}

    assert "__disk__/languagedata_en.loc" in _ids(api.get_children(""))


def test_hidden_companion_still_loads(monkeypatch: pytest.MonkeyPatch) -> None:
    api = _api(handled_only=True)
    monkeypatch.setattr(bdo_api, "cached_read_entry_payload", lambda archive_path, entry: b"x")

    assert _UNHANDLED_TABLE not in _ids(api.search("*"))
    assert api._load_companion_sync(_UNHANDLED_TABLE) == b"x"


# ── Extraction ───────────────────────────────────────────────────────────────

def test_folder_selection_follows_the_visible_tree() -> None:
    assert _api(handled_only=False).get_selection_size(["gamecommondata"])["count"] == 3
    assert _api(handled_only=True).get_selection_size(["gamecommondata"])["count"] == 2


def test_empty_selection_path_selects_nothing() -> None:
    assert _api(handled_only=False).get_selection_size([""]) == {"count": 0, "bytes": 0}


def test_file_selection_is_counted_once() -> None:
    api = _api(handled_only=False)

    result = api.get_selection_size([_HANDLED_TABLE, "gamecommondata/binary"])

    assert result == {"count": 2, "bytes": 20}


# ── Global search ────────────────────────────────────────────────────────────

def test_global_search_scans_only_handled_files(monkeypatch: pytest.MonkeyPatch) -> None:
    api = _api(handled_only=True)
    scanned: list[str] = []
    done = threading.Event()

    def fake_run(needles, candidates, paz_root, cancel) -> None:
        scanned.extend(entry.internal_path for entry in candidates)
        done.set()

    monkeypatch.setattr(api, "_run_global_search", fake_run)

    result = api.search_all_files("abc", "string", [".dbss", ".dds"])

    assert result == {"total": 1}
    assert done.wait(5)
    assert scanned == [_HANDLED_TABLE]


# ── Settings ─────────────────────────────────────────────────────────────────

def test_setting_is_off_by_default(config_file: Path) -> None:
    assert Api().get_settings()["handled_only"] is False


def test_save_settings_stores_and_applies_setting(
    config_file: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    api = _api(handled_only=False)
    monkeypatch.setattr(api, "_reload_loc", lambda language: None)

    assert api.save_settings("", "en", handled_only=True)["ok"] is True

    assert json.loads(config_file.read_text())["handled_only"] is True
    assert api.get_settings()["handled_only"] is True
    assert _ids(api.get_children("")) == {"gamecommondata"}


@pytest.mark.parametrize(
    ("path", "icon"),
    [
        (_HANDLED_TABLE, "parsed"),
        (_HANDLED_WAYPOINT, "parsed"),
        (_UNHANDLED_TABLE, "file"),
        (_TEXTURE, "image"),
        ("languagedata_en.loc", "loc"),
        ("character/no_extension", "file"),
    ],
)
def test_tree_icon_follows_the_handler_registry(path: str, icon: str) -> None:
    assert _file_icon(Path(path).name) == icon
