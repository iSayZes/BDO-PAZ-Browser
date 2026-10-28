"""Disk cache for icon cell thumbnails, beside the PAZ entry cache.

A thumbnail of a large texture costs seconds: the 14 MB journal artwork of
`questjournalvideoinfo.bss` takes about 4.5 s just to decrypt and decompress.
Each finished thumbnail is stored here, so a texture is decoded once per client
content instead of once per session. The store is SQLite because thumbnails
arrive one at a time while the table scrolls; rewriting one pickle per icon, as
the index cache does for its single build, would not scale.

The store keys on the client's content key (`bdo_content_key.py`): a game
patch changes its version and a repack its archive row digest, and an open
with another key clears the store. A store that cannot be opened or written is disabled
for the session, logs a warning and keeps the reason in `error`; icons then
still load, just without the cache.
"""

from __future__ import annotations

import logging
import sqlite3
import threading
from pathlib import Path

CACHE_FILE = "paz_browser_thumbnails.sqlite"
_KEY_NAME = "content_key"

_SCHEMA = (
    "CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)",
    "CREATE TABLE IF NOT EXISTS thumbnails (path TEXT PRIMARY KEY, url TEXT NOT NULL)",
)


class ThumbnailCache:
    """Thumbnail data URLs by normalized icon path, for one client content key."""

    def __init__(self, cache_dir: Path, content_key: str) -> None:
        self._lock = threading.Lock()
        self._conn: sqlite3.Connection | None = None
        self.error = ""
        try:
            self._conn = self._open(cache_dir / CACHE_FILE, content_key)
        except sqlite3.Error as ex:
            self._disable(ex)

    @staticmethod
    def _open(path: Path, content_key: str) -> sqlite3.Connection:
        conn = sqlite3.connect(path, check_same_thread=False)
        try:
            for statement in _SCHEMA:
                conn.execute(statement)
            row = conn.execute("SELECT value FROM meta WHERE key = ?", (_KEY_NAME,)).fetchone()
            if row is None or row[0] != content_key:
                conn.execute("DELETE FROM thumbnails")
                # Also drops the `meta_version` row of stores keyed on the version alone.
                conn.execute("DELETE FROM meta")
                conn.execute("INSERT INTO meta (key, value) VALUES (?, ?)", (_KEY_NAME, content_key))
            conn.commit()
        except sqlite3.Error:
            conn.close()
            raise
        return conn

    def _disable(self, ex: sqlite3.Error) -> None:
        self.error = f"{CACHE_FILE}: {ex}"
        logging.warning("Thumbnail cache disabled: %s", self.error)
        if self._conn is not None:
            self._conn.close()
        self._conn = None

    def get(self, path: str) -> str | None:
        with self._lock:
            if self._conn is None:
                return None
            try:
                row = self._conn.execute("SELECT url FROM thumbnails WHERE path = ?", (path,)).fetchone()
            except sqlite3.Error as ex:
                self._disable(ex)
                return None
        return row[0] if row else None

    def put(self, path: str, url: str) -> None:
        with self._lock:
            if self._conn is None:
                return
            try:
                self._conn.execute(
                    "INSERT OR REPLACE INTO thumbnails (path, url) VALUES (?, ?)", (path, url)
                )
                self._conn.commit()
            except sqlite3.Error as ex:
                self._disable(ex)

    def close(self) -> None:
        with self._lock:
            if self._conn is not None:
                self._conn.close()
                self._conn = None
