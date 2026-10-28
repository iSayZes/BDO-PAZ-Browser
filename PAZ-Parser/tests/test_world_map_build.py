from __future__ import annotations

import io
from pathlib import Path

import pytest

from world_map import MAX_ZOOM, MIN_ZOOM, SEA_COLOR, SEA_FILLER_SECTORS, SEA_VARIANTS, native_tile, parent_tile, pyramid
from world_map_build import (
    BUILD_FORMAT,
    MANIFEST_NAME,
    BuildProgress,
    BuildStopped,
    build_map,
    content_folder,
    read_manifest,
    remove_other_maps,
    sea_path,
    tile_path,
)

Image = pytest.importorskip("PIL.Image")

RED = (200, 0, 0)
BLUE = (0, 0, 200)


def _png(color: tuple[int, int, int], size: int = 128) -> bytes:
    buf = io.BytesIO()
    Image.new("RGB", (size, size), color).save(buf, format="PNG")
    return buf.getvalue()


def _same(data: bytes) -> bytes:
    return data


def _near(pixel: tuple[int, int, int], color: tuple[int, int, int]) -> bool:
    return all(abs(a - b) <= 24 for a, b in zip(pixel, color))  # JPEG is lossy


def _pixel(path: Path, xy: tuple[int, int]) -> tuple[int, int, int]:
    with Image.open(path) as image:
        return image.convert("RGB").getpixel(xy)


def _build(sectors: dict[tuple[int, int], bytes], target: Path, **kwargs) -> object:
    return build_map(sectors=sectors, read=_same, target=target, version=1, workers=0, **kwargs)


def test_build_writes_every_pyramid_tile_sea_tiles_and_the_manifest(tmp_path: Path) -> None:
    sectors = {(0, -1): _png(RED), (40, 30): _png(RED)}
    target = tmp_path / "map" / "1"

    manifest = _build(sectors, target)

    for zoom, tiles in pyramid(sectors).items():
        assert all(tile_path(target, zoom, tile).is_file() for tile in tiles)
    for zoom in range(MIN_ZOOM, MAX_ZOOM + 1):
        assert all(sea_path(target, zoom, variant).is_file() for variant in range(SEA_VARIANTS))
    assert read_manifest(target) == manifest
    assert not target.with_name("1.building").exists()


def test_a_sector_without_a_radar_image_gets_a_sea_filler(tmp_path: Path) -> None:
    filler = {sector: _png(BLUE) for sector in SEA_FILLER_SECTORS}
    target = tmp_path / "map"

    _build({(0, -1): _png(RED), **filler}, target)
    path = tile_path(target, MAX_ZOOM, native_tile((0, -1)))

    assert _near(_pixel(path, (10, 10)), RED)  # (0, -1): top-left
    assert _near(_pixel(path, (200, 200)), BLUE)  # (1, -2): no radar image


def test_without_filler_sectors_the_gap_is_the_sea_colour(tmp_path: Path) -> None:
    target = tmp_path / "map"

    _build({(0, -1): _png(RED)}, target)

    assert _near(_pixel(tile_path(target, MAX_ZOOM, (0, 0)), (200, 200)), SEA_COLOR)


def test_a_lower_zoom_tile_is_made_from_the_tiles_under_it(tmp_path: Path) -> None:
    target = tmp_path / "map"

    _build({(0, -1): _png(RED)}, target)
    parent = parent_tile(native_tile((0, -1)))

    # The red sector fills the top-left quarter of its tile, so a sixteenth of the parent.
    assert _near(_pixel(tile_path(target, MAX_ZOOM - 1, parent), (5, 5)), RED)


def test_an_unreadable_radar_image_is_counted_and_drawn_as_sea(tmp_path: Path) -> None:
    target = tmp_path / "map"

    manifest = _build({(0, -1): b"not an image", (1, -1): _png(RED)}, target)

    assert manifest.missing_sectors == 1  # type: ignore[attr-defined]
    assert _near(_pixel(tile_path(target, MAX_ZOOM, (0, 0)), (10, 10)), SEA_COLOR)


def test_progress_runs_through_every_zoom_from_the_native_one(tmp_path: Path) -> None:
    seen: list[BuildProgress] = []

    _build({(0, -1): _png(RED)}, tmp_path / "map", on_progress=seen.append)
    finished = [progress for progress in seen if progress.done == progress.total]

    assert [progress.zoom for progress in finished] == list(range(MAX_ZOOM, MIN_ZOOM - 1, -1))
    assert [progress.step for progress in finished] == list(range(1, MAX_ZOOM - MIN_ZOOM + 2))


def test_a_stopped_build_leaves_nothing_behind(tmp_path: Path) -> None:
    target = tmp_path / "map" / "1"

    with pytest.raises(BuildStopped):
        _build({(0, -1): _png(RED)}, target, should_stop=lambda: True)

    assert not target.exists()
    assert not target.with_name("1.building").exists()


def test_build_without_sectors_raises(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        _build({}, tmp_path / "map")


def test_read_manifest_is_none_when_missing_or_malformed(tmp_path: Path) -> None:
    assert read_manifest(tmp_path) is None
    (tmp_path / MANIFEST_NAME).write_text("{not json", encoding="utf-8")
    assert read_manifest(tmp_path) is None


def test_remove_other_maps_keeps_only_the_given_one(tmp_path: Path) -> None:
    keep = content_folder(tmp_path, "3464-0123456789abcdef")
    old = content_folder(tmp_path, "3464-fedcba9876543210")
    leftover = keep.with_name("3465-0123456789abcdef.building")
    for folder in (keep, old, leftover):
        folder.mkdir(parents=True)

    remove_other_maps(tmp_path, keep)

    assert keep.is_dir()
    assert not old.exists()
    assert not leftover.exists()


def test_a_map_from_older_build_code_is_not_current(tmp_path: Path) -> None:
    target = tmp_path / "map"
    manifest = _build({(0, -1): _png(RED)}, target)
    old = (target / MANIFEST_NAME).read_text(encoding="utf-8").replace(
        f'"build_format": {BUILD_FORMAT}, ', ""
    )
    (target / MANIFEST_NAME).write_text(old, encoding="utf-8")

    assert manifest.is_current(1)  # type: ignore[attr-defined]
    reread = read_manifest(target)
    assert reread is not None and reread.build_format == 1
    assert not reread.is_current(1)
