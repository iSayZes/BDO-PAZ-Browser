"""Disk cache for the item icon index.

Building the index means decompressing the 194 MB `itemenchant.dbss`, so the
result is cached next to the PAZ entry cache and invalidated on the same meta
version. Mirrors `bdo_cache.py`.
"""

from __future__ import annotations

import pickle
from pathlib import Path

_CACHE_FILE = "paz_browser_icons.cache"


def load_icon_cache(paz_root: Path) -> tuple[int, dict[int, str]] | None:
    cache_path = paz_root / _CACHE_FILE
    if not cache_path.exists():
        return None
    try:
        with cache_path.open("rb") as f:
            data = pickle.load(f)
        return data["version"], data["icons"]
    except Exception:
        return None


def save_icon_cache(paz_root: Path, version: int, icons: dict[int, str]) -> None:
    cache_path = paz_root / _CACHE_FILE
    with cache_path.open("wb") as f:
        pickle.dump(
            {"version": version, "icons": icons},
            f,
            protocol=pickle.HIGHEST_PROTOCOL,
        )
