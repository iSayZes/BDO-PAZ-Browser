from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
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

from .parser import FILE_NAME, JOB_COUNT, parse_employeejobslot_file


# PABR magic, then the u32 record count.
_COUNT_OFFSET = 4
_EPHERIA_CARRACK = 31045

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_key", "job_slot_counts", "name", "has_character_row"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["name"]),
        TargetTest(col="character_key", value=_EPHERIA_CARRACK, expected={
            "name": "Epheria Carrack",
            "has_character_row": True,
        }),
    ],
)


@pytest.fixture(scope="module")
def slot_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_employeejobslotstaticstatus_bss(spec: Any, slot_result: HandlerResult) -> None:
    slot_result.check(spec)


def test_every_ship_has_one_count_per_job(slot_result: HandlerResult) -> None:
    for record in slot_result.records:
        assert len(record["job_slot_counts"]) == JOB_COUNT


def test_ship_keys_are_unique(slot_result: HandlerResult) -> None:
    keys = [record["character_key"] for record in slot_result.records]
    assert len(keys) == len(set(keys))


def test_entries_are_keyed_in_order() -> None:
    # The entry table has no count; its keys run 0, 1, 2, ... up to the string table.
    entries = parse_employeejobslot_file(load_binary_fixture(FILE_NAME)).entries
    assert [entry["unknown_00"] for entry in entries] == list(range(len(entries)))


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_employeejobslot_file(b"XXXX" + bytes(16))
