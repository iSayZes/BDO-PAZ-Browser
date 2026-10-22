from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, KEY_FIELD, parse_landscapepaintingdrop_records


_U32 = struct.Struct("<I")
# Type 13, La Orzeca (LOC type 126 and the window Lua's last member).
_LA_ORZECA = 13

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "drop_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                KEY_FIELD,
                "unknown_01",
                "name_index",
                "name_kr",
                "unknown_09",
                "unknown_0d",
                "drop_item_key",
                "name",
                "drop_item_name",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col=KEY_FIELD, value=_LA_ORZECA, expected={"name": "La Orzeca"}),
        UserLanguageTest(fields=["name", "drop_item_name"]),
    ],
)


@pytest.fixture(scope="module")
def landscape_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_landscapepaintingdropstaticstatus_bss(spec: Any, landscape_result: HandlerResult) -> None:
    landscape_result.check(spec)


def test_the_rows_run_in_type_order(landscape_result: HandlerResult) -> None:
    types = [record[KEY_FIELD] for record in landscape_result.records]
    assert types == list(range(len(types)))


def test_every_painting_has_a_korean_name(landscape_result: HandlerResult) -> None:
    assert all(record["name_kr"] for record in landscape_result.records)


def _row(painting_type: int, name_index: int, keys: list[int], drop_item_key: int) -> bytes:
    return (
        struct.pack("<BII", painting_type, 30009 + painting_type, name_index)
        + _U32.pack(len(keys)) + struct.pack(f"<{len(keys)}I", *keys)
        + _U32.pack(drop_item_key)
    )


def _pabr(body: bytes, names: list[str]) -> bytes:
    table_start = len(b"PABR") + len(body)
    strings = b"".join(b"\x01" + _U32.pack(len(name) * 2) + name.encode("utf-16-le") for name in names)
    return b"PABR" + body + _U32.pack(len(names)) + strings + _U32.pack(table_start) + _U32.pack(0)


def test_a_row_reads_its_list_and_drop_item() -> None:
    body = _U32.pack(1) + _row(0, 0, [217619, 217620], 44273)
    records = parse_landscapepaintingdrop_records(_pabr(body, ["루드 유황 광산"]))
    assert records == [
        {
            KEY_FIELD: 0,
            "unknown_01": 30009,
            "name_index": 0,
            "name_kr": "루드 유황 광산",
            "unknown_09": 2,
            "unknown_0d": [217619, 217620],
            "drop_item_key": 44273,
        }
    ]


def test_a_list_that_runs_past_the_string_table_raises() -> None:
    body = _U32.pack(1) + struct.pack("<BII", 0, 30009, 0) + _U32.pack(1000)
    with pytest.raises(ValueError, match="runs past the end"):
        parse_landscapepaintingdrop_records(_pabr(body, []))
