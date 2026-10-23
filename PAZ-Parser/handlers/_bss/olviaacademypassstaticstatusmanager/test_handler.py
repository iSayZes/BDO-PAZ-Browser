from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, RangeTest, SchemaTest, TargetTest, case_id, run_case
from tests.quest_list_cases import quest_list_case

from _bss.allquestlist.olvia_academy import PASS_LIST
from .handler import OlviaAcademyPassBssHandler
from .parser import FILE_NAME, PASS_TYPE_NAMES, parse_pass_records


_U32 = struct.Struct("<I")
_STEP_SIZE = 8
_PASSES_START = 4
_TRAILER_SIZE = 8
# The pass quest of a step is the next sub ID of its base quest's chain.
_NEXT_SUB_ID = 1 << 16
# Gathering Time! 1.: (101 << 16) | 2324, the first step of the Collect pass.
_GATHERING_TIME_1 = 101 << 16 | 2324


def _declared_steps(source: CaseInput) -> int:
    """The steps the pass sizes declare between the magic and the string table."""
    data = source.data
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    pos, steps = _PASSES_START, 0
    while pos < table_start:
        (pass_size,) = _U32.unpack_from(data, pos)
        pos += _U32.size + pass_size * _STEP_SIZE
        steps += pass_size
    return steps


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["base_quest_text", "pass_quest_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "pass_type", "pass_size", "quest_index", "base_quest", "pass_quest",
                "pass_type_name", "base_quest_text", "pass_quest_text",
            ]
        ),
        DeclaredCountTest(declared=_declared_steps),
        RangeTest(col="pass_type", min_val=0, max_val=len(PASS_TYPE_NAMES) - 1),
        TargetTest(
            col="base_quest",
            value=_GATHERING_TIME_1,
            expected={"pass_type": 0, "pass_type_name": "Collect", "quest_index": 0, "pass_quest": _GATHERING_TIME_1 + _NEXT_SUB_ID},
        ),
    ],
)


@pytest.fixture(scope="module")
def pass_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_olviaacademypassstaticstatusmanager(spec: Any, pass_result: HandlerResult) -> None:
    pass_result.check(spec)


def test_every_pass_quest_follows_its_base_quest(pass_result: HandlerResult) -> None:
    for record in pass_result.records:
        assert record["pass_quest"] == record["base_quest"] + _NEXT_SUB_ID, record


def test_every_pass_type_has_its_steps_in_order(pass_result: HandlerResult) -> None:
    pass_types = sorted({record["pass_type"] for record in pass_result.records})
    assert pass_types == list(range(len(pass_types)))
    for pass_type in pass_types:
        steps = [record for record in pass_result.records if record["pass_type"] == pass_type]
        assert [record["quest_index"] for record in steps] == list(range(steps[0]["pass_size"]))


def test_the_steps_hold_the_pass_quest_list(pass_result: HandlerResult) -> None:
    quests = [quest for record in pass_result.records for quest in (record["base_quest"], record["pass_quest"])]
    listed = {record["packed_quest_id"] for record in run_case(replace(quest_list_case(PASS_LIST), tests=[])).records}
    assert len(quests) == len(set(quests))
    assert set(quests) == listed


def test_both_quests_link_to_the_pass_list(pass_result: HandlerResult) -> None:
    handler = OlviaAcademyPassBssHandler()
    handler.lang = "en"
    html = handler.render_records_page(pass_result.records, 0, len(pass_result.records))
    assert html.count(f'data-path="gamecommondata/binary/{PASS_LIST}"') == 2 * len(pass_result.records)


def _pabr(values: bytes) -> bytes:
    table_start = _PASSES_START + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_a_pass_with_no_steps_keeps_the_next_pass_type() -> None:
    data = _pabr(_U32.pack(0) + struct.pack("<III", 1, _GATHERING_TIME_1, _GATHERING_TIME_1 + _NEXT_SUB_ID))
    (record,) = parse_pass_records(data)
    assert record["pass_type"] == 1


def test_a_step_count_past_the_string_table_raises() -> None:
    with pytest.raises(ValueError, match="runs past"):
        parse_pass_records(_pabr(struct.pack("<III", 2, 1, 2)))
