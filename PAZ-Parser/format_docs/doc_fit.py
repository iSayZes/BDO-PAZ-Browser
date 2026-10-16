"""Finds which layout of a doc a client's files fit, newest first."""
from __future__ import annotations

from collections.abc import Mapping, Sequence

from .doc_checks import resolved_structures
from .model import Layout, Structure
from .reader import FILE_LAYOUT, companion_key
from .walk_model import FileFit, LayoutFit, LayoutMiss, WalkError
from .walker import walk_file


def _top_structure(structures: Mapping[str, Structure], file: str) -> Structure | None:
    """The table a file starts with: its own ``### `file` `` heading, else `### File Layout`."""
    return structures.get(companion_key(file)) or structures.get(FILE_LAYOUT)


def fit_layouts(layouts: Sequence[Layout], files: Mapping[str, bytes]) -> LayoutFit | tuple[LayoutMiss, ...]:
    """The newest layout every file walks to its end by, or why each layout failed.

    Raises `Unwalkable` when a layout holds a form a walk cannot follow.
    """
    misses: list[LayoutMiss] = []
    for index, layout in enumerate(layouts):
        result = _fit_layout(layout.number, resolved_structures(layouts, index), files)
        if isinstance(result, LayoutFit):
            return result
        misses.append(result)
    return tuple(misses)


def _fit_layout(number: int, structures: Mapping[str, Structure], files: Mapping[str, bytes]) -> LayoutFit | LayoutMiss:
    # Files with a table of their own are offset files; walk them first so their sizes are known.
    order = sorted(files, key=lambda name: companion_key(name) not in structures)
    sizes_by_file: dict[str, dict[int, int]] = {}
    fits: dict[str, FileFit] = {}
    for name in order:
        top = _top_structure(structures, name)
        if top is None:
            return LayoutMiss(number, name, WalkError(FILE_LAYOUT, "(none)", 0, "the layout has no table for this file"))
        try:
            fit, sizes = walk_file(name, files[name], top, structures, sizes_by_file)
        except WalkError as error:
            return LayoutMiss(number, name, error)
        fits[name] = fit
        sizes_by_file[name] = sizes
    return LayoutFit(number, tuple(fits[name] for name in files))
