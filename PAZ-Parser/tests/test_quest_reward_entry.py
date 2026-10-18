"""The shared quest reward entry of `quest.dbss` and `guildquest.dbss`."""
from __future__ import annotations

import struct
from collections.abc import Iterator

import pytest

import _common.loc as loc
from _bss.stringtable.parser import GAME_SHEET, GAME_SHEET_LOC_ID2, parse_key_hashes
from _bss.stringtable.text import LOC_UI_STRING
from _common.knowledge import LOC_KNOWLEDGE
from _common.quest.reward_entry import (
    FAMILY_STAT_OFFSET,
    REWARD_ENTRY_SIZE,
    REWARD_EXP_GRADE,
    REWARD_EXPLORE_EXP,
    REWARD_FEVER_POINT,
    REWARD_INTIMACY,
    REWARD_ITEM,
    REWARD_KNOWLEDGE,
    REWARD_SEASON_REWARD,
    REWARD_SKILL_EXP_GRADE,
    REWARD_TYPE_NAMES,
    read_reward_entry,
    read_reward_list,
)
from _common.quest.reward_text import KEY_HASHES, reward_text
from _common.record_reader import RecordReader
from tests.fixtures import load_binary_fixture
from tests.loc_counter import reset_loc
from tests.loc_data import LocRow, loc_bytes

_NO_LIFE_SKILL = 15
_NO_FAMILY_STAT = 16
# Offsets of the tail members, from the entry start.
_MENTAL_CARD_KEY = 0x2B
_EXP_GRADE = 0x31
_MAX_FEVER_POINT = 0xA0
_ADD_FEVER_POINT = 0xA4
_UNKNOWN_A8 = 0xA8
_SEASON_NO = 0xA9
_EXPLORE_EXP = 0xAA
_CARD = 9550


def _entry(
    reward_type: int, *, item_key: int = 0, item_count: int = 0, npc: int = 0, amity: int = 0,
    tail: tuple[tuple[str, int, int], ...] = (),
) -> bytes:
    """One entry; `tail` packs (format, offset, value) into the bytes after the head."""
    head = struct.pack("<IqiiBiIqHi", reward_type, 0, 0, 0, _NO_LIFE_SKILL, 0, item_key, item_count, npc, amity)
    entry = bytearray(head + bytes(REWARD_ENTRY_SIZE - len(head)))
    entry[FAMILY_STAT_OFFSET] = _NO_FAMILY_STAT
    for fmt, offset, value in tail:
        struct.pack_into(fmt, entry, offset, value)
    return bytes(entry)


def _read(raw: bytes) -> dict:
    reader = RecordReader(raw, 0, len(raw), "entry")
    entry = read_reward_entry(reader)
    assert reader.at_end()
    return dict(entry)


def _text(raw: bytes) -> str | None:
    return reward_text(read_reward_entry(RecordReader(raw, 0, len(raw), "entry")))


def test_entry_members_sit_at_the_byte_packed_offsets() -> None:
    raw = _entry(REWARD_ITEM, item_key=0x0100_0222, item_count=7)

    entry = _read(raw)

    assert struct.unpack_from("<I", raw, 0x19)[0] == entry["item_key"] == 0x0100_0222
    assert struct.unpack_from("<q", raw, 0x1D)[0] == entry["item_count"] == 7
    assert entry["life_experience_type"] == _NO_LIFE_SKILL
    assert bytes.fromhex(entry["family_stat"])[0] == _NO_FAMILY_STAT


@pytest.mark.parametrize(("fmt", "offset", "field"), [
    ("<i", _MENTAL_CARD_KEY, "mental_card_key"),
    ("<B", _EXP_GRADE, "exp_grade"),
    ("<I", _MAX_FEVER_POINT, "max_fever_point"),
    ("<I", _ADD_FEVER_POINT, "add_fever_point"),
    ("<B", _SEASON_NO, "season_no"),
    ("<q", _EXPLORE_EXP, "explore_exp"),
])
def test_tail_members_sit_at_their_offsets(fmt: str, offset: int, field: str) -> None:
    value = 0x7B
    entry = _read(_entry(REWARD_KNOWLEDGE, tail=((fmt, offset, value),)))
    assert entry[field] == value
    others = {"mental_card_key", "exp_grade", "max_fever_point", "add_fever_point", "season_no", "explore_exp"} - {field}
    assert all(entry[name] == 0 for name in others)


def test_explore_exp_ends_the_entry() -> None:
    assert _EXPLORE_EXP + struct.calcsize("<q") == REWARD_ENTRY_SIZE


