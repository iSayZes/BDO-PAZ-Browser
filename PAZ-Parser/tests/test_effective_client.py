"""The client version handlers read files as: the core setter and the handlers' helper."""
from __future__ import annotations

import pytest

import bdo_preview
from bdo_preview import handler_client, parsed_handlers, set_handler_client
from _common.data_deps import CLIENT, recording
from _common.effective_client import effective_client


def _cached_handler() -> bdo_preview.PreviewHandler:
    """A registered handler holding one parsed table in its memory cache."""
    handler = parsed_handlers()[0]
    handler._data_cache(b"table bytes", "rows", lambda: [1, 2])
    return handler


def test_no_client_before_a_folder_loads() -> None:
    assert handler_client() is None
    assert effective_client() is None


def test_handlers_read_the_client_the_core_set() -> None:
    set_handler_client(1784)

    assert effective_client() == 1784


def test_a_client_change_drops_parsed_tables() -> None:
    set_handler_client(1784)
    handler = _cached_handler()

    set_handler_client(1784)
    assert handler._handler_caches  # same client: kept

    set_handler_client(3483)
    assert not handler._handler_caches


def test_reading_the_client_is_a_recorded_dependency() -> None:
    with recording() as deps:
        effective_client()

    assert deps == {CLIENT}


def test_an_exe_without_the_getter_reads_as_live(monkeypatch: pytest.MonkeyPatch) -> None:
    set_handler_client(1784)
    monkeypatch.delattr(bdo_preview, "handler_client")

    assert effective_client() is None
