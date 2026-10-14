from __future__ import annotations

import pytest

from _common.html import e, more_marker
from _common.icon_index import (
    ITEM_ICON_DIR,
    IconKind,
    clean_stored_icon_path,
    derive_icon_path,
    icon_path,
    icon_region,
    indexed_icon_path,
)
from _common.item_grade import ITEM_GRADE_COLORS
from _common.item_key import item_key_icon_path, item_key_list_cell, item_key_text
from _common.lookup_index import IndexKind, clear_indexes, init_index
from _common.pa_text import argb_css

_KING_CLAM = 24626
_SWEET_HONEY_WINE = 54030
_FURNITURE_ICON = (
    "ui_texture/icon/new_icon/03_etc/06_housing/"
    "inhouse_cultivate_sea_clam_01_wall.dds"
)


@pytest.mark.parametrize(
    ("stored", "expected"),
    [
        # itemenchant.dbss Essence of Dawn Box and Alchemy Byproduct store backslashes.
        (r"New_Icon\03_ETC\00757120.dds", "new_icon/03_etc/00757120.dds"),
        (r"New_Icon/03_ETC\03_Quest_Item/00042393.dds", "new_icon/03_etc/03_quest_item/00042393.dds"),
        ("New_Icon/04_PC_Skill//04_Debuff/a.dds", "new_icon/04_pc_skill/04_debuff/a.dds"),
        (" Item_Icon/00724507.dds ", "item_icon/00724507.dds"),
    ],
)
def test_clean_stored_icon_path(stored: str, expected: str) -> None:
    assert clean_stored_icon_path(stored) == expected


@pytest.fixture(autouse=True)
def _clear_indexes():
    clear_indexes()
    yield
    clear_indexes()


def test_derives_from_id_when_no_index_loaded() -> None:
    assert icon_path(IconKind.ITEM, _SWEET_HONEY_WINE) == (
        f"{ITEM_ICON_DIR}/00054030.png"
    )


def test_index_entry_wins_over_derivation() -> None:
    init_index(IndexKind.ITEM_ICON, {_KING_CLAM: _FURNITURE_ICON})

    # The furniture case: derivation cannot reach this path.
    assert icon_path(IconKind.ITEM, _KING_CLAM) == _FURNITURE_ICON
    assert derive_icon_path(IconKind.ITEM, _KING_CLAM) != _FURNITURE_ICON


def test_falls_back_when_index_lacks_the_entity() -> None:
    init_index(IndexKind.ITEM_ICON, {_KING_CLAM: _FURNITURE_ICON})

    assert icon_path(IconKind.ITEM, _SWEET_HONEY_WINE) == (
        f"{ITEM_ICON_DIR}/00054030.png"
    )


def test_clearing_the_index_restores_derivation() -> None:
    init_index(IndexKind.ITEM_ICON, {_KING_CLAM: _FURNITURE_ICON})
    init_index(IndexKind.ITEM_ICON, None)

    assert icon_path(IconKind.ITEM, _KING_CLAM) == f"{ITEM_ICON_DIR}/00024626.png"


def test_empty_index_falls_back_to_derivation() -> None:
    init_index(IndexKind.ITEM_ICON, {})

    assert icon_path(IconKind.ITEM, _KING_CLAM) == f"{ITEM_ICON_DIR}/00024626.png"


def test_icon_kinds_read_only_their_own_index() -> None:
    """A link index holds IDs, never paths, so it must not leak into icons."""
    init_index(IndexKind.CHARACTER_ITEM, {2053: 58011})

    assert indexed_icon_path(IconKind.CHARACTER, 2053) == ""


def test_kinds_without_a_deriver_return_empty() -> None:
    """Quest and character icons are asset-named far more often than ID-named,
    so guessing a path would be wrong more often than right."""
    assert derive_icon_path(IconKind.QUEST, 795132) == ""
    assert derive_icon_path(IconKind.CHARACTER, 16111) == ""
    assert icon_path(IconKind.QUEST, 795132) == ""


def test_indexed_kinds_without_a_deriver_still_resolve() -> None:
    init_index(IndexKind.QUEST_ICON, {795132: "ui_texture/icon/quest/8700_12.dds"})

    assert icon_path(IconKind.QUEST, 795132) == "ui_texture/icon/quest/8700_12.dds"
    assert icon_path(IconKind.QUEST, 1) == ""


def test_kinds_are_isolated_from_each_other() -> None:
    init_index(IndexKind.ITEM_ICON, {_KING_CLAM: _FURNITURE_ICON})
    init_index(IndexKind.QUEST_ICON, {1: "ui_texture/icon/quest/a.dds"})
    init_index(IndexKind.QUEST_ICON, None)

    assert icon_path(IconKind.QUEST, 1) == ""
    assert icon_path(IconKind.ITEM, _KING_CLAM) == _FURNITURE_ICON


