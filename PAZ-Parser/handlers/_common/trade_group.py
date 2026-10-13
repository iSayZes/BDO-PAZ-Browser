"""Trade group type codes, shared by `itemtradegrouptonpc.dbss` and `itemtradeetc.bss`.

The client does not name the codes. The labels in `_common/lang/` come from
the trade NPCs and goods that hold each code (docs/file-formats/
itemtradegrouptonpc_dbss.md, Trade Group Types), so columns that show them
carry a `*` and the `tooltip` text.
"""

from __future__ import annotations

from pathlib import Path

from _common.lang import load_handler_strings

_COMMON_LANG_DIR = Path(__file__).parent / "lang"


def _strings(lang: str) -> dict:
    return load_handler_strings(lang, _COMMON_LANG_DIR)["tradeGroups"]


def trade_group_text(lang: str, code: int) -> str:
    """`2 Valencia City`, or the bare code when it has no label."""
    label = _strings(lang).get(str(code))
    return f"{code} {label}" if label else str(code)


def trade_group_tooltip(lang: str) -> str:
    """Header tooltip of a column that shows `trade_group_text`."""
    return _strings(lang)["tooltip"]
