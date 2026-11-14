from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.string_hash import ascii_key_hash
from _paac.element_fields import ELEMENT_PARAMETERS_SIZE
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


def _element(layout: ChartLayout, parameters: bytes = b"") -> bytes:
    names = struct.pack("<13I", _WAIT, _ANI_WAIT, *(_EMPTY,) * 11)
    if layout.loader_element:
        middle = struct.pack("<IIIQ", 0, _EMPTY, _EMPTY, 0)
    else:
        middle = struct.pack("<I", _EMPTY) + bytes(12) + struct.pack("<IIQB", 0, 1, 1, 0x5F)
    return names + middle + struct.pack("<Q", len(parameters)) + parameters


def _action(first_data: bytes, second_data: bytes) -> bytes:
    """`WAIT` with every list empty and the two data blocks given."""
    head = struct.pack("<I6QII", ascii_key_hash("WAIT"), 0, 0, 0, 0, 0, 0, 0, 0)
    return head + struct.pack("<Q", len(first_data)) + first_data + struct.pack("<HQ", 0, len(second_data)) + second_data


def _chart(
    layout: ChartLayout,
    *,
    with_element: bool = True,
    parameters: bytes = b"",
    first_data: bytes = b"",
    second_data: bytes = b"",
) -> bytes:
    flag = 0 if with_element else 1
    package = struct.pack("<IBBI", ascii_key_hash("test/chart"), flag, flag, _PATH) + struct.pack("<10I", *(_WAIT,) * 10)
    package += struct.pack("<H", 0) + bytes(layout.package_header_u8_count) + struct.pack("<I", 0)
    package += struct.pack("<QQQQ", 0, 0, 0, 1)
    package += _action(first_data, second_data)
    package += (_element(layout, parameters) if with_element else b"") + bytes(60)
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


def _parameters(**values: tuple[str, int, float]) -> bytes:
    """337 zero bytes of Element Parameters with `field=(format, offset, value)` written in."""
    block = bytearray(ELEMENT_PARAMETERS_SIZE)
    for kind, offset, value in values.values():
        struct.pack_into(f"<{kind}", block, offset, value)
    return bytes(block)


_PARAMETERS = _parameters(
    animation_speed=("f", 0x10, 1.25), skill_no=("i", 0xE8, 1234), apply_sp=("i", 0xF4, 100), sp_use_type=("B", 0x116, 1)
)


def test_layout_1_names_the_element_parameters() -> None:
    [record] = chart_records(parse_chart(_chart(LAYOUT_1, parameters=_PARAMETERS), "test.paac"), [])
    fields = ("animation_speed", "skill_no", "apply_sp", "sp_use_type")
    assert tuple(record[field] for field in fields) == (1.25, 1234, 100, 1)


def test_layout_2_keeps_the_element_parameters_as_hex() -> None:
    [record] = chart_records(parse_chart(_chart(LAYOUT_2, parameters=_PARAMETERS), "test.paac"), [])
    assert "apply_sp" not in record
    assert record["unknown_parameters"] == _PARAMETERS.hex()


_GROUP_KEY = 0x4F383718
_ACTION_DATA = struct.pack("<fffI", 150.0, 150.0, 30.0, 0)


def _linked_records(elements: list[dict]) -> list[dict]:
    """A Layout 1 class chart action that links to element 1 of `_GROUP_KEY`."""
    link = struct.pack("<IIII", 1, 0, 2, _GROUP_KEY) + bytes(3)
    chart = parse_chart(_chart(LAYOUT_1, with_element=False, first_data=_ACTION_DATA, second_data=link), "test.paac")
    return chart_records(chart, [], {_GROUP_KEY: elements})


def test_a_class_chart_action_reads_its_action_data_and_link() -> None:
    [record] = _linked_records([])
    fields = ("move_speed", "frame_count", "element_index", "weapon_type", "element_group_key")
    assert tuple(record[field] for field in fields) == (150.0, 30.0, 1, 2, _GROUP_KEY)


def test_a_class_chart_action_takes_the_element_its_link_points_at() -> None:
    elements = [
        {"action_name": "RUN", "animation": "Ani_Run", "apply_sp": 5},
        {"action_name": "WAIT", "animation": "Ani_Wait", "apply_sp": 7},
    ]
    [record] = _linked_records(elements)
    assert (record["action_name"], record["animation"], record["apply_sp"]) == ("WAIT", "Ani_Wait", 7)


def test_a_link_to_an_element_of_another_action_is_dropped() -> None:
    [record] = _linked_records([{"action_name": "RUN", "animation": "Ani_Run"}] * 2)
    assert record["animation"] == ""
    assert "apply_sp" not in record
