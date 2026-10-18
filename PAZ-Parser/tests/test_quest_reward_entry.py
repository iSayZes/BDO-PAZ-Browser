"""The shared quest reward entry of `quest.dbss` and `guildquest.dbss`."""
from __future__ import annotations

import struct

import pytest

from _bss.stringtable.parser import GAME_SHEET, parse_key_hashes
from _common.quest.reward_entry import (
    FAMILY_STAT_OFFSET,
    REWARD_ENTRY_SIZE,
    REWARD_INTIMACY,
    REWARD_ITEM,
    read_reward_entry,
    read_reward_list,
)
from _common.quest.reward_text import KEY_HASHES
from _common.record_reader import RecordReader
from tests.fixtures import load_binary_fixture

_NO_LIFE_SKILL = 15
_NO_FAMILY_STAT = 16


def _entry(reward_type: int, *, item_key: int = 0, item_count: int = 0, npc: int = 0, amity: int = 0) -> bytes:
    head = struct.pack("<IqiiBiIqHi", reward_type, 0, 0, 0, _NO_LIFE_SKILL, 0, item_key, item_count, npc, amity)
    entry = bytearray(head + bytes(REWARD_ENTRY_SIZE - len(head)))
    entry[FAMILY_STAT_OFFSET] = _NO_FAMILY_STAT
    return bytes(entry)


def test_entry_members_sit_at_the_byte_packed_offsets() -> None:
    raw = _entry(REWARD_ITEM, item_key=0x0100_0222, item_count=7)
    reader = RecordReader(raw, 0, len(raw), "entry")

    entry = read_reward_entry(reader)

    assert reader.at_end()
    assert struct.unpack_from("<I", raw, 0x19)[0] == entry["item_key"] == 0x0100_0222
    assert struct.unpack_from("<q", raw, 0x1D)[0] == entry["item_count"] == 7
    assert entry["life_experience_type"] == _NO_LIFE_SKILL
    assert len(bytes.fromhex(entry["unknown_2b"])) == REWARD_ENTRY_SIZE - 0x2B


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