def test_kind_values_are_stable_override_keys() -> None:
    """icon_overrides.json is keyed by kind.value, so these must not drift casually."""
    assert IconKind.ITEM.value == "item"
    assert IconKind.QUEST.value == "quest"
    assert IconKind.CHARACTER.value == "character"
    assert len({kind.value for kind in IconKind}) == len(list(IconKind))


def test_override_file_parses_without_error() -> None:
    """A typo in the hand-edited file must be reported, not silently ignored."""
    from _common.icon_index import icon_override_error, reload_icon_overrides

    reload_icon_overrides()
    assert icon_override_error() == ""


def test_override_beats_index_and_derivation(monkeypatch) -> None:
    import _common.icon_index as module

    monkeypatch.setattr(
        module, "_OVERRIDES", {IconKind.ITEM: {_KING_CLAM: "ui_texture/icon/fixed.dds"}}
    )
    init_index(IndexKind.ITEM_ICON, {_KING_CLAM: _FURNITURE_ICON})

    assert icon_path(IconKind.ITEM, _KING_CLAM) == "ui_texture/icon/fixed.dds"
    # Untouched ids still fall through to the index.
    assert icon_path(IconKind.ITEM, 1) == f"{ITEM_ICON_DIR}/00000001.png"


def test_empty_override_suppresses_a_wrong_derived_path(monkeypatch) -> None:
    import _common.icon_index as module

    monkeypatch.setattr(module, "_OVERRIDES", {IconKind.ITEM: {9: ""}})

    # Item 9 derives to a path that is not shipped; "" says so explicitly.
    assert icon_path(IconKind.ITEM, 9) == ""


_FENCE_CHARACTER = 2053
_FENCE_ITEM = 58011
_FENCE_ICON = "ui_texture/icon/new_icon/03_etc/06_housing/00058003.dds"


def _borrow(own: dict[int, str], shipped: set[str]) -> dict[int, str]:
    from _common.icon_index import borrow_icons

    return borrow_icons(
        own,
        {_FENCE_ITEM: _FENCE_ICON},
        {_FENCE_CHARACTER: _FENCE_ITEM},
        shipped.__contains__,
    )


def test_borrow_fills_a_character_with_no_icon() -> None:
    assert _borrow({}, {_FENCE_ICON}) == {_FENCE_CHARACTER: _FENCE_ICON}


def test_borrow_replaces_an_icon_the_client_does_not_ship() -> None:
    dead = "ui_texture/icon/new_icon/03_etc/06_housing/missing.dds"

    assert _borrow({_FENCE_CHARACTER: dead}, {_FENCE_ICON}) == {
        _FENCE_CHARACTER: _FENCE_ICON,
    }


def test_borrow_keeps_a_working_own_icon() -> None:
    own_icon = "ui_texture/icon/new_icon/03_etc/06_housing/own.dds"

    assert _borrow({_FENCE_CHARACTER: own_icon}, {own_icon, _FENCE_ICON}) == {
        _FENCE_CHARACTER: own_icon,
    }


def test_borrow_never_swaps_in_a_dead_item_icon() -> None:
    dead = "ui_texture/icon/new_icon/03_etc/06_housing/missing.dds"

    assert _borrow({_FENCE_CHARACTER: dead}, set()) == {_FENCE_CHARACTER: dead}
    assert _borrow({}, set()) == {}


def test_borrow_leaves_the_input_untouched() -> None:
    own: dict[int, str] = {}
    _borrow(own, {_FENCE_ICON})

    assert own == {}


# Sovereign Longsword: the level-10 key has an icon of its own, level 3 does not.
_SOVEREIGN_LONGSWORD = 747201
_SOVEREIGN_LEVEL_10 = 10 << 24 | _SOVEREIGN_LONGSWORD
_SOVEREIGN_LEVEL_3 = 3 << 24 | _SOVEREIGN_LONGSWORD
_WEAPON_DIR = "ui_texture/icon/new_icon/06_pc_equipitem/00_common/01_weapon"


def test_item_key_icon_prefers_the_level_icon() -> None:
    init_index(IndexKind.ITEM_ICON, {_SOVEREIGN_LONGSWORD: f"{_WEAPON_DIR}/00747201.dds"})
    init_index(IndexKind.ITEM_KEY_ICON, {_SOVEREIGN_LEVEL_10: f"{_WEAPON_DIR}/00747201_02.dds"})

    assert item_key_icon_path(_SOVEREIGN_LEVEL_10) == f"{_WEAPON_DIR}/00747201_02.dds"


