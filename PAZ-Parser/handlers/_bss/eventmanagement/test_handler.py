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
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import FILE_NAME
from .records import CONTENTS_SECTION, EVENT_SECTION, period, row_ref


_EVENT_COUNT_AT = 4
_EVENT_ROW_SIZE = 15
_COUNT_SIZE = 4
_U32 = struct.Struct("<I")
# The oldest event map row: the same function and map on the 2017 server
# table, client 1784 and the live client.
_XMAS_MAP = row_ref(CONTENTS_SECTION, 1001)


def _declared_rows(source: CaseInput) -> int:
    """The event count after the magic plus the contents count after the event rows."""
    (events,) = _U32.unpack_from(source.data, _EVENT_COUNT_AT)
    (contents,) = _U32.unpack_from(source.data, _EVENT_COUNT_AT + _COUNT_SIZE + events * _EVENT_ROW_SIZE)
    return events + contents


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_names"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "section",
                "row_ref",
                "key",
                "name",
                "details",
                "period_start",
                "period_end",
                "character_keys",
                "character_names",
                "linked_keys",
            ],
        ),
        DeclaredCountTest(declared=_declared_rows),
        TargetTest(
            col="row_ref",
            value=_XMAS_MAP,
            expected={"event_contents_no": 1001, "function": "c_seteventmap", "param_1": "xmas"},
        ),
        UserLanguageTest(fields=["character_names"]),
    ],
)

_EVENT_FIELDS = ("event_no", "event_name_ref", "condition_ref", "setted_event_ref", "unknown_0e", "event_name", "condition", "setted_event")
_CONTENTS_FIELDS = ("event_contents_no", "function_ref", "function", *(f"param_{i}" for i in range(1, 5)), *(f"param_{i}_ref" for i in range(1, 5)))


@pytest.fixture(scope="module")
def event_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_eventmanagement_bss(spec: Any, event_result: HandlerResult) -> None:
    event_result.check(spec)


def _section(result: HandlerResult, section: str) -> list[dict]:
    return [r for r in result.records if r["section"] == section]


def test_both_sections_hold_rows_with_their_fields(event_result: HandlerResult) -> None:
    events = _section(event_result, EVENT_SECTION)
    contents = _section(event_result, CONTENTS_SECTION)
    assert events and contents
    assert all(field in r for r in events for field in _EVENT_FIELDS)
    assert all(field in r for r in contents for field in _CONTENTS_FIELDS)


def test_keys_are_unique_within_a_section(event_result: HandlerResult) -> None:
    refs = [r["row_ref"] for r in event_result.records]
    assert len(refs) == len(set(refs))


def test_every_set_contents_key_is_a_contents_row(event_result: HandlerResult) -> None:
    contents_keys = {r["key"] for r in _section(event_result, CONTENTS_SECTION)}
    set_keys = {key for r in _section(event_result, EVENT_SECTION) for key in r["linked_keys"]}
    assert set_keys
    assert set_keys <= contents_keys, sorted(set_keys - contents_keys)[:10]


def test_contents_rows_link_back_to_the_events_that_set_them(event_result: HandlerResult) -> None:
    setters = {r["key"]: set(r["linked_keys"]) for r in _section(event_result, EVENT_SECTION)}
    for row in _section(event_result, CONTENTS_SECTION):
        assert all(row["key"] in setters[event_no] for event_no in row["linked_keys"]), row["key"]


def test_functions_are_stored_in_lower_case(event_result: HandlerResult) -> None:
    functions = {r["function"] for r in _section(event_result, CONTENTS_SECTION)}
    assert functions == {name.lower() for name in functions}


@pytest.mark.parametrize(
    ("condition", "expected"),
    [
        ("checkPeriodbyGMT(0, 2026/09/17-09:00, 2026/10/08-09:00);", ("2026-09-17 09:00", "2026-10-08 09:00")),
        (
            "checkPeriod(2025/07/10-09:00, 2025/07/24-09:00); CheckWeekDayAndDuration(3,20,45,15);",
            ("2025-07-10 09:00", "2025-07-24 09:00"),
        ),
        ("checkperiodbyGmt(0, 2019/9/4-00:00, 2019/9/25-09:00);", ("2019-09-04 00:00", "2019-09-25 09:00")),
        ("CheckWeekDayAndDuration(6,20,00,1440);BiWeeklyCheck(1);", (None, None)),
    ],
)
def test_period_reads_the_period_call(condition: str, expected: tuple[str | None, str | None]) -> None:
    assert period(condition) == expected
