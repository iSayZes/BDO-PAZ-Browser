from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.string_hash import ascii_key_hash
from _paac.layouts import LAYOUT_1, LAYOUT_2, ChartLayout
from _paac.parser import parse_chart
from _paac.records import chart_records
from tests.framework import HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case

_REQUIRED = [
    "action_hash", "action_name", "package_hash", "package_path", "animation",
    "unknown_first_values", "unknown_second_values", "unknown_third_values", "unknown_fourth_rows",
    "unknown_fifth_rows", "unknown_sixth_rows", "unknown_first_data", "unknown_second_data",
]

# A cash shop object: one package with elements, so the action names come from the file itself.
CASH_CASE = HandlerCase(
    handler_name="c0000_pearl_active.paac",
    data_file="c0000_pearl_active.paac",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="character/binaryactionchart/cash/c0000_pearl_active.paac",
    tests=[
        SchemaTest(required_keys=[*_REQUIRED, "unknown_parameters"]),
        TargetTest(col="action_name", value="WAIT", expected={"package_path": "cash/c0000_pearl_active"}),
        TargetTest(col="action_hash", value=ascii_key_hash("WAIT"), expected={"action_name": "WAIT"}),
    ],
)

# A class chart without the shared tables file: names stay mostly empty, every package reads.
CLASS_CASE = HandlerCase(
    handler_name="elfaction_noweapon.paac",
    data_file="elfaction_noweapon.paac",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="character/binaryactionchart/pc/3_pew/elfaction_noweapon.paac",
    tests=[
        SchemaTest(required_keys=_REQUIRED),
        TargetTest(
            col="package_hash",
            value=ascii_key_hash("pc/vehicle/riding_ground/horse/elfaction_ridinghorse"),
            expected={"package_path": "pc/vehicle/riding_ground/horse/elfaction_ridinghorse"},
        ),
    ],
)


def _result(request: Any, case: HandlerCase, slot: str) -> HandlerResult:
    result = getattr(request.module, slot, None)
    if result is None:
        result = run_case(replace(case, tests=[]))
        setattr(request.module, slot, result)
    return result


@pytest.fixture(scope="module")
def cash_result(request: Any) -> HandlerResult:
    return _result(request, CASH_CASE, "_CASH_RESULT")


@pytest.fixture(scope="module")
def class_result(request: Any) -> HandlerResult:
    return _result(request, CLASS_CASE, "_CLASS_RESULT")


@pytest.mark.parametrize("spec", CASH_CASE.tests, ids=case_id)
def test_c0000_pearl_active_paac(spec: Any, cash_result: HandlerResult) -> None:
    cash_result.check(spec)


@pytest.mark.parametrize("spec", CLASS_CASE.tests, ids=case_id)
def test_elfaction_noweapon_paac(spec: Any, class_result: HandlerResult) -> None:
    class_result.check(spec)


def test_every_package_key_is_the_hash_of_its_path(class_result: HandlerResult) -> None:
    assert all(ascii_key_hash(r["package_path"]) == r["package_hash"] for r in class_result.records)


def test_every_element_names_its_own_action(cash_result: HandlerResult) -> None:
    assert all(ascii_key_hash(r["action_name"]) == r["action_hash"] for r in cash_result.records)


# Synthetic charts: one package with one action and its element, every other list empty.
_STRINGS = ["", "WAIT", "Ani_Wait", "test/chart"]
_EMPTY, _WAIT, _ANI_WAIT, _PATH = range(len(_STRINGS))


def _head(layout: ChartLayout) -> bytes:
    body = struct.pack("<BQ", 1, 0)                      # uses_shared_tables, no animations
    body += struct.pack("<III", 0, 0, 0)                 # List Block
    body += struct.pack("<QQQQQ", 0, 0, 0, 0, 0)         # skeletons, pairs, mesh groups, effects, keyed entries
    body += struct.pack("<QIIBI", 0, _EMPTY, 0, 0, 0)    # unknown rows and the names after them
    body += bytes(layout.slot_count)                     # no slot
    body += struct.pack("<BQI", 0, 0, 0)                 # no hit parts, conditions or events
    return body


def _element(layout: ChartLayout) -> bytes:
    names = struct.pack("<13I", _WAIT, _ANI_WAIT, *(_EMPTY,) * 11)
    if layout.loader_element:
        return names + struct.pack("<IIIQQ", 0, _EMPTY, _EMPTY, 0, 0)
    return names + struct.pack("<I", _EMPTY) + bytes(12) + struct.pack("<IIQBQ", 0, 1, 1, 0x5F, 0)


def _chart(layout: ChartLayout) -> bytes:
    package = struct.pack("<IBBI", ascii_key_hash("test/chart"), 0, 0, _PATH) + struct.pack("<10I", *(_WAIT,) * 10)
    package += struct.pack("<H", 0) + bytes(layout.package_header_u8_count) + struct.pack("<I", 0)
    package += struct.pack("<QQQQ", 0, 0, 0, 1)
    package += struct.pack("<I6QIIQHQ", ascii_key_hash("WAIT"), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    package += _element(layout) + bytes(60)
    body = b"PABR" + struct.pack("<I", 1) + _head(layout) + struct.pack("<Q", 1) + package + struct.pack("<I", 1)
    table = struct.pack("<I", len(_STRINGS)) + b"".join(
        struct.pack("<BI", 0, len(text)) + text.encode("ascii") for text in _STRINGS
    )
    return body + table + struct.pack("<II", len(body), 0)


@pytest.mark.parametrize("layout", [LAYOUT_2, LAYOUT_1], ids=lambda layout: f"layout{layout.number}")
def test_each_layout_reads_its_own_chart(layout: ChartLayout) -> None:
    chart = parse_chart(_chart(layout), "test.paac")
    assert chart.layout == layout.number
    [record] = chart_records(chart, [])
    assert (record["action_name"], record["animation"], record["package_path"]) == ("WAIT", "Ani_Wait", "test/chart")


def test_a_chart_that_ends_early_fits_no_layout() -> None:
    data = _chart(LAYOUT_2)
    table_start = struct.unpack_from("<I", data, len(data) - 8)[0]
    # Drop 4 bytes of the package tail and move the trailer with them.
    broken = data[: table_start - 8] + data[table_start - 4 : -8] + struct.pack("<II", table_start - 4, 0)
    with pytest.raises(ValueError, match="Layout 2"):
        parse_chart(broken, "test.paac")
