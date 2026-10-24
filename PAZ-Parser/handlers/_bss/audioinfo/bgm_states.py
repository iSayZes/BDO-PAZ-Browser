"""The four Wwise `BGM` states and the ambience index that end an `audioinfo.bss` row.

`abyssoneaudioinfo.bss` rows end in the same 20 bytes: four string table
indexes (`bgm_states`) and the `ENV_INDEX_<n>` state (`bank_no_environment`).
"""

from __future__ import annotations

import struct

from _common.html import e, html_list_cell
from _common.pabr_strings import string_at


BGM_STATE_SLOTS = 4
# bgm_states, then bank_no_environment.
BGM_TAIL = struct.Struct(f"<{BGM_STATE_SLOTS}II")

BGM_STATE_SEPARATOR = " / "
_EMPTY = "-"


def bgm_fields(values: tuple[int, ...], strings: list[str]) -> dict:
    """`bgm_states`, their names and `bank_no_environment` from the values `BGM_TAIL` unpacks."""
    indexes = list(values[:BGM_STATE_SLOTS])
    names = [string_at(strings, index) for index in indexes]
    return {
        "bgm_states": indexes,
        "bgm_state_names": names,
        # One search and sort field, the four slots in order.
        "bgm_states_text": BGM_STATE_SEPARATOR.join(names),
        "bank_no_environment": values[BGM_STATE_SLOTS],
    }


def bgm_states_cell(names: list[str]) -> str:
    """The four state names, one per line in slot order."""
    return html_list_cell([e(name or _EMPTY) for name in names], separator="<br>")
