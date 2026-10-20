from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from _dbss.servantbuff.parser import servant_buff_skills
from _dbss.servantinteraction.parser import parse_servantinteraction_records


_OFFSET_FILE = "servantinteractionoffset.dbss"
_SERVANT_BUFF_FILE = "servantbuff.dbss"
# An offset row points at `character_id_dup`, past the u16 character_id.
_ID_SIZE = 2

CASE = HandlerCase(
    handler_name="servantinteraction.dbss",
    data_file="servantinteraction.dbss",
    companion_files={
        _OFFSET_FILE: _OFFSET_FILE,
        _SERVANT_BUFF_FILE: _SERVANT_BUFF_FILE,
        "characterstaticoffset.dbss": "characterstaticoffset.dbss",
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "buffs"],
    internal_path="gamecommondata/binary/servantinteraction.dbss",
    tests=[
        SchemaTest(required_keys=["character_id", "name", "cool_time", "buff_keys", "buffs", "has_character_row"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=0, companion=_OFFSET_FILE)),
        UserLanguageTest(fields=["buffs"]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["character_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def interaction_result(request: Any) -> HandlerResult:
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
def test_servantinteraction_dbss(spec: Any, interaction_result: HandlerResult) -> None:
    interaction_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_servantinteractionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_buff_key_is_a_servant_buff(interaction_result: HandlerResult) -> None:
    # Checks buff_keys against its target table: every key is a servantbuff.dbss key.
    buff_keys = set(servant_buff_skills(interaction_result.source.file(_SERVANT_BUFF_FILE)))
    for r in interaction_result.records:
        assert set(r["buff_keys"]) <= buff_keys, r


def test_offset_rows_point_past_each_character_id(interaction_result: HandlerResult) -> None:
    # Checks the index: each row starts at character_id_dup, so the 2 bytes before it are the ID.
    source = interaction_result.source
    rows = parse_bare_offset_rows(source.file(_OFFSET_FILE))
    assert sorted(row.entry_id for row in rows) == sorted(r["character_id"] for r in interaction_result.records)
    for row in rows:
        id_at = row.offset - _ID_SIZE
        assert int.from_bytes(source.data[id_at : row.offset], "little") == row.entry_id, row


def test_repeated_character_id_must_match() -> None:
    # count 1, character 1 repeated as 2, cool_time 0, no buffs.
    data = (1).to_bytes(4, "little") + b"\x01\x00\x02\x00" + bytes(16)
    with pytest.raises(ValueError, match="repeats character 2, expected 1"):
        parse_servantinteraction_records(data)
