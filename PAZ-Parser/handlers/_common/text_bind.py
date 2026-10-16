"""TextBind placeholders: LOC and inline text that names another text.

Two forms occur, `{StringTableBind(TextBind:NAME)}` in quest and dialog text
(quest 4470 / 3, `{StringTableBind(TextBind:GROWTHPASS_PC_CONSOLE_SEP1)}`)
and `{TextBind:NAME}` in item, Pearl Shop, skill and `stringtable.bss` text.
Both name one text: LOC type 59 with `str_id1` the `key_hash()` of NAME and
four variants in `str_id4`, or the Korean `textbind.dbss` record of the same
key. The browser shows variant 0, the PC text
(docs/file-formats/textbind_dbss.md).

This module only finds and replaces placeholders; `_common/loc.py` supplies the
text of a name (LOC first, then `korean_text_bind()`), since every LOC read
fills them. A name with no text keeps its placeholder. A key binding
(`{KeyBind:...}`) is not fixed text and stays as written here; `pa_text.py`
draws it as a key.
"""

from __future__ import annotations

import re
from collections.abc import Callable

from _common.lookup_index import IndexKind, lookup
from _common.string_hash import key_hash

LOC_TEXT_BIND = 59
# LOC str_id4 and textbind.dbss variant of the PC text.
TEXT_BIND_VARIANT = 0
MARKER = "TextBind:"
_PLACEHOLDER = re.compile(
    r"\{StringTableBind\(TextBind:([A-Za-z0-9_]+)\)\}|\{TextBind:([A-Za-z0-9_]+)\}"
)
# A TextBind text can hold another placeholder (452 type 59 rows on client
# 3464); the fill stops this deep so a name that names itself cannot loop.
_MAX_DEPTH = 4


def korean_text_bind(name: str) -> str:
    """Korean `textbind.dbss` text of one name, or '' when the index lacks it."""
    text = lookup(IndexKind.TEXT_BIND_KR, key_hash(name))
    return text if isinstance(text, str) else ""


def fill_text_binds(text: str, text_of: Callable[[str], str], depth: int = 0) -> str:
    """`text` with each placeholder `text_of(name)` has text for replaced by it,
    nested placeholders included."""
    if MARKER not in text or depth >= _MAX_DEPTH:
        return text

    def replace(match: re.Match[str]) -> str:
        found = text_of(match.group(1) or match.group(2))
        return fill_text_binds(found, text_of, depth + 1) if found else match.group(0)

    return _PLACEHOLDER.sub(replace, text)
