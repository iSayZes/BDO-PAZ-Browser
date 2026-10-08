"""What the bottom bar shows: the app's version and the selected file's handler version."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pytest

import api.bdo_api_handler_updates as handler_updates
import bdo_preview
from api.bdo_api import Api
from bdo_preview import BUNDLED_HANDLERS_DIR, handler_key, load_plugins, plugin_failures
from cli.formats import run_handlers
from updates.handler_manifest import HandlerManifest, HandlerVersion, sha256_hex
from updates.handler_packs import Pack


def _pack(handlers: dict[str, str]) -> Pack:
    manifest = HandlerManifest(
        version="2026.10.12",
        commit="c",
        handler_api=1,
        files={"x.py": sha256_hex(b"x")},
        handlers={key: HandlerVersion(version, sha256_hex(key.encode())) for key, version in handlers.items()},
        notes="",
    )
    return Pack(Path("pack"), manifest, "installed")


def test_handler_key_is_the_key_the_handler_registered() -> None:
    assert handler_key("BuffSimply.bss", ".bss") == "buffsimply.bss"
    assert handler_key("languagedata_en.loc", ".loc") == ".loc"


@pytest.mark.parametrize("name", ["readme.txt", "unknown.zzz"])
def test_built_in_views_and_unknown_files_have_no_handler_key(name: str) -> None:
    assert handler_key(name, Path(name).suffix) is None


def test_the_handler_version_comes_from_the_running_pack(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(handler_updates, "active_pack", lambda: _pack({"buffsimply.bss": "2026.10.10"}))
    api = Api()
    assert api.get_handler_version("gamecommondata/binary/buffsimply.bss") == {
        "key": "buffsimply.bss", "version": "2026.10.10",
    }
    assert api.get_handler_version("ui_texture/readme.txt") == {}


def test_from_source_the_handler_version_is_the_commit_of_its_files(monkeypatch: pytest.MonkeyPatch) -> None:
    asked: list[Path] = []

    def commit_of(paths: list[Path]) -> str:
        asked.extend(paths)
        return "d2e474f+"

    monkeypatch.setattr(handler_updates, "active_pack", lambda: Pack(BUNDLED_HANDLERS_DIR, None, "bundled"))
    monkeypatch.setattr(handler_updates, "source_commit_of", commit_of)
    assert Api().get_handler_version("buffsimply.bss") == {"key": "buffsimply.bss", "version": "d2e474f+"}
    assert BUNDLED_HANDLERS_DIR / "_bss" / "buffsimply" / "handler.py" in asked


def test_from_source_without_git_there_is_no_handler_version(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(handler_updates, "active_pack", lambda: Pack(BUNDLED_HANDLERS_DIR, None, "bundled"))
    monkeypatch.setattr(handler_updates, "source_commit_of", lambda paths: None)
    assert Api().get_handler_version("buffsimply.bss") == {}


def test_from_source_the_app_version_is_the_commit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(handler_updates, "build_info", lambda: None)
    monkeypatch.setattr(handler_updates, "source_commit", lambda: "a1b2c3d")
    version = Api().get_app_version()
    assert version["commit"] == "a1b2c3d"
    assert "a1b2c3d" in version["label"]


def test_a_plugin_that_fails_to_import_fails_the_handler_list(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(bdo_preview, "_PLUGIN_FAILURES", {})
    (tmp_path / "broken_handler_for_test.py").write_text("raise ImportError('missing module')\n", encoding="utf-8")
    monkeypatch.syspath_prepend(str(tmp_path))
    load_plugins(tmp_path)
    monkeypatch.delitem(sys.modules, "broken_handler_for_test", raising=False)

    assert "broken_handler_for_test.py" in plugin_failures()
    assert run_handlers(argparse.Namespace()) == 1
    assert "broken_handler_for_test.py" in capsys.readouterr().err
