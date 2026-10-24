from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.binary import u32
from tests.framework import HandlerCase, HandlerResult, SchemaTest, case_id, run_case

from .parser import FILE_NAME, parse_specialpass_file, parse_specialpass_records


_ROW_COUNT_AT = 4
_U32 = struct.Struct("<I")

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["basic_reward", "pass_reward"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "pass_key",
                "start_time",
                "end_time",
                "sale_end_time",
                "title_index",
                "period_index",
                "description_index",
                "content_type",
                "unknown_2a",
                "title_kr",
                "period_kr",
                "description_kr",
                "basic_item_key",
                "basic_item_count",
                "pass_item_key",
                "pass_item_count",
                "reward_point",
                "step_no",
                "content_type_name",
                "basic_reward",
                "pass_reward",
                "description",
            ],
        ),
    ],
)


@pytest.fixture(scope="module")
def specialpass_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_specialpass_bss(spec: Any, specialpass_result: HandlerResult) -> None:
    specialpass_result.check(spec)


def test_the_rows_match_the_declared_count(specialpass_result: HandlerResult) -> None:
    data = specialpass_result.source.data
    assert len(parse_specialpass_file(data).rows) == u32(data, _ROW_COUNT_AT)


def test_each_track_belongs_to_one_pass_row(specialpass_result: HandlerResult) -> None:
    parsed = parse_specialpass_file(specialpass_result.source.data)
    row_keys = {row["pass_key"] for row in parsed.rows}
    for track in parsed.tracks:
        keys = {step["pass_key"] for step in track}
        assert len(keys) == 1 and keys <= row_keys, keys


def test_every_row_has_its_texts_and_a_period(specialpass_result: HandlerResult) -> None:
    for record in specialpass_result.records:
        assert record["title_kr"] and record["period_kr"], record["pass_key"]
        assert record["start_time"] < record["sale_end_time"] < record["end_time"], record["pass_key"]


def test_pass_points_rise_step_by_step(specialpass_result: HandlerResult) -> None:
    for track in parse_specialpass_file(specialpass_result.source.data).tracks:
        points = [step["reward_point"] for step in track]
        assert points == sorted(set(points)), track[0]["pass_key"]


def _pabr(body: bytes, strings: list[str]) -> bytes:
    table = _U32.pack(len(strings)) + b"".join(
        struct.pack("<BI", 1, len(text) * 2) + text.encode("utf-16-le") for text in strings
    )
    table_start = 4 + len(body)
    return b"PABR" + body + table + _U32.pack(table_start) + _U32.pack(0)


_ROW = struct.pack("<HQQQIIIIB", 7, 100, 300, 200, 0, 1, 2, 2, 0)
_STEP = struct.pack("<HIQIQQ", 7, 16080, 5, 45820, 1, 10)


def test_a_step_takes_its_row_texts_and_the_values_after_the_tracks() -> None:
    body = _U32.pack(1) + _ROW + _U32.pack(1) + _U32.pack(1) + _STEP + struct.pack("<II", 5, 2)
    data = _pabr(body, ["T", "P", "D"])
    assert parse_specialpass_file(data).unknown_after_tracks == [5, 2]
    (record,) = parse_specialpass_records(data)
    assert (record["title_kr"], record["period_kr"], record["description_kr"]) == ("T", "P", "D")
    assert (record["content_type"], record["step_no"], record["reward_point"]) == (2, 1, 10)
    assert (record["basic_item_key"], record["basic_item_count"], record["pass_item_key"]) == (16080, 5, 45820)


def test_bytes_after_the_tracks_that_are_not_u32_values_raise() -> None:
    body = _U32.pack(1) + _ROW + _U32.pack(0) + b"\x00"
    with pytest.raises(ValueError, match="not whole u32 values"):
        parse_specialpass_file(_pabr(body, []))
