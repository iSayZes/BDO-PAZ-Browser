from __future__ import annotations

import pytest

from _common.item_icon import (
    ITEM_ICON_DIR,
    derive_item_icon_path,
    init_item_icons,
    is_item_icon_index_loaded,
    item_icon_index_size,
    item_icon_path,
)

_KING_CLAM = 24626
_FURNITURE_ICON = (
    "ui_texture/icon/new_icon/03_etc/06_housing/"
    "inhouse_cultivate_sea_clam_01_wall.dds"
)


@pytest.fixture(autouse=True)
def _clear_index():
    init_item_icons(None)
    yield
    init_item_icons(None)


def test_derives_from_id_when_no_index_loaded() -> None:
    assert not is_item_icon_index_loaded()
    assert item_icon_path(54030) == f"{ITEM_ICON_DIR}/00054030.png"


def test_index_entry_wins_over_derivation() -> None:
    init_item_icons({_KING_CLAM: _FURNITURE_ICON})

    assert is_item_icon_index_loaded()
    assert item_icon_index_size() == 1
    # The furniture case: derivation cannot reach this path.
    assert item_icon_path(_KING_CLAM) == _FURNITURE_ICON
    assert derive_item_icon_path(_KING_CLAM) != _FURNITURE_ICON


def test_falls_back_when_index_lacks_the_item() -> None:
    init_item_icons({_KING_CLAM: _FURNITURE_ICON})

    assert item_icon_path(54030) == f"{ITEM_ICON_DIR}/00054030.png"


def test_clearing_the_index_restores_derivation() -> None:
    init_item_icons({_KING_CLAM: _FURNITURE_ICON})
    init_item_icons(None)

    assert not is_item_icon_index_loaded()
    assert item_icon_path(_KING_CLAM) == f"{ITEM_ICON_DIR}/00024626.png"


def test_empty_index_still_counts_as_loaded() -> None:
    init_item_icons({})

    assert is_item_icon_index_loaded()
    assert item_icon_index_size() == 0
    assert item_icon_path(_KING_CLAM) == f"{ITEM_ICON_DIR}/00024626.png"
