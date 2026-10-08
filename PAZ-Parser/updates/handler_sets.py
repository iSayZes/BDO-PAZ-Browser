"""The manifest of the loaded handlers: their pack files and which of them each handler reads."""

from __future__ import annotations

from pathlib import Path

from bdo_preview import get_binary_handlers, get_handler
from paz.source_fingerprint import project_files

from .handler_manifest import HandlerManifest, build_manifest, file_hashes, is_pack_file


def pack_manifest(
    handlers_dir: Path,
    version: str,
    commit: str,
    handler_api: int,
    previous: HandlerManifest | None = None,
    notes: str = "",
) -> HandlerManifest:
    """The manifest of `handlers_dir` as a pack, versions carried over from `previous`.

    Needs the handlers of `handlers_dir` loaded (`bdo_preview.load_plugins`).
    """
    return build_manifest(
        version, commit, handler_api, file_hashes(handlers_dir), handler_file_sets(handlers_dir), previous, notes,
    )


def handler_file_sets(handlers_dir: Path) -> dict[str, list[str]]:
    """Registry key -> the pack files under `handlers_dir` its handler's code reads.

    Needs the handlers of `handlers_dir` loaded (`bdo_preview.load_plugins`).
    The set is the handler's module, the project modules it imports and the
    JSON files next to them (`source_fingerprint.project_files`), so a
    `_common` change counts for every handler that imports it.
    """
    return {key: handler_files(handlers_dir, key) for key in get_binary_handlers()}


def handler_files(handlers_dir: Path, key: str) -> list[str]:
    """The pack files under `handlers_dir` the handler registered as `key` reads, sorted."""
    root = handlers_dir.resolve()
    names = set()
    for path in project_files([get_handler(key, key)]):
        relative = _relative_to(path.resolve(), root)
        if relative is not None and is_pack_file(relative):
            names.add(relative.as_posix())
    return sorted(names)


def _relative_to(path: Path, root: Path) -> Path | None:
    try:
        return path.relative_to(root)
    except ValueError:
        return None
