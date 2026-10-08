"""Hash of the project code, and the data files next to it, that produced a cached value.

The disk caches outlive the code that filled them. A cache records this
fingerprint and treats a mismatch as stale, so editing a builder, a helper it
imports or a JSON file its package reads forces a rebuild, with no version
number to remember to bump.
"""

from __future__ import annotations

import hashlib
import inspect
import sys
from collections.abc import Callable, Hashable, Iterable, Mapping
from pathlib import Path
from types import ModuleType
from typing import TypeVar

from app_version import build_info

# Top-level packages whose source can change what a cached value contains.
# Standard library and third-party imports are left out: they change with the
# interpreter, not with this project.
_PROJECT_PACKAGES = frozenset({"_common", "_dbss", "_bss", "_bwp", "paz"})

# Data files a package reads next to its modules: column labels and values in
# `lang/*.json`, overrides such as `_common/icon_overrides.json`.
_DATA_PATTERNS = ("*.json", "lang/*.json")

K = TypeVar("K", bound=Hashable)


def source_fingerprint(roots: Iterable[object]) -> str:
    """Hash the source of every project module that `roots` reach.

    `roots` are modules, or functions and classes standing for the module that
    defines them; they count whatever package they live in. Their project
    imports are followed transitively. The JSON files beside each module count
    too. Only file contents are hashed, with line endings normalised, never
    paths or times, so the value is stable across checkouts and machines.

    In the exe, core modules (`paz`) sit in its archive without their source,
    so the build ID (version and commit) stands for them: a new exe rebuilds
    their caches. Handler pack modules are real files and stay hashed.
    """
    return source_fingerprints({None: roots})[None]


def source_fingerprints(root_sets: Mapping[K, Iterable[object]]) -> dict[K, str]:
    """`source_fingerprint()` of each root set, reading every file once."""
    file_digests: dict[Path, bytes] = {}

    def file_digest(path: Path) -> bytes:
        digest = file_digests.get(path)
        if digest is None:
            digest = hashlib.sha256(_normalised(path)).digest()
            file_digests[path] = digest
        return digest

    return {key: _fingerprint(roots, file_digest) for key, roots in root_sets.items()}


def _fingerprint(roots: Iterable[object], file_digest: Callable[[Path], bytes]) -> str:
    modules = project_modules([_module_of(root) for root in roots])
    digest = hashlib.sha256()
    for name in sorted(modules):
        digest.update(name.encode("utf-8"))
        digest.update(_module_digest(modules[name], file_digest))
    for path in _data_files(modules.values()):
        digest.update(path.name.encode("utf-8"))
        digest.update(file_digest(path))
    return digest.hexdigest()


def _module_digest(module: ModuleType, file_digest: Callable[[Path], bytes]) -> bytes:
    path = Path(inspect.getfile(module))
    if path.is_file():
        return file_digest(path)
    info = build_info()
    if info is None:
        # From source every module has its file; a missing one is a real error.
        raise FileNotFoundError(f"no source for {module.__name__} at {path}")
    return hashlib.sha256(info.build_id.encode("utf-8")).digest()


def project_modules(roots: list[ModuleType]) -> dict[str, ModuleType]:
    """`roots` plus every project module they import, directly or not, by name."""
    found: dict[str, ModuleType] = {}
    pending = list(roots)
    while pending:
        module = pending.pop()
        if module.__name__ in found:
            continue
        found[module.__name__] = module
        pending.extend(
            dep for dep in map(project_module_of, vars(module).values())
            if dep is not None and dep.__name__ not in found
        )
    return found


def project_files(roots: Iterable[object]) -> list[Path]:
    """The files `source_fingerprint(roots)` hashes: module sources and the JSON beside them.

    Modules without a source file, the core modules in the exe, are left out.
    """
    modules = project_modules([_module_of(root) for root in roots])
    sources = {Path(inspect.getfile(module)) for module in modules.values()}
    found = {path for path in sources if path.is_file()} | set(_data_files(modules.values()))
    return sorted(found, key=lambda path: path.as_posix())


def _module_of(root: object) -> ModuleType:
    return root if isinstance(root, ModuleType) else sys.modules[getattr(root, "__module__")]


def project_module_of(value: object) -> ModuleType | None:
    """The project module that defines `value` (a module, function, class or instance), or None."""
    name = value.__name__ if inspect.ismodule(value) else getattr(value, "__module__", None)
    if not isinstance(name, str) or name.split(".")[0] not in _PROJECT_PACKAGES:
        return None
    module = sys.modules.get(name)
    return module if getattr(module, "__file__", None) else None


def _data_files(modules: Iterable[ModuleType]) -> list[Path]:
    """The JSON files beside `modules`, once each, in a stable order."""
    folders = {Path(inspect.getfile(module)).parent for module in modules}
    found = {path for folder in folders for pattern in _DATA_PATTERNS for path in folder.glob(pattern)}
    return sorted(found, key=lambda path: path.as_posix())


def _normalised(path: Path) -> bytes:
    return path.read_bytes().replace(b"\r\n", b"\n")
