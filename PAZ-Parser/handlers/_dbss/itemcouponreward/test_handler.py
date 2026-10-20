from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _dbss.itemcouponreward.parser import parse_itemcouponreward_offset_records


_WORD_SIZE = 4


def _word_count(source: CaseInput) -> int:
    """One row per u32 word of the file, the count included."""
    return len(source.file(None)) // _WORD_SIZE


CASE = HandlerCase(
    handler_name="itemcouponrewardoffset.dbss",
    data_file="itemcouponrewardoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/itemcouponrewardoffset.dbss",
    tests=[
        SchemaTest(required_keys=["offset", "field", "value"]),
        DeclaredCountTest(declared=_word_count),
        TargetTest(col="field", value="count", expected=[{"offset": 0}]),
    ],
)


@pytest.fixture(scope="module")
def itemcouponrewardoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemcouponrewardoffset_dbss(spec: Any, itemcouponrewardoffset_result: HandlerResult) -> None:
    itemcouponrewardoffset_result.check(spec)


def test_words_after_the_count_get_unknown_names() -> None:
    records = parse_itemcouponreward_offset_records(bytes(20))
    assert [r["field"] for r in records] == ["count", "unknown_04", "unknown_08", "unknown_0c", "unknown_10"]


def test_a_partial_word_raises() -> None:
    with pytest.raises(ValueError, match="whole number"):
        parse_itemcouponreward_offset_records(bytes(6))
