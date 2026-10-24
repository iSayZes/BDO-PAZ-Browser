from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import FILE_NAME, parse_itembuildkit_entries


_U32 = struct.Struct("<I")
_ENTRY = struct.Struct("<IHIIIIIIIB")
_STRING_HEADER = struct.Struct("<BI")
# PABR magic, the kit count, then per kit a u32 entry count and its entries.
_KIT_COUNT_AT = 4
_KITS_AT = 8
_TRAILER_SIZE = 8
# [Guild] Node/Conquest War Annex Assembly Tool, the kit of clients 1784 and 3482.
_ANNEX_TOOL = 59791
_BARRICADE = 12606


def _declared_entries(source: CaseInput) -> int:
    """Entries from the kits' byte span: every kit is a u32 count and 35-byte entries."""
    data = source.data
    (kit_count,) = _U32.unpack_from(data, _KIT_COUNT_AT)
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    entry_bytes = table_start - _KITS_AT - kit_count * _U32.size
    assert entry_bytes % _ENTRY.size == 0, entry_bytes
    return entry_bytes // _ENTRY.size


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "item_key",
                "character_key",
                "use_condition",
                "use_condition_text",
                "contents_event_type",
                "contents_event_param1",
                "icon_image_file",
                "icon_path",
                "description",
                "description_kr",
                "name",
                "item_name",
                "has_character_row",
            ],
        ),
        DeclaredCountTest(declared=_declared_entries),
        PaFieldTest(field="description_kr"),
        TargetTest(col="character_key", value=_BARRICADE, expected={"item_key": _ANNEX_TOOL}),
    ],
)


@pytest.fixture(scope="module")
def buildkit_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itembuildkit_bss(spec: Any, buildkit_result: HandlerResult) -> None:
    buildkit_result.check(spec)


def test_every_string_index_names_a_text(buildkit_result: HandlerResult) -> None:
    for record in buildkit_result.records:
        assert record["use_condition_text"] and record["description_kr"], record["character_key"]
        assert record["icon_path"].endswith(".dds"), record["icon_path"]


def test_a_structure_is_in_a_kit_once(buildkit_result: HandlerResult) -> None:
    pairs = [(record["item_key"], record["character_key"]) for record in buildkit_result.records]
    assert len(pairs) == len(set(pairs))


def test_every_structure_has_a_characterstatic_row(buildkit_result: HandlerResult) -> None:
    assert all(record["has_character_row"] for record in buildkit_result.records)


def _pabr(body: bytes, strings: list[str]) -> bytes:
    table = _U32.pack(len(strings)) + b"".join(
        _STRING_HEADER.pack(1, len(text) * 2) + text.encode("utf-16-le") for text in strings
    )
    table_start = 4 + len(body)
    return b"PABR" + body + table + _U32.pack(table_start) + _U32.pack(0)


def test_an_entry_reads_its_strings() -> None:
    entry = _ENTRY.pack(_ANNEX_TOOL, 2046, 0, 1, 5000, 1, 2, 30000000, 0, 1)
    data = _pabr(
        _U32.pack(1) + _U32.pack(1) + entry,
        ["checksiegetower(0);", "New_Icon/03_ETC/06_Housing/00056071.dds", "설치물"],
    )
    (record,) = parse_itembuildkit_entries(data)
    assert record["character_key"] == 2046
    assert record["contents_event_param1"] == 5000
    assert record["use_condition_text"] == "checksiegetower(0);"
    assert record["icon_image_file_text"].endswith("00056071.dds")
    assert record["description_kr"] == "설치물"
    assert (record["unknown_1a"], record["unknown_1e"], record["unknown_22"]) == (30000000, 0, 1)


def test_kits_that_stop_short_of_the_string_table_raise() -> None:
    data = _pabr(_U32.pack(1) + _U32.pack(0) + bytes(4), [])
    with pytest.raises(ValueError, match="string table starts"):
        parse_itembuildkit_entries(data)
