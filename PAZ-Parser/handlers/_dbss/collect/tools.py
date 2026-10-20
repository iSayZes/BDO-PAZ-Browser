"""Display names of the gathering tool types in `collect.dbss`.

`CppEnums.CollectToolTypeName` in global_define_cpp_enum.luac names each tool
by a GAME sheet string key; LOC type 37 holds the text under the key's hash.
The numbers are the 2016 `gc::CollectToolType::Type` values, which list the
tools in the Lua's order. The Lua names MassStone and the later tools with
inline Korean text and no key, so they show as their number.
"""

from __future__ import annotations

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.string_hash import key_hash

_KEY_PREFIX = "LUA_GLOBAL_DEFINE_CPP_ENUM_ETYPE_"

# Tool type -> GAME sheet key of its name.
TOOL_NAME_KEYS: dict[int, str] = {
    tool_type: _KEY_PREFIX + name
    for tool_type, name in enumerate((
        "BAREHANDS",
        "EMPTYBOTTLE",
        "AXE",
        "SYRINGE",
        "HOE",
        "BUTCHERYKNIFE",
        "SKINKNIFE",
        "PICKAX",
        "TWEEZERS",
        "PRAY",
        "MAGNIFYINGLENS",
    ))
}


def tool_display_name(tool_type: int) -> str:
    """The tool's name in the loaded LOC language, else the tool type number."""
    key = TOOL_NAME_KEYS.get(tool_type)
    if key is None:
        return str(tool_type)
    return ui_hash_text(GAME_SHEET, key_hash(key)) or str(tool_type)
