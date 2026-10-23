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


_U32 = struct.Struct("<I")
_TRAILER_SIZE = 8
_PSTR_HEAD = struct.Struct("<BI")


def _declared_rows(source: CaseInput) -> int:
    """One row per named head field plus the `string_count` the string table declares."""
    (table_start,) = _U32.unpack_from(source.data, len(source.data) - _TRAILER_SIZE)
    (string_count,) = _U32.unpack_from(source.data, table_start)
    return len(NAMED_HEAD_FIELDS) + string_count


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
        SchemaTest(required_keys=["offset", "field", "value", "text"]),
        DeclaredCountTest(declared=_declared_rows),
        # Layout 2 offsets (gameoption_bss.md).
        TargetTest(col="field", value="inn_rental_time", expected={"offset": 0x28}),
        TargetTest(col="field", value="re_awakening_item_key", expected={"offset": 0xC1}),
        TargetTest(col="field", value="strings[0]", expected={"offset": None}),
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
    head = [r for r in gameoption_result.records if r["offset"] is not None]
    assert [r["offset"] for r in head] == [_head_offset(r["field"]) for r in head]


def test_head_ends_at_0xc5() -> None:
    assert _head_offset("re_awakening_item_key") + 4 == 0xC5


def test_the_body_runs_to_the_string_table(gameoption_result: HandlerResult) -> None:
    data = gameoption_result.source.data
    option = parse_gameoption(data)
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    assert option.body_offset + option.body_size == table_start


def test_the_condition_ref_points_into_the_string_table(gameoption_result: HandlerResult) -> None:
    strings = [r for r in gameoption_result.records if r["offset"] is None]
    (ref,) = [r for r in gameoption_result.records if r["field"] == "final_level_up_condition_ref"]
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


def test_a_built_file_reads_back() -> None:
    option = parse_gameoption(_file(_head_bytes(), b"\1\2\3", ("0", "x")))
    assert option.body_offset == 0xC5
    assert option.body_size == 3
    assert option.strings == ("0", "x")


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
