from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    fixed_rows,
    run_case,
)

from ..vehicleskill.parser import FILE_NAME as SKILL_FILE, parse_vehicleskill_records
from .handler import VehicleSkillCountHandler
from .parser import FILE_NAME, FILE_SIZE, parse_vehicleskillcount_record


_ENTRY = PazEntry("", f"gamecommondata/binary/{FILE_NAME}", 0, 0, 0, 0, 0)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["count", "highest_key"]),
        # The whole file is the one value.
        DeclaredCountTest(declared=fixed_rows(row_size=FILE_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def count_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_vehicleskillcount_dbss(spec: Any, count_result: HandlerResult) -> None:
    count_result.check(spec)


def test_count_is_the_highest_skill_key_plus_one(count_result: HandlerResult) -> None:
    """The byte is one above the highest key of vehicleskill.dbss, as the 2016 `_count`."""
    skill_keys = [record["key"] for record in parse_vehicleskill_records(load_binary_fixture(SKILL_FILE))]
    assert count_result.records[0]["count"] == max(skill_keys) + 1


def test_count_matches_the_vehicleskill_header_byte(count_result: HandlerResult) -> None:
    assert count_result.records[0]["count"] == load_binary_fixture(SKILL_FILE)[0]


def test_parser_reads_the_byte() -> None:
    assert parse_vehicleskillcount_record(b"\x6b") == {"count": 107}


@pytest.mark.parametrize("data", [b"", b"\x6b\x00"], ids=["empty", "two bytes"])
def test_parser_rejects_any_other_size(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_vehicleskillcount_record(data)


def test_handler_shows_the_highest_key() -> None:
    records = VehicleSkillCountHandler().get_records(b"\x6b", _ENTRY, {})
    assert records == [{"count": 107, "highest_key": 106}]


def test_handler_has_no_highest_key_without_skills() -> None:
    records = VehicleSkillCountHandler().get_records(b"\x00", _ENTRY, {})
    assert records == [{"count": 0, "highest_key": None}]


def test_handler_reports_a_wrong_size() -> None:
    records = VehicleSkillCountHandler().get_records(b"", _ENTRY, {})
    assert "_error" in records[0]
