"""Layouts of the client, sound and web option tables that fit the PABR value tables.

Each file's doc is `docs/file-formats/bss/<stem>_bss.md`. The field names follow
the sheets of a private server's `DataSheets.bexcel` on client 1784
(`CharacterLobby_Table`, `BgmState_Table`, `BgmStateSA_Table`, `SA_Web_URL`
and `Leddevice`). `weburl.bss` has rows of its own size and its own handler
(`_bss/weburl/`).
"""

from __future__ import annotations

from .client_names import rgb_text
from .fields import CHARACTER_KEY
from .layout import RowCount, TextRef, ValueField, ValueTable


def _text(name: str, column: str) -> ValueField:
    """A string-table index `<name>_ref`; the record keeps its string as `<name>`."""
    return ValueField(f"{name}_ref", "I", text=TextRef(name, column))


# The row key of the two background music tables (bgmstate_bss.md, bgmstatesa_bss.md).
_BGM_INDEX = ValueField("index", "H", "index")


CLIENT_TABLES: tuple[ValueTable, ...] = (
    ValueTable(
        "characterlobby.bss",
        (
            CHARACTER_KEY,
            ValueField("zoom_in_max", "f", "zoomInMax"),
            ValueField("zoom_out_max", "f", "zoomOutMax"),
        ),
        RowCount.COUNTED,
        count_key="lobbyCharacters",
    ),
    ValueTable(
        "bgmstate.bss",
        (
            _text("event_name", "eventName"),
            ValueField("unknown_04", "I"),
            _BGM_INDEX,
            ValueField("processor_type", "B", "processorType"),
            ValueField("lobby_mode", "B", "lobbyMode"),
        ),
        RowCount.COUNTED,
        count_key="bgmStates",
        first_fields=(_BGM_INDEX.name,),
    ),
    ValueTable(
        "bgmstatesa.bss",
        (
            _text("event_name", "eventName"),
            ValueField("unknown_04", "I"),
            _text("game_condition", "gameCondition"),
            _BGM_INDEX,
        ),
        RowCount.COUNTED,
        count_key="gameConditions",
        first_fields=(_BGM_INDEX.name,),
    ),
    ValueTable(
        "sha_weburl.bss",
        (
            _text("record_client", "recordClient"),
            ValueField("unknown_08", "I"),
            ValueField("unknown_0c", "I"),
            _text("cash_shop", "cashShop"),
            ValueField("unknown_14", "I"),
            _text("replay", "replay"),
            _text("payment", "payment"),
        ),
    ),
    ValueTable(
        "leddevice.bss",
        (
            ValueField("device_type", "H", "deviceType"),
            ValueField("animation_no", "H", "animationNo"),
            _text("asus", "asus"),
            _text("razer", "razer"),
            ValueField("real_rgb", "i", "realRgb", display=rgb_text),
        ),
        RowCount.COUNTED,
        count_key="ledEffects",
        first_fields=("animation_no",),
    ),
)
