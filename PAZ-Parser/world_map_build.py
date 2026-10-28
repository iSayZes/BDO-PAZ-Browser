"""Building the world map's tile pyramid on disk (`world_map.py` holds the grid).

`build_map()` writes every tile as `<zoom>/<x>/<y>.jpg` into a `.building`
folder next to the target, writes `map.json` last and renames the folder into
place, so a stopped or failed build never leaves half a map behind.
`MAX_ZOOM` tiles are made from the radar images, each lower zoom from the four
tiles under it.

The tiles are made in a process pool. Reading a radar image is ICE decryption
and `bdo_decompress`; with the Python decoders threads cannot run them in
parallel: on client 3464, 8 processes read and decode the 27,691 radar images
in 5.8 s, one process in 34 s and 8 threads in 59 s. `_bdo_native` decodes
without holding the GIL, and threads still lose: a radar image is 128x128
pixels, and each step of a tile (read, DDS open, convert, JPEG save) takes 10
to 60 µs, mostly Python and Pillow call overhead under the GIL. On client 3464
with `_bdo_native`, zoom 7 takes 2.4 s on 8 processes and 8.6 s on 8 threads.
"""

from __future__ import annotations

import io
import json
import logging
import os
import shutil
from collections.abc import Callable, Collection, Iterable, Mapping
from concurrent.futures import Executor, ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Generic, TypeVar

from api.bdo_icon_images import open_image
from bdo_models import PazEntry
from paz.bdo_payload_reader import read_entry_payload
from world_map import (
    MAX_ZOOM,
    MIN_ZOOM,
    SEA_COLOR,
    SEA_FILLER_SECTORS,
    SEA_VARIANTS,
    SECTOR_PX,
    TILE_PX,
    Sector,
    TileKey,
    WorldBounds,
    child_tiles,
    filler_sector,
    pyramid,
    sea_parts,
    sea_variant,
    tile_count,
    tile_sectors,
    world_bounds,
)

MAP_FOLDER = "map"
SEA_FOLDER = "sea"
MANIFEST_NAME = "map.json"
_BUILDING_SUFFIX = ".building"
JPEG_QUALITY = 88
# Raised when a change here or in world_map.py (hidden sectors, sea fill)
# changes the tiles, so maps built before it count as out of date.
BUILD_FORMAT = 2
# More processes stopped paying off past 8 on a 32-core machine, and each one
# holds its own Python and Pillow.
MAX_WORKERS = 8
# Jobs per hand-off to a worker: fewer round trips, still even progress steps.
_CHUNK_SIZE = 32

S = TypeVar("S")
# A radar image inside the PAZ archives: the archive file and the entry.
RadarSource = tuple[Path, PazEntry]


class BuildStopped(Exception):
    """`should_stop` asked the build to end; nothing was written in place."""


@dataclass(frozen=True)
class BuildProgress:
    """Tiles done of the zoom being built; `step` counts zooms from 1 to `steps`."""

    zoom: int
    done: int
    total: int
    step: int
    steps: int

    def to_dict(self) -> dict[str, int]:
        return {"zoom": self.zoom, "done": self.done, "total": self.total, "step": self.step, "steps": self.steps}


@dataclass(frozen=True)
class MapManifest:
    """What `map.json` records about a finished map."""

    version: int
    tiles: int
    bytes: int
    missing_sectors: int
    bounds: WorldBounds
    build_format: int = BUILD_FORMAT

    def is_current(self, version: int) -> bool:
        """True when this map is of client `version` and built by this code."""
        return self.version == version and self.build_format == BUILD_FORMAT

    def to_json(self) -> str:
        return json.dumps({
            "build_format": self.build_format,
            "version": self.version,
            "tiles": self.tiles,
            "bytes": self.bytes,
            "missing_sectors": self.missing_sectors,
            "bounds": self.bounds.to_dict(),
        })

    @staticmethod
    def from_json(text: str) -> MapManifest:
        """Raises ValueError (or KeyError, TypeError) on a malformed manifest."""
        data = json.loads(text)
        bounds = data["bounds"]
        return MapManifest(
            version=int(data["version"]),
            tiles=int(data["tiles"]),
            bytes=int(data["bytes"]),
            missing_sectors=int(data["missing_sectors"]),
            bounds=WorldBounds(
                min_x=int(bounds["minX"]), max_x=int(bounds["maxX"]),
                min_z=int(bounds["minZ"]), max_z=int(bounds["maxZ"]),
            ),
            # The first maps had no build format.
            build_format=int(data.get("build_format", 1)),
        )


