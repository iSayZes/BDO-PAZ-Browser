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
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from .parser import (
    DIALOG_LINE_COUNT,
    FILE_NAME,
    OFFSET_FILE,
    knowledge_key_of,
    parse_intimacyrelation_records,
    parse_intimacyrelationoffset_rows,
)


_COUNT_SIZE = 4
_KEY = struct.Struct("<H")
_OFFSET_ROW_SIZE = 10
# Lillia in Velia: her discovery plays her cutscene and grants her own
# knowledge, on clients 1784 and 3483 and in the client 1784 NpcRelation sheet.
_LILLIA = 40604
_LILLIA_CUTSCENE = "CS_Velia_01_Lilia_0001.pas"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["npc_name", "covered_dialog", "discover_dialog"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "npc_key",
                "covered_dialog_kr",
                "discover_cutscene",
                "discover_dialog_kr",
                "discover_function",
                "discover_conditions",
                "discover_dialogs_kr",
                "unknown_discover_dialogs_kr_00",
                "npc_name",
                "knowledge_key",
                "knowledge_name",
                "covered_dialog",
                "discover_dialog",
                "discover_dialogs",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="npc_key", value=_LILLIA, expected={"discover_cutscene": _LILLIA_CUTSCENE}),
        RangeTest(col="unknown_discover_dialogs_kr_00", min_val=0, max_val=0),
        UserLanguageTest(fields=["npc_name", "knowledge_name", "covered_dialog", "discover_dialog", "discover_dialogs"]),
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
        SchemaTest(required_keys=["npc_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def intimacy_relation_result(request: Any) -> HandlerResult:
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
def test_intimacyrelation_dbss(spec: Any, intimacy_relation_result: HandlerResult) -> None:
    intimacy_relation_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_intimacyrelationoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_past_the_key_prefix() -> None:
    rows = parse_intimacyrelationoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, _KEY, lead=_KEY.size)
    assert not problems, problems


def test_a_condition_is_set_exactly_where_its_line_is() -> None:
    for record in parse_intimacyrelation_records(load_binary_fixture(FILE_NAME)):
        set_conditions = [bool(condition) for condition in record["discover_conditions"]]
        set_lines = [bool(line) for line in record["discover_dialogs_kr"]]
        assert set_conditions == set_lines, record["npc_key"]


def test_every_script_grants_a_knowledge() -> None:
    """A non-empty discover_function is a Pushknowledge call the handler reads a key from."""
    scripts = [r["discover_function"] for r in parse_intimacyrelation_records(load_binary_fixture(FILE_NAME))]
    unread = [script for script in scripts if script and knowledge_key_of(script) is None]
    assert not unread, unread


def test_every_cutscene_is_a_pas_file() -> None:
    records = parse_intimacyrelation_records(load_binary_fixture(FILE_NAME))
    wrong = [r["discover_cutscene"] for r in records if r["discover_cutscene"] and not r["discover_cutscene"].endswith(".pas")]
    assert not wrong, wrong


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    def text(value: str, *, wide: bool = True) -> bytes:
        return struct.pack("<Q", len(value)) + value.encode("utf-16-le" if wide else "ascii")

    lines = ["0", "", "", "", ""], ["안녕", "", "", "", ""]
    row = struct.pack("<H", 40604) + text("...") + text("CS_A.pas", wide=False) + text("반가워")
    row += text("Pushknowledge(388,0)") + b"".join(text(s) for s in lines[0]) + b"".join(text(s) for s in lines[1])
    row += struct.pack("<I", 0)
    data = struct.pack("<IH", 1, 40604) + row
    assert parse_intimacyrelation_records(data) == [
        {
            "npc_key": 40604,
            "covered_dialog_kr": "...",
            "discover_cutscene": "CS_A.pas",
            "discover_dialog_kr": "반가워",
            "discover_function": "Pushknowledge(388,0)",
            "discover_conditions": lines[0],
            "discover_dialogs_kr": lines[1],
            "unknown_discover_dialogs_kr_00": 0,
        }
    ]
    assert len(lines[0]) == DIALOG_LINE_COUNT
    assert knowledge_key_of("PushKnowledge(388,0);") == 388
    with pytest.raises(ValueError):
        parse_intimacyrelation_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_intimacyrelation_records(data[:-1])
