from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _bss.manufacture.actions import ACTION_NAME_KEYS
from _bss.manufacture.parser import Material, Recipe, action_hash, parse_manufacture_records
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

_COMPANIONS = ("itemmaingroup.bss", "itemsubgroup.dbss", "itemsubgroupoffset.dbss")
_HEAT = "MANUFACTURE_HEAT"
# Melted Copper Shard, which Heating turns into Copper Ingot.
_MELTED_COPPER_SHARD = 4057

CASE = HandlerCase(
    handler_name="manufacture.bss",
    data_file="manufacture.bss",
    companion_files={name: name for name in _COMPANIONS},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["action_name", "materials", "result_items"],
    internal_path="gamecommondata/binary/manufacture.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "index", "action", "action_name", "material_keys", "material_counts", "materials",
                "result_group", "has_result_group", "result_item_keys", "result_items",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        UserLanguageTest(fields=["action_name", "materials", "result_items"]),
    ],
)


@pytest.fixture(scope="module")
def manufacture_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_manufacture_bss(spec: Any, manufacture_result: HandlerResult) -> None:
    manufacture_result.check(spec)


def test_known_actions_show_their_window_name(manufacture_result: HandlerResult) -> None:
    unnamed = {
        record["action"]
        for record in manufacture_result.records
        if record["action"] in ACTION_NAME_KEYS and record["action_name"] == record["action"]
    }
    assert not unnamed


def test_heating_melted_copper_shard_is_a_recipe(manufacture_result: HandlerResult) -> None:
    assert any(
        record["action"] == _HEAT and record["material_keys"][0] == _MELTED_COPPER_SHARD
        for record in manufacture_result.records
    )


def test_found_result_groups_list_items(manufacture_result: HandlerResult) -> None:
    found = [record for record in manufacture_result.records if record["has_result_group"]]
    assert found
    assert all(record["result_item_keys"] for record in found)
    assert not any(record["result_item_keys"] for record in manufacture_result.records if not record["has_result_group"])


def _ascii(text: str) -> bytes:
    payload = text.encode("ascii")
    return struct.pack("<BI", 0, len(payload)) + payload


def _row(action_index: int, stored_hash: int, result_group: int, materials: list[tuple[int, int]], first_key: int | None = None) -> bytes:
    key = materials[0][0] if first_key is None else first_key
    head = struct.pack("<I8xIIIBII", key, action_index, 700_000, stored_hash, 40, result_group, len(materials))
    return head + b"".join(struct.pack("<IQ", item_key, count) for item_key, count in materials)


def _file(rows: list[bytes], actions: list[str]) -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows)) + b"".join(rows)
    strings = struct.pack("<I", len(actions)) + b"".join(_ascii(action) for action in actions)
    return body + strings + struct.pack("<II", len(body), 0)


def test_action_hash_matches_the_stored_value() -> None:
    # The value row 0 of the client file stores for its action.
    assert action_hash(_HEAT) == 0x1B6F02F1


def test_parser_reads_rows_and_materials() -> None:
    actions = [_HEAT, "MANUFACTURE_DRY"]
    data = _file(
        [
            _row(0, action_hash(_HEAT), 12006, [(4057, 10)]),
            _row(1, action_hash("MANUFACTURE_DRY"), 9978, [(5, 1), (1 << 24 | 6, 300)]),
        ],
        actions,
    )

    assert parse_manufacture_records(data) == [
        Recipe(_HEAT, 12006, (Material(4057, 10),)),
        Recipe("MANUFACTURE_DRY", 9978, (Material(5, 1), Material(1 << 24 | 6, 300))),
    ]


def test_parser_rejects_a_hash_of_another_action() -> None:
    data = _file([_row(0, action_hash("MANUFACTURE_DRY"), 1, [(4057, 10)])], [_HEAT])
    with pytest.raises(ValueError):
        parse_manufacture_records(data)


def test_parser_rejects_an_action_past_the_table() -> None:
    data = _file([_row(1, action_hash(_HEAT), 1, [(4057, 10)])], [_HEAT])
    with pytest.raises(ValueError):
        parse_manufacture_records(data)


def test_parser_rejects_a_key_that_is_not_the_first_material() -> None:
    data = _file([_row(0, action_hash(_HEAT), 1, [(4057, 10)], first_key=4058)], [_HEAT])
    with pytest.raises(ValueError):
        parse_manufacture_records(data)


def test_parser_rejects_rows_that_miss_the_string_table() -> None:
    data = bytearray(_file([_row(0, action_hash(_HEAT), 1, [(4057, 10)])], [_HEAT]))
    # Claim no rows: the walk stops before the string table.
    struct.pack_into("<I", data, 4, 0)
    with pytest.raises(ValueError):
        parse_manufacture_records(bytes(data))
