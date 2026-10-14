from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.exploration.parser import parse_exploration_records
from _bss.itemmaingroup.parser import parse_itemmaingroup_records
from _common.pabr_offset import parse_pabr_offset_rows
from _common.vehicle_type import VEHICLE_TYPE_NAMES
from _dbss.characterfunction.layout import ITEM_GROUP_FIELDS, SLOTS
from _dbss.characterfunction.parser import CharacterFunctionRecord, parse_characterfunction_records
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

_OFFSET_FILE = "characterfunctionoffset.dbss"
# Igor Bartali represents Velia (node 1), the anchor exploration.bss uses too.
_VELIA_REPRESENTATIVE = 40017
_VELIA_NODE = 1
# eShopType_ItemMarket in the _shopType table of panel_dialog_main_all.luac.
_SHOP_TYPE_ITEM_MARKET = 14
# servant_type on records without a stable (past eServantType's members).
_NO_SERVANT_TYPE = 6

FUNCTION_CASE = HandlerCase(
    handler_name="characterfunction.dbss",
    data_file="characterfunction.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/characterfunction.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id", "name", "functions", "functions_text",
                "managed_node_keys", "managed_nodes", "managed_nodes_text",
                "town_node_keys", "town_nodes", "town_nodes_text",
                *(field for _, field in ITEM_GROUP_FIELDS),
                "vehicle_types", "vehicles", "vehicles_text",
            ]
        ),
        # The data file's own count; the parser walks the offset table's rows.
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="character_id",
            value=_VELIA_REPRESENTATIVE,
            expected={"name": "Igor Bartali", "town_node_keys": [_VELIA_NODE]},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["character_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # The first record follows the data file's u32 count and the record's u16 ID.
        TargetTest(col="offset", value=6, expected={}),
    ],
)


@pytest.fixture(scope="module")
def function_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_FUNCTION_RESULT", None)
    if result is None:
        result = run_case(replace(FUNCTION_CASE, tests=[]))
        request.module._FUNCTION_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", FUNCTION_CASE.tests, ids=case_id)
def test_characterfunction(spec: Any, function_result: HandlerResult) -> None:
    function_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_characterfunctionoffset(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def _parsed_records(function_result: HandlerResult) -> list[CharacterFunctionRecord]:
    source = function_result.source
    return parse_characterfunction_records(source.data, parse_pabr_offset_rows(source.file(_OFFSET_FILE)))


def test_has_button_flags_match_the_button_text(function_result: HandlerResult) -> None:
    """Where a slot has the flag, it is 1 exactly when the slot has button text."""
    records = _parsed_records(function_result)
    flagged = {spec.key for spec in SLOTS if any(field.name == "has_button" for field in spec.fields)}

    mismatches = [
        (record.character_id, slot.key)
        for record in records
        for slot in record.slots
        if slot.key in flagged and slot.fields["has_button"] != (1 if slot.name else 0)
    ]

    assert not mismatches


def test_node_lists_match_exploration(function_result: HandlerResult) -> None:
    """Managed nodes name this character as manager, town nodes as representative."""
    nodes = {node["node_key"]: node for node in parse_exploration_records(load_binary_fixture("exploration.bss"))}

    mismatches = [
        (record["character_id"], key)
        for record in function_result.records
        for field, owner in (("managed_node_keys", "manager_id"), ("town_node_keys", "representative_id"))
        for key in record[field]
        if nodes.get(key, {}).get(owner) != record["character_id"]
    ]

    assert not mismatches


def test_item_groups_are_itemmaingroup_groups(function_result: HandlerResult) -> None:
    """Every non-zero shop, sell and trade group is a group ID of itemmaingroup.bss."""
    group_ids = {group.group_id for group in parse_itemmaingroup_records(load_binary_fixture("itemmaingroup.bss"))}

    missing = [
        (record["character_id"], field, record[field])
        for record in function_result.records
        for _, field in ITEM_GROUP_FIELDS
        if record[field] and record[field] not in group_ids
    ]

    assert not missing


def test_vehicle_types_are_enum_members(function_result: HandlerResult) -> None:
    """Stable vehicle types are CppEnums.VehicleType values, and only stables store them."""
    records = _parsed_records(function_result)

    unknown = [
        (record.character_id, value)
        for record in records
        for value in record.vehicle_types
        if value not in VEHICLE_TYPE_NAMES
    ]
    without_stable = [record.character_id for record in records if record.vehicle_types and not record.slot("stable").name]

    assert not unknown
    assert not without_stable


def test_central_market_npcs_have_the_item_market_shop_type(function_result: HandlerResult) -> None:
    """A Central Market button comes with shop_type eShopType_ItemMarket, and only there."""
    mismatches = [
        record.character_id
        for record in _parsed_records(function_result)
        if bool(record.slot("central_market").name) != (record.head["shop_type"] == _SHOP_TYPE_ITEM_MARKET)
    ]

    assert not mismatches


def test_servant_type_is_set_exactly_on_stables(function_result: HandlerResult) -> None:
    """Records whose stable keeps vehicles have a servant type; the rest store the filler."""
    mismatches = [
        record.character_id
        for record in _parsed_records(function_result)
        if bool(record.vehicle_types) == (record.head["servant_type"] == _NO_SERVANT_TYPE)
    ]

    assert not mismatches
