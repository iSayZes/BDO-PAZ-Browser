"""The handler pack manifest: the files of a pack, their hashes, and each handler's version.

A handler pack is the `handlers/` folder of one commit without its tests, as
plain files. Text files (`.py`, `.json`) go in with LF line endings, as git
stores them and raw.githubusercontent.com serves them, so a file hashes the
same in the exe's bundled pack, in a downloaded pack and on GitHub.

`manifest.json` sits in the pack folder and, for the newest pack, in the
`handlers-latest` release:

    {
      "format": 1,
      "version": "2026.10.12",          date version of the pack
      "commit": "<sha>",                commit whose files raw.githubusercontent.com serves
      "handler_api": 1,                 handler_api.HANDLER_API the pack was written for
      "files": {"_bss/buffsimply/handler.py": "<sha256>", ...},
      "handlers": {"buffsimply.bss": {"version": "2026.10.12", "digest": "<sha256>"}, ...},
      "notes": "### Fixes\\n- fix: ..."
    }

A handler's version is the pack version in which its code last changed: the
module that defines it, the project modules it imports (with `_common`), and
the JSON files next to them. `digest` hashes that file set, so the next pack
keeps the version of every handler whose digest did not change.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

from app_version import parse_version

MANIFEST_NAME = "manifest.json"
MANIFEST_FORMAT = 1
# Stored with LF line endings in the pack, whatever the checkout uses.
_TEXT_SUFFIXES = frozenset({".py", ".json"})
_SHA256_LENGTH = 64


class ManifestError(ValueError):
    """A manifest is malformed or written in another format; the message says what."""


@dataclass(frozen=True)
class HandlerVersion:
    version: str
    digest: str


@dataclass(frozen=True)
class HandlerManifest:
    version: str
    commit: str
    handler_api: int
    # Path under handlers/, with forward slashes -> SHA-256 of the file.
    files: Mapping[str, str]
    # Registry key (`buffsimply.bss`, `.loc`) -> its version.
    handlers: Mapping[str, HandlerVersion]
    notes: str

    def is_same_pack(self, other: HandlerManifest) -> bool:
        """True when both hold the same files for the same handler API."""
        return self.handler_api == other.handler_api and dict(self.files) == dict(other.files)


# ── Pack files ────────────────────────────────────────────────────────────────

def is_pack_file(relative: Path) -> bool:
    """True for a file under handlers/ that ships in a pack: no tests, no bytecode."""
    return (
        "__pycache__" not in relative.parts
        and not relative.name.startswith("test_")
        and relative.suffix != ".pyc"
        and relative != Path(MANIFEST_NAME)
    )


def pack_file_bytes(path: Path) -> bytes:
    """A pack file's content as it ships: text files with LF line endings."""
    data = path.read_bytes()
    return data.replace(b"\r\n", b"\n") if path.suffix in _TEXT_SUFFIXES else data


def pack_files(handlers_dir: Path) -> dict[str, Path]:
    """Every pack file under `handlers_dir`, by its path with forward slashes, sorted."""
    found = {
        path.relative_to(handlers_dir).as_posix(): path
        for path in handlers_dir.rglob("*")
        if path.is_file() and is_pack_file(path.relative_to(handlers_dir))
    }
    return dict(sorted(found.items()))


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_hashes(handlers_dir: Path) -> dict[str, str]:
    """SHA-256 of every pack file under `handlers_dir`, as it ships."""
    return {name: sha256_hex(pack_file_bytes(path)) for name, path in pack_files(handlers_dir).items()}


# ── Building ──────────────────────────────────────────────────────────────────

def handler_digest(names: Iterable[str], files: Mapping[str, str]) -> str:
    """Hash of a handler's file set, from the hashes in `files`.

    Raises ManifestError when a file of the set is not a pack file.
    """
    digest = hashlib.sha256()
    for name in sorted(set(names)):
        file_hash = files.get(name)
        if file_hash is None:
            raise ManifestError(f"{name} is used by a handler but is not in the pack")
        digest.update(f"{name}\0{file_hash}\n".encode("utf-8"))
    return digest.hexdigest()


def build_manifest(
    version: str,
    commit: str,
    handler_api: int,
    files: Mapping[str, str],
    handler_files: Mapping[str, Iterable[str]],
    previous: HandlerManifest | None,
    notes: str,
) -> HandlerManifest:
    """The manifest of a pack, handler versions carried over from `previous`.

    `handler_files` maps each registry key to the pack files its code reads.
    """
    old = previous.handlers if previous is not None else {}
    handlers: dict[str, HandlerVersion] = {}
    for key in sorted(handler_files):
        digest = handler_digest(handler_files[key], files)
        kept = old.get(key)
        handlers[key] = kept if kept is not None and kept.digest == digest else HandlerVersion(version, digest)
    return HandlerManifest(version, commit, handler_api, dict(sorted(files.items())), handlers, notes)


