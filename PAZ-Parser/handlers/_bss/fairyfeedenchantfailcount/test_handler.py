from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


_HEADER_SIZE = 8
_RECORD_HEADER_SIZE = 4
_ENTRY_SIZE = 11


def _entry_rows() -> DeclaredCount:
    """Entry rows: the record bytes up to the trailer's end_of_records, less
    each declared record's 4-byte entry_count, in 11-byte entries."""

    def read(source: CaseInput) -> int:
        raw = source.file(None)
        (count,) = struct.unpack_from("<I", raw, 4)
        end_of_records = struct.unpack_from("<I", raw, len(raw) - 8)[0]
        entry_bytes = end_of_records - _HEADER_SIZE - count * _RECORD_HEADER_SIZE
        if entry_bytes < 0 or entry_bytes % _ENTRY_SIZE:
            raise AssertionError(f"{count} records do not end on whole entries at 0x{end_of_records:X}")
        return entry_bytes // _ENTRY_SIZE

    return read


CASE = HandlerCase(
    handler_name="fairyfeedenchantfailcount.bss",
    data_file="fairyfeedenchantfailcount.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fairyfeedenchantfailcount.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "record",
                "fairy_feed_key",
                "enchant_level",
                "feed_value",
                "equip_exp",
            ],
        ),
        DeclaredCountTest(declared=_entry_rows()),
        # Every entry repeats its record's FairyFeedKey, which is the record index plus one.
        TargetTest(col="record", value=0, expected={"fairy_feed_key": 1}),
        TargetTest(col="record", value=1, expected={"fairy_feed_key": 2}),
    ],
)


@pytest.fixture(scope="module")
def fairyfeedenchantfailcount_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyfeedenchantfailcount_bss(
    spec: Any,
    fairyfeedenchantfailcount_result: HandlerResult,
) -> None:
    fairyfeedenchantfailcount_result.check(spec)
