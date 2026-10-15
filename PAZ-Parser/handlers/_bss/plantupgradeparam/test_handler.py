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
    handler_name="plantupgradeparam.bss",
    data_file="plantupgradeparam.bss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/plantupgradeparam.bss",
    tests=[
        SchemaTest(required_keys=["key", "param_key", "max_level"]),
        DeclaredCountTest(declared=header_count(offset=4)),
    ],
)


@pytest.fixture(scope="module")
def plantupgradeparam_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantupgradeparam_bss(spec: Any, plantupgradeparam_result: HandlerResult) -> None:
    plantupgradeparam_result.check(spec)


def test_key_repeats_in_the_entry(plantupgradeparam_result: HandlerResult) -> None:
    """The map key and the struct's own `_key` agree on every entry."""
    assert all(record["key"] == record["param_key"] for record in plantupgradeparam_result.records)


def test_town_upgrade_keys_are_entries(plantupgradeparam_result: HandlerResult) -> None:
    """Every warehouse and worker capacity key of `planttown.bss` is a key here."""
    keys = {record["key"] for record in plantupgradeparam_result.records}
    towns = parse_planttown_records(load_binary_fixture("planttown.bss"))
    used = {town["warehouse_upgrade_group_index"] for town in towns}
    used |= {town["worker_capacity_upgrade_group_index"] for town in towns}
    assert used <= keys
