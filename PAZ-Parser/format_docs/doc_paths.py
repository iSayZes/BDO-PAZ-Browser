"""Where a format doc lives: `docs/file-formats/<group>/<name>.md`, grouped like the wiki's side bar.

`buff_dbss.md` is in `dbss/`, `regioninfo_bss.md` in `bss/`, every other format
(`aiscript_ai.md`, `languagedata_loc.md`) in `other/`. The template stays in
`docs/file-formats/` itself.
"""
from __future__ import annotations

from pathlib import Path

TEMPLATE_PREFIX = "_"
TABLE_GROUPS = ("bss", "dbss")
OTHER_GROUP = "other"


def doc_group(name: str) -> str:
    """The folder of a doc by its file name: `bss` or `dbss` from its suffix (`buff_dbss.md`), else `other`."""
    suffix = Path(name).stem.rpartition("_")[2]
    return suffix if suffix in TABLE_GROUPS else OTHER_GROUP


def doc_path(folder: Path, name: str) -> Path:
    """Where the doc `name` (`buff_dbss.md`) lives under `folder`, the docs/file-formats/ folder."""
    return folder / doc_group(name) / name


def format_doc_paths(folder: Path) -> tuple[Path, ...]:
    """Every format doc under `folder`, the docs/file-formats/ folder, by file name; the template left out."""
    paths = (path for path in folder.glob("*/*.md") if not path.name.startswith(TEMPLATE_PREFIX))
    return tuple(sorted(paths, key=lambda path: path.name))
