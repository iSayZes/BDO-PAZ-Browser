"""Disk cache for the lookup indexes.

Building an index means decompressing its source table, 194 MB for
`itemenchant.dbss`, so the result is cached beside the PAZ entry cache and
invalidated on the same meta version. Mirrors `bdo_cache.py`. Values are pickled,
so an index may hold icon paths, linked IDs or tuples of IDs.

Indexes are stored keyed by `IndexKind.value` rather than by the enum member, so
renaming a kind cannot silently bind cached data to the wrong one.

The meta version only changes with a game patch, so a cache also records a
fingerprint of the code that built it (`builder_fingerprint`, see
`source_fingerprint.py`). Editing a builder, any project module it imports or
a JSON file beside one forces a rebuild on the next launch.
"""

from __future__ import annotations

import hashlib
import pickle
import sys
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

from .source_fingerprint import source_fingerprint

CACHE_FILE = "paz_browser_indexes.cache"
# Written next to the PAZ files before the icon indexes became general lookup
# indexes; deleted from there when a folder loads.
LEGACY_CACHE_FILE = "paz_browser_icons.cache"

# Values match `LookupValue` in handlers/_common/lookup_index.py.
CachedIndexes = dict[str, Mapping[int, int | str | tuple[int, ...]]]


@dataclass(frozen=True)
class IndexCacheData:
    """What the cache holds besides the fingerprint."""

    version: int
    indexes: CachedIndexes
    # Content digest of each index by kind value (`index_digests`), so the
    # records cache can tell which indexes a patch changed.
    digests: Mapping[str, str]


def load_index_cache(cache_dir: Path, fingerprint: str) -> IndexCacheData | None:
    """The cached indexes, or None when absent, unreadable or stale."""
    cache_path = cache_dir / CACHE_FILE
    if not cache_path.exists():
        return None
    try:
        with cache_path.open("rb") as f:
            data = pickle.load(f)
        if data.get("fingerprint") != fingerprint:
            return None
        return IndexCacheData(data["version"], data["indexes"], data["digests"])
    except Exception:
        return None


def save_index_cache(cache_dir: Path, fingerprint: str, data: IndexCacheData) -> None:
    cache_path = cache_dir / CACHE_FILE
    with cache_path.open("wb") as f:
        pickle.dump(
            {
                "fingerprint": fingerprint,
                "version": data.version,
                "indexes": data.indexes,
                "digests": dict(data.digests),
            },
            f,
            protocol=pickle.HIGHEST_PROTOCOL,
        )


def drop_index_cache(cache_dir: Path) -> None:
    """Delete the cache, for a client whose archive files or meta file changed under the same meta version."""
    (cache_dir / CACHE_FILE).unlink(missing_ok=True)


def index_digests(indexes: CachedIndexes) -> dict[str, str]:
    """A digest of each index's content, by kind value.

    Pickles each mapping, so equal content built the same way hashes the same.
    Runs only when the indexes are built, never on a cache hit.
    """
    return {
        name: hashlib.sha256(pickle.dumps(mapping, protocol=pickle.HIGHEST_PROTOCOL)).hexdigest()
        for name, mapping in indexes.items()
    }


def builder_fingerprint(functions: Iterable[Callable]) -> str:
    """Hash the source of every project module that shapes the lookup indexes.

    Starts from the modules defining `functions` and always includes this
    module, so a change to the cache layout also counts.
    """
    return source_fingerprint([*functions, sys.modules[__name__]])
