"""Cell text of the mount tables (`servant_tables.py`)."""

from __future__ import annotations

from _common.servant_kind import servant_kind_name


def servant_kind_text(servant_kind: int) -> str:
    """`23 Carrack`: a `CppEnums.ServantKind` value and its member name."""
    name = servant_kind_name(servant_kind)
    return name if name == str(servant_kind) else f"{servant_kind} {name}"
