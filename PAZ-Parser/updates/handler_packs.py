"""Handler packs in the exe: which pack runs, installing a newer one, removing old ones.

    <Data Folder>\\handlers\\
        current.json            {"version": "2026.10.12"}: the pack the next start runs
        bad.json                {"2026.10.13": "<why>"}: packs that failed to load, never tried again
        2026.10.12\\             a pack: the handler files and its manifest.json
        2026.10.14.partial\\     a pack being installed

The exe's own `handlers\\` folder is the bundled pack, with a manifest written
by build.py. A start runs the installed pack when it is usable and newer than
the bundled one, so an app update that bundles newer handlers wins. From
source, `PAZ-Parser/handlers` runs and none of this applies.

An install builds `<version>.partial\\`: files whose hash is unchanged are
copied from the running pack, the others are downloaded from
raw.githubusercontent.com at the manifest's commit. Every hash is checked,
the pack must load in `bdo-paz-cli.exe --handlers`, then the folder is renamed
and `current.json` switched. A failure at any step leaves the running pack in
place; a pack that does not load is marked bad. The new pack runs from the
next start; old ones are removed on a later start, when no other copy of the
app runs.
"""

from __future__ import annotations

import json
import logging
import os
import shutil
import subprocess
import sys
import urllib.request
from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Literal

from app_dirs import data_dir
from app_version import is_frozen, parse_version
from bdo_preview import BUNDLED_HANDLERS_DIR
from handler_api import HANDLER_API

from .handler_manifest import (
    MANIFEST_NAME,
    HandlerManifest,
    ManifestError,
    file_hashes,
    manifest_json,
    parse_manifest,
    read_manifest,
    sha256_hex,
)
from .releases import REPO, UpdateError

PACKS_FOLDER = "handlers"
CURRENT_FILE = "current.json"
BAD_FILE = "bad.json"
PARTIAL_SUFFIX = ".partial"
# BDO_PAZ_HANDLERS_URL and BDO_PAZ_HANDLER_FILES_URL test an update without
# GitHub, file:// URLs too. The files URL has {commit} and {path} fields.
MANIFEST_URL = (
    os.environ.get("BDO_PAZ_HANDLERS_URL")
    or f"https://github.com/{REPO}/releases/download/handlers-latest/{MANIFEST_NAME}"
)
FILES_URL = (
    os.environ.get("BDO_PAZ_HANDLER_FILES_URL")
    or f"https://raw.githubusercontent.com/{REPO}/{{commit}}/PAZ-Parser/handlers/{{path}}"
)
# Runs one pack for one process, set by the install check below; also handy to try a pack by hand.
PACK_OVERRIDE_ENV = "BDO_PAZ_HANDLERS_DIR"
# Seconds. The manifest check runs on every start; files come from a CDN.
CHECK_TIMEOUT = 3
FILE_TIMEOUT = 15
VALIDATE_TIMEOUT = 120
DOWNLOAD_WORKERS = 8
CLI_EXE = "bdo-paz-cli.exe"

Fetch = Callable[[str, float], bytes]
Validate = Callable[[Path, HandlerManifest], None]
# installed: switched to the newer pack, it runs from the next start.
# up_to_date: nothing newer. needs_app: the pack is for another HANDLER_API.
# bad: the newer pack failed to load here before.
Outcome = Literal["installed", "up_to_date", "needs_app", "bad"]
# bundled: the exe's own handlers/ (or PAZ-Parser/handlers from source).
# installed: a pack in the Data Folder. override: PACK_OVERRIDE_ENV.
PackSource = Literal["bundled", "installed", "override"]


class PackLoadError(UpdateError):
    """A downloaded pack does not load in this app; it is marked bad."""


@dataclass(frozen=True)
class Pack:
    """A handlers folder the app can run, and its manifest (None from source)."""

    folder: Path
    manifest: HandlerManifest | None
    source: PackSource

    @property
    def version(self) -> str | None:
        return self.manifest.version if self.manifest is not None else None


@dataclass(frozen=True)
class PackCheck:
    """What a check against the published pack found."""

    outcome: Outcome
    latest: HandlerManifest
    downloaded: int = 0


def packs_dir() -> Path:
    return data_dir() / PACKS_FOLDER


# ── Picking the pack to run ───────────────────────────────────────────────────

@cache
def active_pack() -> Pack:
    """The pack this process runs, picked once, before the core imports `_common`."""
    override = os.environ.get(PACK_OVERRIDE_ENV)
    if override:
        folder = Path(override)
        return Pack(folder, _manifest_or_none(folder), "override")
    if not is_frozen():
        return Pack(BUNDLED_HANDLERS_DIR, None, "bundled")
    return choose_pack(packs_dir(), bundled_pack(), HANDLER_API)


def bundled_pack() -> Pack:
    return Pack(BUNDLED_HANDLERS_DIR, _manifest_or_none(BUNDLED_HANDLERS_DIR), "bundled")


