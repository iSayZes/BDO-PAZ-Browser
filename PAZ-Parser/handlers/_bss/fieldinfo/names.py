"""Field names by field number, for the tables that store a `fieldinfo.bss` `field_no`.

`fieldinfo.bss` names a field in the world editor's words: Korean (`월드`,
`칼페온 크자카 인던`) or the instance field's internal name (`A1_001`). An
`A1_` field is also the `instancefield.dbss` record with the same key and
name, whose `instancefieldmapinfo.bss` title is LOC text, so those fields
read `The Magnus: The Great Single Path (A1_001)`.
"""

from __future__ import annotations

from _bss.instancefieldmapinfo.titles import instance_field_label
from _common.html import record_link
from _common.instance_field import instance_field_name
from _common.lookup_index import IndexKind, lookup

FIELDINFO_PATH = "gamecommondata/binary/fieldinfo.bss"
_LINK_CLASS = "record-link"


def field_label(field_no: int, name: str) -> str:
    """The instance field label when an instance field shares the key and name, else `name`."""
    if name and instance_field_name(field_no) == name:
        return instance_field_label(field_no)
    return name


def field_no_label(field_no: int) -> str:
    """`field_label()` of a field number through the FIELD_NAME index; '' when the index lacks it."""
    name = lookup(IndexKind.FIELD_NAME, field_no)
    return field_label(field_no, name) if isinstance(name, str) else ""


def field_no_link(field_no: int) -> str:
    """The field number as a button that opens its `fieldinfo.bss` row."""
    return record_link(str(field_no), FIELDINFO_PATH, "field_no", field_no, _LINK_CLASS)
