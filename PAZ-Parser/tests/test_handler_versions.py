"""Handler versions: the bottom bar, `--records --json` and `--handler-version`; the app's version."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pytest

import api.bdo_api_handler_updates as handler_updates
import bdo_preview
import updates.handler_versions as handler_versions
from api.bdo_api import Api
from bdo_preview import BUNDLED_HANDLERS_DIR, handler_key, load_plugins, plugin_failures
from cli.formats import run_handler_version, run_handlers
from cli.records import json_export
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
    monkeypatch.setattr(handler_versions, "active_pack", lambda: _pack({"buffsimply.bss": "2026.10.10"}))
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

    monkeypatch.setattr(handler_versions, "active_pack", lambda: Pack(BUNDLED_HANDLERS_DIR, None, "bundled"))
    monkeypatch.setattr(handler_versions, "source_commit_of", commit_of)
    assert Api().get_handler_version("buffsimply.bss") == {"key": "buffsimply.bss", "version": "d2e474f+"}
    assert BUNDLED_HANDLERS_DIR / "_bss" / "buffsimply" / "handler.py" in asked


def test_from_source_without_git_there_is_no_handler_version(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(handler_versions, "active_pack", lambda: Pack(BUNDLED_HANDLERS_DIR, None, "bundled"))
    monkeypatch.setattr(handler_versions, "source_commit_of", lambda paths: None)
    assert Api().get_handler_version("buffsimply.bss") == {}


def test_a_key_the_manifest_lacks_has_no_version(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(handler_versions, "active_pack", lambda: _pack({}))
    assert Api().get_handler_version("buffsimply.bss") == {}
    assert json_export("gamecommondata/binary/buffsimply.bss", 3464, [])["handler_version"] is None


def test_the_records_json_names_the_file_client_handler_and_version(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(handler_versions, "active_pack", lambda: _pack({".loc": "2026.10.10"}))
    rows = [{"key": 1, "text": "Adventure's Boon"}]
    assert json_export("languagedata_en.loc", 3464, rows) == {
        "file": "languagedata_en.loc",
        "client_version": 3464,
        "handler": ".loc",
        "handler_version": "2026.10.10",
        "records": rows,
    }


def _version_args(name: str, *, json: bool = False) -> argparse.Namespace:
    return argparse.Namespace(handler_version=name, json=json, csv=False)


def test_handler_version_prints_the_key_and_version(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(handler_versions, "active_pack", lambda: _pack({"buffsimply.bss": "2026.10.10"}))
    assert run_handler_version(_version_args("gamecommondata/binary/buffsimply.bss", json=True)) == 0
    assert json.loads(capsys.readouterr().out) == [{"handler": "buffsimply.bss", "version": "2026.10.10"}]


def test_handler_version_without_a_name_lists_every_handler(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(handler_versions, "active_pack", lambda: _pack({"buffsimply.bss": "2026.10.10"}))
    assert run_handler_version(_version_args("", json=True)) == 0
    listed = {row["handler"]: row["version"] for row in json.loads(capsys.readouterr().out)}
    assert set(listed) == set(bdo_preview.get_binary_handlers())
    assert listed["buffsimply.bss"] == "2026.10.10"
    assert listed[".loc"] is None


@pytest.mark.parametrize(("name", "message"), [("readme.txt", "no handler reads"), (".loc", "has no version")])
def test_handler_version_fails_without_a_handler_or_a_version(
    name: str, message: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(handler_versions, "active_pack", lambda: _pack({}))
    assert run_handler_version(_version_args(name)) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert message in captured.err


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
