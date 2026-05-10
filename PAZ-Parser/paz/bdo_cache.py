from __future__ import annotations

import pickle
import struct
from pathlib import Path

from bdo_models import PazEntry

_CACHE_FILE = "paz_browser.cache"


def read_meta_version(meta_path: Path) -> int:
    with meta_path.open("rb") as f:
        data = f.read(4)
    if len(data) != 4:
        raise ValueError(f"Cannot read version from: {meta_path}")
    return struct.unpack("<I", data)[0]


def load_cache(paz_root: Path) -> tuple[int, list[PazEntry]] | None:
    cache_path = paz_root / _CACHE_FILE
    if not cache_path.exists():
        return None
    try:
        with cache_path.open("rb") as f:
            data = pickle.load(f)
        return data["version"], data["entries"]
    except Exception:
        return None


def save_cache(paz_root: Path, version: int, entries: list[PazEntry]) -> None:
    cache_path = paz_root / _CACHE_FILE
    with cache_path.open("wb") as f:
        pickle.dump(
            {"version": version, "entries": entries},
            f,
            protocol=pickle.HIGHEST_PROTOCOL,
        )
