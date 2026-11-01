from __future__ import annotations

import sqlite3
from pathlib import Path

from paz.bdo_thumbnail_cache import CACHE_FILE, ThumbnailCache

_PATH = "ui_texture/icon/quest/morningland_boss_03_02_full.dds"
_URL = "data:image/png;base64,AAAA"
_KEY = "3458-0123456789abcdef"


def test_thumbnail_survives_a_reopen_on_the_same_content_key(tmp_path: Path) -> None:
    cache = ThumbnailCache(tmp_path, _KEY)
    cache.put(_PATH, _URL)
    cache.close()

    reopened = ThumbnailCache(tmp_path, _KEY)

    assert reopened.get(_PATH) == _URL
    assert reopened.error == ""
    reopened.close()


def test_a_new_content_key_clears_the_store(tmp_path: Path) -> None:
    cache = ThumbnailCache(tmp_path, _KEY)
    cache.put(_PATH, _URL)
    cache.close()

    repacked = ThumbnailCache(tmp_path, "3458-fedcba9876543210")

    assert repacked.get(_PATH) is None
    repacked.close()


def test_a_store_keyed_on_the_meta_version_alone_is_cleared(tmp_path: Path) -> None:
    conn = sqlite3.connect(tmp_path / CACHE_FILE)
    conn.execute("CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
    conn.execute("CREATE TABLE thumbnails (path TEXT PRIMARY KEY, url TEXT NOT NULL)")
    conn.execute("INSERT INTO meta VALUES ('meta_version', '3458')")
    conn.execute("INSERT INTO thumbnails VALUES (?, ?)", (_PATH, _URL))
    conn.commit()
    conn.close()

    cache = ThumbnailCache(tmp_path, _KEY)

    assert cache.get(_PATH) is None
    cache.close()


def test_missing_entries_return_none(tmp_path: Path) -> None:
    cache = ThumbnailCache(tmp_path, _KEY)

    assert cache.get(_PATH) is None
    cache.close()


def test_an_unusable_folder_disables_the_cache(tmp_path: Path) -> None:
    cache = ThumbnailCache(tmp_path / "missing", _KEY)
    cache.put(_PATH, _URL)

    assert cache.error
    assert cache.get(_PATH) is None
