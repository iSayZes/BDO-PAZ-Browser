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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)
from tests.fixtures import FIXTURES_DIR

from _bss.jewelgroupstaticstatus.parser import parse_jewel_group_records
from _bss.jewelspecialslotsgroupstaticstatus.slots import SPECIAL_SLOTS


_DATA_FILE = "jewelspecialslotsgroupstaticstatus.bss"
_GROUP_FILE = "jewelgroupstaticstatus.bss"
# The rows start after the PABR magic with this count.
_COUNT_OFFSET = 4
# `__eJewelSpecialSlotNecklace`, the necklace's Kharazad accessory slot.
_NECKLACE_SLOT = 17

CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={_GROUP_FILE: _GROUP_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["equipment", "group_labels"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    tests=[
        SchemaTest(required_keys=["slot", "groups", "equipment", "group_labels"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="slot", value=_NECKLACE_SLOT, expected={"equipment": "Necklace"}),
        UserLanguageTest(fields=["equipment", "group_labels"]),
    ],
)


@pytest.fixture(scope="module")
def slot_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_jewelspecialslotsgroupstaticstatus_bss(spec: Any, slot_result: HandlerResult) -> None:
    slot_result.check(spec)


def test_every_slot_is_a_special_slot(slot_result: HandlerResult) -> None:
    unknown = [r["slot"] for r in slot_result.records if r["slot"] not in SPECIAL_SLOTS]
    assert not unknown, f"slots outside __eJewelSpecialSlot*: {unknown}"


def test_every_group_is_a_crystal_group(slot_result: HandlerResult) -> None:
    known = {g["group"] for g in parse_jewel_group_records((FIXTURES_DIR / _GROUP_FILE).read_bytes())}
    missing = sorted({group for r in slot_result.records for group in r["groups"]} - known)
    assert not missing, f"groups missing from {_GROUP_FILE}: {missing}"
