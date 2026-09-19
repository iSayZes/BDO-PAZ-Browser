"""Disk cache for the icon indexes.

Building an index means decompressing its source table, 194 MB for
`itemenchant.dbss`, so the result is cached next to the PAZ entry cache and
invalidated on the same meta version. Mirrors `bdo_cache.py`.

Indexes are stored keyed by `IconKind.value` rather than by the enum member, so
renaming a kind cannot silently bind cached data to the wrong one.
"""

from __future__ import annotations

import pickle
from pathlib import Path

_CACHE_FILE = "paz_browser_icons.cache"


def load_icon_cache(paz_root: Path) -> tuple[int, dict[str, dict[int, str]]] | None:
    cache_path = paz_root / _CACHE_FILE
    if not cache_path.exists():
        return None
    try:
        with cache_path.open("rb") as f:
            data = pickle.load(f)
        return data["version"], data["indexes"]
    except Exception:
        return None


def save_icon_cache(
    paz_root: Path,
    version: int,
    indexes: dict[str, dict[int, str]],
) -> None:
    cache_path = paz_root / _CACHE_FILE
    with cache_path.open("wb") as f:
        pickle.dump(
            {"version": version, "indexes": indexes},
            f,
            protocol=pickle.HIGHEST_PROTOCOL,
        )
