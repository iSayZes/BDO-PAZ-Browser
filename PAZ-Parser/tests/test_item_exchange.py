from __future__ import annotations

import pytest

from _common.item_exchange import ITEMEXCHANGESOURCE_PATH, exchange_cell, exchange_list_cell, exchange_text
from _common.lookup_index import IndexKind, clear_indexes, init_index

# Exchange keys no LOC names, so the results do not depend on a loaded LOC.
_NAMED = 0xFFFFFF00
_UNNAMED = _NAMED + 1
_MISSING = _NAMED + 2


@pytest.fixture(autouse=True)
def _exchange_names():
    clear_indexes()
    init_index(IndexKind.EXCHANGE_NAME_KR, {_NAMED: "아스웰 장검", _UNNAMED: ""})
    yield
    clear_indexes()


def test_text_is_the_name_and_key_or_the_bare_key() -> None:
    assert exchange_text(_NAMED) == f"아스웰 장검 ({_NAMED})"
    assert exchange_text(_UNNAMED) == str(_UNNAMED)
    assert exchange_text(_MISSING) == str(_MISSING)


def test_cell_links_only_the_keys_with_a_row() -> None:
    assert f'data-path="{ITEMEXCHANGESOURCE_PATH}"' in exchange_cell(_UNNAMED)
    assert f'data-value="{_NAMED}"' in exchange_cell(_NAMED)
    assert exchange_cell(_MISSING) == str(_MISSING)


def test_list_cell_hides_the_rest_behind_a_count() -> None:
    cell = exchange_list_cell([_NAMED, _UNNAMED, _MISSING], 1)
    assert cell.count("data-action=") == 1
    assert "(+2)" in cell
    assert exchange_list_cell([], 1) == ""
