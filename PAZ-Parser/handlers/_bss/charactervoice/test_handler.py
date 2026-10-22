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

from _bss.charactervoice.parser import APPEARANCE_TYPES, FILE_NAME, parse_charactervoice_records


# PABR magic, then the u32 record count.
_COUNT_OFFSET = 4
_WARRIOR = 1
_VOICE_PREFIX = "PC_VCE_"

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
                "voice_types",
                "voice_names",
                "voice_count",
                "name",
                "has_character_row",
                "voices_0_text",
                "voices_1_text",
                "voice_count_0",
                "voice_count_1",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="character_key", value=_WARRIOR, expected={"name": "Warrior"}),
    ],
)


@pytest.fixture(scope="module")
def voice_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_charactervoice_bss(spec: Any, voice_result: HandlerResult) -> None:
    voice_result.check(spec)


def test_keys_are_unique(voice_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in voice_result.records]
    assert len(keys) == len(set(keys))


def test_every_voice_index_names_a_voice(voice_result: HandlerResult) -> None:
    # Checks voice_types: indexes into the string table, which holds the voice names.
    for record in voice_result.records:
        assert len(record["voice_names"]) == APPEARANCE_TYPES
        for names in record["voice_names"]:
            assert all(name.startswith(_VOICE_PREFIX) for name in names), record["character_key"]


def test_every_character_has_a_first_voice(voice_result: HandlerResult) -> None:
    assert all(r["voice_names"][0] for r in voice_result.records)


def _file(rows: list[tuple[int, list[int], list[int], int, int]], strings: list[str]) -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows))
    for key, first, second, count_0, count_1 in rows:
        body += struct.pack("<H", key)
        for indexes in (first, second):
            body += struct.pack(f"<I{len(indexes)}I", len(indexes), *indexes)
        body += struct.pack("<II", count_0, count_1)
    table_start = len(body)
    body += struct.pack("<I", len(strings))
    for text in strings:
        raw = text.encode("utf-8")
        body += struct.pack("<BI", 0, len(raw)) + raw
    return body + struct.pack("<II", table_start, 0)


def test_parse_reads_both_appearance_lists() -> None:
    data = _file([(1, [0, 1], [], 2, 0), (29, [1], [2], 8, 8)], ["PC_VCE_1Warrior_1", "PC_VCE_A", "PC_VCE_B"])

    records = parse_charactervoice_records(data)

    assert records[0]["voice_names"] == [["PC_VCE_1Warrior_1", "PC_VCE_A"], []]
    assert records[1]["voice_types"] == [[1], [2]]
    assert records[1]["voice_count"] == [8, 8]


def test_parse_rejects_rows_that_stop_before_the_string_table() -> None:
    data = bytearray(_file([(1, [0], [], 1, 0), (2, [0], [], 1, 0)], ["PC_VCE_A"]))
    struct.pack_into("<I", data, _COUNT_OFFSET, 1)
    with pytest.raises(ValueError):
        parse_charactervoice_records(bytes(data))
