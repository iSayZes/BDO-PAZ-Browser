from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import FILE_NAME, HEAD_FIELDS, HEAD_START, NAMED_HEAD_FIELDS, parse_gameoption
from .run_fields import BODY_RUNS


_U32 = struct.Struct("<I")
_TRAILER_SIZE = 8
_PSTR_HEAD = struct.Struct("<BI")
_SHOWN_RUN_FIELDS = sum(field.is_shown for run in BODY_RUNS for field in run.fields)


def _declared_rows(source: CaseInput) -> int:
    """One row per named head and run field plus the `string_count` the string table declares."""
    (table_start,) = _U32.unpack_from(source.data, len(source.data) - _TRAILER_SIZE)
    (string_count,) = _U32.unpack_from(source.data, table_start)
    return len(NAMED_HEAD_FIELDS) + _SHOWN_RUN_FIELDS + string_count


def _head_offset(name: str) -> int:
    """The layout offset of a head field: the sizes of the fields before it, after the magic."""
    offset = HEAD_START
    for field in HEAD_FIELDS:
        if field.name == name:
            return offset
        offset += struct.calcsize("<" + field.fmt)
    raise KeyError(name)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["offset", "sheet", "field", "value", "text"]),
        DeclaredCountTest(declared=_declared_rows),
        # Layout 6 offsets (gameoption_bss.md).
        TargetTest(col="field", value="inn_rental_time", expected={"offset": 0x28, "sheet": "BattleOption"}),
        TargetTest(col="field", value="re_awakening_item_key", expected={"offset": 0xC1}),
        TargetTest(col="field", value="mating_regist_time", expected={"sheet": "ServantOption"}),
        TargetTest(col="field", value="client_version", expected={"sheet": "MovementVerifyOption"}),
        TargetTest(col="field", value="world_chat_condition", expected={"sheet": "EtcOption"}),
        TargetTest(col="field", value="reservation_arsha_price", expected={"sheet": "GuildOption"}),
        TargetTest(col="field", value="item_market_register_count_per_user", expected={"sheet": "ItemMarket"}),
        TargetTest(col="field", value="strings[0]", expected={"offset": None, "sheet": None}),
    ],
)


@pytest.fixture(scope="module")
def gameoption_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_gameoption_bss(spec: Any, gameoption_result: HandlerResult) -> None:
    gameoption_result.check(spec)


def test_head_fields_sit_at_their_layout_offsets(gameoption_result: HandlerResult) -> None:
    head = [r for r in gameoption_result.records if r["sheet"] == "BattleOption"]
    assert [r["offset"] for r in head] == [_head_offset(r["field"]) for r in head]


def test_head_ends_at_0xc5() -> None:
    assert _head_offset("re_awakening_item_key") + 4 == 0xC5


def test_the_runs_follow_the_head_without_gaps(gameoption_result: HandlerResult) -> None:
    option = parse_gameoption(gameoption_result.source.data)
    assert option.body_error == ""
    offsets = [value.offset for value in option.runs]
    ends = [value.offset + value.size for value in option.runs]
    assert offsets[0] == 0xC5
    assert offsets[1:] == ends[:-1]


def test_the_counted_arrays_hold_their_count(gameoption_result: HandlerResult) -> None:
    runs = {value.field.name: value.value for value in parse_gameoption(gameoption_result.source.data).runs}
    counted = [field for run in BODY_RUNS for field in run.fields if field.count and not field.count.isdigit()]
    assert counted
    for field in counted:
        array = runs[field.name]
        assert isinstance(array, tuple), field.name
        assert len(array) == runs[field.count], field.name


def test_the_condition_refs_point_into_the_string_table(gameoption_result: HandlerResult) -> None:
    strings = [r for r in gameoption_result.records if r["offset"] is None]
    refs = [r for r in gameoption_result.records if r["field"].endswith("_condition_ref")]
    assert {r["field"] for r in refs} == {"final_level_up_condition_ref", "tutorial_condition_ref"}
    for ref in refs:
        assert 0 <= ref["value"] < len(strings)
        assert ref["text"] == strings[ref["value"]]["value"]


def _file(head: bytes, body: bytes, strings: tuple[str, ...]) -> bytes:
    """PABR, the head and body, a string table of wide strings and the trailer."""
    out = b"PABR" + head + body
    table_start = len(out)
    out += _U32.pack(len(strings))
    for text in strings:
        raw = text.encode("utf-16-le")
        out += _PSTR_HEAD.pack(1, len(raw)) + raw
    return out + struct.pack("<II", table_start, 0)


def _head_bytes() -> bytes:
    return b"".join(
        b"\0" * struct.calcsize("<" + field.fmt) for field in HEAD_FIELDS
    )


def _empty_body() -> bytes:
    """Every run with each counted array empty."""
    return b"".join(
        b"\0" * struct.calcsize(f"<{field.count if field.count.isdigit() else ''}{field.fmt}")
        for run in BODY_RUNS
        for field in run.fields
        if not field.count or field.count.isdigit()
    )


def test_a_built_file_reads_back() -> None:
    option = parse_gameoption(_file(_head_bytes(), _empty_body() + b"\1\2\3", ("0", "x")))
    assert option.body_error == ""
    assert option.runs[0].offset == 0xC5
    assert option.runs[-1].offset + option.runs[-1].size == 0xC5 + len(_empty_body())
    assert option.strings == ("0", "x")


def test_a_short_body_keeps_the_head() -> None:
    option = parse_gameoption(_file(_head_bytes(), b"\1\2\3", ("0",)))
    assert option.runs == ()
    assert option.body_error
    assert len(option.head) == len(HEAD_FIELDS)


@pytest.mark.parametrize(
    "data",
    [
        b"XXXX" + _file(_head_bytes(), b"", ())[4:],
        _file(_head_bytes()[:-1], b"", ()),
    ],
    ids=["bad_magic", "head_past_the_string_table"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_gameoption(data)