def map_root(cache_dir: Path) -> Path:
    """The folder of every built map of a client's cache folder."""
    return cache_dir / MAP_FOLDER


def content_folder(cache_dir: Path, content_key: str) -> Path:
    """The map of the client with `content_key` (`paz/bdo_content_key.py`)."""
    return map_root(cache_dir) / content_key


def tile_path(folder: Path, zoom: int, tile: TileKey) -> Path:
    return folder / str(zoom) / str(tile[0]) / f"{tile[1]}.jpg"


def sea_path(folder: Path, zoom: int, variant: int) -> Path:
    """Sea tile `variant` of `zoom` (`world_map.sea_variant`)."""
    return folder / SEA_FOLDER / str(zoom) / f"{variant}.jpg"


def tile_file(folder: Path, zoom: int, tile: TileKey) -> Path | None:
    """The file a map in `folder` shows for `tile`: its own, else its zoom's sea tile, else None."""
    path = tile_path(folder, zoom, tile)
    if path.is_file():
        return path
    sea = sea_path(folder, zoom, sea_variant(zoom, tile))
    return sea if sea.is_file() else None


def read_manifest(folder: Path) -> MapManifest | None:
    """The manifest of a finished map in `folder`, or None when there is none or it is unreadable."""
    try:
        return MapManifest.from_json((folder / MANIFEST_NAME).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError, KeyError, TypeError):
        logging.warning("Ignoring the unreadable world map manifest in %s", folder, exc_info=True)
        return None


def remove_other_maps(cache_dir: Path, keep: Path | None) -> None:
    """Delete every map folder in the cache folder but `keep`, leftover `.building` ones included."""
    root = map_root(cache_dir)
    if not root.is_dir():
        return
    for folder in root.iterdir():
        if folder != keep and folder.is_dir():
            shutil.rmtree(folder, ignore_errors=True)


def read_radar(source: RadarSource) -> bytes:
    """A radar image's DDS bytes; module level, so the worker processes can call it."""
    archive_path, entry = source
    return read_entry_payload(archive_path, entry)


def worker_count() -> int:
    """Processes for a build: one core is left for the app, at most `MAX_WORKERS`."""
    return max(1, min(MAX_WORKERS, (os.cpu_count() or 2) - 1))


@dataclass(frozen=True)
class _NativeJob(Generic[S]):
    path: Path
    sources: tuple[S | None, S | None, S | None, S | None]
    read: Callable[[S], bytes]


@dataclass(frozen=True)
class _ParentJob:
    path: Path
    children: tuple[Path, Path, Path, Path]


@dataclass(frozen=True)
class _TileResult:
    bytes: int
    # Radar images that could not be read or decoded; drawn as sea.
    failed: int


