"""Display names of the processing actions in `manufacture.bss`.

The processing window (`MANUFACTURE_INFO` in panel_window_manufacture_all.luac)
pairs each `actionName` with a GAME sheet string key for its tab name. LOC
type 37 holds the text under the key's hash.
"""

from __future__ import annotations

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.string_hash import key_hash

# actionName -> GAME sheet key of its name, as MANUFACTURE_INFO lists them.
ACTION_NAME_KEYS: dict[str, str] = {
    "MANUFACTURE_SHAKE": "ALCHEMY_MANUFACTURE_SHAKE",
    "MANUFACTURE_GRIND": "ALCHEMY_MANUFACTURE_GRIND",
    "MANUFACTURE_FIREWOOD": "ALCHEMY_MANUFACTURE_WOODSPLITTING",
    "MANUFACTURE_DRY": "ALCHEMY_MANUFACTURE_DRY",
    "MANUFACTURE_THINNING": "ALCHEMY_MANUFACTURE_THINNING",
    "MANUFACTURE_HEAT": "ALCHEMY_MANUFACTURE_HEATING",
    "MANUFACTURE_RAINWATER": "GAME_MANUFACTURE_RAINWATER",
    "REPAIR_ITEM": "ALCHEMY_MANUFACTURE_REPAIR",
    "MANUFACTURE_ALCHEMY": "LUA_ALCHEMY_MANUFACTURE_ALCHEMY",
    "MANUFACTURE_COOK": "LUA_ALCHEMY_MANUFACTURE_COOK",
    "MANUFACTURE_ROYALGIFT_COOK": "LUA_ALCHEMY_MANUFACTURE_ROYALGIFT_COOK",
    "MANUFACTURE_ROYALGIFT_ALCHEMY": "LUA_ALCHEMY_MANUFACTURE_ROYALGIFT_ALCHEMY",
    # The client's spelling.
    "MANUFACTURE_GUILD": "LUA_MANUFACTURE_GUILDMANURACTURE_NAME",
    "MANUFACTURE_CRAFT": "LUA_MANUFACTURE_CRAFT_NAME",
}


def action_display_name(action: str) -> str:
    """The processing window's name of an action in the loaded LOC language, else the action name."""
    key = ACTION_NAME_KEYS.get(action)
    if key is None:
        return action
    return ui_hash_text(GAME_SHEET, key_hash(key)) or action
