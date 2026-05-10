"""Unit tests for Phase 3: PreviewHandler base lazy helpers (_data_cache, auto-lazy defaults)."""
from __future__ import annotations

import pytest

from bdo_models import PazEntry
from bdo_preview import PreviewHandler


# ── Minimal concrete handler for testing ────────────────────────────────────

class _SimpleHandler(PreviewHandler):
    """Minimal handler: only implements get_records + render_records_page."""

    def __init__(self) -> None:
        self.get_records_call_count = 0

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        self.get_records_call_count += 1
        return [{"value": b} for b in data[:3]]

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        start = page * page_size
        rows = "".join(f"<tr><td>{r['value']}</td></tr>" for r in records[start:start + page_size])
        return f"<table>{rows}</table>"


def _entry() -> PazEntry:
    return PazEntry(
        archive_name="test.paz",
        internal_path="foo.dbss",
        offset=0,
        compressed_size=3,
        uncompressed_size=3,
        compression_type=0,
        encryption_type=0,
    )


# ── supports_lazy_records default ────────────────────────────────────────────

def test_supports_lazy_records_default_true() -> None:
    assert _SimpleHandler().supports_lazy_records() is True


# ── get_record_count auto-lazy ────────────────────────────────────────────────

def test_get_record_count_uses_get_records() -> None:
    h = _SimpleHandler()
    data = bytes([10, 20, 30])
    assert h.get_record_count(data, _entry(), {}) == 3


def test_get_record_count_caches_result() -> None:
    h = _SimpleHandler()
    data = bytes([10, 20, 30])
    h.get_record_count(data, _entry(), {})
    h.get_record_count(data, _entry(), {})
    assert h.get_records_call_count == 1


# ── render_data_page auto-lazy ────────────────────────────────────────────────

def test_render_data_page_matches_render_records_page() -> None:
    h = _SimpleHandler()
    data = bytes([1, 2, 3])
    entry = _entry()
    html_lazy = h.render_data_page(data, entry, {}, 0, 10)
    records = h.get_records(data, entry, {})
    html_eager = h.render_records_page(records, 0, 10)
    assert html_lazy == html_eager


def test_render_data_page_reuses_cached_records() -> None:
    h = _SimpleHandler()
    data = bytes([1, 2, 3])
    entry = _entry()
    h.render_data_page(data, entry, {}, 0, 10)
    h.render_data_page(data, entry, {}, 0, 10)
    assert h.get_records_call_count == 1


# ── search_records auto-lazy ──────────────────────────────────────────────────

def test_search_records_finds_match() -> None:
    h = _SimpleHandler()
    data = bytes([10, 20, 30])
    indices = h.search_records(data, _entry(), {}, "10")
    assert 0 in indices


def test_search_records_returns_empty_for_no_match() -> None:
    h = _SimpleHandler()
    data = bytes([1, 2, 3])
    assert h.search_records(data, _entry(), {}, "999") == []


def test_search_records_reuses_cached_records() -> None:
    h = _SimpleHandler()
    data = bytes([1, 2, 3])
    entry = _entry()
    h.search_records(data, entry, {}, "1")
    h.search_records(data, entry, {}, "2")
    assert h.get_records_call_count == 1


# ── _data_cache ───────────────────────────────────────────────────────────────

def test_data_cache_returns_same_object_for_same_data() -> None:
    h = _SimpleHandler()
    data = b"hello"
    call_count = 0

    def build():
        nonlocal call_count
        call_count += 1
        return object()

    v1 = h._data_cache(data, "x", build)
    v2 = h._data_cache(data, "x", build)
    assert v1 is v2
    assert call_count == 1


def test_data_cache_rebuilds_on_new_data() -> None:
    h = _SimpleHandler()
    data1 = b"aaa"
    data2 = b"bbb"
    call_count = 0

    def build():
        nonlocal call_count
        call_count += 1
        return call_count

    h._data_cache(data1, "x", build)
    h._data_cache(data2, "x", build)
    assert call_count == 2


def test_data_cache_multiple_names_independent() -> None:
    h = _SimpleHandler()
    data = b"hello"
    v_a = h._data_cache(data, "a", lambda: "alpha")
    v_b = h._data_cache(data, "b", lambda: "beta")
    assert v_a == "alpha"
    assert v_b == "beta"
    assert h._data_cache(data, "a", lambda: "other") == "alpha"


def test_data_cache_survives_data_identity_change() -> None:
    h = _SimpleHandler()
    data1 = bytes(10)
    data2 = bytes(10)
    assert data1 == data2
    assert data1 is not data2

    v1 = h._data_cache(data1, "k", lambda: "first")
    v2 = h._data_cache(data2, "k", lambda: "second")
    assert v1 == "first"
    assert v2 == "second"
