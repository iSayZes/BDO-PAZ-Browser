from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.regioninfo.parser import parse_regioninfo_records
from tests.fixtures import load_binary_fixture
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


CASE = HandlerCase(
    handler_name="regioninfo_linkandcheckvalid2.bss",
    data_file="regioninfo_linkandcheckvalid2.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Region"],
    internal_path="gamecommondata/binary/regioninfo_linkandcheckvalid2.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "region_key",
                "region_name",
                "link_count",
                "pc_delivery_region_keys",
                "linked_regions",
                "unknown_06",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="region_key", value=5, expected={"region_name": "Velia"}),
        TargetTest(col="region_key", value=77, expected={"region_name": "Calpheon City"}),
    ],
)


@pytest.fixture(scope="module")
def region_link_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_region_link(spec: Any, region_link_result: HandlerResult) -> None:
    region_link_result.check(spec)


def _links(result: HandlerResult) -> dict[int, list[int]]:
    return {record["region_key"]: record["pc_delivery_region_keys"] for record in result.records}


def test_one_record_per_region(region_link_result: HandlerResult) -> None:
    """Same region keys as regioninfo.bss, each once."""
    regions = parse_regioninfo_records(load_binary_fixture("regioninfo.bss"))
    keys = [record["region_key"] for record in region_link_result.records]
    assert len(keys) == len(set(keys))
    assert set(keys) == {region["region_key"] for region in regions}


def test_lists_match_regioninfo(region_link_result: HandlerResult) -> None:
    """Each list repeats the region's pc_delivery_region_keys in regioninfo.bss, in order."""
    regions = parse_regioninfo_records(load_binary_fixture("regioninfo.bss"))
    links = _links(region_link_result)
    for region in regions:
        assert links[region["region_key"]] == region["pc_delivery_region_keys"], region["region_key"]


def test_links_include_self_and_are_mutual(region_link_result: HandlerResult) -> None:
    links = _links(region_link_result)
    for key, linked in links.items():
        if not linked:
            continue
        assert key in linked, f"region {key} does not list itself"
        for other in linked:
            assert key in links[other], f"region {key} links {other} but not back"
