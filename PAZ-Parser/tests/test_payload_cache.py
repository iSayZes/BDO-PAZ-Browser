"""Unit tests for bdo_payload_cache._PayloadCache."""
from __future__ import annotations

import pytest

from bdo_models import PazEntry
from paz.bdo_payload_cache import _PayloadCache


def _entry(offset: int = 0, compressed_size: int = 10) -> PazEntry:
    return PazEntry(
        archive_name="test.paz",
        internal_path="foo.bin",
        offset=offset,
        compressed_size=compressed_size,
        uncompressed_size=compressed_size,
        compression_type=0,
        encryption_type=0,
    )


def _path(name: str = "archive.paz"):
    from pathlib import Path
    return Path(name)


# ── Basic hit / miss ──────────────────────────────────────────────────────────

def test_miss_returns_none() -> None:
    cache = _PayloadCache(max_bytes=1024)
    assert cache.get(_path(), _entry()) is None


def test_hit_returns_same_bytes() -> None:
    cache = _PayloadCache(max_bytes=1024)
    data = b"hello"
    e = _entry()
    cache.put(_path(), e, data)
    assert cache.get(_path(), e) is data


def test_different_offset_is_separate_key() -> None:
    cache = _PayloadCache(max_bytes=1024)
    e1 = _entry(offset=0)
    e2 = _entry(offset=100)
    cache.put(_path(), e1, b"aaa")
    cache.put(_path(), e2, b"bbb")
    assert cache.get(_path(), e1) == b"aaa"
    assert cache.get(_path(), e2) == b"bbb"


def test_different_archive_path_is_separate_key() -> None:
    cache = _PayloadCache(max_bytes=1024)
    e = _entry()
    cache.put(_path("a.paz"), e, b"aaa")
    cache.put(_path("b.paz"), e, b"bbb")
    assert cache.get(_path("a.paz"), e) == b"aaa"
    assert cache.get(_path("b.paz"), e) == b"bbb"


# ── LRU eviction ─────────────────────────────────────────────────────────────

def test_evicts_oldest_when_over_cap() -> None:
    cache = _PayloadCache(max_bytes=10)
    e1 = _entry(offset=0, compressed_size=5)
    e2 = _entry(offset=10, compressed_size=5)
    e3 = _entry(offset=20, compressed_size=5)
    cache.put(_path(), e1, b"a" * 5)
    cache.put(_path(), e2, b"b" * 5)
    # e3 pushes total to 15 — e1 (oldest) evicted
    cache.put(_path(), e3, b"c" * 5)
    assert cache.get(_path(), e1) is None
    assert cache.get(_path(), e2) == b"b" * 5
    assert cache.get(_path(), e3) == b"c" * 5


def test_access_promotes_to_most_recent() -> None:
    cache = _PayloadCache(max_bytes=10)
    e1 = _entry(offset=0, compressed_size=5)
    e2 = _entry(offset=10, compressed_size=5)
    e3 = _entry(offset=20, compressed_size=5)
    cache.put(_path(), e1, b"a" * 5)
    cache.put(_path(), e2, b"b" * 5)
    # access e1 — makes e2 the oldest
    cache.get(_path(), e1)
    cache.put(_path(), e3, b"c" * 5)
    assert cache.get(_path(), e1) == b"a" * 5  # promoted — survives
    assert cache.get(_path(), e2) is None        # evicted
    assert cache.get(_path(), e3) == b"c" * 5


def test_oversized_entry_not_cached() -> None:
    cache = _PayloadCache(max_bytes=4)
    e = _entry()
    cache.put(_path(), e, b"hello")  # 5 bytes > 4 cap
    assert cache.get(_path(), e) is None


# ── total_bytes / entry_count ──────────────────────────────────────────────────

def test_total_bytes_tracks_stored_data() -> None:
    cache = _PayloadCache(max_bytes=1024)
    cache.put(_path(), _entry(offset=0), b"abc")
    cache.put(_path(), _entry(offset=10), b"de")
    assert cache.total_bytes == 5
    assert cache.entry_count == 2


# ── clear ─────────────────────────────────────────────────────────────────────

def test_clear_empties_cache() -> None:
    cache = _PayloadCache(max_bytes=1024)
    e = _entry()
    cache.put(_path(), e, b"data")
    cache.clear()
    assert cache.get(_path(), e) is None
    assert cache.total_bytes == 0
    assert cache.entry_count == 0


# ── put overwrites existing entry ─────────────────────────────────────────────

def test_put_overwrites_existing_key() -> None:
    cache = _PayloadCache(max_bytes=1024)
    e = _entry()
    cache.put(_path(), e, b"old")
    cache.put(_path(), e, b"new-value")
    assert cache.get(_path(), e) == b"new-value"
    assert cache.total_bytes == len(b"new-value")
