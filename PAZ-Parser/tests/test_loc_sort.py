"""LOC viewer: sorting runs on the handler's index, not on materialised
records, and text shows its game colours without the tags."""
from __future__ import annotations

import re

import pytest

from bdo_models import PazEntry
from bdo_preview import get_handler
from table_sort import TableSort

from tests.loc_data import LocRow, loc_bytes

_ROWS: list[LocRow] = [
    (6, 300, 0, 0, 0, "gamma"),
    (5, 100, 0, 0, 0, "Alpha"),
    (6, 200, 0, 0, 0, ""),
    (18, 400, 1, 0, 3, "beta"),
]


@pytest.fixture
def loc() -> tuple:
    data = loc_bytes(_ROWS)
    entry = PazEntry("t.paz", "ads/languagedata_en.loc", 0, len(data), len(data), 0, 0)
    return get_handler("languagedata_en.loc", ".loc"), data, entry


def _id1_column(html: str) -> list[str]:
    return re.findall(r"<tr><td>(\d+)</td>", html)


def test_loc_headers_are_sortable(loc: tuple) -> None:
    handler, data, entry = loc

    html = handler.render_data_page(data, entry, {}, 0, 10)

    # The type name shares the Type column with its number; it sorts from the CLI only.
    headers = set(re.findall(r'data-sort-key="(\w+)"', html))
    assert headers == set(handler.sortable_fields()) - {"str_type_text"}
    assert "text" in handler.sortable_fields()


@pytest.mark.parametrize(
    ("field", "direction", "expected_id1"),
    [
        ("str_id1", "desc", ["400", "300", "200", "100"]),
        ("str_type", "asc", ["100", "300", "200", "400"]),
        ("str_type_text", "asc", ["100", "300", "200", "400"]),
        ("text", "asc", ["100", "400", "300", "200"]),  # blank text last
        ("text", "desc", ["300", "400", "100", "200"]),  # blank text still last
    ],
)
def test_loc_sorts_by_index_field(loc: tuple, field: str, direction: str, expected_id1: list[str]) -> None:
    handler, data, entry = loc

    html = handler.render_sorted_page(data, entry, {}, 0, 10, TableSort(field, direction))

    assert _id1_column(html) == expected_id1


def test_loc_sorted_paging_keeps_total_and_order(loc: tuple) -> None:
    handler, data, entry = loc
    sort = TableSort("str_id1", "asc")

    second_page = handler.render_sorted_page(data, entry, {}, 1, 2, sort)

    assert _id1_column(second_page) == ["300", "400"]
    assert "of 4 strings" in second_page


def test_loc_sort_does_not_build_all_record_dicts(loc: tuple, monkeypatch: pytest.MonkeyPatch) -> None:
    handler, data, entry = loc

    def fail(*_args: object) -> list[dict]:
        raise AssertionError("sorting LOC must not call get_records()")

    monkeypatch.setattr(handler, "get_records", fail)

    handler.render_sorted_page(data, entry, {}, 0, 10, TableSort("str_id2", "desc"))


def test_loc_text_draws_the_colour_without_the_tags() -> None:
    data = loc_bytes([(5, 48723, 0, 0, 0, "<PAColor0xffe9bd23>Boon & Co<PAOldColor>")])
    entry = PazEntry("t.paz", "ads/languagedata_en.loc", 0, len(data), len(data), 0, 0)
    handler = get_handler("languagedata_en.loc", ".loc")

    html = handler.render_data_page(data, entry, {}, 0, 10)

    assert '<span class="pa-color" style="color: rgba(233, 189, 35, 1)">Boon &amp; Co</span>' in html
    assert "PAColor" not in html
    assert "PAOldColor" not in html
