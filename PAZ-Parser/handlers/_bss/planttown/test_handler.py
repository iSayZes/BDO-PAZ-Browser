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


CASE = HandlerCase(
    handler_name="planttown.bss",
    data_file="planttown.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Node Name"],
    internal_path="gamecommondata/binary/planttown.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "slot",
                "node_id",
                "node_name",
                "warehouse_upgrade_group_index",
                "worker_capacity_upgrade_group_index",
                "max_level",
                "upgrade_resource_key",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="node_id", value=1785, expected={"node_name": "Nampo's Moodle Village"}),
        TargetTest(col="node_id", value=1623, expected={"node_name": "Grána"}),
        TargetTest(col="node_id", value=1301, expected={"node_name": "Valencia City"}),
        TargetTest(col="node_id", value=301, expected={"node_name": "Heidel"}),
    ],
)


@pytest.fixture(scope="module")
def planttown_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_planttown_bss(spec: Any, planttown_result: HandlerResult) -> None:
    planttown_result.check(spec)
