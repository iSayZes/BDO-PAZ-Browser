"""File name search in the tree: every match, by folder, then file name, a page at a time."""
from __future__ import annotations

from pathlib import Path

import pytest

from api.bdo_api import Api
from api.bdo_api_file_search import SEARCH_PAGE_SIZE
from api.bdo_tree import build_tree
from bdo_models import PazEntry

# In .meta order. A plain path sort would put "a/b/x.txt" above "a/bz.txt"
# ("/" sorts before "z"); by folder, "a" comes before "a/b".
_META_ORDER = (
    "a/b/x.txt",
    "a/B/w.txt",
    "a/bz.txt",
    "a/A.txt",
    "c.txt",
)
_EXPECTED = ["c.txt", "a/A.txt", "a/bz.txt", "a/B/w.txt", "a/b/x.txt"]
_MANY = tuple(f"ui_texture/icon/{index:05}.dds" for index in range(SEARCH_PAGE_SIZE * 2 + 1))


def _entries(paths: tuple[str, ...]) -> list[PazEntry]:
    return [PazEntry("test.paz", path, 0, 1, 1, 0, 0) for path in paths]


def _api(paths: tuple[str, ...]) -> Api:
    api = Api()
    api._paz_root = Path("paz")
    api._entries = _entries(paths)
    api._entry_map = {entry.internal_path: entry for entry in api._entries}
    api._tree_data = build_tree(api._entries)
    return api


def _paths(page: dict) -> list[str]:
    return [item["path"] for item in page["items"]]


def test_results_sort_by_folder_then_name_ignoring_case() -> None:
    assert _paths(_api(_META_ORDER).search("*")) == _EXPECTED


def test_pages_cover_every_match_once_in_order() -> None:
    api = _api(_MANY)

    pages = [api.search(".dds", offset) for offset in range(0, len(_MANY), SEARCH_PAGE_SIZE)]

    assert all(page["total"] == len(_MANY) for page in pages)
    assert all(len(page["items"]) <= SEARCH_PAGE_SIZE for page in pages)
    assert [path for page in pages for path in _paths(page)] == list(_MANY)


def test_offset_past_the_end_is_an_empty_page() -> None:
    page = _api(_META_ORDER).search("*", len(_META_ORDER))

    assert page == {"total": len(_META_ORDER), "items": []}


@pytest.mark.parametrize("offset", [-1, 1.5, True, "0"])
def test_bad_offset_is_rejected(offset: object) -> None:
    with pytest.raises(ValueError):
        _api(_META_ORDER).search("*", offset)  # type: ignore[arg-type]


def test_a_new_entry_list_is_searched_again() -> None:
    api = _api(("a/old.txt",))
    api.search("*")

    api._entries = _entries(("a/new.txt",))

    assert _paths(api.search("*")) == ["a/new.txt"]


def test_result_row_names_the_file() -> None:
    [row] = _api(("gamecommondata/binary/buff.dbss",)).search("buff")["items"]

    assert row == {
        "id": "gamecommondata/binary/buff.dbss",
        "name": "buff.dbss",
        "path": "gamecommondata/binary/buff.dbss",
        "icon": "parsed",
    }
