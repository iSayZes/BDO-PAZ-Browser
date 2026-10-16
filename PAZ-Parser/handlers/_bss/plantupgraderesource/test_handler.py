from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _bss.planttown.parser import parse_planttown_records


CASE = HandlerCase(
    handler_name="plantupgraderesource.bss",
    data_file="plantupgraderesource.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["need_items_text"],
    internal_path="gamecommondata/binary/plantupgraderesource.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "group",
                "level",
                "key_group",
                "key_level",
                "need_time",
                "need_items",
                "need_items_text",
                "need_point",
                "need_money",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
    ],
)


@pytest.fixture(scope="module")
def plantupgraderesource_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantupgraderesource_bss(spec: Any, plantupgraderesource_result: HandlerResult) -> None:
    plantupgraderesource_result.check(spec)


def test_key_repeats_in_the_entry(plantupgraderesource_result: HandlerResult) -> None:
    """The map key and the struct's own (group, level) key agree on every entry."""
    assert all(
        (record["group"], record["level"]) == (record["key_group"], record["key_level"])
        for record in plantupgraderesource_result.records
    )


def test_each_group_has_levels_from_one(plantupgraderesource_result: HandlerResult) -> None:
    """Every level group holds the levels 1 to its highest without a gap."""
    levels: dict[int, set[int]] = {}
    for record in plantupgraderesource_result.records:
        levels.setdefault(record["group"], set()).add(record["level"])
    assert all(found == set(range(1, max(found) + 1)) for found in levels.values())


def test_town_upgrade_groups_are_entries(plantupgraderesource_result: HandlerResult) -> None:
    """Every `planttown.bss` upgrade resource key is a level group here."""
    groups = {record["group"] for record in plantupgraderesource_result.records}
    towns = parse_planttown_records(load_binary_fixture("planttown.bss"))
    assert {town["upgrade_resource_key"] for town in towns} <= groups
