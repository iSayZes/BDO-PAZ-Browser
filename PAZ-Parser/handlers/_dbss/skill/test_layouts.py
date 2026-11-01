"""The three documented Skill Record layouts read back from a small built file and its offset file."""

from __future__ import annotations

import struct
from dataclasses import dataclass

import pytest

from bdo_preview import set_handler_client
from .parser import parse_skill_records


_KEY = 0x00020001  # skill 2, level 1
_NEXT_KEY = 0x00020002
_RELATED_KEY = 0x00030001
_COOLDOWN_MS = 12000
_BUFF_IDS = (356, 353)
_DESCRIPTION = "검술 수련"
_SCRIPT = "ALL_AP_UP(1);"


@dataclass(frozen=True)
class _Shape:
    """One layout as skill_dbss.md writes it."""

    # need_item_key to cooldown_ms: 21 bytes with unknown_n4c, 19 without.
    use_rules_size: int
    buff_id_format: str
    has_special_weapon_hit_effects: bool
    # target_search_angle, is_except_cool_time and unknown_end.
    end_size: int


_SHAPES = {
    3: _Shape(21, "I", False, 7),
    2: _Shape(21, "H", False, 7),
    1: _Shape(19, "H", True, 5),
}


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _key_list(*keys: int) -> bytes:
    return struct.pack(f"<I{len(keys)}I", len(keys), *keys)


def _record(shape: _Shape, key: int = _KEY, *, has_text_and_links: bool = True) -> bytes:
    description, script = (_DESCRIPTION, _SCRIPT) if has_text_and_links else ("", "")
    next_keys, related_keys = ((_NEXT_KEY,), (_RELATED_KEY,)) if has_text_and_links else ((), ())
    buff_slots = _BUFF_IDS + (0,) * (10 - len(_BUFF_IDS))
    return (
        struct.pack("<IIB", key, key, 0)
        + _str8("")
        + struct.pack("<I", 0)  # action_hash
        + bytes(35)  # learning rules
        + bytes(5)  # do_require_point_need, require_hp
        + struct.pack("<I", 0)  # resource_cost
        + bytes(5)  # require_sub_resource_point, sub_resource_type
        + struct.pack("<I", 0)  # stamina_cost
        + bytes(shape.use_rules_size)
        + struct.pack("<I", _COOLDOWN_MS)
        + struct.pack(f"<10{shape.buff_id_format}", *buff_slots)
        + _str16(description)
        + _str16(script)
        + bytes(36)
        + _key_list(*next_keys)
        + struct.pack("<I", 0)
        + _key_list(*related_keys)
        + (_key_list() if shape.has_special_weapon_hit_effects else b"")
        + bytes(shape.end_size)
    )


def _files(*records: tuple[int, bytes]) -> tuple[bytes, bytes]:
    """`skill.dbss` holding `records` (key, record) and its `skilloffset.dbss`."""
    data = bytearray(struct.pack("<I", len(records)))
    rows = bytearray()
    for key, record in records:
        data += struct.pack("<I", key)  # key_prefix
        rows += struct.pack("<III", key, len(data), len(record))
        data += record
    rows_end = 8 + len(rows)
    offset_data = b"PABR" + struct.pack("<I", len(records)) + bytes(rows) + struct.pack("<III", 0, rows_end, 0)
    return bytes(data), offset_data


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_each_layout_reads_the_same_record(layout: int) -> None:
    (record,) = parse_skill_records(*_files((_KEY, _record(_SHAPES[layout]))))

    assert (record.skill_key, record.cooldown_ms, record.buff_ids) == (_KEY, _COOLDOWN_MS, _BUFF_IDS)
    assert (record.description_kr, record.script) == (_DESCRIPTION, _SCRIPT)
    assert (record.next_skill_keys, record.related_cool_time_skill_keys) == ((_NEXT_KEY,), (_RELATED_KEY,))


def test_a_bare_layout_1_record_also_walks_as_layout_2() -> None:
    """Why the whole file picks the layout: with no text and no linked skills
    Layout 2 reads the record to its end, 2 bytes off from the cooldown on."""
    (record,) = parse_skill_records(*_files((_KEY, _record(_SHAPES[1], has_text_and_links=False))))

    assert record.cooldown_ms != _COOLDOWN_MS


def test_the_whole_file_picks_the_layout() -> None:
    shape = _SHAPES[1]
    bare = _record(shape, has_text_and_links=False)
    data, offset_data = _files((_KEY, bare), (_NEXT_KEY, _record(shape, _NEXT_KEY)))

    first, _second = parse_skill_records(data, offset_data)

    assert (first.cooldown_ms, first.buff_ids) == (_COOLDOWN_MS, _BUFF_IDS)


def test_a_record_with_a_byte_too_many_names_where_each_layout_broke() -> None:
    data, offset_data = _files((_KEY, _record(_SHAPES[3]) + b"\x00"))

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 3: .*; Layout 2: .*; Layout 1: "):
        parse_skill_records(data, offset_data)


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)
    data, offset_data = _files((_KEY, bytes(16)))

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 3: .*; Layout 2: "):
        parse_skill_records(data, offset_data)
