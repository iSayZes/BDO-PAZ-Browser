"""Table sort through the API: per-file persistence, paging and search positions."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import api.bdo_config as bdo_config
from api.bdo_api import Api
from api.bdo_config import (
    forget_table_sort,
    load_table_sort,
    save_table_sort,
    table_sort_file_key,
)
from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

_PATH = "gamecommondata/binary/numbers.dbss"
_FILE_KEY = "numbers.dbss"


@pytest.fixture
def config_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "paz_config.json"
    monkeypatch.setattr(bdo_config, "config_file", lambda: path)
    return path


def _saved_sorts(config_file: Path) -> dict:
    return json.loads(config_file.read_text()).get("table_sort", {})


# ── bdo_config ───────────────────────────────────────────────────────────────

def test_table_sort_file_key_is_lowercased_file_name() -> None:
    assert table_sort_file_key("GameCommonData\\Binary\\Buff.dbss") == "buff.dbss"


def test_save_and_load_table_sort(config_file: Path) -> None:
    save_table_sort(_FILE_KEY, TableSort("v", "desc"))

    assert load_table_sort(_FILE_KEY, frozenset({"v"})) == TableSort("v", "desc")
    assert _saved_sorts(config_file) == {_FILE_KEY: {"field": "v", "dir": "desc"}}


def test_save_table_sort_keeps_other_settings(config_file: Path) -> None:
    config_file.write_text(json.dumps({"language": "de"}))

    save_table_sort(_FILE_KEY, TableSort("v", "asc"))

    assert json.loads(config_file.read_text())["language"] == "de"


def test_load_table_sort_drops_undeclared_field(config_file: Path) -> None:
    save_table_sort(_FILE_KEY, TableSort("removed_field", "asc"))

    assert load_table_sort(_FILE_KEY, frozenset({"v"})) is None
    assert _FILE_KEY not in _saved_sorts(config_file)


def test_load_table_sort_drops_malformed_entry(config_file: Path) -> None:
    config_file.write_text(json.dumps({"table_sort": {_FILE_KEY: {"field": "v", "dir": "sideways"}}}))

    assert load_table_sort(_FILE_KEY, frozenset({"v"})) is None
    assert _saved_sorts(config_file) == {}


def test_forget_table_sort_leaves_other_files(config_file: Path) -> None:
    save_table_sort(_FILE_KEY, TableSort("v", "asc"))
    save_table_sort("other.dbss", TableSort("v", "asc"))

    forget_table_sort(_FILE_KEY)

    assert list(_saved_sorts(config_file)) == ["other.dbss"]


# ── Api ──────────────────────────────────────────────────────────────────────

class _NumberHandler(PreviewHandler):
    def sortable_fields(self) -> tuple[str, ...]:
        return ("v",)

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        return [{"v": b} for b in data]

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        start = page * page_size
        return ",".join(str(r["v"]) for r in records[start:start + page_size])


class _FileOrderHandler(_NumberHandler):
    def default_sort(self) -> TableSort | None:
        return None


def _entry(data: bytes) -> PazEntry:
    return PazEntry(
        archive_name="test.paz",
        internal_path=_PATH,
        offset=0,
        compressed_size=len(data),
        uncompressed_size=len(data),
        compression_type=0,
        encryption_type=0,
    )


def _api_with_cached_file(data: bytes) -> Api:
    api = Api()
    api._cached_path = _PATH
    api._cached_data = data
    api._cached_handler = _NumberHandler()
    api._cached_entry = _entry(data)
    return api


def _open(data: bytes, handler: PreviewHandler) -> dict:
    return Api()._build_entry_response(data, _PATH, _entry(data), handler, {}, {})


def test_open_uses_default_sort_without_saving_it(config_file: Path) -> None:
    response = _open(bytes([3, 1, 2]), _NumberHandler())

    assert response["sort"] == {"field": "v", "dir": "desc"}
    assert response["html"] == "3,2,1"
    assert not config_file.exists()


def test_open_sends_the_counts_the_page_bar_shows(config_file: Path) -> None:
    response = _open(bytes([3, 1, 2]), _NumberHandler())

    assert response["record_count"] == 3
    assert response["byte_count"] == 3


def test_open_prefers_saved_sort_over_default(config_file: Path) -> None:
    save_table_sort(_FILE_KEY, TableSort("v", "asc"))

    response = _open(bytes([3, 1, 2]), _NumberHandler())

    assert response["sort"] == {"field": "v", "dir": "asc"}
    assert response["html"] == "1,2,3"


def test_open_without_default_sort_shows_file_order(config_file: Path) -> None:
    response = _open(bytes([3, 1, 2]), _FileOrderHandler())

    assert response["sort"] is None
    assert response["html"] == "3,1,2"


def test_get_parsed_page_sorts_and_remembers(config_file: Path) -> None:
    api = _api_with_cached_file(bytes([3, 1, 2]))

    result = api.get_parsed_page(_PATH, 0, "v", "desc")

    assert result == {"html": "3,2,1"}
    assert api._cached_sort == TableSort("v", "desc")
    assert _saved_sorts(config_file) == {_FILE_KEY: {"field": "v", "dir": "desc"}}


def test_get_parsed_page_without_sort_shows_file_order(config_file: Path) -> None:
    api = _api_with_cached_file(bytes([3, 1, 2]))

    assert api.get_parsed_page(_PATH, 0) == {"html": "3,1,2"}
    assert api._cached_sort is None


def test_get_parsed_page_rejects_undeclared_field(config_file: Path) -> None:
    api = _api_with_cached_file(bytes([3, 1, 2]))

    assert "error" in api.get_parsed_page(_PATH, 0, "secret", "asc")
    assert not config_file.exists()


def test_search_reports_positions_in_sorted_view(config_file: Path) -> None:
    api = _api_with_cached_file(bytes([30, 10, 20]))
    api.get_parsed_page(_PATH, 0, "v", "asc")  # shows 10, 20, 30

    result = api.search_content(_PATH, "30", "string", "parsed")

    assert result["record_indices"] == [2]
