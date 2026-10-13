from __future__ import annotations

import pytest

from _common.lookup_index import (
    IndexKind,
    clear_indexes,
    index_size,
    init_index,
    is_index_loaded,
    lookup,
)

_FENCE_CHARACTER = 2053
_FENCE_ITEM = 58011


@pytest.fixture(autouse=True)
def _clear_indexes():
    clear_indexes()
    yield
    clear_indexes()


def test_lookup_is_none_when_the_index_is_not_loaded() -> None:
    assert not is_index_loaded(IndexKind.CHARACTER_ITEM)
    assert lookup(IndexKind.CHARACTER_ITEM, _FENCE_CHARACTER) is None


def test_lookup_returns_the_stored_value() -> None:
    init_index(IndexKind.CHARACTER_ITEM, {_FENCE_CHARACTER: _FENCE_ITEM})

    assert is_index_loaded(IndexKind.CHARACTER_ITEM)
    assert index_size(IndexKind.CHARACTER_ITEM) == 1
    assert lookup(IndexKind.CHARACTER_ITEM, _FENCE_CHARACTER) == _FENCE_ITEM
    assert lookup(IndexKind.CHARACTER_ITEM, 1) is None


def test_empty_index_still_counts_as_loaded() -> None:
    init_index(IndexKind.CHARACTER_ITEM, {})

    assert is_index_loaded(IndexKind.CHARACTER_ITEM)
    assert index_size(IndexKind.CHARACTER_ITEM) == 0


def test_clearing_one_kind_leaves_the_others() -> None:
    init_index(IndexKind.CHARACTER_ITEM, {_FENCE_CHARACTER: _FENCE_ITEM})
    init_index(IndexKind.ITEM_ICON, {_FENCE_ITEM: "ui_texture/a.dds"})
    init_index(IndexKind.CHARACTER_ITEM, None)

    assert not is_index_loaded(IndexKind.CHARACTER_ITEM)
    assert is_index_loaded(IndexKind.ITEM_ICON)


def test_clear_all_drops_every_kind() -> None:
    init_index(IndexKind.CHARACTER_ITEM, {_FENCE_CHARACTER: _FENCE_ITEM})
    clear_indexes()

    assert not is_index_loaded(IndexKind.CHARACTER_ITEM)
    assert index_size(IndexKind.CHARACTER_ITEM) == 0


def test_kind_values_are_stable_cache_keys() -> None:
    """The disk cache stores kind.value, so these must not drift casually."""
    assert IndexKind.ITEM_ICON.value == "item_icon"
    assert IndexKind.QUEST_ICON.value == "quest_icon"
    assert IndexKind.CHARACTER_ICON.value == "character_icon"
    assert IndexKind.CHARACTER_ITEM.value == "character_item"
    assert len({kind.value for kind in IndexKind}) == len(list(IndexKind))


def test_item_name_falls_back_to_the_korean_name() -> None:
    from _common.item_key import item_name

    # An item ID no LOC names, so the result does not depend on a loaded LOC.
    unnamed_item = 0xFFFFFE
    init_index(IndexKind.ITEM_NAME_KR, {unnamed_item: "[이벤트] 울타리"})

    assert item_name(unnamed_item) == "[이벤트] 울타리"
    assert item_name(unnamed_item - 1) == ""
