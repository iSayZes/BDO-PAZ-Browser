"""NA copies: tables a client ships only under `#na#<name>`.

Clients 837 to 1246 ship 27 to 33,774 `.bss` / `.dbss` files only as
`#na#<name>`, never next to a plain copy (every test client from 794 to 1256).
Such a copy is the table itself: the browser shows it under its plain name,
reads it with that name's handler, and a lookup of the plain name finds it
when the client has no plain copy. A plain copy always wins.

Only `.bss` and `.dbss` files follow the rule. `#na#default` and
`#na#userdefault.xml` keep their names: their plain copies hold other bytes,
on every client up to 3482.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

NA_COPY_PREFIX = "#na#"
_TABLE_EXTENSIONS = (".bss", ".dbss")

T = TypeVar("T")


def _is_table(file_name: str) -> bool:
    return file_name.lower().endswith(_TABLE_EXTENSIONS)


def na_copy_name(path: str) -> str:
    """`path` with the NA prefix on its file name: `#na#x.bss`, `folder/#na#x.bss` for a full path."""
    folder, slash, file_name = path.rpartition("/")
    return f"{folder}{slash}{NA_COPY_PREFIX}{file_name}"


def plain_name(path: str) -> str:
    """`path` without the NA prefix when it names a table's NA copy, else `path` as it is.

    Takes a file name or a `/` path: `folder/#na#x.bss` becomes `folder/x.bss`.
    Spaces after the prefix go too: client 1000 ships `#na# cashshoose.bss`.
    """
    if "#" not in path:  # nearly every path; skips the split
        return path
    folder, slash, file_name = path.rpartition("/")
    if not (file_name[: len(NA_COPY_PREFIX)].lower() == NA_COPY_PREFIX and _is_table(file_name)):
        return path
    return f"{folder}{slash}{file_name[len(NA_COPY_PREFIX):].lstrip()}"


def shown_name(path: str, exists: Callable[[str], bool]) -> str:
    """The name the browser shows for `path`: its plain name, unless `exists` finds a plain copy."""
    plain = plain_name(path)
    return path if plain == path or exists(plain) else plain


def find_or_na_copy(find: Callable[[str], T | None], path: str) -> T | None:
    """`find(path)`; when that is None and `path` names a table, `find` of its NA copy."""
    found = find(path)
    if found is not None or not _is_table(path):
        return found
    return find(na_copy_name(path))
