from __future__ import annotations

import struct
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


_HEADER_SIZE = 8
_RECORD_HEADER_SIZE = 9
_ENTRY_SIZE = 16
_PPM_SCALE = 1_000_000

_ICON_DIR = "ui_texture/icon/new_icon/product_icon_png"
_SWEET_HONEY_WINE = 54030
_ORNETTES_DARK_HONEY_WINE = 18448


def _entry_rows() -> DeclaredCount:
    """Entry rows: the record bytes up to the trailer's end_of_records, less
    each declared record's 9-byte header, in 16-byte entries."""

    def read(source: CaseInput) -> int:
        raw = source.file(None)
        (count,) = struct.unpack_from("<I", raw, 4)
        end_of_records = struct.unpack_from("<I", raw, len(raw) - 8)[0]
        entry_bytes = end_of_records - _HEADER_SIZE - count * _RECORD_HEADER_SIZE
        if entry_bytes < 0 or entry_bytes % _ENTRY_SIZE:
            raise AssertionError(f"{count} records do not end on whole entries at 0x{end_of_records:X}")
        return entry_bytes // _ENTRY_SIZE

    return read


CASE = HandlerCase(
    handler_name="fairyupgraderate.bss",
    data_file="fairyupgraderate.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item"],
    internal_path="gamecommondata/binary/fairyupgraderate.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "step",
                "unknown_00",
                "success_cap_ppm",
                "item_id",
                "rate_ppm",
                "items_for_max",
                "unknown_0c",
                "chance_pct",
                "upgrade",
                "item_name",
                "icon_path",
            ],
        ),
        DeclaredCountTest(declared=_entry_rows()),
        # Rates are parts-per-million of a 100% cap.
        RangeTest(col="success_cap_ppm", min_val=_PPM_SCALE, max_val=_PPM_SCALE),
        RangeTest(col="rate_ppm", min_val=1, max_val=_PPM_SCALE),
        RangeTest(col="chance_pct", min_val=0.0, max_val=100.0),
        RangeTest(col="unknown_0c", min_val=0, max_val=0),
        TargetTest(col="step", value=0, expected={"upgrade": "Faint → Glimmering"}),
        TargetTest(col="step", value=1, expected={"upgrade": "Glimmering → Brilliant"}),
        TargetTest(col="step", value=2, expected={"upgrade": "Brilliant → Radiant"}),
        TargetTest(
            col="item_id",
            value=_SWEET_HONEY_WINE,
            expected={
                "item_name": "Sweet Honey Wine",
                "icon_path": f"{_ICON_DIR}/00054030.png",
            },
        ),
        TargetTest(
            col="item_id",
            value=_ORNETTES_DARK_HONEY_WINE,
            expected={
                "item_name": "Ornette's Dark Honey Wine",
                "icon_path": f"{_ICON_DIR}/00018448.png",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def fairyupgraderate_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyupgraderate_bss(
    spec: Any,
    fairyupgraderate_result: HandlerResult,
) -> None:
    fairyupgraderate_result.check(spec)
