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
    case_id,
    header_count,
    run_case,
)

from _bss.pcroommaid.parser import parse_pcroommaid


_MAID_OFFSET_FILE = "maidoffset.dbss"
# maidoffset.dbss: u32 count, then rows of u16 key, u32 offset, u32 size.
_MAID_OFFSET_ROW = struct.Struct("<HII")

CASE = HandlerCase(
    handler_name="pcroommaid.bss",
    data_file="pcroommaid.bss",
    # maidoffset.dbss is not read by the handler; the order check below uses it.
    companion_files={
        "characterstaticoffset.dbss": "characterstaticoffset.dbss",
        _MAID_OFFSET_FILE: _MAID_OFFSET_FILE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path="gamecommondata/binary/pcroommaid.bss",
    tests=[
        SchemaTest(required_keys=["character_key", "name", "has_character_row"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        # The first PC room maid pair (client 1230 onward): warehouse and marketplace.
        TargetTest(col="character_key", value=18964, expected={"name": "[Oasis] Fairy Chiara"}),
        TargetTest(col="character_key", value=18967, expected={"name": "[Oasis] Ethan the Butler"}),
    ],
)


@pytest.fixture(scope="module")
def pcroommaid_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_pcroommaid_bss(spec: Any, pcroommaid_result: HandlerResult) -> None:
    pcroommaid_result.check(spec)


def test_keys_are_maid_rows_in_maid_order(pcroommaid_result: HandlerResult) -> None:
    """Every key is a maid.dbss row, listed in the order maidoffset.dbss lists the rows."""
    offset_data = pcroommaid_result.source.file(_MAID_OFFSET_FILE)
    count = struct.unpack_from("<I", offset_data, 0)[0]
    maid_keys = [
        _MAID_OFFSET_ROW.unpack_from(offset_data, 4 + index * _MAID_OFFSET_ROW.size)[0]
        for index in range(count)
    ]
    keys = [r["character_key"] for r in pcroommaid_result.records]
    assert set(keys) <= set(maid_keys)
    assert keys == [key for key in maid_keys if key in set(keys)]


def test_every_key_has_a_character_row(pcroommaid_result: HandlerResult) -> None:
    assert all(r["has_character_row"] for r in pcroommaid_result.records)


def test_the_keys_read_back() -> None:
    data = struct.pack("<IHH", 2, 18965, 18964)
    assert parse_pcroommaid(data) == [{"character_key": 18965}, {"character_key": 18964}]


@pytest.mark.parametrize(
    "data",
    [b"\x02\x00", struct.pack("<IH", 2, 18964), struct.pack("<IHH", 1, 18964, 18965)],
    ids=["short_count", "missing_key", "extra_bytes"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_pcroommaid(data)
