from __future__ import annotations

import math
import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _bss.houseinfo.parser import FILE_NAME as HOUSEINFO_FILE
from _dbss.guildhouseinfo.house_rows import GUILDHOUSEINFO_PATH, HOUSEINFO_PATH
from _dbss.guildhouseinfo.parser import FILE_NAME as GUILDHOUSEINFO_FILE
from _dbss.houseinforeceipe.house_enums import HOUSE_USE_TYPE_NAMES
from .parser import (
    FILE_NAME,
    OFFSET_FILE,
    parse_houseinfoviewposition_records,
    parse_houseinfoviewpositionoffset_records,
    yaw_degrees,
)


_COUNT_SIZE = 4
# PABR magic and the u32 row count.
_PABR_HEADER_SIZE = 8
_ROW_SIZE = 32
_OFFSET_ROW_SIZE = 16
_KEY = struct.Struct("<HhI")
# Morning Light Nampo 1, a node house with a Ranch row; Velia Guild House.
_MORNING_LIGHT_NAMPO_1 = 3823
_RANCH = 3
_VELIA_GUILD_HOUSE = 2110

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={HOUSEINFO_FILE: HOUSEINFO_FILE, GUILDHOUSEINFO_FILE: GUILDHOUSEINFO_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "town"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key", "padding_02", "house_group_type", "position", "direction",
                "name", "house_path", "town", "house_group_type_name", "position_text", "yaw",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="house_group_type", min_val=0, max_val=len(HOUSE_USE_TYPE_NAMES) - 1),
        RangeTest(col="padding_02", min_val=0, max_val=0),
        TargetTest(
            col="character_key",
            value=_MORNING_LIGHT_NAMPO_1,
            expected={"house_group_type": _RANCH, "house_group_type_name": "Ranch", "house_path": HOUSEINFO_PATH},
        ),
        TargetTest(
            col="character_key",
            value=_VELIA_GUILD_HOUSE,
            expected={"name": "Velia Guild House", "house_path": GUILDHOUSEINFO_PATH, "town": "Velia"},
        ),
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
        SchemaTest(required_keys=["character_key", "padding_02", "house_group_type", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="character_key", value=_MORNING_LIGHT_NAMPO_1, expected={"house_group_type": _RANCH}),
    ],
)


@pytest.fixture(scope="module")
def view_result(request: Any) -> HandlerResult:
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
def test_houseinfoviewposition_dbss(spec: Any, view_result: HandlerResult) -> None:
    view_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_houseinfoviewpositionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_each_house_and_use_type_has_one_row(view_result: HandlerResult) -> None:
    keys = [(r["character_key"], r["house_group_type"]) for r in view_result.records]
    assert len(keys) == len(set(keys))


def test_every_house_has_a_house_row(view_result: HandlerResult) -> None:
    """Each key is a node house of houseinfo.bss or a guild house of guildhouseinfo.dbss."""
    assert all(r["house_path"] for r in view_result.records)


def test_every_direction_is_a_level_unit_vector(view_result: HandlerResult) -> None:
    for record in view_result.records:
        x, y, z = record["direction"]
        assert y == 0
        assert math.isclose(math.hypot(x, z), 1, abs_tol=1e-4), record["character_key"]


def test_offset_rows_point_at_the_row_with_their_key() -> None:
    data = load_binary_fixture(FILE_NAME)
    rows = parse_houseinfoviewpositionoffset_records(load_binary_fixture(OFFSET_FILE))
    row_count = len(parse_houseinfoviewposition_records(data))

    assert sorted(row["data_offset"] for row in rows) == [_PABR_HEADER_SIZE + i * _ROW_SIZE for i in range(row_count)]
    for row in rows:
        assert row["data_size"] == _ROW_SIZE
        stored = _KEY.unpack_from(data, row["data_offset"])
        assert stored == (row["character_key"], row["padding_02"], row["house_group_type"])


@pytest.mark.parametrize(
    ("direction", "yaw"),
    [
        ((-0.0, 0.0, -1.0), 0.0),
        # rotationYaw 84 and 199 of the client 1784 HouseViewPostion sheet.
        ((-0.9945219, 0.0, -0.1045284), 84.0),
        ((0.3255681, 0.0, 0.9455186), 199.0),
    ],
)
def test_the_direction_reads_back_as_the_sheet_yaw(direction: tuple[float, float, float], yaw: float) -> None:
    assert math.isclose(yaw_degrees(list(direction)), yaw, abs_tol=1e-3)
