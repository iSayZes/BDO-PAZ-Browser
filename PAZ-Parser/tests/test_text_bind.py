from __future__ import annotations

from collections.abc import Iterator

import pytest

from _common.loc import init_loc
from _common.quest.quest import LOC_QUEST, quest_text_tagged, quest_title
from _common.string_hash import key_hash
from _common.text_bind import LOC_TEXT_BIND, resolve_text_binds, text_bind_tagged
from tests.loc_counter import reset_loc
from tests.loc_data import loc_bytes

_NAME = "GROWTHPASS_PC_CONSOLE_SEP1"
_MENU = "<PAColor0xfff5ba3a>[Menu]<PAOldColor> Quick Hotkey Settings"
_RING = "<PAColor0xfff5ba3a>[Menu]<PAOldColor> Ring Menu Setting"
_PLACEHOLDER = f"{{StringTableBind(TextBind:{_NAME})}}"
_UNKNOWN = "{StringTableBind(TextBind:NOT_IN_LOC)}"
_KEY_BIND = "{StringTableBind(KeyBind:Attack2)}"


@pytest.fixture(autouse=True)
def _loc() -> Iterator[None]:
    init_loc(loc_bytes([
        (LOC_TEXT_BIND, key_hash(_NAME), 0, 0, 0, _MENU),
        (LOC_TEXT_BIND, key_hash(_NAME), 0, 0, 1, _RING),
        (LOC_QUEST, 4470, 3, 0, 0, _PLACEHOLDER),
    ]))
    yield
    reset_loc()


def test_text_bind_reads_variant_0() -> None:
    assert text_bind_tagged(_NAME) == _MENU


def test_placeholder_takes_its_text_in_place() -> None:
    assert resolve_text_binds(f"Open {_PLACEHOLDER}.") == f"Open {_MENU}."


def test_unknown_name_and_key_bind_stay_as_written() -> None:
    text = f"{_UNKNOWN} {_KEY_BIND} {{KeyBind:Jump}}"

    assert resolve_text_binds(text) == text


def test_quest_text_fills_the_placeholder() -> None:
    assert quest_text_tagged(4470, 3) == _MENU
    assert quest_title(4470, 3) == "[Menu] Quick Hotkey Settings"