def test_item_key_icon_falls_back_to_the_item_icon() -> None:
    init_index(IndexKind.ITEM_ICON, {_SOVEREIGN_LONGSWORD: f"{_WEAPON_DIR}/00747201.dds"})
    init_index(IndexKind.ITEM_KEY_ICON, {_SOVEREIGN_LEVEL_10: f"{_WEAPON_DIR}/00747201_02.dds"})

    assert item_key_icon_path(_SOVEREIGN_LEVEL_3) == f"{_WEAPON_DIR}/00747201.dds"
    assert item_key_icon_path(_SOVEREIGN_LONGSWORD) == f"{_WEAPON_DIR}/00747201.dds"


def test_item_key_icon_without_indexes_derives_from_the_item_id() -> None:
    assert item_key_icon_path(_SOVEREIGN_LEVEL_3) == f"{ITEM_ICON_DIR}/00747201.png"


def test_item_key_list_cell_shows_each_level_icon_and_counts_the_rest() -> None:
    init_index(IndexKind.ITEM_ICON, {_SOVEREIGN_LONGSWORD: f"{_WEAPON_DIR}/00747201.dds"})
    init_index(IndexKind.ITEM_KEY_ICON, {_SOVEREIGN_LEVEL_10: f"{_WEAPON_DIR}/00747201_02.dds"})

    html = item_key_list_cell([_SOVEREIGN_LEVEL_10, _SOVEREIGN_LEVEL_3, _SOVEREIGN_LONGSWORD], 2)

    assert f'data-icon-path="{_WEAPON_DIR}/00747201_02.dds"' in html
    assert f'data-icon-path="{_WEAPON_DIR}/00747201.dds"' in html
    # Names come from LOC when another test loaded it, else the item ID.
    assert f">{e(item_key_text(_SOVEREIGN_LEVEL_10))}<" in html
    assert f">{e(item_key_text(_SOVEREIGN_LEVEL_3))}<" in html
    # The hidden item is named when the count is hovered.
    assert html.endswith(f", {more_marker(1, [item_key_text(_SOVEREIGN_LONGSWORD)])}")


def test_item_key_list_cell_draws_each_name_in_its_grade_colour() -> None:
    init_index(IndexKind.ITEM_GRADE, {_SOVEREIGN_LONGSWORD: 5})

    html = item_key_list_cell([_SOVEREIGN_LEVEL_10, _SOVEREIGN_LONGSWORD + 1], 2)

    # Every level shares the base item's grade; an item without one stays plain.
    purple = argb_css(ITEM_GRADE_COLORS[5])
    assert f'<span class="pa-color" style="color: {purple}">{e(item_key_text(_SOVEREIGN_LEVEL_10))}</span>' in html
    assert f">{e(item_key_text(_SOVEREIGN_LONGSWORD + 1))}<" in html


def test_lease_text_colours_the_item_by_grade(monkeypatch: pytest.MonkeyPatch) -> None:
    import _common.item_key as item_key
    from _common.lease import Lease, lease_text_tagged

    monkeypatch.setattr(item_key, "item_name", lambda item_id: "Sovereign Longsword")
    init_index(IndexKind.ITEM_GRADE, {_SOVEREIGN_LONGSWORD: 5})
    lease = Lease(item_id=_SOVEREIGN_LONGSWORD, cost=3)

    tagged = f"<PAColor0x{ITEM_GRADE_COLORS[5]:08X}>Sovereign Longsword<PAOldColor> (3 CP)"
    assert lease_text_tagged(lease, has_loc=True) == tagged
    # Without LOC the item ID stands in, plain.
    assert lease_text_tagged(lease, has_loc=False) == f"{_SOVEREIGN_LONGSWORD} (3 CP)"


_TITLE_SHEET = "ui_texture/combine/icon/combine_title_icon_00.dds"


def test_sprite_kinds_give_the_sheet_and_the_region() -> None:
    init_index(IndexKind.MENU_ICON, {2: _TITLE_SHEET})
    init_index(IndexKind.MENU_ICON_REGION, {2: (2, 457, 57, 512)})

    assert icon_path(IconKind.MENU, 2) == _TITLE_SHEET
    assert icon_region(IconKind.MENU, 2) == (2, 457, 57, 512)


def test_region_is_none_for_whole_file_kinds_and_misses() -> None:
    init_index(IndexKind.MENU_ICON_REGION, {2: (2, 457, 57, 512)})

    assert icon_region(IconKind.MENU, 3) is None
    assert icon_region(IconKind.SUBMENU, 2) is None
    assert icon_region(IconKind.ITEM, 2) is None
