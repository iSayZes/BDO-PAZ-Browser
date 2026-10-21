from __future__ import annotations

from collections.abc import Callable
from dataclasses import replace
from functools import cache
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from _dbss.itemenchant.parser import build_item_name_kr_index
from _dbss.knowledgelearning.parser import (
    build_knowledge_learning_character_index,
    build_knowledge_learning_item_index,
)
from tests.character_indexes import character_name_kr_index
from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)


# A 4-byte lead source_id before each 13-byte record.
_ENTRY_SIZE = 4 + 13


def _table_rows() -> DeclaredCount:
    """Rows across the data file's tables: each is a u32 count and `count`
    17-byte entries, back to back up to the end of the file."""

    def read(source: CaseInput) -> int:
        raw = source.data
        pos = 0
        total = 0
        while pos < len(raw):
            count = int.from_bytes(raw[pos : pos + 4], "little")
            total += count
            pos += 4 + count * _ENTRY_SIZE
        if pos != len(raw):
            raise AssertionError(f"tables end at {pos}, not at the end of {len(raw)} bytes")
        return total

    return read


@cache
def _item_name_kr_index() -> dict[int, str]:
    """`IndexKind.ITEM_NAME_KR` of the fixture client."""
    return build_item_name_kr_index(
        load_binary_fixture("itemenchant.dbss"), load_binary_fixture("itemenchantoffset.dbss")
    )


# The Korean names a Source Name falls back to; with LOC loaded none may show.
_KOREAN_NAMES = {IndexKind.CHARACTER_NAME_KR: character_name_kr_index, IndexKind.ITEM_NAME_KR: _item_name_kr_index}


CASE = HandlerCase(
    handler_name="knowledgelearning.dbss",
    data_file="knowledgelearning.dbss",
    companion_files={"knowledgelearningoffset.dbss": "knowledgelearningoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Knowledge Name"],
    internal_path="gamecommondata/binary/knowledgelearning.dbss",
    lookup_indexes=_KOREAN_NAMES,
    tests=[
        SchemaTest(required_keys=["table", "source_type", "source_id", "source_name", "card_id", "card_name"]),
        DeclaredCountTest(declared=_table_rows()),
        UserLanguageTest(fields=["source_name"]),
        TargetTest(
            col="source_id",
            value=10004,
            expected={
                "table": 0,
                "source_type": "Character",
                "source_name": "Feldspar",
                "card_id": 7302,
                "card_name": "Feldspar",
            },
        ),
        # The item table was misread before; its first row teaches the item's own card.
        TargetTest(
            col="source_id",
            value=4070,
            expected={
                "table": 1,
                "source_type": "Item",
                "source_name": "Processed Coal",
                "card_id": 7605,
                "card_name": "Processed Coal",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def knowledgelearning_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_knowledgelearning_dbss(spec: Any, knowledgelearning_result: HandlerResult) -> None:
    knowledgelearning_result.check(spec)


@pytest.mark.parametrize(
    ("build", "table"),
    [(build_knowledge_learning_character_index, 0), (build_knowledge_learning_item_index, 1)],
    ids=["characters", "items"],
)
def test_learning_index_groups_one_table_by_card(
    build: Callable[[bytes, bytes], dict[int, tuple[int, ...]]],
    table: int,
    knowledgelearning_result: HandlerResult,
) -> None:
    """Each index is one table's rows grouped by card, the other table left out."""
    source = knowledgelearning_result.source
    index = build(source.data, source.file("knowledgelearningoffset.dbss"))

    expected: dict[int, list[int]] = {}
    for record in knowledgelearning_result.records:
        if record["table"] == table:
            expected.setdefault(record["card_id"], []).append(record["source_id"])

    assert index == {card_id: tuple(sorted(ids)) for card_id, ids in expected.items()}


def test_source_names_fall_back_to_the_korean_name() -> None:
    """Without LOC a character row shows its Korean characterstatic.dbss name
    and an item row its Korean itemenchant.dbss name."""
    case = replace(CASE, tests=[], loc_file=None, uses_loc=False)
    records = run_case(case).records
    names_by_table = {0: character_name_kr_index(), 1: _item_name_kr_index()}

    assert {r["table"] for r in records} == set(names_by_table)
    assert all(r["source_name"] == names_by_table[r["table"]].get(r["source_id"], "") for r in records)
    assert all(any(r["source_name"] for r in records if r["table"] == table) for table in names_by_table)
