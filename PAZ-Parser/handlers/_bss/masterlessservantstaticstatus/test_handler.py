from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _bss.masterlessservantstaticstatus.parser import parse_masterlessservantstaticstatus_records


# PABR magic, then the u32 record count.
_COUNT_OFFSET = 4
# `_rentCharacterKeyRaw` in panel_dialog_horsewithoutowner_all.luac.
_TRAVELERS_HORSE = 31560

CASE = HandlerCase(
    handler_name="masterlessservantstaticstatus.bss",
    data_file="masterlessservantstaticstatus.bss",
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path="gamecommondata/binary/masterlessservantstaticstatus.bss",
    tests=[
        SchemaTest(
            required_keys=["character_id", "name", "unknown_00", "unknown_04", "unknown_08", "has_character_row"]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def masterless_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_masterlessservantstaticstatus_bss(spec: Any, masterless_result: HandlerResult) -> None:
    masterless_result.check(spec)


def test_every_row_is_the_travelers_horse(masterless_result: HandlerResult) -> None:
    # Checks character_id: the horse the Lua rents out, on every row.
    assert {r["character_id"] for r in masterless_result.records} == {_TRAVELERS_HORSE}


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_masterlessservantstaticstatus_records(b"XXXX" + bytes(16))
