from __future__ import annotations

from collections.abc import Iterator

import pytest

from _common.loc import init_loc, loc_lookup, loc_lookup_prefix, loc_type_entries, resolve_text_binds, text_bind_tagged
from _common.lookup_index import IndexKind, init_index
from _common.quest.quest import LOC_QUEST, quest_text_tagged, quest_title
from _common.string_hash import key_hash
from _common.text_bind import LOC_TEXT_BIND, fill_text_binds
from tests.loc_counter import reset_loc
from tests.loc_data import loc_bytes

_NAME = "GROWTHPASS_PC_CONSOLE_SEP1"
_MENU = "<PAColor0xfff5ba3a>[Menu]<PAOldColor> Quick Hotkey Settings"
_RING = "<PAColor0xfff5ba3a>[Menu]<PAOldColor> Ring Menu Setting"
_PLACEHOLDER = f"{{StringTableBind(TextBind:{_NAME})}}"
_BARE = f"{{TextBind:{_NAME}}}"
_UNKNOWN = "{StringTableBind(TextBind:NOT_IN_LOC)}"
_KEY_BIND = "{StringTableBind(KeyBind:Attack2)}"
# A type 59 text that names another one, as USING_CLICK_RMB texts do.
_OUTER = "OUTER_NAME"
_KOREAN_ONLY = "KOREAN_ONLY_NAME"
_KOREAN_TEXT = "간편 단축키 설정"
_ITEM = 10010
_PEARL_PRODUCT = 2001


@pytest.fixture(autouse=True)
def _loc() -> Iterator[None]:
    init_loc(loc_bytes([
        (LOC_TEXT_BIND, key_hash(_NAME), 0, 0, 0, _MENU),
        (LOC_TEXT_BIND, key_hash(_NAME), 0, 0, 1, _RING),
        (LOC_TEXT_BIND, key_hash(_OUTER), 0, 0, 0, f"Open {_BARE}"),
        (LOC_QUEST, 4470, 3, 0, 0, _PLACEHOLDER),
        (0, _ITEM, 0, 0, 1, f"Use: {_BARE}"),
        (50, _PEARL_PRODUCT, 0, 12, 1, f"{{TextBind:{_OUTER}}}."),
    ]))
    init_index(IndexKind.TEXT_BIND_KR, {key_hash(_KOREAN_ONLY): _KOREAN_TEXT, key_hash(_NAME): "PC 한국어"})
    yield
    init_index(IndexKind.TEXT_BIND_KR, None)
    reset_loc()


def test_text_bind_reads_variant_0() -> None:
    assert text_bind_tagged(_NAME) == _MENU


def test_both_forms_take_their_text_in_place() -> None:
    assert resolve_text_binds(f"Open {_PLACEHOLDER}.") == f"Open {_MENU}."
    assert resolve_text_binds(f"Open {_BARE}.") == f"Open {_MENU}."


def test_unknown_name_and_key_bind_stay_as_written() -> None:
    text = f"{_UNKNOWN} {_KEY_BIND} {{KeyBind:Jump}}"

    assert resolve_text_binds(text) == text


def test_nested_text_bind_is_filled() -> None:
    assert text_bind_tagged(_OUTER) == f"Open {_MENU}"


def test_name_missing_from_loc_falls_back_to_korean() -> None:
    assert resolve_text_binds(f"{{TextBind:{_KOREAN_ONLY}}}") == _KOREAN_TEXT


def test_without_loc_the_korean_text_fills_it() -> None:
    init_loc(None)

    assert resolve_text_binds(f"{_BARE} 열기") == "PC 한국어 열기"


def test_every_loc_read_fills_text_binds() -> None:
    assert loc_lookup(0, _ITEM, 0, 0, 1) == f"Use: {_MENU}"
    assert loc_lookup_prefix(0, _ITEM) == [f"Use: {_MENU}"]
    assert loc_type_entries(50)[(50, _PEARL_PRODUCT, 0, 12, 1)] == f"Open {_MENU}."


def test_a_name_that_names_itself_stops() -> None:
    loop = "{TextBind:LOOP}"

    assert fill_text_binds(loop, lambda _name: loop) == loop


def test_quest_text_fills_the_placeholder() -> None:
    assert quest_text_tagged(4470, 3) == _MENU
    assert quest_title(4470, 3) == "[Menu] Quick Hotkey Settings"