def choose_pack(store: Path, bundled: Pack, handler_api: int) -> Pack:
    """The installed pack when it is usable and newer than `bundled`, else `bundled`."""
    installed = installed_pack(store, handler_api)
    if installed is None or installed.manifest is None:
        return bundled
    if bundled.manifest is not None and not _is_newer(installed.manifest, bundled.manifest):
        return bundled
    return installed


def installed_pack(store: Path, handler_api: int) -> Pack | None:
    """The pack `current.json` names, or None when there is none or it can't run."""
    version = _current_version(store)
    if version is None:
        return None
    folder = store / version
    problem = pack_problem(store, version, handler_api)
    if problem is not None:
        logging.info("Not running handler pack %s: %s", version, problem)
        return None
    return Pack(folder, read_manifest(folder / MANIFEST_NAME), "installed")


def pack_problem(store: Path, version: str, handler_api: int) -> str | None:
    """Why installed pack `version` can't run, or None when it can."""
    bad = bad_packs(store).get(version)
    if bad is not None:
        return f"it failed to load before ({bad})"
    try:
        manifest = read_manifest(store / version / MANIFEST_NAME)
    except (OSError, ManifestError) as ex:
        return f"its manifest is unreadable ({ex})"
    if manifest.version != version:
        return f"its manifest is for {manifest.version}"
    if manifest.handler_api != handler_api:
        return f"it needs handler API {manifest.handler_api}, this app has {handler_api}"
    return None


