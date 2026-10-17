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

from _common.texture_string import TEXTURE_STRING_COMBINE


# The rows start after the PABR magic with this count.
_COUNT_OFFSET = 4
_PARTY_ZONES = 1

CASE = HandlerCase(
    handler_name="dropuisubcategoryinfo.bss",
    data_file="dropuisubcategoryinfo.bss",
    companion_files={TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path="gamecommondata/binary/dropuisubcategoryinfo.bss",
    tests=[
        SchemaTest(required_keys=["key", "name_kr", "icon_texture", "name", "icon_path", "icon_region"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="key", value=_PARTY_ZONES, expected={"name_kr": "파티 사냥터", "name": "Party Zones"}),
    ],
)


@pytest.fixture(scope="module")
def category_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_dropuisubcategoryinfo_bss(spec: Any, category_result: HandlerResult) -> None:
    category_result.check(spec)


def test_every_filter_icon_resolves(category_result: HandlerResult) -> None:
    missing = [r["icon_texture"] for r in category_result.records if not r["icon_path"]]
    assert not missing, f"filter icons missing from {TEXTURE_STRING_COMBINE}: {missing}"
