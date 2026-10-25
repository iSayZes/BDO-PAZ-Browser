from __future__ import annotations

import sys

from paz.source_fingerprint import project_modules
from _common.lookup_index import IndexKind
from _common.lookup_builders import INDEX_SPECS, IndexSpec, build_indexes, skipped_tables

_FENCE_CHARACTER = 2053
_FENCE_ITEM = 58011
_FENCE_ICON = "ui_texture/icon/new_icon/03_etc/06_housing/00058003.dds"


def _spec(kind: IndexKind, *sources: str) -> IndexSpec:
    return IndexSpec(kind, sources, lambda *data: {len(data): b"".join(data).decode()})


def test_every_kind_has_exactly_one_spec() -> None:
    kinds = [spec.kind for spec in INDEX_SPECS]

    assert sorted(kinds, key=lambda k: k.value) == sorted(IndexKind, key=lambda k: k.value)


def test_builder_receives_its_sources_in_order() -> None:
    payloads = {"a": b"A", "b": b"B"}

    indexes = build_indexes(payloads.get, lambda _: False, (_spec(IndexKind.ITEM_ICON, "b", "a"),))

    assert indexes == {"item_icon": {2: "BA"}}


def test_shared_sources_are_read_once() -> None:
    reads: list[str] = []

    def read(path: str) -> bytes:
        reads.append(path)
        return b"x"

    specs = (_spec(IndexKind.ITEM_ICON, "a", "b"), _spec(IndexKind.CHARACTER_ITEM, "a", "b"))
    build_indexes(read, lambda _: False, specs)

    assert sorted(reads) == ["a", "b"]


def test_spec_with_a_missing_source_is_skipped() -> None:
    payloads = {"a": b"A"}
    specs = (_spec(IndexKind.ITEM_ICON, "a"), _spec(IndexKind.QUEST_ICON, "a", "missing"))

    indexes = build_indexes(payloads.get, lambda _: False, specs)

    assert set(indexes) == {"item_icon"}


def test_a_source_that_does_not_parse_drops_only_its_own_spec() -> None:
    def fails(*_: bytes) -> dict:
        raise ValueError("does not fit the layout")

    failing = IndexSpec(IndexKind.QUEST_ICON, ("folder/a.bss",), fails)
    specs = (failing, _spec(IndexKind.ITEM_ICON, "folder/a.bss"))
    skipped: list[IndexSpec] = []

    indexes = build_indexes({"folder/a.bss": b"A"}.get, lambda _: False, specs, on_skip=skipped.append)

    assert set(indexes) == {"item_icon"}
    assert skipped == [failing]
    assert skipped_tables(skipped) == "a.bss"


def test_characters_borrow_the_icon_of_their_item() -> None:
    specs = (
        IndexSpec(IndexKind.CHARACTER_ICON, (), lambda: {}),
        IndexSpec(IndexKind.ITEM_ICON, (), lambda: {_FENCE_ITEM: _FENCE_ICON}),
        IndexSpec(IndexKind.CHARACTER_ITEM, (), lambda: {_FENCE_CHARACTER: _FENCE_ITEM}),
    )

    indexes = build_indexes(lambda _: None, {_FENCE_ICON}.__contains__, specs)

    assert indexes["character_icon"] == {_FENCE_CHARACTER: _FENCE_ICON}


def test_fingerprint_reaches_every_builder() -> None:
    """Editing any builder must rebuild the cache, so none may hide behind a lazy import."""
    modules = project_modules([sys.modules[build_indexes.__module__]])

    for spec in INDEX_SPECS:
        assert spec.build.__module__ in modules
    assert "_common.icon_index" in modules
