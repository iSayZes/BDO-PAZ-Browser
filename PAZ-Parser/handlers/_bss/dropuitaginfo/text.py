"""Drop item window tag text from LOC type 117, by tag key.

`str_id4` 0 is the tag name (`#LotsOfMobs`) and 1 its tooltip, which holds
`<PAColor>` tags.
"""

from __future__ import annotations

from _common.loc import loc_tagged, loc_text

LOC_TAG = 117
_NAME_FIELD = 0
_DESCRIPTION_FIELD = 1


def tag_name(key: int) -> str:
    """The tag name, or '' when LOC has none or is not loaded."""
    return loc_text(LOC_TAG, key, _NAME_FIELD)


def tag_description_tagged(key: int) -> str:
    """The tag tooltip with its PA tags, or '' when LOC has none or is not loaded."""
    return loc_tagged(LOC_TAG, key, _DESCRIPTION_FIELD)
