"""Handler packs in the Data Folder: which one runs, installing a newer one, cleanup."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import updates.handler_packs as handler_packs
from updates.handler_manifest import (
    MANIFEST_NAME,
    HandlerManifest,
    HandlerVersion,
    file_hashes,
    sha256_hex,
    write_manifest,
)
from updates.handler_packs import (
    BAD_FILE,
    CURRENT_FILE,
    Pack,
    PackLoadError,
    bad_packs,
    choose_pack,
    installed_pack,
    mark_bad,
    mark_running_pack_bad,
    remove_old_packs,
    update_pack,
    versions_to_keep,
)
from updates.releases import UpdateError

API = 1
OLD_FILES = {"x_handler.py": b"x = 1\n", "_common/shared.py": b"shared = 1\n"}


def _manifest(version: str, files: dict[str, bytes], handler_api: int = API) -> HandlerManifest:
    return HandlerManifest(
        version=version,
        commit=f"commit-{version}",
        handler_api=handler_api,
        files={name: sha256_hex(data) for name, data in files.items()},
        handlers={"x.bss": HandlerVersion(version, sha256_hex(b"digest"))},
        notes="",
    )


def _write_pack(folder: Path, version: str, files: dict[str, bytes], handler_api: int = API) -> HandlerManifest:
    for name, data in files.items():
        path = folder / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    manifest = _manifest(version, files, handler_api)
    write_manifest(manifest, folder / MANIFEST_NAME)
    return manifest


def _install(store: Path, version: str, files: dict[str, bytes], handler_api: int = API) -> HandlerManifest:
    manifest = _write_pack(store / version, version, files, handler_api)
    (store / CURRENT_FILE).write_text(json.dumps({"version": version}), encoding="utf-8")
    return manifest


@pytest.fixture
def store(tmp_path: Path) -> Path:
    folder = tmp_path / "data" / "handlers"
    folder.mkdir(parents=True)
    return folder


@pytest.fixture
def bundled(tmp_path: Path) -> Pack:
    folder = tmp_path / "bundled"
    return Pack(folder, _write_pack(folder, "2026.10.07", OLD_FILES), "bundled")


class FakeGitHub:
    """Serves pack files by URL and counts what was fetched."""

    def __init__(self, manifest: HandlerManifest, files: dict[str, bytes]) -> None:
        self.files = {handler_packs.FILES_URL.format(commit=manifest.commit, path=name): data for name, data in files.items()}
        self.fetched: list[str] = []

    def __call__(self, url: str, timeout: float) -> bytes:
        self.fetched.append(url)
        if url not in self.files:
            raise UpdateError(f"404 {url}")
        return self.files[url]


def _no_check(folder: Path, manifest: HandlerManifest) -> None:
    pass


# ── Picking the pack ──────────────────────────────────────────────────────────

def test_without_an_installed_pack_the_bundled_one_runs(store: Path, bundled: Pack) -> None:
    assert choose_pack(store, bundled, API) == bundled


def test_a_newer_installed_pack_runs(store: Path, bundled: Pack) -> None:
    _install(store, "2026.10.12", OLD_FILES)
    picked = choose_pack(store, bundled, API)
    assert picked.source == "installed"
    assert picked.version == "2026.10.12"


def test_an_app_update_with_newer_bundled_handlers_wins(store: Path, bundled: Pack) -> None:
    _install(store, "2026.10.05", OLD_FILES)
    assert choose_pack(store, bundled, API) == bundled


@pytest.mark.parametrize("problem", ["bad", "other_api", "garbled_current", "missing_folder"])
def test_an_unusable_installed_pack_falls_back_to_the_bundled_one(store: Path, bundled: Pack, problem: str) -> None:
    _install(store, "2026.10.12", OLD_FILES, handler_api=API + 1 if problem == "other_api" else API)
    if problem == "bad":
        mark_bad(store, "2026.10.12", "broken")
    elif problem == "garbled_current":
        (store / CURRENT_FILE).write_text("{not json", encoding="utf-8")
    elif problem == "missing_folder":
        (store / CURRENT_FILE).write_text(json.dumps({"version": "2026.10.13"}), encoding="utf-8")
    assert choose_pack(store, bundled, API) == bundled


def test_a_running_pack_that_fails_to_load_is_marked_bad(store: Path, bundled: Pack) -> None:
    _install(store, "2026.10.12", OLD_FILES)
    installed = installed_pack(store, API)
    assert installed is not None
    mark_running_pack_bad(installed, "x_handler.py: ImportError")
    mark_running_pack_bad(bundled, "x_handler.py: ImportError")
    assert list(bad_packs(store)) == ["2026.10.12"]
    assert not (bundled.folder.parent / BAD_FILE).exists()
    assert choose_pack(store, bundled, API) == bundled


# ── Updating ──────────────────────────────────────────────────────────────────

def test_an_update_downloads_only_changed_files(store: Path, bundled: Pack) -> None:
    new_files = {**OLD_FILES, "_common/shared.py": b"shared = 2\n", "y_handler.py": b"y = 1\n"}
    latest = _manifest("2026.10.12", new_files)
    github = FakeGitHub(latest, new_files)

    check = update_pack(bundled, store, latest, github, _no_check, API)

    assert check.outcome == "installed"
    assert sorted(url.rsplit("/", 1)[-1] for url in github.fetched) == ["shared.py", "y_handler.py"]
    installed = installed_pack(store, API)
    assert installed is not None and installed.version == "2026.10.12"
    assert file_hashes(installed.folder) == dict(latest.files)


def test_files_the_new_pack_drops_are_not_copied(store: Path, bundled: Pack) -> None:
    new_files = {"x_handler.py": OLD_FILES["x_handler.py"]}
    latest = _manifest("2026.10.12", new_files)
    update_pack(bundled, store, latest, FakeGitHub(latest, new_files), _no_check, API)
    assert not (store / "2026.10.12" / "_common" / "shared.py").exists()


@pytest.mark.parametrize("failure", ["bad_hash", "missing_file", "check_fails"])
def test_a_failed_install_keeps_the_running_pack(store: Path, bundled: Pack, failure: str) -> None:
    _install(store, "2026.10.10", OLD_FILES)
    new_files = {**OLD_FILES, "y_handler.py": b"y = 1\n"}
    latest = _manifest("2026.10.12", new_files)
    served = {**new_files, "y_handler.py": b"tampered\n"} if failure == "bad_hash" else new_files
    if failure == "missing_file":
        served = OLD_FILES

    def check(folder: Path, manifest: HandlerManifest) -> None:
        if failure == "check_fails":
            raise UpdateError("does not load")

    running = installed_pack(store, API)
    assert running is not None
    with pytest.raises(UpdateError):
        update_pack(running, store, latest, FakeGitHub(latest, served), check, API)
    assert installed_pack(store, API) == running
    assert sorted(child.name for child in store.iterdir()) == ["2026.10.10", CURRENT_FILE]


def test_a_pack_that_does_not_load_is_never_downloaded_again(store: Path, bundled: Pack) -> None:
    new_files = {**OLD_FILES, "y_handler.py": b"raise ImportError\n"}
    latest = _manifest("2026.10.12", new_files)

    def check(folder: Path, manifest: HandlerManifest) -> None:
        raise PackLoadError("y_handler.py failed to load")

    with pytest.raises(PackLoadError):
        update_pack(bundled, store, latest, FakeGitHub(latest, new_files), check, API)
    github = FakeGitHub(latest, new_files)
    assert update_pack(bundled, store, latest, github, check, API).outcome == "bad"
    assert github.fetched == []
    assert installed_pack(store, API) is None


def test_the_install_check_sees_the_complete_pack(store: Path, bundled: Pack) -> None:
    new_files = {**OLD_FILES, "y_handler.py": b"y = 1\n"}
    latest = _manifest("2026.10.12", new_files)
    seen: dict[str, str] = {}

    def check(folder: Path, manifest: HandlerManifest) -> None:
        seen.update(file_hashes(folder))
        assert (folder / MANIFEST_NAME).is_file()

    update_pack(bundled, store, latest, FakeGitHub(latest, new_files), check, API)
    assert seen == dict(latest.files)


@pytest.mark.parametrize(("installed", "outcome"), [
    ("2026.10.12", "up_to_date"),
    ("2026.10.13", "up_to_date"),
    (None, "needs_app"),
    ("bad", "bad"),
])
def test_nothing_is_installed_when(store: Path, bundled: Pack, installed: str | None, outcome: str) -> None:
    latest = _manifest("2026.10.12", OLD_FILES, handler_api=API + 1 if outcome == "needs_app" else API)
    if installed == "bad":
        mark_bad(store, "2026.10.12", "broken")
    elif installed is not None:
        _install(store, installed, OLD_FILES)
    github = FakeGitHub(latest, OLD_FILES)

    assert update_pack(bundled, store, latest, github, _no_check, API).outcome == outcome
    assert github.fetched == []


# ── Cleanup ───────────────────────────────────────────────────────────────────

def test_cleanup_keeps_the_running_and_the_current_pack(store: Path) -> None:
    for version in ("2026.10.07", "2026.10.10", "2026.10.12"):
        _write_pack(store / version, version, OLD_FILES)
    (store / "2026.10.13.partial").mkdir()
    (store / CURRENT_FILE).write_text(json.dumps({"version": "2026.10.12"}), encoding="utf-8")
    mark_bad(store, "2026.10.14", "broken")
    running = Pack(store / "2026.10.10", _manifest("2026.10.10", OLD_FILES), "installed")

    remove_old_packs(store, versions_to_keep(store, running))

    assert sorted(child.name for child in store.iterdir()) == ["2026.10.10", "2026.10.12", BAD_FILE, CURRENT_FILE]
