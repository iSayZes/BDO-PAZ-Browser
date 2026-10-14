"""`{StringTableBind(TextBind:NAME)}` placeholders in LOC text.

Quest and dialog text can be one of these instead of the text itself, such as
quest 4470 / 3, `{StringTableBind(TextBind:GROWTHPASS_PC_CONSOLE_SEP1)}`. The
text is LOC type 59 with `str_id1` the `key_hash()` of NAME and four variants
in `str_id4`; this reads variant 0 (docs/file-formats/languagedata_loc.md).
A name LOC does not hold keeps its placeholder.

`{StringTableBind(KeyBind:...)}` names a player key binding, not fixed text,
so it stays as written, and so does a `{KeyBind:...}` inside a TextBind text.
"""

from __future__ import annotations

import re

from _common.loc import loc_lookup
from _common.string_hash import key_hash

LOC_TEXT_BIND = 59
_DEFAULT_VARIANT = 0
_MARKER = "TextBind:"
_PLACEHOLDER = re.compile(r"\{StringTableBind\(TextBind:([A-Za-z0-9_]+)\)\}")


def text_bind_tagged(name: str) -> str:
    """LOC text of one TextBind name with its PA tags, or ''."""
    return loc_lookup(LOC_TEXT_BIND, key_hash(name), 0, 0, _DEFAULT_VARIANT).strip()


def _replacement(match: re.Match[str]) -> str:
    return text_bind_tagged(match.group(1)) or match.group(0)


def resolve_text_binds(text: str) -> str:
    """`text` with every TextBind placeholder LOC can fill replaced by its text."""
    if _MARKER not in text:
        return text
    return _PLACEHOLDER.sub(_replacement, text)
