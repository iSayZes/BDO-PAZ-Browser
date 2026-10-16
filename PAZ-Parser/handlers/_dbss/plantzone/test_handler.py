from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
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


_ALL_BASE_SPECIES = [0, 1, 2, 3, 4, 5]
# Zone 2050, Platerra Mountains lumbering: Elder Tree Timber, Bloody Tree Knot, Elder Tree Sap.
_LUMBERING_KEY = 1928
_LUMBERING_ITEMS = (4611, 5005, 5014)

PLANTZONE_CASE = HandlerCase(
    handler_name="plantzone.dbss",
    data_file="plantzone.dbss",
    companion_files={"plantzoneoffset.dbss": "plantzoneoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Node Name", "Produced Items"],
    internal_path="gamecommondata/binary/plantzone.dbss",
    lookup_indexes={IndexKind.PRODUCTION_ITEMS: {_LUMBERING_KEY: _LUMBERING_ITEMS}},
    tests=[
        SchemaTest(
            required_keys=[
                "record_id",
                "node_name",
                "work_ani_type",
                "work_animation",
                "production_key",
                "max_capacity_level",
                "worker_species",
                "worker_species_text",
                "item_keys",
                "items",
                "data_size",
            ]
        ),
        # The data file's own count; the parser walks the offset table's rows.
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="record_id",
            value=1030,
            expected={
                "node_name": "Fish Drying Yard 2",
                "production_key": 2017,
                "worker_species": _ALL_BASE_SPECIES,
                "worker_species_text": "Goblin, Human, Giant, Papu, Fadus, Dwarf",
                "data_size": 37,
            },
        ),
        # Dokkebi Forest excavation takes Dokkebi workers only.
        TargetTest(
            col="record_id",
            value=1807,
            expected={"worker_species": [6], "worker_species_text": "Dokkebi", "data_size": 32},
        ),
        # Balenos Specialties farms count max_capacity_level up from 1 to 7.
        TargetTest(
            col="record_id",
            value=110,
            expected={"production_key": 977, "max_capacity_level": 7},
        ),
        TargetTest(
            col="record_id",
            value=2050,
            expected={
                "work_animation": "Logging",
                "production_key": _LUMBERING_KEY,
                "item_keys": list(_LUMBERING_ITEMS),
                "items": ["Elder Tree Timber", "Bloody Tree Knot", "Elder Tree Sap"],
            },
        ),
        # Fish Drying Yard; not in the installed index, so no items (on the
        # client its subgroup 45018 is missing from itemsubgroupoffset.dbss).
        TargetTest(
            col="record_id",
            value=2051,
            expected={"production_key": 1929, "item_keys": None, "items": []},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="plantzoneoffset.dbss",
    data_file="plantzoneoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/plantzoneoffset.dbss",
    tests=[
        SchemaTest(required_keys=["record_id", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count()),
        # The first record follows the data file's u32 count.
        TargetTest(col="data_offset", value=4, expected={}),
        TargetTest(col="record_id", value=1807, expected={"data_size": 32}),
    ],
)


@pytest.fixture(scope="module")
def plantzone_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PLANTZONE_RESULT", None)
    if result is None:
        result = run_case(replace(PLANTZONE_CASE, tests=[]))
        request.module._PLANTZONE_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PLANTZONE_CASE.tests, ids=case_id)
def test_plantzone_dbss(spec: Any, plantzone_result: HandlerResult) -> None:
    plantzone_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_plantzoneoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)