def test_list_reads_its_count_then_the_entries() -> None:
    raw = struct.pack("<I", 2) + _entry(REWARD_ITEM, item_key=1, item_count=500) + _entry(
        REWARD_INTIMACY, npc=41011, amity=40
    )
    reader = RecordReader(raw, 0, len(raw), "list")

    rewards = read_reward_list(reader)

    assert reader.at_end()
    assert [r["reward_type"] for r in rewards] == [REWARD_ITEM, REWARD_INTIMACY]
    assert (rewards[1]["intimacy_character"], rewards[1]["intimacy_value"]) == (41011, 40)


def test_list_past_its_record_is_rejected() -> None:
    raw = struct.pack("<I", 2) + _entry(REWARD_ITEM)
    with pytest.raises(ValueError, match="runs past"):
        read_reward_list(RecordReader(raw, 0, len(raw), "list"))


def test_label_hashes_match_stringtable() -> None:
    hashes = parse_key_hashes(load_binary_fixture("stringtable.bss"), GAME_SHEET)
    wrong = {
        key: (key_hash, hashes.get(key))
        for key, key_hash in KEY_HASHES[GAME_SHEET].items()
        if hashes.get(key) != key_hash
    }
    assert not wrong, f"reward label hashes differ from stringtable.bss (stored, file): {wrong}"


def _ui_row(key: str, text: str) -> LocRow:
    return (LOC_UI_STRING, KEY_HASHES[GAME_SHEET][key], GAME_SHEET_LOC_ID2, 0, 0, text)


_ROWS: list[LocRow] = [
    _ui_row("LUA_REWARDITEM_KNOWLEDGE", "<PAColor0xffffc832>[Knowledge] {mentalCardName}<PAOldColor>"),
    _ui_row("LUA_QUESTREWARD_EXPLOREEXP", "Contribution EXP +{exp}"),
    _ui_row("LUA_ACHIEVEMENT_REWARD_TYPE_MAXFEVERPOINT", "Max Points +{maxFeverPoint}"),
    _ui_row("LUA_ACHIEVEMENT_REWARD_TYPE_ADDFEVERPOINT", "Recovery Point +{addFeverPoint}"),
    _ui_row("LUA_QUESTREWARD_SIMPLE_TOOLTIP_EXP_GRADE", "Combat EXP"),
    _ui_row("LUA_QUESTREWARD_SIMPLE_TOOLTIP_SKILLEXP_GRADE", "Skill EXP"),
    _ui_row("LUA_QUESTREWARD_SIMPLE_TOOLTIP_COMPLETE_SEASON", "Season Gift Exchange Coupon"),
    (LOC_KNOWLEDGE, _CARD, 0, 0, 0, "Pet - Dog"),
]


@pytest.fixture
def _loc() -> Iterator[None]:
    reset_loc()
    loc.init_loc(loc_bytes(_ROWS))
    yield
    reset_loc()


@pytest.mark.usefixtures("_loc")
@pytest.mark.parametrize(("reward_type", "tail", "text"), [
    (REWARD_KNOWLEDGE, (("<i", _MENTAL_CARD_KEY, _CARD),), "[Knowledge] Pet - Dog"),
    (REWARD_EXPLORE_EXP, (("<q", _EXPLORE_EXP, 1500),), "Contribution EXP +1,500"),
    (REWARD_FEVER_POINT, (("<I", _MAX_FEVER_POINT, 5000),), "Max Points +5,000"),
    (REWARD_FEVER_POINT, (("<I", _ADD_FEVER_POINT, 2500),), "Recovery Point +2,500"),
    (REWARD_EXP_GRADE, (("<B", _EXP_GRADE, 36),), "Combat EXP"),
    (REWARD_SKILL_EXP_GRADE, (), "Skill EXP"),
    (REWARD_SEASON_REWARD, (("<B", _SEASON_NO, 13),), "Season Gift Exchange Coupon"),
])
def test_later_types_read_as_the_reward_widget_names_them(
    reward_type: int, tail: tuple[tuple[str, int, int], ...], text: str,
) -> None:
    assert _text(_entry(reward_type, tail=tail)) == text


@pytest.mark.usefixtures("_loc")
def test_fever_reward_without_points_has_no_text() -> None:
    assert _text(_entry(REWARD_FEVER_POINT, tail=(("<B", _UNKNOWN_A8, 1),))) is None


def test_without_loc_a_reward_shows_its_enum_name() -> None:
    reset_loc()
    text = _text(_entry(REWARD_KNOWLEDGE, tail=(("<i", _MENTAL_CARD_KEY, _CARD),)))
    assert text == f"{REWARD_TYPE_NAMES[REWARD_KNOWLEDGE]} {_CARD}"