def bad_packs(store: Path) -> dict[str, str]:
    """Version -> why it failed to load, for every pack marked bad."""
    try:
        saved = json.loads((store / BAD_FILE).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except (OSError, ValueError):
        logging.warning("Ignoring unreadable %s", store / BAD_FILE, exc_info=True)
        return {}
    if not isinstance(saved, dict):
        return {}
    return {version: str(reason) for version, reason in saved.items() if isinstance(version, str)}


def mark_bad(store: Path, version: str, reason: str) -> None:
    """Never run or install pack `version` again."""
    try:
        _write_json(store / BAD_FILE, {**bad_packs(store), version: reason})
    except OSError:
        logging.warning("Could not mark handler pack %s bad", version, exc_info=True)
    logging.warning("Handler pack %s marked bad: %s", version, reason)


def mark_running_pack_bad(pack: Pack, reason: str) -> None:
    """Mark the running pack bad when it is an installed one; the next start runs the bundled pack."""
    if pack.source == "installed" and pack.version is not None:
        mark_bad(pack.folder.parent, pack.version, reason)


def _current_version(store: Path) -> str | None:
    try:
        saved = json.loads((store / CURRENT_FILE).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError):
        logging.warning("Ignoring unreadable %s", store / CURRENT_FILE, exc_info=True)
        return None
    version = saved.get("version") if isinstance(saved, dict) else None
    if not isinstance(version, str):
        return None
    try:
        parse_version(version)
    except ValueError:
        return None
    return version


def _manifest_or_none(folder: Path) -> HandlerManifest | None:
    try:
        return read_manifest(folder / MANIFEST_NAME)
    except FileNotFoundError:
        return None
    except (OSError, ManifestError):
        logging.warning("Ignoring the unreadable manifest in %s", folder, exc_info=True)
        return None


def _is_newer(manifest: HandlerManifest, than: HandlerManifest) -> bool:
    return parse_version(manifest.version) > parse_version(than.version)


# ── Updating ──────────────────────────────────────────────────────────────────

def fetch_latest(fetch: Fetch | None = None) -> HandlerManifest:
    """The published pack's manifest. Raises UpdateError when it can't be read."""
    data = (fetch or http_get)(MANIFEST_URL, CHECK_TIMEOUT)
    try:
        return parse_manifest(json.loads(data.decode("utf-8")))
    except (ValueError, ManifestError) as ex:
        raise UpdateError(f"the published handler manifest is unreadable: {ex}") from ex


def update_pack(
    running: Pack,
    store: Path,
    latest: HandlerManifest,
    fetch: Fetch | None = None,
    validate: Validate | None = None,
    handler_api: int = HANDLER_API,
) -> PackCheck:
    """Install `latest` when it is newer than both the running and the installed pack.

    Raises UpdateError when the install fails; the running pack stays.
    """
    if latest.handler_api != handler_api:
        return PackCheck("needs_app", latest)
    newest = _newest_known(running, installed_pack(store, handler_api))
    if newest is not None and not _is_newer(latest, newest):
        return PackCheck("up_to_date", latest)
    if latest.version in bad_packs(store):
        return PackCheck("bad", latest)
    downloaded = install_pack(latest, running, store, fetch or http_get, validate or validate_with_cli)
    return PackCheck("installed", latest, downloaded)


def _newest_known(running: Pack, installed: Pack | None) -> HandlerManifest | None:
    manifests = [pack.manifest for pack in (running, installed) if pack is not None and pack.manifest is not None]
    return max(manifests, key=lambda manifest: parse_version(manifest.version), default=None)


def install_pack(latest: HandlerManifest, running: Pack, store: Path, fetch: Fetch, validate: Validate) -> int:
    """Build, check and switch to `latest`. Returns how many files were downloaded."""
    partial = store / f"{latest.version}{PARTIAL_SUFFIX}"
    shutil.rmtree(partial, ignore_errors=True)
    have = file_hashes(running.folder)
    missing = [name for name, file_hash in latest.files.items() if have.get(name) != file_hash]
    try:
        partial.mkdir(parents=True)
        for name in latest.files.keys() - set(missing):
            _copy(running.folder / name, partial / name)
        _download_all(latest, missing, partial, fetch)
        (partial / MANIFEST_NAME).write_text(manifest_json(latest), encoding="utf-8", newline="\n")
        try:
            validate(partial, latest)
        except PackLoadError as ex:
            mark_bad(store, latest.version, str(ex))
            raise
        final = store / latest.version
        shutil.rmtree(final, ignore_errors=True)
        partial.rename(final)
    except OSError as ex:
        raise UpdateError(f"could not install handler pack {latest.version} in {store}: {ex}") from ex
    finally:
        shutil.rmtree(partial, ignore_errors=True)
    _write_current(store, latest.version)
    logging.info("Installed handler pack %s, %d files downloaded", latest.version, len(missing))
    return len(missing)


def _copy(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def _download_all(latest: HandlerManifest, names: Iterable[str], target: Path, fetch: Fetch) -> None:
    def download(name: str) -> None:
        url = FILES_URL.format(commit=latest.commit, path=name)
        data = fetch(url, FILE_TIMEOUT)
        if sha256_hex(data) != latest.files[name]:
            raise UpdateError(f"{name} of handler pack {latest.version} does not match its SHA-256")
        path = target / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    with ThreadPoolExecutor(max_workers=DOWNLOAD_WORKERS, thread_name_prefix="handler-pack") as pool:
        # list() re-raises the first failed download here.
        list(pool.map(download, names))


def _write_current(store: Path, version: str) -> None:
    """Point `current.json` at `version`."""
    try:
        _write_json(store / CURRENT_FILE, {"version": version})
    except OSError as ex:
        raise UpdateError(f"could not switch to handler pack {version}: {ex}") from ex


def _write_json(path: Path, value: object) -> None:
    """Write `value` to `path` atomically: a temp file, then a rename."""
    temp = path.with_name(f"{path.name}.tmp")
    temp.write_text(json.dumps(value, indent=1), encoding="utf-8")
    os.replace(temp, path)


def http_get(url: str, timeout: float) -> bytes:
    """The body of `url`. Raises UpdateError."""
    request = urllib.request.Request(url, headers={"User-Agent": "BDO-PAZ-Browser"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except (OSError, ValueError) as ex:
        raise UpdateError(f"could not download {url}: {ex}") from ex


def validate_with_cli(folder: Path, manifest: HandlerManifest) -> None:
    """The pack must load in this exe's CLI and register exactly the manifest's handlers."""
    cli = Path(sys.executable).resolve().parent / CLI_EXE
    try:
        result = subprocess.run(
            [str(cli), "--handlers"],
            env={**os.environ, PACK_OVERRIDE_ENV: str(folder)},
            capture_output=True, text=True, encoding="utf-8", timeout=VALIDATE_TIMEOUT,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    except (OSError, subprocess.SubprocessError) as ex:
        raise UpdateError(f"could not check handler pack {manifest.version} with {cli.name}: {ex}") from ex
    if result.returncode != 0:
        lines = result.stderr.strip().splitlines() or [f"exit code {result.returncode}"]
        raise PackLoadError(f"handler pack {manifest.version} does not load: {lines[-1].removeprefix('Error: ')}")
    if set(result.stdout.split()) != set(manifest.handlers):
        raise PackLoadError(f"handler pack {manifest.version} registers other handlers than its manifest lists")


# ── Cleanup ───────────────────────────────────────────────────────────────────

def remove_old_packs(store: Path, keep: Iterable[str]) -> None:
    """Delete pack folders other than `keep`, and unfinished installs.

    Call it only while no other copy of the app runs: one may still import
    from its pack lazily.
    """
    kept = set(keep)
    if not store.is_dir():
        return
    for child in store.iterdir():
        if child.is_dir() and child.name not in kept:
            shutil.rmtree(child, ignore_errors=True)
            logging.info("Removed old handler pack %s", child.name)


def versions_to_keep(store: Path, running: Pack) -> set[str]:
    """The running pack and the one `current.json` names."""
    return {version for version in (running.version, _current_version(store)) if version is not None}


# ── Entry points ──────────────────────────────────────────────────────────────

def check_for_update(fetch: Fetch | None = None, validate: Validate | None = None) -> PackCheck:
    """Check the published pack and install it when newer; the GUI and the CLI call this.

    Raises UpdateError when GitHub can't be reached or the install fails.
    """
    return update_pack(active_pack(), packs_dir(), fetch_latest(fetch), fetch, validate)


def clean_up_packs() -> None:
    """Remove old packs, unless another copy of the app runs (it may use one)."""
    from .install import other_instances_running

    if other_instances_running():
        logging.info("Another copy of the app runs; old handler packs stay for now")
        return
    store = packs_dir()
    remove_old_packs(store, versions_to_keep(store, active_pack()))
