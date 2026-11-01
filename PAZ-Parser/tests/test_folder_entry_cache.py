"""A folder load reuses the entry cache only while the meta version, the meta file and the archive files match; the content key follows the archive rows."""
from __future__ import annotations

import json
import os
import struct
from pathlib import Path

import pytest

from api.bdo_api import Api
from api.bdo_config import config_file
from app_dirs import default_data_dir
from bdo_models import PazEntry
from paz import bdo_index_cache

_VERSION = 435


@pytest.fixture(autouse=True)
def local_app_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A fresh default Data Folder, with no records store."""
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "local"))
    default_data_dir().mkdir(parents=True)
    config_file().write_text(json.dumps({"records_cache": "off"}))


class _CountingParse:
    """Stands in for the meta parse: one entry per archive file on disk."""

    def __init__(self) -> None:
        self.calls = 0

    def __call__(self, meta_path: Path) -> list[PazEntry]:
        self.calls += 1
        archives = sorted(path.name.lower() for path in meta_path.parent.glob("*.paz"))
        return [PazEntry(name, f"gamecommondata/{name}.bss", 0, 1, 1, 0, 0) for name in archives]


def _client(tmp_path: Path, *archives: str) -> Path:
    paz_root = tmp_path / "Paz"
    paz_root.mkdir(exist_ok=True)
    (paz_root / "pad00000.meta").write_bytes(struct.pack("<II", _VERSION, 0))
    for name in archives:
        (paz_root / name).write_bytes(b"")
    return paz_root


def _load(api: Api, paz_root: Path, parse: _CountingParse) -> None:
    api.load_folder(paz_root, parse=parse, load_loc=False, load_indexes=False)


def test_a_second_load_of_the_same_folder_uses_the_cache(tmp_path: Path) -> None:
    paz_root = _client(tmp_path, "PAD00001.PAZ")
    parse = _CountingParse()
    api = Api()

    _load(api, paz_root, parse)
    _load(api, paz_root, parse)

    assert parse.calls == 1


def test_an_added_archive_parses_again_and_drops_the_lookup_indexes(tmp_path: Path) -> None:
    paz_root = _client(tmp_path, "PAD00001.PAZ")
    parse = _CountingParse()
    api = Api()
    _load(api, paz_root, parse)
    assert api.cache_dir is not None
    index_cache = api.cache_dir / bdo_index_cache.CACHE_FILE
    index_cache.write_bytes(b"built without pad00002")

    _client(tmp_path, "PAD00002.PAZ")
    _load(api, paz_root, parse)

    assert parse.calls == 2
    assert {entry.archive_name for entry in api._entries} == {"pad00001.paz", "pad00002.paz"}
    assert not index_cache.exists()


def test_a_deleted_archive_parses_again(tmp_path: Path) -> None:
    paz_root = _client(tmp_path, "PAD00001.PAZ", "PAD00002.PAZ")
    parse = _CountingParse()
    api = Api()
    _load(api, paz_root, parse)

    (paz_root / "PAD00002.PAZ").unlink()
    _load(api, paz_root, parse)

    assert parse.calls == 2
    assert {entry.archive_name for entry in api._entries} == {"pad00001.paz"}


def test_a_repacked_meta_file_parses_again_and_drops_the_lookup_indexes(tmp_path: Path) -> None:
    paz_root = _client(tmp_path, "PAD00001.PAZ")
    parse = _CountingParse()
    api = Api()
    _load(api, paz_root, parse)
    assert api.cache_dir is not None
    index_cache = api.cache_dir / bdo_index_cache.CACHE_FILE
    index_cache.write_bytes(b"built from the old offsets")

    # Same version, archives and size; only the modification time tells.
    meta = paz_root / "pad00000.meta"
    later = meta.stat().st_mtime_ns + 2_000_000_000
    os.utime(meta, ns=(later, later))
    _load(api, paz_root, parse)

    assert parse.calls == 2
    assert not index_cache.exists()


def test_a_rewritten_archive_row_gives_a_new_content_key(tmp_path: Path) -> None:
    paz_root = _client(tmp_path, "PAD00001.PAZ")
    meta = paz_root / "pad00000.meta"
    meta.write_bytes(struct.pack("<IIIII", _VERSION, 1, 1, 0x1234ABCD, 4_096))
    api = Api()
    _load(api, paz_root, _CountingParse())
    before = api._content_key

    meta.write_bytes(struct.pack("<IIIII", _VERSION, 1, 1, 0x1234ABCE, 4_096))
    _load(api, paz_root, _CountingParse())

    assert before is not None and api._content_key is not None
    assert api._content_key != before
    assert api._content_key.startswith(f"{_VERSION}-")
