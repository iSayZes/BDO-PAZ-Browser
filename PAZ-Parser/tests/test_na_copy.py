"""NA copies (`#na#x.bss`): the plain-name rule, the handler lookup, entry lookups, tree and searches."""
from __future__ import annotations

from pathlib import Path

import pytest

import bdo_preview
from api.bdo_api import Api
from api.bdo_api_helpers import fold_entry_map, path_matcher
from api.bdo_tree import build_tree
from bdo_models import PazEntry
from bdo_preview import HexHandler, get_handler, handler_key
from cli.parsed_file import find_entry
from paz.na_copy import find_or_na_copy, na_copy_name, plain_name, shown_name

_BINARY = "gamecommondata/binary"
_NA_ONLY = f"{_BINARY}/#na#eventmanagement.bss"
_PLAIN = f"{_BINARY}/quest.dbss"
_NA_BESIDE_PLAIN = f"{_BINARY}/#na#quest.dbss"
_NA_DEFAULT = "gamecommondata/customization/0/#na#default"
_NA_USERDEFAULT = "gamecommondata/#na#userdefault.xml"


def _entry(path: str) -> PazEntry:
    return PazEntry("pad00001.paz", path, 0, 1, 1, 0, 0)


def _api(paths: tuple[str, ...] = (_NA_ONLY, _PLAIN, _NA_BESIDE_PLAIN, _NA_DEFAULT, _NA_USERDEFAULT)) -> Api:
    api = Api()
    api._paz_root = Path("paz")
    api._entries = [_entry(path) for path in paths]
    api._entry_map = {entry.internal_path: entry for entry in api._entries}
    api._entry_map_folded = fold_entry_map(api._entry_map)
    api._tree_data = build_tree(api._entries)
    return api


# ── The rule ──────────────────────────────────────────────────────────────────

def test_the_na_copy_name_prefixes_the_file_name_of_a_full_path() -> None:
    assert na_copy_name("eventmanagement.bss") == "#na#eventmanagement.bss"
    assert na_copy_name(f"{_BINARY}/x.bss") == f"{_BINARY}/#na#x.bss"


def test_a_table_na_copy_has_the_plain_name() -> None:
    assert plain_name("#na#eventmanagement.bss") == "eventmanagement.bss"
    assert plain_name(_NA_ONLY) == f"{_BINARY}/eventmanagement.bss"
    assert plain_name("#na#title.dbss") == "title.dbss"
    assert plain_name("#na# cashshoose.bss") == "cashshoose.bss"


@pytest.mark.parametrize("name", ["#na#default", _NA_DEFAULT, "#na#userdefault.xml", _NA_USERDEFAULT, "quest.dbss"])
def test_other_files_keep_their_name(name: str) -> None:
    assert plain_name(name) == name


def test_a_plain_copy_keeps_the_na_copy_under_its_own_name() -> None:
    assert shown_name(_NA_ONLY, lambda _: False) == f"{_BINARY}/eventmanagement.bss"
    assert shown_name(_NA_BESIDE_PLAIN, {_PLAIN}.__contains__) == _NA_BESIDE_PLAIN


def test_a_lookup_falls_back_to_the_na_copy_of_a_table_only() -> None:
    files = {"#na#x.bss": "na", "y.bss": "plain", "#na#y.bss": "na", "#na#default": "na"}

    assert find_or_na_copy(files.get, "x.bss") == "na"
    assert find_or_na_copy(files.get, "y.bss") == "plain"
    assert find_or_na_copy(files.get, "default") is None


# ── Handler lookup ────────────────────────────────────────────────────────────

def test_an_na_copy_resolves_to_the_handler_of_its_plain_name(monkeypatch: pytest.MonkeyPatch) -> None:
    handler = HexHandler()
    monkeypatch.setitem(bdo_preview._REGISTRY, "x.bss", handler)

    assert get_handler("#na#x.bss", ".bss") is handler
    assert handler_key("#na#x.bss", ".bss") == "x.bss"


def test_na_default_and_na_userdefault_keep_the_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    handler = HexHandler()
    monkeypatch.setitem(bdo_preview._REGISTRY, "default", handler)
    monkeypatch.setitem(bdo_preview._REGISTRY, "userdefault.xml", handler)

    assert get_handler("#na#default", "") is not handler
    assert get_handler("#na#userdefault.xml", ".xml") is not handler


# ── Entry lookups ─────────────────────────────────────────────────────────────

def test_a_plain_path_finds_the_na_copy_when_the_client_has_no_plain_copy() -> None:
    api = _api()

    assert api.get_entry(f"{_BINARY}/eventmanagement.bss") is api._entry_map[_NA_ONLY]
    assert api._entry_ignoring_case(f"{_BINARY}/EventManagement.bss") is api._entry_map[_NA_ONLY]


def test_a_plain_copy_wins_over_its_na_copy() -> None:
    api = _api()

    assert api.get_entry(_PLAIN) is api._entry_map[_PLAIN]
    assert api.get_entry(_NA_BESIDE_PLAIN) is api._entry_map[_NA_BESIDE_PLAIN]


def test_other_files_are_not_found_by_their_plain_name() -> None:
    api = _api()

    assert api.get_entry("gamecommondata/customization/0/default") is None
    assert api.get_entry("gamecommondata/userdefault.xml") is None


# ── Tree, searches and the command line ───────────────────────────────────────

def test_the_tree_shows_an_na_copy_under_its_plain_name_and_keeps_its_path() -> None:
    rows = {row["id"]: row["name"] for row in _api().get_children(_BINARY)}

    assert rows == {
        _NA_ONLY: "eventmanagement.bss",
        _PLAIN: "quest.dbss",
        _NA_BESIDE_PLAIN: "#na#quest.dbss",
    }
    assert {row["name"] for row in _api().get_children("gamecommondata")} >= {"#na#userdefault.xml"}


def test_a_search_finds_an_na_copy_by_its_plain_name() -> None:
    [row] = _api().search("event*.bss")["items"]

    assert row["id"] == _NA_ONLY
    assert row["name"] == "eventmanagement.bss"
    assert row["path"] == f"{_BINARY}/eventmanagement.bss"
    assert path_matcher(f"{_BINARY}/eventmanagement.bss")(_NA_ONLY)
    assert path_matcher("*#na#*")(_NA_ONLY)


def test_the_command_line_finds_an_na_copy_by_its_plain_name() -> None:
    entries = _api()._entries

    assert find_entry(entries, "eventmanagement.bss").internal_path == _NA_ONLY
    assert find_entry(entries, "quest.dbss").internal_path == _PLAIN