def next_pack_version(previous: HandlerManifest | None, today: str) -> str:
    """`today`, or `today.N` when `previous` is a pack from today already."""
    if previous is None:
        return today
    old = parse_version(previous.version)
    if old[:3] != parse_version(today):
        return today
    return f"{today}.{(old[3] if len(old) > 3 else 1) + 1}"


# ── Reading and writing ───────────────────────────────────────────────────────

def manifest_json(manifest: HandlerManifest) -> str:
    """The manifest as JSON text, keys in a stable order, LF line endings."""
    payload = {
        "format": MANIFEST_FORMAT,
        "version": manifest.version,
        "commit": manifest.commit,
        "handler_api": manifest.handler_api,
        "files": dict(manifest.files),
        "handlers": {
            key: {"version": handler.version, "digest": handler.digest}
            for key, handler in manifest.handlers.items()
        },
        "notes": manifest.notes,
    }
    return json.dumps(payload, indent=1, ensure_ascii=False) + "\n"


def write_manifest(manifest: HandlerManifest, path: Path) -> None:
    path.write_text(manifest_json(manifest), encoding="utf-8", newline="\n")


def read_manifest(path: Path) -> HandlerManifest:
    """Raises ManifestError for a malformed manifest, OSError when it can't be read."""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as ex:
        raise ManifestError(f"{path} is not JSON: {ex}") from ex
    return parse_manifest(payload)


def parse_manifest(payload: object) -> HandlerManifest:
    """A manifest from its JSON value. Raises ManifestError when anything is off."""
    if not isinstance(payload, dict):
        raise ManifestError("the manifest is not a JSON object")
    if payload.get("format") != MANIFEST_FORMAT:
        raise ManifestError(f"the manifest has format {payload.get('format')!r}, this app reads {MANIFEST_FORMAT}")
    version = _version(payload.get("version"), "version")
    commit = payload.get("commit")
    handler_api = payload.get("handler_api")
    notes = payload.get("notes", "")
    if not isinstance(commit, str) or not commit:
        raise ManifestError("the manifest has no commit")
    if not isinstance(handler_api, int) or isinstance(handler_api, bool):
        raise ManifestError("the manifest has no handler_api number")
    if not isinstance(notes, str):
        raise ManifestError("the manifest notes are not text")
    return HandlerManifest(version, commit, handler_api, _files(payload.get("files")), _handlers(payload.get("handlers")), notes)


def _version(value: object, field: str) -> str:
    if not isinstance(value, str):
        raise ManifestError(f"the manifest {field} is not a date version")
    try:
        parse_version(value)
    except ValueError as ex:
        raise ManifestError(f"the manifest {field}: {ex}") from ex
    return value


def _files(value: object) -> dict[str, str]:
    if not isinstance(value, dict) or not value:
        raise ManifestError("the manifest lists no files")
    for name, file_hash in value.items():
        if not is_safe_pack_path(name):
            raise ManifestError(f"the manifest lists a file outside the pack: {name!r}")
        if not _is_sha256(file_hash):
            raise ManifestError(f"the manifest hash of {name} is not a SHA-256")
    return dict(value)


def _handlers(value: object) -> dict[str, HandlerVersion]:
    if not isinstance(value, dict):
        raise ManifestError("the manifest has no handlers table")
    handlers: dict[str, HandlerVersion] = {}
    for key, entry in value.items():
        if not isinstance(entry, dict) or not _is_sha256(entry.get("digest")):
            raise ManifestError(f"the manifest entry of handler {key!r} is malformed")
        handlers[key] = HandlerVersion(_version(entry.get("version"), f"version of {key}"), entry["digest"])
    return handlers


def is_safe_pack_path(name: object) -> bool:
    """True for a relative path with forward slashes that stays inside the pack folder."""
    if not isinstance(name, str) or not name or "\\" in name or ":" in name or name.startswith("/"):
        return False
    parts = name.split("/")
    return all(part not in ("", ".", "..") for part in parts) and is_pack_file(Path(*parts))


def _is_sha256(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == _SHA256_LENGTH
        and all(char in "0123456789abcdef" for char in value)
    )
