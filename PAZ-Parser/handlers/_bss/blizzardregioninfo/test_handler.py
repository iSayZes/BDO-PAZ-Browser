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

from .parser import ROW_SIZE, parse_blizzardregioninfo_records


CASE = HandlerCase(
    handler_name="blizzardregioninfo.bss",
    data_file="blizzardregioninfo.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Region"],
    internal_path="gamecommondata/binary/blizzardregioninfo.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "region_key",
                "region_name",
                "effect_spawn_percent_min",
                "effect_spawn_percent_max",
                "wind_x",
                "wind_y",
                "wind_z",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        # Rows join regioninfo.bss regions of the Mountain of Eternal Winter and Ulukita.
        TargetTest(col="key", value=1, expected={"region_key": 1126, "region_name": "Mountain of Eternal Winter"}),
        TargetTest(col="key", value=11, expected={"region_key": 1123, "region_name": "Bronte's Bolt"}),
    ],
)


@pytest.fixture(scope="module")
def blizzardregioninfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_blizzardregioninfo_bss(spec: Any, blizzardregioninfo_result: HandlerResult) -> None:
    blizzardregioninfo_result.check(spec)


def test_keys_are_unique(blizzardregioninfo_result: HandlerResult) -> None:
    keys = [record["key"] for record in blizzardregioninfo_result.records]
    assert len(keys) == len(set(keys))


def test_every_region_has_a_name(blizzardregioninfo_result: HandlerResult) -> None:
    unnamed = [r["region_key"] for r in blizzardregioninfo_result.records if not r["region_name"]]
    assert not unnamed, f"region keys without a LOC name: {unnamed}"


def test_spawn_chances_are_ordered_rates(blizzardregioninfo_result: HandlerResult) -> None:
    # The server loader of the Blizzard_Region_Table sheet rejects a chance
    # outside 1 to 100% (1,000,000) and a minimum above the maximum.
    bad = [
        r["key"]
        for r in blizzardregioninfo_result.records
        if not 1 <= r["effect_spawn_percent_min"] <= r["effect_spawn_percent_max"] <= 1_000_000
    ]
    assert not bad, f"keys with an out-of-range or reversed spawn chance: {bad}"


def test_rows_that_miss_the_string_table_are_rejected() -> None:
    # PABR, 1 row declared, but the trailer puts the string table right after the header.
    data = b"PABR" + (1).to_bytes(4, "little") + bytes(ROW_SIZE) + (0).to_bytes(4, "little")
    data += (8).to_bytes(4, "little") + bytes(4)
    with pytest.raises(ValueError, match="string table starts"):
        parse_blizzardregioninfo_records(data)
