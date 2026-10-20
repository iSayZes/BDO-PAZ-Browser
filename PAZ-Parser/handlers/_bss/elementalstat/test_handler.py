from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _bss.elementalstat.handler import aura_name
from _bss.elementalstat.parser import ELEMENT_TYPE_NAMES, parse_elementalstat


CASE = HandlerCase(
    handler_name="elementalstat.bss",
    data_file="elementalstat.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["aura"],
    internal_path="gamecommondata/binary/elementalstat.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "element_type",
                "aura",
                "ap_per_orb",
                "dp_per_orb",
                "stat_points_per_orb",
                "element_type_dup",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        # __eElementalStat_Sun, _Moon, _Land.
        RangeTest(col="element_type", min_val=0, max_val=len(ELEMENT_TYPE_NAMES) - 1),
        TargetTest(col="element_type", value=0, expected={"aura": "Sun Aura"}),
        TargetTest(col="element_type", value=1, expected={"aura": "Moon Aura"}),
        TargetTest(col="element_type", value=2, expected={"aura": "Earth Aura"}),
    ],
)


@pytest.fixture(scope="module")
def elementalstat_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_elementalstat_bss(spec: Any, elementalstat_result: HandlerResult) -> None:
    elementalstat_result.check(spec)


def test_each_row_repeats_its_key(elementalstat_result: HandlerResult) -> None:
    for record in elementalstat_result.records:
        assert record["element_type_dup"] == record["element_type"]


def test_each_aura_has_one_row(elementalstat_result: HandlerResult) -> None:
    types = [r["element_type"] for r in elementalstat_result.records]
    assert len(types) == len(set(types))


def test_the_rows_read_back() -> None:
    data = struct.pack("<I", 2) + struct.pack("<BIIIB", 1, 50, 100, 3, 1) + struct.pack("<BIIIB", 0, 7, 8, 9, 0)
    assert parse_elementalstat(data) == [
        {"element_type": 1, "ap_per_orb": 50, "dp_per_orb": 100, "stat_points_per_orb": 3, "element_type_dup": 1},
        {"element_type": 0, "ap_per_orb": 7, "dp_per_orb": 8, "stat_points_per_orb": 9, "element_type_dup": 0},
    ]


def test_a_type_outside_the_enum_shows_its_value() -> None:
    assert aura_name(7) == "7"


@pytest.mark.parametrize(
    "data",
    [
        b"\x01\x00",
        struct.pack("<I", 1) + bytes(13),
        struct.pack("<I", 1) + bytes(15),
    ],
    ids=["short_count", "short_row", "extra_bytes"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_elementalstat(data)
