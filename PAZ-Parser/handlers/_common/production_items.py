"""The items a worker production key produces, read from the `PRODUCTION_ITEMS` and
`PRODUCTION_LUCK_ITEMS` indexes.

    production_key -> plantexchangegroup.bss exchange_key
                   -> itemexchangesource.bss product_drop_key / luck_drop_key
                   -> itemmaingroup.bss group -> itemsubgroup.dbss item keys

Shared by the tables that show production items (`plantexchangegroup.bss`,
`plantzone.dbss`). The indexes are built by `build_production_item_index` and
`build_production_luck_item_index` in `_bss/plantexchangegroup/parser.py`.
"""

from __future__ import annotations

from _common.item_key import item_key_text
from _common.lookup_index import IndexKind, lookup


def production_item_keys(production_key: int) -> tuple[int, ...] | None:
    """The packed item keys a production key produces, or None when unknown."""
    return _item_keys(IndexKind.PRODUCTION_ITEMS, production_key)


def production_luck_item_keys(production_key: int) -> tuple[int, ...] | None:
    """The packed item keys of the production key's luck drops, or None when it has none."""
    return _item_keys(IndexKind.PRODUCTION_LUCK_ITEMS, production_key)


def production_item_fields(production_key: int) -> dict:
    """`item_keys` and item names for a record; `item_keys` is None when unknown."""
    return _item_fields("", production_item_keys(production_key))


def production_luck_item_fields(production_key: int) -> dict:
    """`luck_item_keys` and `luck_items` for a record; `luck_item_keys` is None without luck drops."""
    return _item_fields("luck_", production_luck_item_keys(production_key))


def _item_keys(kind: IndexKind, production_key: int) -> tuple[int, ...] | None:
    value = lookup(kind, production_key)
    return value if isinstance(value, tuple) else None


def _item_fields(prefix: str, item_keys: tuple[int, ...] | None) -> dict:
    if item_keys is None:
        return {f"{prefix}item_keys": None, f"{prefix}items": []}
    return {
        f"{prefix}item_keys": list(item_keys),
        f"{prefix}items": [item_key_text(key) for key in item_keys],
    }
