"""Every handler with a fixture case renders sortable headers, opens in its
default sort, sorts by each of them and sorts its empty cells last."""
from __future__ import annotations

import re

import pytest

from table_sort import SORT_ASC, SORT_DESC, TableSort
from tests.empty_cells import assert_empty_cells_sort_last
from tests.handler_cases import case_file_name, handler_cases
from tests.models import HandlerCase
from tests.runner import LoadedCase, load_case

_SORT_KEY_RE = re.compile(r'data-sort-key="([^"]+)"')
_PAGE_SIZE = 50


def _assert_headers_are_declared(loaded: LoadedCase) -> None:
    fields = loaded.handler.sortable_fields()
    html = loaded.handler.render_data_page(loaded.data, loaded.entry, loaded.companions, 0, _PAGE_SIZE)
    rendered = set(_SORT_KEY_RE.findall(html))

    assert fields, "handler declares no sortable fields"
    assert rendered, "first page renders no sortable headers"
    # Handlers may declare fields for columns hidden on this page (LOC names,
    # inactive flags) so a saved sort survives, but never render undeclared ones.
    assert rendered <= set(fields)


def _assert_default_sort_is_shown(loaded: LoadedCase) -> None:
    handler = loaded.handler
    sort = handler.default_sort()
    if sort is None:
        return

    assert sort.field in handler.sortable_fields(), f"default {sort} is not sortable"
    html = handler.render_sorted_page(loaded.data, loaded.entry, loaded.companions, 0, _PAGE_SIZE, sort)
    # The header marks the default like a clicked sort, so its column must render.
    assert sort.field in _SORT_KEY_RE.findall(html), f"default {sort} has no rendered header"


def _assert_sorts_every_field(loaded: LoadedCase) -> None:
    handler = loaded.handler
    count = handler.get_record_count(loaded.data, loaded.entry, loaded.companions)

    for field in sorted(handler.sortable_fields()):
        for direction in (SORT_ASC, SORT_DESC):
            sort = TableSort(field, direction)
            order = handler.sorted_order(loaded.data, loaded.entry, loaded.companions, sort)
            assert sorted(order) == list(range(count)), f"{sort} is not a permutation"

            html = handler.render_sorted_page(
                loaded.data, loaded.entry, loaded.companions, 0, _PAGE_SIZE, sort
            )
            assert "<tr>" in html, f"{sort} rendered no rows"


@pytest.mark.parametrize("case", handler_cases(), ids=case_file_name)
def test_handler_sorts_every_column_with_empty_cells_last(case: HandlerCase) -> None:
    loaded = load_case(case)
    # all_records() caches the parse on the data object, so the sort checks
    # below reuse it instead of parsing the fixture a second time.
    records = loaded.handler.all_records(loaded.data, loaded.entry, loaded.companions)
    if records and "_error" not in records[0]:
        assert_empty_cells_sort_last(loaded.handler, records)

    _assert_headers_are_declared(loaded)
    _assert_default_sort_is_shown(loaded)
    _assert_sorts_every_field(loaded)
