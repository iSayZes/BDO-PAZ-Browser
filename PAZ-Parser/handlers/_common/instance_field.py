"""Instance field names by key, from the INSTANCE_FIELD_NAME lookup index.

`instancefield.dbss` names each field with an internal ASCII name
(`A1_001`, `Solare_Arena_Kell`); no LOC type holds a display name for them.
"""

from __future__ import annotations

from _common.lookup_index import IndexKind, lookup


def instance_field_name(key: int) -> str:
    """The field's internal name, '' when the index is not loaded or lacks the key."""
    name = lookup(IndexKind.INSTANCE_FIELD_NAME, key)
    return name if isinstance(name, str) else ""
