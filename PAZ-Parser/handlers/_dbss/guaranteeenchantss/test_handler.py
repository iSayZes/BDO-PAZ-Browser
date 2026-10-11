from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.guaranteeenchantss.parser import COUNT, ROW, parse_guaranteeenchantss_records


# Enhancement type 2 is Blackstar gear (guaranteeenchantss_dbss.md, Groups).
_BLACKSTAR = 2
_BLACKSTAR_LONGSWORD = 715001
# Enhancement type 1 is ordinary weapons and armour.
_ORDINARY_GEAR = 1
_MAX_U8 = 0xFF


CASE = HandlerCase(
    handler_name="guaranteeenchantss.dbss",
    data_file="guaranteeenchantss.dbss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path="gamecommondata/binary/guaranteeenchantss.dbss",
    lookup_indexes={IndexKind.ENHANCEMENT_TYPE_ITEMS: {_BLACKSTAR: (_BLACKSTAR_LONGSWORD,)}},
    tests=[
        SchemaTest(
            required_keys=[
                "enhancement_type",
                "enchant_level",
                "agris_count",
                "item_ids",
                "item_names",
                "item_count",
            ],
        ),
        # The u32 row count at +0x00.
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="enhancement_type", min_val=1, max_val=_MAX_U8),
        # Every level of a type lists that type's items from the lookup index.
        TargetTest(
            col="enhancement_type",
            value=_BLACKSTAR,
            expected={"item_ids": [_BLACKSTAR_LONGSWORD], "item_names": ["Blackstar Longsword"], "item_count": 1},
        ),
        # A type with no indexed items lists none; None sorts last.
        TargetTest(
            col="enhancement_type",
            value=_ORDINARY_GEAR,
            expected={"item_ids": [], "item_names": [], "item_count": None},
        ),
    ],
)


@pytest.fixture(scope="module")
def guaranteeenchantss_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_guaranteeenchantss(spec: Any, guaranteeenchantss_result: HandlerResult) -> None:
    guaranteeenchantss_result.check(spec)


def test_each_type_and_level_appears_once(guaranteeenchantss_result: HandlerResult) -> None:
    keys = [(r["enhancement_type"], r["enchant_level"]) for r in guaranteeenchantss_result.records]
    assert len(keys) == len(set(keys))


def test_rows_sort_by_type_then_level(guaranteeenchantss_result: HandlerResult) -> None:
    keys = [(r["enhancement_type"], r["enchant_level"]) for r in guaranteeenchantss_result.records]
    assert keys == sorted(keys)


def _file(*rows: tuple[int, int, int]) -> bytes:
    return COUNT.pack(len(rows)) + b"".join(ROW.pack(*row) for row in rows)


def test_rows_read_type_level_and_count_in_sorted_order() -> None:
    data = _file((2, 19, 15), (1, 7, 3), (2, 7, 3))
    assert parse_guaranteeenchantss_records(data) == [
        {"enhancement_type": 1, "enchant_level": 7, "agris_count": 3},
        {"enhancement_type": 2, "enchant_level": 7, "agris_count": 3},
        {"enhancement_type": 2, "enchant_level": 19, "agris_count": 15},
    ]


def test_a_count_the_rows_do_not_fill_raises() -> None:
    data = _file((1, 7, 3))
    with pytest.raises(ValueError, match="need"):
        parse_guaranteeenchantss_records(COUNT.pack(2) + data[COUNT.size:])


def test_extra_bytes_after_the_rows_raise() -> None:
    with pytest.raises(ValueError, match="need"):
        parse_guaranteeenchantss_records(_file((1, 7, 3)) + b"\0")


def test_a_file_without_a_count_raises() -> None:
    with pytest.raises(ValueError, match="too short"):
        parse_guaranteeenchantss_records(b"\0\0")
