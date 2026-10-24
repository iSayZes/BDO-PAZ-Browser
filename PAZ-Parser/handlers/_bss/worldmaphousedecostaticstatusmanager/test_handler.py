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

from _bss.worldmaphousedecostaticstatusmanager.parser import FILE_NAME, KEY_FIELD, parse_worldmaphousedeco_records


# Character 2008 is the guild command post (지휘소).
_COMMAND_POST = 2008

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key",
                "character_key_dup",
                "world_map_object_file",
                "object_change_level",
                "name",
                "has_character_row",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col=KEY_FIELD, value=_COMMAND_POST, expected={"character_key_dup": _COMMAND_POST}),
    ],
)


@pytest.fixture(scope="module")
def house_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_worldmaphousedecostaticstatusmanager_bss(spec: Any, house_result: HandlerResult) -> None:
    house_result.check(spec)


def test_keys_are_unique(house_result: HandlerResult) -> None:
    keys = [r[KEY_FIELD] for r in house_result.records]
    assert len(keys) == len(set(keys))


def test_every_row_names_a_model(house_result: HandlerResult) -> None:
    assert all(r["world_map_object_file"] for r in house_result.records)


def _row(key: int, model: str, level: int) -> bytes:
    raw = model.encode("ascii")
    return struct.pack("<HHQ", key, key, len(raw)) + raw + struct.pack("<I", level)


def test_parse_reads_each_row() -> None:
    data = struct.pack("<I", 2) + _row(2008, "Worldmap_Guild_Tent_A", 1) + _row(2009, "B", 2)

    records = parse_worldmaphousedeco_records(data)

    assert records[0] == {
        "character_key": 2008,
        "character_key_dup": 2008,
        "world_map_object_file": "Worldmap_Guild_Tent_A",
        "object_change_level": 1,
    }
    assert records[1]["object_change_level"] == 2


def test_parse_rejects_bytes_after_the_last_row() -> None:
    data = struct.pack("<I", 1) + _row(2008, "A", 1) + b"\x00"
    with pytest.raises(ValueError):
        parse_worldmaphousedeco_records(data)
