from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .handler import RESET_TYPES, LimitedItemSubGroupBssHandler
from .parser import FILE_NAME, KEY_FIELD, parse_limiteditemsubgroup_records


_U32 = struct.Struct("<I")
_ROW_COUNT_AT = 4
_ROWS_AT = 8
_ENTRY = struct.Struct("<HIBIBI")


def _declared_entries(source: CaseInput) -> int:
    """The entry counts of every row the file declares, added up."""
    data = source.data
    (row_count,) = _U32.unpack_from(data, _ROW_COUNT_AT)
    pos, total = _ROWS_AT, 0
    for _ in range(row_count):
        (entry_count,) = _U32.unpack_from(data, pos)
        pos += _U32.size + entry_count * _ENTRY.size
        total += entry_count
    return total


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                KEY_FIELD,
                "item_key",
                "purchase_subject",
                "purchase_count_limit",
                "reset_type",
                "unknown_0c",
                "item_name",
            ],
        ),
        DeclaredCountTest(declared=_declared_entries),
        RangeTest(col="reset_type", min_val=min(RESET_TYPES), max_val=max(RESET_TYPES)),
        UserLanguageTest(fields=["item_name"]),
    ],
)


@pytest.fixture(scope="module")
def limited_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_limiteditemsubgroup_bss(spec: Any, limited_result: HandlerResult) -> None:
    limited_result.check(spec)


def test_each_subgroup_keeps_its_items_together(limited_result: HandlerResult) -> None:
    """One row per subgroup: a key never comes back after another key's entries."""
    seen: list[int] = []
    for record in limited_result.records:
        key = record[KEY_FIELD]
        if not seen or seen[-1] != key:
            assert key not in seen, key
            seen.append(key)
    assert seen


def test_every_limit_is_positive(limited_result: HandlerResult) -> None:
    assert all(record["purchase_count_limit"] > 0 for record in limited_result.records)


def _pabr(body: bytes) -> bytes:
    table_start = len(b"PABR") + len(body)
    return b"PABR" + body + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_a_row_reads_its_entries() -> None:
    entries = _ENTRY.pack(51658, 16001, 2, 10, 1, 0) + _ENTRY.pack(51658, 4998, 2, 1, 4, 0)
    records = parse_limiteditemsubgroup_records(_pabr(_U32.pack(1) + _U32.pack(2) + entries))
    assert records == [
        {KEY_FIELD: 51658, "item_key": 16001, "purchase_subject": 2, "purchase_count_limit": 10,
         "reset_type": 1, "unknown_0c": 0},
        {KEY_FIELD: 51658, "item_key": 4998, "purchase_subject": 2, "purchase_count_limit": 1,
         "reset_type": 4, "unknown_0c": 0},
    ]


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    body = _U32.pack(1) + _U32.pack(0) + b"\x00"
    with pytest.raises(ValueError, match="string table starts"):
        parse_limiteditemsubgroup_records(_pabr(body))


def test_a_reset_type_reads_with_its_name() -> None:
    handler = LimitedItemSubGroupBssHandler()
    handler.lang = "en"
    assert handler._reset_type_text(1) == "1 Daily"
    assert handler._reset_type_text(4) == "4 Siege"
    assert handler._reset_type_text(9) == "9"
