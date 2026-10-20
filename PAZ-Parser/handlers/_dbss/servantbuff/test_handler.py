from __future__ import annotations

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

from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.string_hash import ascii_key_hash
from _dbss.servantbuff.parser import parse_servantbuff_records


_OFFSET_FILE = "servantbuffoffset.dbss"
# An offset row points at `key_dup`, past the u32 key.
_KEY_SIZE = 4

CASE = HandlerCase(
    handler_name="servantbuff.dbss",
    data_file="servantbuff.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill_name"],
    internal_path="gamecommondata/binary/servantbuff.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "condition",
                "action_name",
                "action_hash",
                "servant_action_name",
                "servant_action_hash",
                "skill_no",
                "skill_name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=0, companion=_OFFSET_FILE)),
        # Horse Communion 1 to 3 are skills 220 to 222.
        TargetTest(
            col="key",
            value=1,
            expected={"action_name": "VEHICLE_INTERACTION_HORSE_1", "skill_no": 220, "skill_name": "Horse Communion 1"},
        ),
        TargetTest(col="key", value=3, expected={"servant_action_name": "HORSE_INTERACTION_3", "skill_no": 222}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def servantbuff_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_servantbuff_dbss(spec: Any, servantbuff_result: HandlerResult) -> None:
    servantbuff_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_servantbuffoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_hashes_are_the_ascii_key_hash_of_the_names(servantbuff_result: HandlerResult) -> None:
    # Checks both hash fields: each is the client's lookup3 hash of the name before it.
    for r in servantbuff_result.records:
        assert r["action_hash"] == ascii_key_hash(r["action_name"]), r
        assert r["servant_action_hash"] == ascii_key_hash(r["servant_action_name"]), r


def test_offset_rows_point_past_each_key(servantbuff_result: HandlerResult) -> None:
    # Checks the index: each row starts at key_dup, so the 4 bytes before it are the key.
    source = servantbuff_result.source
    rows = parse_bare_u32_offset_rows(source.file(_OFFSET_FILE))
    assert sorted(row.entry_id for row in rows) == sorted(r["key"] for r in servantbuff_result.records)
    for row in rows:
        key_at = row.offset - _KEY_SIZE
        assert int.from_bytes(source.data[key_at : row.offset], "little") == row.entry_id, row


def test_repeated_key_must_match() -> None:
    # count 1, key 1 repeated as 2.
    data = (1).to_bytes(4, "little") + (1).to_bytes(4, "little") + (2).to_bytes(4, "little")
    with pytest.raises(ValueError, match="repeats key 2, expected 1"):
        parse_servantbuff_records(data)
