from __future__ import annotations

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
    header_count,
    run_case,
)

from .parser import FILE_NAME, WAYPOINT_SLOTS, parse_deliverer_records


# CppEnums.DelivererType: NotDeliverer 0 to OfferingCarrier 5.
_TYPE_MAX = 5
_WAGON = 1
_MODEL_SUFFIX = ".pam"
# Velia Freight Wagon.
_VELIA_FREIGHT_WAGON = 522

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key", "character_key_dup", "delivery_route", "load_age", "fee", "object_file_index",
                "object_file", "waypoint_name_indexes", "waypoint_names", "deliverer_type", "unknown_69",
                "name", "waypoints_text", "deliverer_type_name",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="deliverer_type", min_val=0, max_val=_TYPE_MAX),
        TargetTest(
            col="character_key",
            value=_VELIA_FREIGHT_WAGON,
            expected={"name": "Velia Freight Wagon", "deliverer_type": _WAGON, "deliverer_type_name": "Wagon"},
        ),
    ],
)


@pytest.fixture(scope="module")
def deliverer_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_deliverer_bss(spec: Any, deliverer_result: HandlerResult) -> None:
    deliverer_result.check(spec)


def test_every_carrier_has_a_model_and_a_route() -> None:
    for record in parse_deliverer_records(load_binary_fixture(FILE_NAME)):
        assert record["character_key_dup"] == record["character_key"]
        assert record["object_file"].lower().endswith(_MODEL_SUFFIX), record["character_key"]
        assert record["waypoint_names"], record["character_key"]


def _pstr(value: str) -> bytes:
    raw = value.encode("utf-16-le")
    return struct.pack("<BI", 1, len(raw)) + raw


def test_parse_drops_the_empty_waypoint_slots() -> None:
    empty, model, first, second = 0, 1, 2, 3
    slots = [first, second] + [empty] * (WAYPOINT_SLOTS - 2)
    row = struct.pack(f"<HHIIqI{WAYPOINT_SLOTS}IBB", 522, 522, 1, 30, 10, model, *slots, _WAGON, 0)
    strings = struct.pack("<I", 4) + _pstr("") + _pstr("WorldMap/WorldMap_Cart.pam") + _pstr("loopline_1") + _pstr("loopline_70")
    data = b"PABR" + struct.pack("<I", 1) + row + strings + struct.pack("<II", 8 + len(row), 0)

    (record,) = parse_deliverer_records(data)

    assert record["object_file"] == "WorldMap/WorldMap_Cart.pam"
    assert record["waypoint_names"] == ["loopline_1", "loopline_70"]
    assert record["deliverer_type"] == _WAGON
