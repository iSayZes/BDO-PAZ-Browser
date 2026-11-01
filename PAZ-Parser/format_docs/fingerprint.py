"""A short hash of what a doc's game check depends on, so a client checked against it is not read again.

It covers the layouts as the walk reads them (structure names and sizes; field offsets, types and names,
as names decide the known bytes) and the files the doc reads. Line numbers, notes and columns such as
`Source` are left out, so editing prose does not send a doc back to every client.
"""
from __future__ import annotations

import hashlib
from collections.abc import Sequence

from .model import Layout

# Raise when the walk or the coverage count changes, so every doc reads every client again.
CHECK_VERSION = 1
_LENGTH = 12


def layouts_fingerprint(layouts: Sequence[Layout], files: Sequence[str]) -> str:
    parts = [f"check {CHECK_VERSION}", *(f"file {name}" for name in files)]
    for layout in layouts:
        parts.append(f"layout {layout.number}")
        for structure in layout.structures:
            parts.append(f"structure {structure.name} {structure.size!r}")
            parts.extend(f"field {field.offset}|{field.type_text}|{field.name}" for field in structure.fields)
    return hashlib.sha1("\n".join(parts).encode("utf-8")).hexdigest()[:_LENGTH]
