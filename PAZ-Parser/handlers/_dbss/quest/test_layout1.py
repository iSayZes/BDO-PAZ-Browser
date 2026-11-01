"""Layout 1 (client 1784) reads back from a small built file, through the parser and the handler."""

from __future__ import annotations

import struct

import pytest

from bdo_models import PazEntry
from _common.quest.reward_entry import REWARD_ENTRY_LAYOUT_1, REWARD_FAMILY_STAT, REWARD_ITEM

from .handler import QuestDbssHandler
from .layout1 import QuestIndexLayout1
from .parser import build_quest_index, build_quest_icon_index, parse_quest_record


_FOLDER = "gamecommondata/binary"
_NO_LIFE_SKILL = 15
_NO_FAMILY_STAT = 16
_HP_TYPE = 2
# Family Stat Union start, and the HP field within it.
_FAMILY_STAT_OFFSET = 0x67
_HP_OFFSET = 0x0C
_HP = 40.0
# Packed IDs: (quest_id << 16) | quest_chain_id.
_FIRST_ID = (4 << 16) | 343
_SECOND_ID = (1 << 16) | 1003
_QUEST_TYPE = 6
_BLOCK_KIND = 7
_ICON = "Icon/Quest/343_2.dds"


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _entry(reward_type: int, *, item_key: int = 0, item_count: int = 0, hp: float = 0.0) -> bytes:
    """One 188-byte entry; `hp` sets an HP Family stat."""
    head = struct.pack("<IqiiBiIqHi", reward_type, 0, 0, 0, _NO_LIFE_SKILL, 0, item_key, item_count, 0, 0)
    entry = bytearray(head + bytes(REWARD_ENTRY_LAYOUT_1.size - len(head)))
    struct.pack_into("<I", entry, _FAMILY_STAT_OFFSET, _HP_TYPE if hp else _NO_FAMILY_STAT)
    struct.pack_into("<f", entry, _FAMILY_STAT_OFFSET + _HP_OFFSET, hp)
    return bytes(entry)


def _rewards(*entries: bytes) -> bytes:
    return struct.pack("<I", len(entries)) + b"".join(entries)


def _record(packed_quest_id: int, *, icon: str = _ICON) -> bytes:
    """One record in the order of quest_dbss.md "Layout 1", every list and string filled."""
    return b"".join((
        struct.pack("<II", 102689, 102690),
        _str16("반하"),
        struct.pack("<I", 56),
        _str16("clearquest(343,4);"),
        _str16("collectKnowledge(5706);"),
        _str16("미스틱의 자질 습득하기;"),
        _str16("getLevel()>8;"),
        b"\x00",
        _rewards(_entry(REWARD_ITEM, item_key=55, item_count=1), _entry(REWARD_FAMILY_STAT, hp=_HP)),
        _rewards(_entry(REWARD_ITEM, item_key=184, item_count=2)),
        _rewards(_entry(REWARD_ITEM, item_key=56467, item_count=1)),
        bytes(25),
        _str16("세상에 일어날 파란"),
        _str16("반하는 자신이 주는 세 가지 의뢰를 완수하면"),
        struct.pack("<I", 1) + struct.pack("<4f", 1.0, 2.0, 3.0, 1000.0),
        _str8(icon),
        _str8(""),
        struct.pack("<I", 1) + struct.pack("<BI", 7, 1) + _str8("https://example.com/notes") + _str16("notes"),
        _str16("accept") + _str16("") + _str16("complete") + _str16("progress"),
        struct.pack("<IBBIII", 24, _BLOCK_KIND, 1, 3, _QUEST_TYPE, 5),
        struct.pack("<I", packed_quest_id),
        bytes(5),
        struct.pack("<II", 1, 0xFEED568F),
        bytes(14),
    ))


def _quest_file(records: list[bytes]) -> bytes:
    return struct.pack("<I", len(records)) + b"".join(records)


def _allquestlist(ids: list[int]) -> bytes:
    return b"PABR" + struct.pack(f"<I{len(ids)}I", len(ids), *ids) + bytes(12)


def test_layout1_reads_every_field_the_record_model_holds() -> None:
    data = _quest_file([_record(_FIRST_ID), _record(_SECOND_ID)])

    index = build_quest_index(data, [_FIRST_ID, _SECOND_ID])
    first = parse_quest_record(data, index, 0)

    assert isinstance(index, QuestIndexLayout1)
    assert len(index) == 2
    assert (first["quest_chain_id"], first["quest_id"]) == (343, 4)
    assert (first["accept_dialog_key"], first["complete_dialog_key"]) == (102689, 102690)
    assert first["condition_script"] == "clearquest(343,4);"
    assert first["action_script"] == "collectKnowledge(5706);"
    assert first["objective_text_kr"] == "미스틱의 자질 습득하기;"
    assert (first["quest_category"], first["block_kind"]) == (_QUEST_TYPE, _BLOCK_KIND)
    assert first["icon_path"] == _ICON
    assert [r["item_key"] for r in first["base_rewards"]] == [55, 0]
    assert [r["item_key"] for r in first["select_rewards"]] == [184]
    assert first["family_stats"] == [{"entry": 1, "type": _HP_TYPE, "label": "HP", "value": _HP}]
    assert first["offset"] + first["size"] == parse_quest_record(data, index, 1)["offset"]


def test_layout1_icon_index_reads_each_record() -> None:
    data = _quest_file([_record(_FIRST_ID), _record(_SECOND_ID, icon="")])

    icons = build_quest_icon_index(data, _allquestlist([_FIRST_ID, _SECOND_ID]))

    assert list(icons) == [_FIRST_ID]
    assert icons[_FIRST_ID].endswith("343_2.dds")


def test_a_record_with_another_quest_id_fits_no_layout() -> None:
    data = _quest_file([_record(_FIRST_ID)])

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .*; Layout 1: .*allquestlist.bss lists"):
        build_quest_index(data, [_SECOND_ID])


def test_bytes_after_the_last_record_fit_no_layout() -> None:
    data = _quest_file([_record(_FIRST_ID)]) + b"\x00"

    with pytest.raises(ValueError, match="Layout 1: quest.dbss records end at"):
        build_quest_index(data, [_FIRST_ID])


def test_handler_names_layout1_quest_types_by_the_1784_enum() -> None:
    """With no string table the name is the enum name: 6 is `Repetition` there, `OceanLife` on Layout 2."""
    data = _quest_file([_record(_FIRST_ID)])
    entry = PazEntry("", f"{_FOLDER}/quest.dbss", 0, 0, 0, 0, 0)
    companions = {"allquestlist.bss": _allquestlist([_FIRST_ID])}

    (record,) = QuestDbssHandler().get_records(data, entry, companions)

    assert record["quest_category"] == _QUEST_TYPE
    assert record["quest_type_name"] == "Repetition"