def build_map(
    *,
    sectors: Mapping[Sector, S],
    read: Callable[[S], bytes],
    target: Path,
    version: int,
    workers: int,
    zooms: Collection[int] | None = None,
    on_progress: Callable[[BuildProgress], None] = lambda _progress: None,
    should_stop: Callable[[], bool] = lambda: False,
) -> MapManifest:
    """Build the pyramid of `sectors` into `target` and return its manifest.

    `zooms` keeps only those levels (every level when None); the levels above
    the lowest one asked for are still built, since each is made from the one
    under it. `read` turns a sector's source into DDS bytes and must be a
    module-level function when `workers` > 1, so the worker processes can
    import it; `workers` <= 1 builds in this process. Raises BuildStopped when
    `should_stop` turns true, and ValueError when `sectors` is empty or a zoom
    is out of range.
    """
    bounds = world_bounds(sectors)
    if bounds is None:
        raise ValueError("there are no radar images to build the map from")
    kept = frozenset(range(MIN_ZOOM, MAX_ZOOM + 1) if zooms is None else zooms)
    if not kept or not kept <= set(range(MIN_ZOOM, MAX_ZOOM + 1)):
        raise ValueError(f"zoom levels must be {MIN_ZOOM} to {MAX_ZOOM}, got {sorted(kept)}")

    building = target.with_name(target.name + _BUILDING_SUFFIX)
    shutil.rmtree(building, ignore_errors=True)
    levels = pyramid(sectors)
    try:
        zoom_bytes, failed = _build_levels(
            sectors, read, building, levels, min(kept), workers, on_progress, should_stop
        )
        for zoom in set(zoom_bytes) - kept:
            shutil.rmtree(building / str(zoom))
            shutil.rmtree(sea_path(building, zoom, 0).parent)
    except BaseException:
        shutil.rmtree(building, ignore_errors=True)
        raise

    if failed:
        logging.warning("World map: %d radar images could not be read and are drawn as sea", failed)
    manifest = MapManifest(
        version=version,
        tiles=tile_count({zoom: levels[zoom] for zoom in kept}),
        bytes=sum(zoom_bytes[zoom] for zoom in kept),
        missing_sectors=failed,
        bounds=bounds,
    )
    (building / MANIFEST_NAME).write_text(manifest.to_json(), encoding="utf-8")
    shutil.rmtree(target, ignore_errors=True)
    building.rename(target)
    return manifest


def _build_levels(
    sectors: Mapping[Sector, S],
    read: Callable[[S], bytes],
    folder: Path,
    levels: Mapping[int, frozenset[TileKey]],
    lowest_zoom: int,
    workers: int,
    on_progress: Callable[[BuildProgress], None],
    should_stop: Callable[[], bool],
) -> tuple[dict[int, int], int]:
    """Write `MAX_ZOOM` down to `lowest_zoom` into `folder`: (bytes per zoom, unreadable radar images)."""
    steps = MAX_ZOOM - lowest_zoom + 1
    zoom_bytes: dict[int, int] = {}
    failed = 0
    pool: Executor | None = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    try:
        for step, zoom in enumerate(range(MAX_ZOOM, lowest_zoom - 1, -1), start=1):
            jobs = [
                *_sea_jobs(zoom, sectors, read, folder),
                *_zoom_jobs(zoom, levels, sectors, read, folder),
            ]
            report = _reporter(zoom, len(jobs), step, steps, on_progress)
            zoom_bytes[zoom] = 0
            for result in _run(jobs, pool):
                if should_stop():
                    raise BuildStopped()
                zoom_bytes[zoom] += result.bytes
                failed += result.failed
                report()
    except BaseException:
        if pool is not None:
            pool.shutdown(wait=True, cancel_futures=True)
            pool = None
        raise
    finally:
        if pool is not None:
            pool.shutdown(wait=True)
    return zoom_bytes, failed


def _zoom_jobs(
    zoom: int,
    levels: Mapping[int, frozenset[TileKey]],
    sectors: Mapping[Sector, S],
    read: Callable[[S], bytes],
    folder: Path,
) -> list[_NativeJob[S]] | list[_ParentJob]:
    ordered = sorted(levels[zoom])
    if zoom == MAX_ZOOM:
        return [
            _NativeJob(tile_path(folder, zoom, tile), _sources(tile, sectors), read)
            for tile in ordered
        ]
    built = levels[zoom + 1]
    return [
        _ParentJob(
            tile_path(folder, zoom, tile),
            _four(tuple(
                tile_path(folder, zoom + 1, child) if child in built
                else sea_path(folder, zoom + 1, sea_variant(zoom + 1, child))
                for child in child_tiles(tile)
            )),
        )
        for tile in ordered
    ]


