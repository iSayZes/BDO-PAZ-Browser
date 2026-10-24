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

from _bss.abyssoneaudioinfo.parser import FILE_NAME, KEY_FIELD, parse_abyssoneaudioinfo_records
from _bss.audioinfo.bgm_states import BGM_STATE_SLOTS
from _common.lookup_index import IndexKind


# PABR magic, then the u32 row count.
_COUNT_OFFSET = 4
# Field 4001 is A1_001, the first Abyss One field of fieldinfo.bss.
_FIRST_FIELD = 4001
_FIRST_FIELD_NAME = "A1_001"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "field_no",
                "bgm_states",
                "bgm_state_names",
                "bgm_states_text",
                "bank_no_environment",
                "field_name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col=KEY_FIELD, value=_FIRST_FIELD, expected={"field_name": _FIRST_FIELD_NAME}),
    ],
    lookup_indexes={IndexKind.FIELD_NAME: {_FIRST_FIELD: _FIRST_FIELD_NAME}},
)


@pytest.fixture(scope="module")
def abyss_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_abyssoneaudioinfo_bss(spec: Any, abyss_result: HandlerResult) -> None:
    abyss_result.check(spec)


def test_keys_are_unique(abyss_result: HandlerResult) -> None:
    keys = [r[KEY_FIELD] for r in abyss_result.records]
    assert len(keys) == len(set(keys))


def test_every_row_names_its_states(abyss_result: HandlerResult) -> None:
    for record in abyss_result.records:
        assert len(record["bgm_state_names"]) == BGM_STATE_SLOTS
        assert all(record["bgm_state_names"]), record[KEY_FIELD]


def _file(rows: list[tuple[int, int, int]], strings: list[str]) -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows))
    for field_no, state, env in rows:
        body += struct.pack("<H4II", field_no, state, state, state, state, env)
    table_start = len(body)
    body += struct.pack("<I", len(strings))
    for text in strings:
        raw = text.encode("utf-8")
        body += struct.pack("<BI", 0, len(raw)) + raw
    return body + struct.pack("<II", table_start, 0)


def test_parse_reads_states_and_ambience() -> None:
    data = _file([(4009, 1, 203), (4001, 0, 208)], ["W11_A", "W11_B"])

    records = parse_abyssoneaudioinfo_records(data)

    assert records[0]["field_no"] == 4009
    assert records[0]["bgm_state_names"] == ["W11_B"] * BGM_STATE_SLOTS
    assert records[1]["bank_no_environment"] == 208


def test_parse_rejects_rows_that_stop_before_the_string_table() -> None:
    data = bytearray(_file([(4001, 0, 1), (4002, 0, 1)], ["W11_A"]))
    struct.pack_into("<I", data, _COUNT_OFFSET, 1)
    with pytest.raises(ValueError):
        parse_abyssoneaudioinfo_records(bytes(data))
