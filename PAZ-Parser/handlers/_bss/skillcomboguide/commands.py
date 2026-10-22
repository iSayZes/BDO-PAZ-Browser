"""The key binding text of a combo step, ready for `pa_html()`.

A step's command is stored like `<{KeyBind:MoveBack}> + <{KeyBind:Kick}>`
or `<{KeyBind:Dash}> + [ComboSheet_CommonString_1]`: each key binding in
angle brackets, and `[key]` for a `GAME` sheet string of `stringtable.bss`
(`ComboSheet_CommonString_1` is "Directional Key"). The brackets go, so the
key bindings show as key chips and the keys as their LOC text.
"""

from __future__ import annotations

import re
from collections.abc import Mapping

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_tagged

# `<{KeyBind:Name}>`: the binding without its angle brackets.
_BRACKETED_KEY_BIND_RE = re.compile(r"<(\{KeyBind:[A-Za-z0-9_]+\})>")
# `[ComboSheet_CommonString_1]`; `[/]` and other brackets stay.
_STRING_KEY_RE = re.compile(r"\[([A-Za-z][A-Za-z0-9_]*)\]")


def command_tagged(raw: str, game_key_hashes: Mapping[str, int]) -> str:
    """`raw` with bare key bindings and every `[key]` that has a LOC text replaced by it."""
    hashes = {GAME_SHEET: game_key_hashes}

    def _key_text(match: re.Match[str]) -> str:
        return ui_key_tagged(hashes, GAME_SHEET, match.group(1)) or match.group(0)

    return _STRING_KEY_RE.sub(_key_text, _BRACKETED_KEY_BIND_RE.sub(r"\1", raw)).strip()
