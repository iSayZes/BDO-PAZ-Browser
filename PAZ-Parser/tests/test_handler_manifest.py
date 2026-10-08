"""Handler pack manifests: pack files, per-handler versions, reading and refusing bad ones."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from bdo_preview import BUNDLED_HANDLERS_DIR
from updates.handler_manifest import (
    MANIFEST_FORMAT,
    HandlerManifest,
    HandlerVersion,
    ManifestError,
    build_manifest,
    file_hashes,
    handler_digest,
    manifest_json,
    next_pack_version,
    pack_file_bytes,
    pack_files,
    parse_manifest,
    sha256_hex,
)
from updates.handler_sets import handler_file_sets

HASH_A = sha256_hex(b"a")
HASH_B = sha256_hex(b"b")
HASH_C = sha256_hex(b"c")


def _manifest(**changes: object) -> HandlerManifest:
    fields: dict = {
        "version": "2026.10.12",
        "commit": "0123456789abcdef0123456789abcdef01234567",
        "handler_api": 1,
        "files": {"_bss/a/handler.py": HASH_A, "_common/shared.py": HASH_B},
        "handlers": {"a.bss": HandlerVersion("2026.10.12", HASH_C)},
        "notes": "### Fixes\n\n- fix: a\n",
    }
    return HandlerManifest(**{**fields, **changes})


def _payload(**changes: object) -> dict:
    return {**json.loads(manifest_json(_manifest())), **changes}


# ── Pack files ────────────────────────────────────────────────────────────────

def test_pack_files_leave_out_tests_bytecode_and_the_manifest(tmp_path: Path) -> None:
    for name in ("x_handler.py", "_bss/a/handler.py", "_bss/a/test_handler.py", "_bss/a/lang/en.json",
                 "_bss/a/__pycache__/handler.cpython-312.pyc", "manifest.json"):
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"x")
    assert list(pack_files(tmp_path)) == ["_bss/a/handler.py", "_bss/a/lang/en.json", "x_handler.py"]


def test_text_files_ship_with_lf_line_endings(tmp_path: Path) -> None:
    source, data, binary = tmp_path / "a.py", tmp_path / "a.json", tmp_path / "a.bin"
    for path in (source, data, binary):
        path.write_bytes(b"one\r\ntwo\r\n")
    assert pack_file_bytes(source) == b"one\ntwo\n"
    assert pack_file_bytes(data) == b"one\ntwo\n"
    assert pack_file_bytes(binary) == b"one\r\ntwo\r\n"


def test_a_crlf_checkout_hashes_like_an_lf_one(tmp_path: Path) -> None:
    lf, crlf = tmp_path / "lf", tmp_path / "crlf"
    for folder, text in ((lf, b"a = 1\n"), (crlf, b"a = 1\r\n")):
        folder.mkdir()
        (folder / "a.py").write_bytes(text)
    assert file_hashes(lf) == file_hashes(crlf)


# ── Handler versions ──────────────────────────────────────────────────────────

def test_a_new_pack_starts_every_handler_at_its_version() -> None:
    files = {"a.py": HASH_A, "b.py": HASH_B}
    manifest = build_manifest("2026.10.12", "c", 1, files, {"a.bss": ["a.py"], "b.bss": ["b.py"]}, None, "")
    assert {key: handler.version for key, handler in manifest.handlers.items()} == {
        "a.bss": "2026.10.12", "b.bss": "2026.10.12",
    }


def test_only_handlers_whose_files_changed_get_the_new_version() -> None:
    sets = {"a.bss": ["a.py", "shared.py"], "b.bss": ["b.py"], "c.bss": ["c.py", "shared.py"]}
    old_files = {"a.py": HASH_A, "b.py": HASH_A, "c.py": HASH_A, "shared.py": HASH_A}
    old = build_manifest("2026.10.12", "c1", 1, old_files, sets, None, "")

    new = build_manifest("2026.10.14", "c2", 1, {**old_files, "b.py": HASH_B}, sets, old, "")
    assert new.handlers["a.bss"] == old.handlers["a.bss"]
    assert new.handlers["b.bss"].version == "2026.10.14"

    shared = build_manifest("2026.10.15", "c3", 1, {**old_files, "shared.py": HASH_C}, sets, old, "")
    assert shared.handlers["a.bss"].version == "2026.10.15"
    assert shared.handlers["c.bss"].version == "2026.10.15"
    assert shared.handlers["b.bss"] == old.handlers["b.bss"]


def test_a_handler_file_outside_the_pack_is_refused() -> None:
    with pytest.raises(ManifestError):
        handler_digest(["missing.py"], {"a.py": HASH_A})


def test_same_pack_means_same_files_and_handler_api() -> None:
    assert _manifest().is_same_pack(_manifest(version="2026.10.13", commit="other", notes=""))
    assert not _manifest().is_same_pack(_manifest(handler_api=2))
    assert not _manifest().is_same_pack(_manifest(files={"_bss/a/handler.py": HASH_C}))


@pytest.mark.parametrize(("previous", "today", "expected"), [
    (None, "2026.10.12", "2026.10.12"),
    ("2026.10.11", "2026.10.12", "2026.10.12"),
    ("2026.10.12", "2026.10.12", "2026.10.12.2"),
    ("2026.10.12.2", "2026.10.12", "2026.10.12.3"),
])
def test_next_pack_version(previous: str | None, today: str, expected: str) -> None:
    manifest = _manifest(version=previous) if previous else None
    assert next_pack_version(manifest, today) == expected


def test_the_real_handlers_read_their_own_module_and_common_files() -> None:
    sets = handler_file_sets(BUNDLED_HANDLERS_DIR)
    files = file_hashes(BUNDLED_HANDLERS_DIR)
    assert all(names and set(names) <= set(files) for names in sets.values())
    assert "_bss/buffsimply/handler.py" in sets["buffsimply.bss"]
    assert any(name.startswith("_common/") for name in sets["buffsimply.bss"])


# ── Reading ───────────────────────────────────────────────────────────────────

def test_a_manifest_reads_back_as_written() -> None:
    assert parse_manifest(json.loads(manifest_json(_manifest()))) == _manifest()


@pytest.mark.parametrize("changes", [
    {"format": MANIFEST_FORMAT + 1},
    {"version": "latest"},
    {"commit": ""},
    {"handler_api": "1"},
    {"files": {}},
    {"files": {"../outside.py": HASH_A}},
    {"files": {"_bss\\a.py": HASH_A}},
    {"files": {"C:/a.py": HASH_A}},
    {"files": {"_bss/test_a.py": HASH_A}},
    {"files": {"a.py": "not a hash"}},
    {"handlers": {"a.bss": {"version": "2026.10.12"}}},
], ids=lambda changes: next(iter(changes)) + "=" + str(next(iter(changes.values())))[:20])
def test_a_malformed_manifest_is_refused(changes: dict) -> None:
    with pytest.raises(ManifestError):
        parse_manifest(_payload(**changes))
