from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from _dbss.enchantstaticstatus.parser import parse_enchantstaticstatusoffset_records
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

from .parser import FILE_NAME


# The Kzarka main weapon enchant keys (enchantstaticstatus_dbss.md): longsword,
# longbow, amulet and the 662 family that holds Kzarka Gauntlet.
_KZARKA_GROUP = [62, 262, 462, 662]
_KZARKA_GAUNTLET_KEY = 662
_KZARKA_GAUNTLET_ITEM = 11210
_ESS_OFFSET_FILE = "enchantstaticstatusoffset.dbss"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Items"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    # Only the link the TargetTest checks; the real index is built from itemenchant.dbss.
    lookup_indexes={IndexKind.ENCHANT_KEY_ITEMS: {_KZARKA_GAUNTLET_KEY: (_KZARKA_GAUNTLET_ITEM,)}},
    tests=[
        SchemaTest(
            required_keys=[
                "enchant_key",
                "unknown_04",
                "group_count",
                "group_enchant_keys",
                "item_ids",
                "item_names",
                "item_count",
                "group_item_ids",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(
            col="enchant_key",
            value=_KZARKA_GAUNTLET_KEY,
            expected={
                "group_enchant_keys": _KZARKA_GROUP,
                "item_ids": [_KZARKA_GAUNTLET_ITEM],
                "item_names": ["Kzarka Gauntlet"],
                "group_item_ids": [_KZARKA_GAUNTLET_ITEM],
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def group_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemviewstackenchantgroupss_bss(spec: Any, group_result: HandlerResult) -> None:
    group_result.check(spec)


def test_each_row_lists_its_own_key(group_result: HandlerResult) -> None:
    bad = [
        r["enchant_key"]
        for r in group_result.records
        if r["enchant_key"] not in r["group_enchant_keys"]
        or len(r["group_enchant_keys"]) != r["group_count"]
        or r["unknown_04"] != r["group_count"]
    ]
    assert not bad, f"rows whose group misses the key or whose counts disagree: {bad[:10]}"


def test_every_group_key_has_a_row_with_the_same_group(group_result: HandlerResult) -> None:
    groups = {r["enchant_key"]: set(r["group_enchant_keys"]) for r in group_result.records}
    assert len(groups) == len(group_result.records), "an enchant key has two rows"
    bad = [
        (key, member)
        for key, group in groups.items()
        for member in group
        if groups.get(member) != group
    ]
    assert not bad, f"group keys without a matching row: {bad[:10]}"


def test_every_key_is_an_enchantstaticstatus_key(group_result: HandlerResult) -> None:
    known = {row["enchant_key"] for row in parse_enchantstaticstatusoffset_records(load_binary_fixture(_ESS_OFFSET_FILE))}
    missing = sorted({r["enchant_key"] for r in group_result.records} - known)
    assert not missing, f"keys without enchantstaticstatus.dbss data: {missing[:10]}"
