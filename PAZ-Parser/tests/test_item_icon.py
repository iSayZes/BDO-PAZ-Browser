from __future__ import annotations

from api.bdo_api_preview import _icon_sibling_paths
from _common.item_icon import ITEM_ICON_DIR, item_icon_path


def test_item_icon_path_zero_pads_to_eight_digits() -> None:
    assert item_icon_path(54030) == f"{ITEM_ICON_DIR}/00054030.png"
    assert item_icon_path(1) == f"{ITEM_ICON_DIR}/00000001.png"


def test_icon_sibling_paths_offers_web_variant() -> None:
    path = item_icon_path(18448)

    assert _icon_sibling_paths(path) == [f"{ITEM_ICON_DIR}/web_00018448.png"]


def test_icon_sibling_paths_does_not_double_prefix() -> None:
    assert _icon_sibling_paths(f"{ITEM_ICON_DIR}/web_00018448.png") == []


def test_icon_sibling_paths_ignores_bare_filename() -> None:
    assert _icon_sibling_paths("00018448.png") == []
