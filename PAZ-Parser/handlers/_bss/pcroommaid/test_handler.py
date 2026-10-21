from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

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

from _bss.pcroommaid.handler import maid_key_cell, maid_row_keys
from _bss.pcroommaid.parser import parse_pcroommaid
from _common.pabr_offset import parse_bare_offset_rows
from _dbss.maid.parser import FILE_NAME as MAID_FILE, OFFSET_FILE as MAID_OFFSET_FILE, parse_maid_records


CASE = HandlerCase(
    handler_name="pcroommaid.bss",
    data_file="pcroommaid.bss",
    # maid.dbss is not read by the handler; the link check below uses it.
    companion_files={MAID_OFFSET_FILE: MAID_OFFSET_FILE, MAID_FILE: MAID_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path="gamecommondata/binary/pcroommaid.bss",
    tests=[
        SchemaTest(required_keys=["character_key", "name", "has_maid_row"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        # The first PC room maid pair (client 1230 onward): warehouse and marketplace.
        TargetTest(col="character_key", value=18964, expected={"name": "[Oasis] Fairy Chiara"}),
        TargetTest(col="character_key", value=18967, expected={"name": "[Oasis] Ethan the Butler"}),
    ],
)


@pytest.fixture(scope="module")
def pcroommaid_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_pcroommaid_bss(spec: Any, pcroommaid_result: HandlerResult) -> None:
    pcroommaid_result.check(spec)


def test_keys_are_maid_rows_in_maid_order(pcroommaid_result: HandlerResult) -> None:
    """Every key is a maid.dbss row, listed in the order maidoffset.dbss lists the rows."""
    maid_keys = [row.entry_id for row in parse_bare_offset_rows(pcroommaid_result.source.file(MAID_OFFSET_FILE))]
    keys = [r["character_key"] for r in pcroommaid_result.records]
    assert set(keys) <= set(maid_keys)
    assert keys == [key for key in maid_keys if key in set(keys)]


def test_every_key_links_to_its_maid_row(pcroommaid_result: HandlerResult) -> None:
    """Each key cell opens maid.dbss on a row with that character_key and pc_room_type set."""
    maid_rows = {r["character_key"]: r for r in parse_maid_records(pcroommaid_result.source.file(MAID_FILE))}
    for record in pcroommaid_result.records:
        key = record["character_key"]
        assert record["has_maid_row"], key
        assert maid_rows[key]["pc_room_type"], key
        cell = maid_key_cell(key, record["has_maid_row"])
        assert 'data-action="open-record"' in cell
        assert f'data-path="gamecommondata/binary/{MAID_FILE}"' in cell
        assert f'data-field="character_key" data-value="{key}"' in cell


def test_a_key_without_a_maid_row_is_plain_text() -> None:
    assert maid_key_cell(18964, False) == "18964"


def test_a_missing_maid_offset_file_keeps_the_links() -> None:
    assert maid_row_keys({}) is None


def test_a_broken_maid_offset_file_names_it() -> None:
    with pytest.raises(ValueError, match=MAID_OFFSET_FILE):
        maid_row_keys({MAID_OFFSET_FILE: b"\x01\x00"})


def test_the_keys_read_back() -> None:
    data = struct.pack("<IHH", 2, 18965, 18964)
    assert parse_pcroommaid(data) == [{"character_key": 18965}, {"character_key": 18964}]


@pytest.mark.parametrize(
    "data",
    [b"\x02\x00", struct.pack("<IH", 2, 18964), struct.pack("<IHH", 1, 18964, 18965)],
    ids=["short_count", "missing_key", "extra_bytes"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_pcroommaid(data)
