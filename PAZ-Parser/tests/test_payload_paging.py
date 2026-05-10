"""Unit tests for Phase 2 range-read and hex-render APIs."""
from __future__ import annotations

import pytest

from bdo_models import PazEntry
from paz.bdo_payload_reader import can_range_read, read_entry_range
from bdo_preview import HEX_ROWS_PER_PAGE, HexHandler


# ── Helpers ───────────────────────────────────────────────────────────────────

def _entry(
    *,
    path: str = "foo.dbss",
    offset: int = 0,
    compressed: int = 100,
    uncompressed: int = 100,
) -> PazEntry:
    return PazEntry(
        archive_name="test.paz",
        internal_path=path,
        offset=offset,
        compressed_size=compressed,
        uncompressed_size=uncompressed,
        compression_type=0,
        encryption_type=0,
    )


# ── can_range_read ────────────────────────────────────────────────────────────

def test_can_range_read_raw_dbss() -> None:
    assert can_range_read(_entry(path="foo.dbss", compressed=100, uncompressed=100))


def test_can_range_read_compressed_dbss() -> None:
    assert not can_range_read(_entry(path="foo.dbss", compressed=60, uncompressed=100))


def test_can_range_read_non_dbss() -> None:
    assert not can_range_read(_entry(path="foo.bss", compressed=100, uncompressed=100))


def test_can_range_read_compressed_non_dbss() -> None:
    assert not can_range_read(_entry(path="foo.bss", compressed=60, uncompressed=100))


# ── read_entry_range — direct seek path ──────────────────────────────────────

def test_read_entry_range_direct_full(tmp_path: pytest.TempPathFactory) -> None:
    payload = bytes(range(256))
    archive = tmp_path / "test.paz" # type: ignore
    archive.write_bytes(b"\x00" * 16 + payload)  # 16-byte header before payload

    entry = _entry(path="foo.dbss", offset=16, compressed=256, uncompressed=256)
    result = read_entry_range(archive, entry, 0, 256)
    assert result == payload


def test_read_entry_range_direct_slice(tmp_path: pytest.TempPathFactory) -> None:
    payload = bytes(range(256))
    archive = tmp_path / "test.paz" # type: ignore
    archive.write_bytes(b"\x00" * 16 + payload)

    entry = _entry(path="foo.dbss", offset=16, compressed=256, uncompressed=256)
    result = read_entry_range(archive, entry, 10, 20)
    assert result == payload[10:30]


def test_read_entry_range_direct_matches_full_payload_slice(tmp_path: pytest.TempPathFactory) -> None:
    payload = bytes(range(256))
    archive = tmp_path / "test.paz" # type: ignore
    archive.write_bytes(b"\x00" * 16 + payload)

    entry = _entry(path="foo.dbss", offset=16, compressed=256, uncompressed=256)
    for page in range(4):
        offset = page * 64
        assert read_entry_range(archive, entry, offset, 64) == payload[offset : offset + 64]


def test_read_entry_range_clamps_at_end(tmp_path: pytest.TempPathFactory) -> None:
    payload = bytes(range(100))
    archive = tmp_path / "test.paz" # type: ignore
    archive.write_bytes(payload)

    entry = _entry(path="foo.dbss", offset=0, compressed=100, uncompressed=100)
    result = read_entry_range(archive, entry, 90, 50)
    assert result == payload[90:]
    assert len(result) == 10


def test_read_entry_range_past_end_returns_empty(tmp_path: pytest.TempPathFactory) -> None:
    payload = bytes(range(100))
    archive = tmp_path / "test.paz" # type: ignore
    archive.write_bytes(payload)

    entry = _entry(path="foo.dbss", offset=0, compressed=100, uncompressed=100)
    result = read_entry_range(archive, entry, 100, 50)
    assert result == b""


# ── HexHandler.render_bytes ───────────────────────────────────────────────────

def test_render_bytes_produces_hex_view() -> None:
    h = HexHandler()
    chunk = bytes(range(16))
    html = h.render_bytes(chunk, 0)
    assert '<div class="hex-view">' in html
    assert "00000000" in html  # offset


def test_render_bytes_base_offset_reflected() -> None:
    h = HexHandler()
    chunk = bytes(range(16))
    html = h.render_bytes(chunk, 0x100)
    assert "00000100" in html


def test_render_bytes_matches_render_page_slice() -> None:
    h = HexHandler()
    data = bytes(range(256))
    page_size_bytes = HEX_ROWS_PER_PAGE * 16
    for page in range(2):
        base = page * page_size_bytes
        chunk = data[base : base + page_size_bytes]
        assert h.render_bytes(chunk, base) == h.render_page(data, page)


# ── HexHandler.page_count_for_size ───────────────────────────────────────────

def test_page_count_for_size_zero() -> None:
    assert HexHandler.page_count_for_size(0) == 1


def test_page_count_for_size_one_page() -> None:
    one_page = HEX_ROWS_PER_PAGE * 16
    assert HexHandler.page_count_for_size(one_page) == 1
    assert HexHandler.page_count_for_size(one_page - 1) == 1


def test_page_count_for_size_two_pages() -> None:
    one_page = HEX_ROWS_PER_PAGE * 16
    assert HexHandler.page_count_for_size(one_page + 1) == 2


def test_page_count_for_size_matches_page_count() -> None:
    for size in [0, 1, 255, 256, 8192, 8193, 65536]:
        data = bytes(size)
        assert HexHandler.page_count_for_size(size) == HexHandler.page_count(data), (
            f"mismatch at size={size}"
        )
