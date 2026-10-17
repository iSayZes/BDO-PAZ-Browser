from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, SchemaTest, case_id, run_case

from _bss.pcgrowthdefaultcharacterkey.parser import parse_default_character_key
from _common.pabr_offset import PABR_MAGIC


CASE = HandlerCase(
    handler_name="pcgrowthdefaultcharacterkey.bss",
    data_file="pcgrowthdefaultcharacterkey.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path="gamecommondata/binary/pcgrowthdefaultcharacterkey.bss",
    tests=[SchemaTest(required_keys=["character_key", "name"])],
)


def _file(rows: bytes) -> bytes:
    """PABR, the rows, an empty string table and the trailer pointing at it."""
    rows_end = len(PABR_MAGIC) + len(rows)
    return PABR_MAGIC + rows + struct.pack("<III", 0, rows_end, 0)


@pytest.fixture(scope="module")
def key_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_pcgrowthdefaultcharacterkey_bss(spec: Any, key_result: HandlerResult) -> None:
    key_result.check(spec)


def test_the_file_holds_one_key(key_result: HandlerResult) -> None:
    assert len(key_result.records) == 1


def test_the_key_reads_back() -> None:
    assert parse_default_character_key(_file(struct.pack("<H", 47))) == [{"character_key": 47}]


@pytest.mark.parametrize(
    "data",
    [_file(struct.pack("<HH", 47, 48)), b"XXXX" + _file(struct.pack("<H", 47))[4:]],
    ids=["second_key", "bad_magic"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_default_character_key(data)
