from __future__ import annotations

import sys
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Iterator


@dataclass
class LocStats:
    total: int | None = None
    misses: int | None = None


def reset_loc() -> None:
    import _common.loc as loc

    loc._LOC_INDEX = None
    loc._LOC_PREFIX = None
    loc._LOC_ALL = None


@contextmanager
def patch_loc_counter() -> Iterator[LocStats]:
    import _common.loc as loc

    original = loc.loc_lookup
    total = 0
    misses = 0

    def patched(*args, **kwargs):
        nonlocal total, misses
        result = original(*args, **kwargs)
        total += 1
        if not result:
            misses += 1
        return result

    patched_attrs: list[tuple[Any, str, Any]] = [(loc, "loc_lookup", original)]
    loc.loc_lookup = patched

    for module in list(sys.modules.values()):
        if getattr(module, "loc_lookup", None) is original:
            setattr(module, "loc_lookup", patched)
            patched_attrs.append((module, "loc_lookup", original))

    stats = LocStats()
    try:
        yield stats
        stats.total = total
        stats.misses = misses
    finally:
        for module, attr, value in patched_attrs:
            setattr(module, attr, value)


@contextmanager
def null_loc_counter() -> Iterator[LocStats]:
    yield LocStats()
