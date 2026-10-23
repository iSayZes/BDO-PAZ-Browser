"""Challenge texts: LOC type 48, keyed by the `challenge.dbss` challenge key.

A row is `(48, challenge_key, 0, str_id3, slot)`: slot 0 is the title, 1 the
description. `str_id3` is `12` on every key of `challenge.dbss` and `28` on
111 keys from `10000` up that the file does not hold (client 3483;
challenge_dbss.md, Notes).
"""

from __future__ import annotations

from _common.loc import loc_lookup, strip_pa_tags


LOC_CHALLENGE = 48
TITLE_SLOT = 0
DESCRIPTION_SLOT = 1
_STR_ID3 = (12, 28)


def challenge_tagged(challenge_key: int, slot: int) -> str:
    """The LOC text of one slot with its PA tags, or '' on a miss or without LOC."""
    for str_id3 in _STR_ID3:
        text = loc_lookup(LOC_CHALLENGE, challenge_key, 0, str_id3, slot).strip()
        if text:
            return text
    return ""


def challenge_name(challenge_key: int) -> str:
    """The challenge title without tags, or ''."""
    return strip_pa_tags(challenge_tagged(challenge_key, TITLE_SLOT)).strip()
