from __future__ import annotations

import math
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _bss.usernpc.parser import parse_usernpc_records
from _common.pabr_strings import read_string_table


# Highest class type the u8 can hold; the playable ones run 0 to 35.
_MAX_CLASS_TYPE = 0xFF

CASE = HandlerCase(
    handler_name="usernpc.bss",
    data_file="usernpc.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path="gamecommondata/binary/usernpc.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "player_character_no",
                "pos_x",
                "pos_y",
                "pos_z",
                "direction",
                "action_ref",
                "action_name",
                "class_type",
                "class_name",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="class_type", min_val=0, max_val=_MAX_CLASS_TYPE),
    ],
)


@pytest.fixture(scope="module")
def usernpc_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_usernpc_bss(spec: Any, usernpc_result: HandlerResult) -> None:
    usernpc_result.check(spec)


def test_every_action_ref_points_into_the_string_table(usernpc_result: HandlerResult) -> None:
    strings = read_string_table(usernpc_result.source.data)

    for record in usernpc_result.records:
        assert 0 <= record["action_ref"] < len(strings)
        assert record["action_name"] == strings[record["action_ref"]]


def test_positions_and_directions_are_finite(usernpc_result: HandlerResult) -> None:
    for record in usernpc_result.records:
        assert all(math.isfinite(record[field]) for field in ("pos_x", "pos_y", "pos_z", "direction"))


def test_a_row_size_change_is_rejected(usernpc_result: HandlerResult) -> None:
    """A count one higher than the rows before the string table is a layout change."""
    data = bytearray(usernpc_result.source.data)
    data[4:8] = (int.from_bytes(data[4:8], "little") + 1).to_bytes(4, "little")

    with pytest.raises(ValueError, match="string table starts"):
        parse_usernpc_records(bytes(data))
