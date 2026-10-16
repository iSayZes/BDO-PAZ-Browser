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
_CALPHEON_TAB = 3
_CALPHEON = 2
# LOC type 12 `str_id4` 0 calls territory 13 `Alyaelli`; the tab name is 1.
_INNER_EDANIA_TAB = 13
_INNER_EDANIA = 13

CASE = HandlerCase(
    handler_name="dropuimaincategoryinfo.bss",
    data_file="dropuimaincategoryinfo.bss",
    companion_files={TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path="gamecommondata/binary/dropuimaincategoryinfo.bss",
    tests=[
        SchemaTest(required_keys=["key", "territory_key", "icon_texture", "name", "icon_path", "icon_region"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="key", value=_CALPHEON_TAB, expected={"territory_key": _CALPHEON, "name": "Calpheon"}),
        TargetTest(col="key", value=_INNER_EDANIA_TAB, expected={"territory_key": _INNER_EDANIA, "name": "Inner Edania"}),
    ],
)


@pytest.fixture(scope="module")
def tab_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_dropuimaincategoryinfo_bss(spec: Any, tab_result: HandlerResult) -> None:
    tab_result.check(spec)


def test_every_tab_icon_resolves_in_its_normal_state(tab_result: HandlerResult) -> None:
    missing = [r["icon_texture"] for r in tab_result.records if not r["icon_path"]]
    assert not missing, f"tab icons without a `_Normal` texture: {missing}"


def test_every_tab_has_a_name(tab_result: HandlerResult) -> None:
    unnamed = [r["key"] for r in tab_result.records if not r["name"]]
    assert not unnamed, f"tabs whose territory has no LOC type 12 name: {unnamed}"
