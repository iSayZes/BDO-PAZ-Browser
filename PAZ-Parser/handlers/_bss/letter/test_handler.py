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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_letter_records


_TEXTURE_SUFFIX = ".dds"
_KEY_PREFIX = "PANEL_"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_key", "main_desc_string_index", "main_desc_string_key", "texture_path_index",
                "texture_path", "is_center_alignment", "item_name", "text",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="is_center_alignment", min_val=0, max_val=1),
        UserLanguageTest(fields=["item_name", "text"]),
    ],
)


@pytest.fixture(scope="module")
def letter_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_letter_bss(spec: Any, letter_result: HandlerResult) -> None:
    letter_result.check(spec)


def test_every_row_names_a_text_key_and_a_texture() -> None:
    for record in parse_letter_records(load_binary_fixture(FILE_NAME)):
        assert record["main_desc_string_key"].startswith(_KEY_PREFIX), record["item_key"]
        assert record["texture_path"].lower().endswith(_TEXTURE_SUFFIX), record["item_key"]


def test_every_letter_has_its_text(letter_result: HandlerResult) -> None:
    missing = [record["item_key"] for record in letter_result.records if not record["text"]]
    assert not missing, missing


def _pstr(value: str) -> bytes:
    raw = value.encode("utf-16-le")
    return struct.pack("<BI", 1, len(raw)) + raw


def test_parse_reads_the_strings_by_index() -> None:
    rows = struct.pack("<IIIB", 65950, 1, 0, 1)
    strings = struct.pack("<I", 2) + _pstr("Combine/ETC/Letter.dds") + _pstr("PANEL_LETTER_X")
    data = b"PABR" + struct.pack("<I", 1) + rows + strings + struct.pack("<II", 8 + len(rows), 0)

    (record,) = parse_letter_records(data)

    assert record["main_desc_string_key"] == "PANEL_LETTER_X"
    assert record["texture_path"] == "Combine/ETC/Letter.dds"
    assert record["is_center_alignment"] == 1