def _sea_jobs(
    zoom: int, sectors: Mapping[Sector, S], read: Callable[[S], bytes], folder: Path
) -> list[_NativeJob[S]] | list[_ParentJob]:
    """The `SEA_VARIANTS` sea tiles of `zoom`; the zoom one out is made from them."""
    if zoom == MAX_ZOOM:
        return [
            _NativeJob(
                sea_path(folder, zoom, variant),
                _four(tuple(sectors.get(SEA_FILLER_SECTORS[part]) for part in sea_parts(zoom, variant))),
                read,
            )
            for variant in range(SEA_VARIANTS)
        ]
    return [
        _ParentJob(
            sea_path(folder, zoom, variant),
            _four(tuple(sea_path(folder, zoom + 1, part) for part in sea_parts(zoom, variant))),
        )
        for variant in range(SEA_VARIANTS)
    ]


def _sources(tile: TileKey, sectors: Mapping[Sector, S]) -> tuple[S | None, S | None, S | None, S | None]:
    """The radar image of each sector of a tile, a sea filler's for a sector without one."""
    return _four(tuple(_source(sector, sectors) for sector in tile_sectors(tile)))


def _source(sector: Sector, sectors: Mapping[Sector, S]) -> S | None:
    source = sectors.get(sector)
    return source if source is not None else sectors.get(filler_sector(sector))


def _four(items: tuple) -> tuple:
    if len(items) != 4:
        raise ValueError(f"a tile has 4 parts, got {len(items)}")
    return items


def _reporter(
    zoom: int, total: int, step: int, steps: int, on_progress: Callable[[BuildProgress], None]
) -> Callable[[], None]:
    done = 0
    on_progress(BuildProgress(zoom=zoom, done=0, total=total, step=step, steps=steps))

    def report() -> None:
        nonlocal done
        done += 1
        on_progress(BuildProgress(zoom=zoom, done=done, total=total, step=step, steps=steps))

    return report


def _run(jobs: Iterable[_NativeJob | _ParentJob], pool: Executor | None) -> Iterable[_TileResult]:
    if pool is None:
        return map(_render, jobs)
    return pool.map(_render, jobs, chunksize=_CHUNK_SIZE)


def _render(job: _NativeJob | _ParentJob) -> _TileResult:
    """Draw and save one tile; runs in a worker process."""
    from PIL import Image

    canvas = Image.new("RGB", (TILE_PX, TILE_PX), SEA_COLOR)
    failed = 0
    if isinstance(job, _NativeJob):
        for index, source in enumerate(job.sources):
            if source is None:
                continue
            try:
                part = open_image(job.read(source)).convert("RGB")
            except Exception:
                failed += 1
                continue
            if part.size != (SECTOR_PX, SECTOR_PX):
                part = part.resize((SECTOR_PX, SECTOR_PX), Image.Resampling.BOX)
            canvas.paste(part, _quadrant(index, SECTOR_PX))
    else:
        half = TILE_PX // 2
        for index, child in enumerate(job.children):
            if not child.is_file():
                continue
            with Image.open(child) as image:
                canvas.paste(image.convert("RGB").resize((half, half), Image.Resampling.BOX), _quadrant(index, half))
    return _TileResult(bytes=_save(canvas, job.path), failed=failed)


def _quadrant(index: int, size: int) -> tuple[int, int]:
    """Top-left pixel of part `index` (top-left, top-right, bottom-left, bottom-right)."""
    return (index % 2) * size, (index // 2) * size


def _save(image, path: Path) -> int:
    buf = io.BytesIO()
    image.save(buf, format="JPEG", quality=JPEG_QUALITY)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(buf.getvalue())
    return len(buf.getvalue())
