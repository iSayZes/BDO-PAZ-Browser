from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.skill import skill_key, split_skill_key
from .handler import ExceptionSkillCoolTimeWidgetHandler
from .parser import FILE_NAME, OFFSET_FILE, ROW, parse_exceptionskillcooltimewidget_records


# PABR magic, then the u32 count; the bare index opens with its count.
_COUNT_OFFSET = 4
_OFFSET_COUNT_OFFSET = 0
_FIRST_ROW = 8
_KEY_FIELDS = ("skill_key_from", "skill_key_to", "skill_learn_check_key")
# The loader stores every skill number with level 1.
_LEVEL = 1
# Sorceress "Ultimate: Dark Flame" swaps to its Succession version on
# clients 1485, 1784 and 3474.
_DARK_FLAME = 94
_SORCERESS = 8
_ENTRY = PazEntry("", f"gamecommondata/binary/{FILE_NAME}", 0, 0, 0, 0, 0)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill_name_from", "skill_name_to", "skill_learn_check_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "skill_key_from",
                "class_mask",
                "skill_key_to",
                "skill_learn_check_key",
                "skill_no_from",
                "skill_name_from",
                "classes",
                "skill_no_to",
                "skill_name_to",
                "skill_learn_check_no",
                "skill_learn_check_name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["skill_name_from", "skill_name_to", "skill_learn_check_name"]),
        TargetTest(
            col="skill_no_from",
            value=_DARK_FLAME,
            expected={
                "skill_name_from": "Ultimate: Dark Flame",
                "class_mask": 1 << _SORCERESS,
                "classes": "Sorceress",
                "skill_name_to": "Succession: Ultimate: Dark Flame",
            },
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
        SchemaTest(required_keys=["skill_key_from", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_OFFSET_COUNT_OFFSET)),
        TargetTest(
            col="skill_key_from",
            value=skill_key(_DARK_FLAME, _LEVEL),
            expected={"skill_key_from": skill_key(_DARK_FLAME, _LEVEL), "size": ROW.size},
        ),
    ],
)


@pytest.fixture(scope="module")
def widget_result(request: Any) -> HandlerResult:
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
def test_exceptionskillcooltimewidget_dbss(spec: Any, widget_result: HandlerResult) -> None:
    widget_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_exceptionskillcooltimewidgetoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_key_is_a_level_1_skill_key(widget_result: HandlerResult) -> None:
    for record in widget_result.records:
        for field in _KEY_FIELDS:
            skill_no, level = split_skill_key(record[field])
            assert level == _LEVEL, (field, record)
            assert skill_no, (field, record)


def test_skill_keys_from_are_unique(widget_result: HandlerResult) -> None:
    keys = [r["skill_key_from"] for r in widget_result.records]
    assert len(keys) == len(set(keys))


def test_every_row_names_a_class(widget_result: HandlerResult) -> None:
    assert all(r["class_mask"] and r["classes"] for r in widget_result.records)


def test_every_offset_row_points_at_its_row() -> None:
    records = parse_exceptionskillcooltimewidget_records(load_binary_fixture(FILE_NAME))
    row_starts = {r["skill_key_from"]: _FIRST_ROW + index * ROW.size for index, r in enumerate(records)}
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: row.offset for row in rows} == row_starts


def _table(*rows: tuple[int, int, int, int]) -> bytes:
    """A PABR table of the given rows with an empty string table."""
    body = b"".join(ROW.pack(*row) for row in rows)
    rows_end = _FIRST_ROW + len(body)
    return b"PABR" + struct.pack("<I", len(rows)) + body + struct.pack("<III", 0, rows_end, 0)


_SAMPLE_ROW = (skill_key(_DARK_FLAME, _LEVEL), 1 << _SORCERESS, skill_key(4840, _LEVEL), skill_key(4594, _LEVEL))


def test_a_small_table_reads_back() -> None:
    assert parse_exceptionskillcooltimewidget_records(_table(_SAMPLE_ROW)) == [
        {
            "skill_key_from": skill_key(_DARK_FLAME, _LEVEL),
            "class_mask": 1 << _SORCERESS,
            "skill_key_to": skill_key(4840, _LEVEL),
            "skill_learn_check_key": skill_key(4594, _LEVEL),
        }
    ]


def test_a_missing_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_exceptionskillcooltimewidget_records(b"XXXX" + _table(_SAMPLE_ROW)[4:])


def test_rows_that_miss_the_string_table_raise() -> None:
    data = _table(_SAMPLE_ROW)
    with pytest.raises(ValueError):
        parse_exceptionskillcooltimewidget_records(data[:4] + struct.pack("<I", 2) + data[8:])


def test_bad_file_renders_an_error() -> None:
    handler = ExceptionSkillCoolTimeWidgetHandler()
    handler.lang = "en"
    records = handler.get_records(b"PABR", _ENTRY, {})
    assert "could not be parsed" in handler.render_records_page(records, 0, 50)
