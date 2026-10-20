from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_pabr_u8_offset_rows
from _dbss.vehicleskill.parser import parse_vehicleskill_records


_OFFSET_FILE = "vehicleskilloffset.dbss"
# u8 unknown_00, then the u32 count.
_COUNT_OFFSET = 1
_ICON_FOLDER = "ui_texture/icon/new_icon/04_pc_skill/06_riding_skill/"

CASE = HandlerCase(
    handler_name="vehicleskill.dbss",
    data_file="vehicleskill.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "key_command", "description", "console_key_command"],
    internal_path="gamecommondata/binary/vehicleskill.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "name_kr",
                "name",
                "max_exp",
                "add_exp_for_check",
                "base_price",
                "add_mating_rate",
                "is_learn_from_item",
                "icon_path",
                "icon_file",
                "desc_kr",
                "key_command",
                "desc2_kr",
                "description",
                "console_desc_kr",
                "console_key_command",
                "training_skill_characters",
                "is_market_filter",
                "contents_group_key_hashes",
                "contents_groups",
                "unknown_contents_group_key_hashes_00",
                "condition_desc",
                "vehicle_skill_lock",
                "unknown_condition_desc_01",
                "skill_order",
                "need_life_level_for_auto_skill",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=header_count(offset=4, companion=_OFFSET_FILE)),
        RangeTest(col="is_learn_from_item", min_val=0, max_val=1),
        RangeTest(col="is_market_filter", min_val=0, max_val=1),
        RangeTest(col="vehicle_skill_lock", min_val=0, max_val=1),
        UserLanguageTest(fields=["name", "key_command", "description", "console_key_command"]),
        PaFieldTest(field="description"),
        TargetTest(
            col="key",
            value=1,
            expected={"name_kr": "뒷발차기", "icon_file": f"{_ICON_FOLDER}riding_skill_0004.dds"},
        ),
        # Sprint is one of the skills the horse stamina widget gates by life level.
        TargetTest(col="key", value=4, expected={"name_kr": "전력질주", "name": "Sprint"}),
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
        SchemaTest(required_keys=["key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
    ],
)


@pytest.fixture(scope="module")
def vehicleskill_result(request: Any) -> HandlerResult:
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
def test_vehicleskill_dbss(spec: Any, vehicleskill_result: HandlerResult) -> None:
    vehicleskill_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_vehicleskilloffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_tile_the_records(vehicleskill_result: HandlerResult) -> None:
    # Checks the walk against the index: same keys in order, each record ends
    # where the next starts, the first after the 5-byte header, the last at EOF.
    source = vehicleskill_result.source
    rows = parse_pabr_u8_offset_rows(source.file(_OFFSET_FILE))
    assert [row.entry_id for row in rows] == [r["key"] for r in vehicleskill_result.records]
    position = _COUNT_OFFSET + 4
    for row in rows:
        assert row.offset == position, row
        position += row.size
    assert position == len(source.data)


def test_contents_groups_resolve_to_keys(vehicleskill_result: HandlerResult) -> None:
    # Checks the hash field: every stored hash is the key_hash of a contents group key.
    for record in vehicleskill_result.records:
        assert record["contents_group_key_hashes"], record["key"]
        assert "0x" not in record["contents_groups"], record


def test_bytes_after_the_last_record_raise() -> None:
    # unknown_00, a count of 0, then one stray byte.
    with pytest.raises(ValueError, match="bytes follow record 0"):
        parse_vehicleskill_records(bytes(5) + b"\x00")
