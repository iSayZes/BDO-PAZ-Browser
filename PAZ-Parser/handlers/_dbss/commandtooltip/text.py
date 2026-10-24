"""The command text of a `commandtooltip.dbss` row in the user's language.

LOC type 55 holds both texts under `(key_hash, 0, 0, variant)`: variant 0 is
`pc_command_kr`, 1 is `console_command_kr`. Kept out of `handler.py` so tests
can import it without loading the handler registry.
"""

from __future__ import annotations

from _common.loc import loc_tagged, resolve_text_binds

LOC_COMMAND_TOOLTIP = 55
PC_VARIANT = 0
CONSOLE_VARIANT = 1

# The Korean text stores line breaks as the two characters "\n".
_LINE_BREAK = "\\n"


def command_text(key_hash: int, variant: int, text_kr: str) -> str:
    """The LOC text of one variant with its PA tags, else the Korean with real line breaks."""
    return loc_tagged(LOC_COMMAND_TOOLTIP, key_hash, variant) or resolve_text_binds(
        text_kr.replace(_LINE_BREAK, "\n")
    ).strip()
