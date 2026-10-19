"""Names and links for tables that store an `itemexchangesource.bss` key.

`itemexchangesource.bss` is 3 MB, so those tables read the `EXCHANGE_NAME_KR`
lookup index instead of opening it as a companion. The index holds every
exchange key with its Korean name, '' when the row has none; it is built by
`build_exchange_name_kr_index` in `_bss/itemexchangesource/parser.py`.
"""

from __future__ import annotations

from collections.abc import Sequence

from _common.html import e, hidden_slice, html_list_cell, record_link
from _common.loc import loc_text
from _common.lookup_index import IndexKind, lookup

ITEMEXCHANGESOURCE_PATH = "gamecommondata/binary/itemexchangesource.bss"
# LOC type 24: exchange name (str_id4 0) and description (1), keyed by the exchange key.
LOC_EXCHANGE = 24
LOC_EXCHANGE_NAME = 0
LOC_EXCHANGE_DESCRIPTION = 1


def exchange_name(key: int) -> str:
    """The LOC type 24 name in the user language, else the Korean name, else ''."""
    name_kr = lookup(IndexKind.EXCHANGE_NAME_KR, key)
    return loc_text(LOC_EXCHANGE, key, LOC_EXCHANGE_NAME) or (name_kr if isinstance(name_kr, str) else "")


def exchange_text(key: int) -> str:
    """`Azwell Longsword (5026)`, or the bare key when the exchange has no name."""
    name = exchange_name(key)
    return f"{name} ({key})" if name else str(key)


def exchange_cell(key: int) -> str:
    """`exchange_text()` as a link to the exchange's row, or as plain text when the index lacks the key."""
    text = exchange_text(key)
    if lookup(IndexKind.EXCHANGE_NAME_KR, key) is None:
        return e(text)
    return record_link(text, ITEMEXCHANGESOURCE_PATH, "key", key, "record-link")


def exchange_list_cell(keys: Sequence[int], max_items: int, separator: str = ", ") -> str:
    """The first `max_items` exchanges as `exchange_cell()`s and a hoverable count of the rest, or ''."""
    return html_list_cell(
        [exchange_cell(key) for key in keys[:max_items]],
        len(keys) - max_items,
        [exchange_text(key) for key in hidden_slice(keys, max_items)],
        separator,
    )
