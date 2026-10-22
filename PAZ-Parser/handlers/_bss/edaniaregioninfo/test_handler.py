from __future__ import annotations

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

from .parser import EDANIA_REGION_NAMES, ROW_SIZE, parse_edaniaregioninfo_records


CASE = HandlerCase(
    handler_name="edaniaregioninfo.bss",
    data_file="edaniaregioninfo.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Castle"],
    internal_path="gamecommondata/binary/edaniaregioninfo.bss",
    tests=[
        SchemaTest(required_keys=["edania_region", "castle_name", "map_color", "unknown_04"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # __eEdaniaRegion values plus _Count, the "no region" value.
        RangeTest(col="edania_region", min_val=0, max_val=len(EDANIA_REGION_NAMES)),
        # Orbita and Tenebraum swap their castle name keys (4 and 3).
        TargetTest(col="edania_region", value=0, expected={"castle_name": "Aetherion Castle"}),
        TargetTest(col="edania_region", value=2, expected={"castle_name": "Orbita Castle"}),
        TargetTest(col="edania_region", value=3, expected={"castle_name": "Tenebraum Castle"}),
        TargetTest(col="edania_region", value=len(EDANIA_REGION_NAMES), expected={"castle_name": ""}),
    ],
)


@pytest.fixture(scope="module")
def edaniaregioninfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_edaniaregioninfo_bss(spec: Any, edaniaregioninfo_result: HandlerResult) -> None:
    edaniaregioninfo_result.check(spec)


def test_edania_regions_are_unique(edaniaregioninfo_result: HandlerResult) -> None:
    regions = [record["edania_region"] for record in edaniaregioninfo_result.records]
    assert len(regions) == len(set(regions))


def test_every_castle_has_a_name(edaniaregioninfo_result: HandlerResult) -> None:
    castles = [r for r in edaniaregioninfo_result.records if r["edania_region"] < len(EDANIA_REGION_NAMES)]
    assert castles and all(r["castle_name"] for r in castles)


def test_rows_that_miss_the_string_table_are_rejected() -> None:
    # PABR, 1 row declared, but the trailer puts the string table right after the header.
    data = b"PABR" + (1).to_bytes(4, "little") + bytes(ROW_SIZE) + (0).to_bytes(4, "little")
    data += (8).to_bytes(4, "little") + bytes(4)
    with pytest.raises(ValueError, match="string table starts"):
        parse_edaniaregioninfo_records(data)
