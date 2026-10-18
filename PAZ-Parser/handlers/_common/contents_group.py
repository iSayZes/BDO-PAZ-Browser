"""Contents group keys stored as the client's string hash of their decimal text.

`characterstatic.dbss`, `skillsimply.dbss` and `guildquest.dbss` store each
contents group as `key_hash(str(key))` (`_common/string_hash.py`); the open
list of `contentsgroupoptionstaticstatusmanager.bss` holds the same hashes.
"""

from __future__ import annotations

from functools import cache

from _common.string_hash import KEY_HASH_SEED, hashlittle

# Contents group keys are 16-bit (2016 `KeyType<short>`); client 3474 uses up to 8,122.
_CONTENTS_GROUP_KEY_COUNT = 0x8000


@cache
def _contents_group_keys_by_hash() -> dict[int, int]:
    # hashlittle, not the cached key_hash: 32,768 keys would flush its cache.
    return {
        hashlittle(str(key).encode("utf-16-le"), KEY_HASH_SEED): key
        for key in range(_CONTENTS_GROUP_KEY_COUNT)
    }


def contents_group_key(group_hash: int) -> int | None:
    """The contents group key whose decimal text hashes to `group_hash`, or None."""
    return _contents_group_keys_by_hash().get(group_hash)


def contents_groups_text(group_hashes: tuple[int, ...] | list[int]) -> str:
    """`1307, 1981`: the keys behind the hashes, a hash in hex where no key fits."""
    texts = []
    for group_hash in group_hashes:
        key = contents_group_key(group_hash)
        texts.append(f"0x{group_hash:08X}" if key is None else str(key))
    return ", ".join(texts)
