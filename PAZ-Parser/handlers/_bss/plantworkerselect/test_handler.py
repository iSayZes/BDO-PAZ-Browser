from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _common.worker import WorkerGrade


_ICON_FOLDER = "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/"
_ENTRY_SIZE = 0x10


def _entry_rows() -> DeclaredCount:
    """Entries in the file: its bytes after the group count and each group's
    u32 entry count, 16 bytes per entry."""

    def read(source: CaseInput) -> int:
        raw = source.file(None)
        group_count = int.from_bytes(raw[:4], "little")
        entry_bytes = len(raw) - 4 - 4 * group_count
        if entry_bytes < 0 or entry_bytes % _ENTRY_SIZE:
            raise AssertionError(f"{len(raw)} bytes do not hold {group_count} groups of 16-byte entries")
        return entry_bytes // _ENTRY_SIZE

    return read


CASE = HandlerCase(
    handler_name="plantworkerselect.bss",
    data_file="plantworkerselect.bss",
    companion_files={"plantworker.bss": "plantworker.bss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["SelectionName", "WorkerName"],
    internal_path="gamecommondata/binary/plantworkerselect.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "group",
                "row",
                "entry_count",
                "selection_id",
                "selection_name",
                "worker_id",
                "worker_name",
                "worker_grade",
                "hire_cost",
                "worker_icon_path",
                "worker_move_speed",
                "worker_stamina",
                "worker_luck",
                "worker_base_work_speed",
                "unknown_04",
                "unknown_0c",
            ],
        ),
        DeclaredCountTest(declared=_entry_rows()),
        RangeTest(col="unknown_04", min_val=0, max_val=0),
        RangeTest(col="unknown_0c", min_val=0, max_val=0),
        RangeTest(col="worker_grade", min_val=WorkerGrade.NAIVE, max_val=WorkerGrade.ARTISAN),
        TargetTest(col="selection_id", value=77, expected={"selection_name": "Calpheon City"}),
        TargetTest(col="selection_id", value=735, expected={"selection_name": "Grána"}),
        # Worker names and icons come from the plantworker.bss companion.
        TargetTest(
            col="worker_id",
            value=7501,
            expected={
                "worker_name": "Naive Worker",
                "worker_grade": WorkerGrade.NAIVE,
                "worker_icon_path": f"{_ICON_FOLDER}Worker_Giant01.dds",
            },
        ),
        TargetTest(
            col="worker_id",
            value=7571,
            expected={
                "worker_name": "Artisan Giant Worker",
                "worker_grade": WorkerGrade.ARTISAN,
                "worker_icon_path": f"{_ICON_FOLDER}Worker_Giant04.dds",
            },
        ),
        # O'draxxia is the only town that offers this Dwarf worker.
        TargetTest(
            col="worker_id",
            value=8020,
            expected={
                "selection_id": 955,
                "selection_name": "O'draxxia",
                "worker_name": "Dwarf Worker",
                "worker_grade": WorkerGrade.BASE,
                "worker_icon_path": f"{_ICON_FOLDER}Worker_Odilita_Dwarf01.dds",
            },
        ),
        TargetTest(
            col="worker_id",
            value=8047,
            expected={
                "worker_name": "Dokkebi Worker",
                "worker_icon_path": f"{_ICON_FOLDER}Morning_Dokev01.dds",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def plantworkerselect_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantworkerselect_bss(
    spec: Any,
    plantworkerselect_result: HandlerResult,
) -> None:
    plantworkerselect_result.check(spec)
