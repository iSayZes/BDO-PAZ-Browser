from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from _dbss.servantupgrade.parser import (
    OFFSET_FILE,
    UPGRADE_SIZE,
    parse_servantupgrade_offset_records,
    parse_servantupgrade_records,
)


_COUNT_SIZE = 4


def _upgrades_by_size(source: CaseInput) -> int:
    """Upgrades the file holds: its size less the group count and one u32 per group, in 172-byte upgrades."""
    group_count = struct.unpack_from("<I", source.data, 0)[0]
    body = len(source.data) - _COUNT_SIZE - group_count * _COUNT_SIZE
    if body % UPGRADE_SIZE:
        raise AssertionError(f"{body} bytes of upgrades is not whole {UPGRADE_SIZE}-byte upgrades")
    return body // UPGRADE_SIZE


CASE = HandlerCase(
    handler_name="servantupgrade.dbss",
    data_file="servantupgrade.dbss",
    companion_files={
        OFFSET_FILE: OFFSET_FILE,
        "characterstaticoffset.dbss": "characterstaticoffset.dbss",
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "upgrade_name", "main_item_names", "sub_item_names"],
    internal_path="gamecommondata/binary/servantupgrade.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id",
                "upgrade_character_id",
                "group_index",
                "name",
                "upgrade_name",
                "main_items",
                "sub_items",
                "main_item_names",
                "sub_item_names",
                "has_character_row",
                "upgrade_has_character_row",
            ]
        ),
        DeclaredCountTest(declared=_upgrades_by_size),
        UserLanguageTest(fields=["name", "upgrade_name", "main_item_names", "sub_item_names"]),
        TargetTest(
            col="upgrade_character_id",
            value=31054,
            expected={"character_id": 31048, "name": "Epheria Caravel", "upgrade_name": "Epheria Carrack: Advance"},
        ),
        TargetTest(col="upgrade_character_id", value=31001, expected={"character_id": 31053, "name": "Bartali Sailboat"}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["character_id", "upgrade_character_id", "offset", "size"]),
    ],
)


@pytest.fixture(scope="module")
def upgrade_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_servantupgrade_dbss(spec: Any, upgrade_result: HandlerResult) -> None:
    upgrade_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_servantupgradeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_each_upgrade(upgrade_result: HandlerResult) -> None:
    # Checks the index: one row per upgrade, each 172 bytes at the upgrade's two ship IDs.
    source = upgrade_result.source
    rows = parse_servantupgrade_offset_records(source.file(OFFSET_FILE))
    pairs = sorted((r["character_id"], r["upgrade_character_id"]) for r in upgrade_result.records)
    assert sorted((row["character_id"], row["upgrade_character_id"]) for row in rows) == pairs
    for row in rows:
        assert row["size"] == UPGRADE_SIZE, row
        ships = struct.unpack_from("<HH", source.data, row["offset"])
        assert ships == (row["character_id"], row["upgrade_character_id"]), row


def test_every_upgrade_takes_four_gear_pieces(upgrade_result: HandlerResult) -> None:
    # Checks main_items: four filled slots, the gear the upgrade consumes.
    for r in upgrade_result.records:
        assert all(item["item_key"] for item in r["main_items"]), r["upgrade_character_id"]


def test_bytes_after_the_last_group_raise() -> None:
    with pytest.raises(ValueError, match="bytes follow group 0"):
        parse_servantupgrade_records(bytes(4) + b"\x00")
