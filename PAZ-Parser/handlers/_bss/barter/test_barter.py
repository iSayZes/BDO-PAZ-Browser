from __future__ import annotations

from .category import category_numbers
from .display import count_range_text, exchange_cells, exchange_text_fields, is_empty_exchange
from .exchange import EXCHANGE, EXCHANGE_FIELDS, read_exchange
from .sub_group import sub_group_ref


def test_the_exchange_is_56_bytes_with_one_value_per_field() -> None:
    assert EXCHANGE.size == 56
    assert len(EXCHANGE.unpack(bytes(EXCHANGE.size))) == len(EXCHANGE_FIELDS)


def test_read_exchange_names_the_values_in_doc_order() -> None:
    # Crow Coins for a +2 item: the level sits in the top byte of the item key.
    values = (2 << 24 | 705507, 1, 2, 10, 900, 1000, 14286, 4, 2551, 1000000)
    exchange = read_exchange(b"\xff" * 3 + EXCHANGE.pack(*values), 3)
    assert exchange == dict(zip(EXCHANGE_FIELDS, values))


def test_category_numbers_are_the_set_bits() -> None:
    assert category_numbers(0) == []
    assert category_numbers(1 << 7) == [7]
    assert category_numbers(1 << 7 | 1 << 8) == [7, 8]


def test_count_range_text() -> None:
    assert count_range_text(5, 5) == "5"
    assert count_range_text(900, 1000) == "900 - 1,000"


def test_an_all_zero_exchange_gets_no_text_and_dash_cells() -> None:
    empty = dict.fromkeys(EXCHANGE_FIELDS, 0)
    assert is_empty_exchange(empty)
    fields = exchange_text_fields(empty)
    assert set(fields) >= set(EXCHANGE_FIELDS) and not any(fields.values())
    assert set(exchange_cells({**empty, **fields})) == {"-"}


def test_sub_group_refs_tell_the_lists_apart() -> None:
    assert sub_group_ref(False, 3) == "trade:3"
    assert sub_group_ref(True, 3) == "material:3"
