from __future__ import annotations

import threading
from collections import OrderedDict
from pathlib import Path

from bdo_models import PazEntry
from .bdo_payload_reader import read_entry_payload

_MAX_BYTES = 256 * 1024 * 1024  # 256 MB


class _PayloadCache:
    def __init__(self, max_bytes: int = _MAX_BYTES) -> None:
        self._max_bytes = max_bytes
        self._cache: OrderedDict[tuple, bytes] = OrderedDict()
        self._total = 0
        self._lock = threading.Lock()

    def get(self, archive_path: Path, entry: PazEntry) -> bytes | None:
        key = (str(archive_path), entry.offset, entry.compressed_size)
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
                return self._cache[key]
            return None

    def put(self, archive_path: Path, entry: PazEntry, data: bytes) -> None:
        if len(data) > self._max_bytes:
            return
        key = (str(archive_path), entry.offset, entry.compressed_size)
        with self._lock:
            if key in self._cache:
                self._total -= len(self._cache[key])
                del self._cache[key]
            while self._total + len(data) > self._max_bytes and self._cache:
                _, evicted = self._cache.popitem(last=False)
                self._total -= len(evicted)
            self._cache[key] = data
            self._total += len(data)

    def clear(self) -> None:
        with self._lock:
            self._cache.clear()
            self._total = 0

    @property
    def total_bytes(self) -> int:
        with self._lock:
            return self._total

    @property
    def entry_count(self) -> int:
        with self._lock:
            return len(self._cache)


_cache = _PayloadCache()


def cached_read_entry_payload(archive_path: Path, entry: PazEntry) -> bytes:
    hit = _cache.get(archive_path, entry)
    if hit is not None:
        return hit
    data = read_entry_payload(archive_path, entry)
    _cache.put(archive_path, entry, data)
    return data


def clear_payload_cache() -> None:
    _cache.clear()
