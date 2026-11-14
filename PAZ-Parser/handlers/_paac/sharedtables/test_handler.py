from __future__ import annotations

import struct

import pytest

from _paac.parser import parse_shared_tables
from _paac.records import shared_element_records

_STRINGS = ["", "WAIT", "Ani_Wait"]
_EMPTY, _WAIT, _ANI_WAIT = range(len(_STRINGS))
_GROUP_KEY = 0x1234ABCD


def _shared_tables(extra_event_count: int = 0) -> bytes:
    """A Layout 1 (client 1784) shared tables file: no conditions or events, one group of one element."""
    element = struct.pack("<13I", _WAIT, _ANI_WAIT, *(_EMPTY,) * 11) + struct.pack("<IIIQQ", 0, _EMPTY, _EMPTY, 0, 0)
    body = b"PABR" + struct.pack("<IQI", 1, 0, extra_event_count)
    body += struct.pack("<QIQ", 1, _GROUP_KEY, 1) + element + struct.pack("<I", 1)
    table = struct.pack("<I", len(_STRINGS)) + b"".join(
        struct.pack("<BI", 0, len(text)) + text.encode("ascii") for text in _STRINGS
    )
    return body + table + struct.pack("<II", len(body), 0)


def test_layout_1_lists_each_element_with_its_group_key() -> None:
    [record] = shared_element_records(parse_shared_tables(_shared_tables()))
    assert (record["key"], record["action_name"], record["animation"]) == (_GROUP_KEY, "WAIT", "Ani_Wait")


def test_a_file_layout_1_does_not_read_raises() -> None:
    # One event announced but none there: the walk runs into the element groups.
    with pytest.raises(ValueError, match="Layout 1"):
        parse_shared_tables(_shared_tables(extra_event_count=1))
