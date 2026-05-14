from __future__ import annotations

from api.bdo_api import _table_row_height
from _common.html import icon_cell


def test_icon_cell_renders_escaped_icon_path() -> None:
    html = icon_cell('Icon/Quest/Hadum08"><.dds')

    assert 'class="icon-cell"' in html
    assert 'Icon/Quest/Hadum08&quot;&gt;&lt;.dds' in html
    assert 'data-icon-path="Icon/Quest/Hadum08&quot;&gt;&lt;.dds"' in html
    assert 'icon-cell-placeholder' in html


def test_icon_cell_renders_empty_path_as_dash() -> None:
    assert icon_cell("") == "-"


def test_table_row_height_clamps_to_supported_range() -> None:
    assert _table_row_height("bad") == 27
    assert _table_row_height(10) == 20
    assert _table_row_height(80) == 64
    assert _table_row_height(32) == 32
