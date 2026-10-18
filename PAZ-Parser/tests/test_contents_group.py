from __future__ import annotations

from _common.contents_group import contents_group_key, contents_groups_text
from _common.string_hash import key_hash


def test_contents_group_key_reverses_the_key_hash() -> None:
    assert contents_group_key(key_hash("0")) == 0
    assert contents_group_key(key_hash("1448")) == 1448
    assert contents_group_key(key_hash("not a key")) is None


def test_contents_groups_text_falls_back_to_the_hash_in_hex() -> None:
    unknown = key_hash("not a key")
    assert contents_groups_text([key_hash("1307"), unknown]) == f"1307, 0x{unknown:08X}"
    assert contents_groups_text(()) == ""
