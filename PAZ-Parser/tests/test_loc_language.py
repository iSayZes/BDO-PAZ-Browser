"""LOC viewer labels follow the UI language, and a language change drops
tables parsed in the old one."""
from __future__ import annotations

import re
from collections.abc import Iterator

import pytest

from bdo_models import PazEntry
from bdo_preview import PreviewHandler, get_handler, set_handler_lang
from ui_text import ui_text

from tests.loc_data import LocRow, loc_bytes

_KNOWN_TYPE = 6
_UNKNOWN_TYPE = 9_999
_ROWS: list[LocRow] = [
    (_KNOWN_TYPE, 100, 0, 0, 0, "Alpha"),
    (_UNKNOWN_TYPE, 200, 0, 0, 0, "Beta"),
]


@pytest.fixture(autouse=True)
def _english_after_each_test() -> Iterator[None]:
    yield
    set_handler_lang("en")


@pytest.fixture
def loc() -> tuple[PreviewHandler, bytes, PazEntry]:
    data = loc_bytes(_ROWS)
    entry = PazEntry("t.paz", "ads/languagedata_en.loc", 0, len(data), len(data), 0, 0)
    return get_handler("languagedata_en.loc", ".loc"), data, entry


def _type_cells(html: str) -> list[str]:
    """The type name of each row, after the type number in the Type cell."""
    return re.findall(r"<span class='loc-type-num'>\d+</span> ([^<]*)</td>", html)


def test_labels_are_in_the_ui_language(loc: tuple) -> None:
    handler, data, entry = loc
    english_header = ui_text("loc.columns.type")

    set_handler_lang("de")
    html = handler.render_data_page(data, entry, {}, 0, 10)

    assert ui_text("loc.columns.type") != english_header
    assert ui_text("loc.columns.type") in html
    assert _type_cells(html) == [ui_text(f"loc.types.{_KNOWN_TYPE}"), ui_text("loc.typeUnknown")]
    assert ui_text("loc.showing", first="1", last="2", total="2") in html


def test_search_finds_type_names_in_the_new_language(loc: tuple) -> None:
    handler, data, entry = loc
    handler.search_records(data, entry, {}, "alpha")  # builds the English search text

    set_handler_lang("de")
    german_name = ui_text(f"loc.types.{_KNOWN_TYPE}")

    assert handler.search_records(data, entry, {}, german_name) == [0]


def test_a_language_change_drops_parsed_tables(loc: tuple) -> None:
    handler, data, entry = loc
    handler.get_record_count(data, entry, {})

    set_handler_lang("en")
    assert handler._handler_caches  # same language: kept

    set_handler_lang("de")
    assert not handler._handler_caches
