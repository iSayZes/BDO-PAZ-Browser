from __future__ import annotations

import pytest

from _common.string_hash import KEY_HASH_SEED, hashlittle, key_hash

_SCORE = b"Four score and seven years ago"


@pytest.mark.parametrize(
    ("data", "seed", "expected"),
    [
        # The driver5() checks in Bob Jenkins' lookup3.c.
        (b"", 0, 0xDEADBEEF),
        (b"", 0xDEADBEEF, 0xBD5B7DDE),
        (_SCORE, 0, 0x17770551),
        (_SCORE, 1, 0xCD628161),
    ],
)
def test_hashlittle_matches_the_reference(data: bytes, seed: int, expected: int) -> None:
    assert hashlittle(data, seed) == expected


def test_key_hash_reads_the_utf16_key() -> None:
    # stringtable.bss GAME key hash; also the LOC type 37 str_id1 of the key.
    assert key_hash("LUA_GROWTHPASS_WIDGET_ICON_NOTICE_NEW_DESC") == 1517777731
    assert key_hash("GAME") == hashlittle("GAME".encode("utf-16-le"), KEY_HASH_SEED)
