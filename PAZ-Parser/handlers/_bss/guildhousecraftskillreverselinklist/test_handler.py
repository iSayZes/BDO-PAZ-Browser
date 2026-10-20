from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _dbss.guildhousecraftskill.parser import FILE_NAME as FORWARD_FILE, parse_guildhousecraftskill_records
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

from .parser import FILE_NAME, parse_reverse_link_records


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# Building Boat Lv. 1, the first skill slot of the Guild Shipyard.
_BUILDING_BOAT_1 = 65042
_GUILD_SHIPYARD = 1601
_STORAGE = 2
# `skill_nos[0]` of a guildhousecraftskill.dbss row is slot 1.
_FIRST_SLOT = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill_name", "house_uses"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "skill_no", "link_count", "links", "skill_name", "house_uses", "house_uses_text",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="skill_no",
            value=_BUILDING_BOAT_1,
            expected={"links": [{"receipe_key": _GUILD_SHIPYARD, "slot": _FIRST_SLOT}]},
        ),
        UserLanguageTest(fields=["skill_name", "house_uses"]),
    ],
)


@pytest.fixture(scope="module")
def reverse_link_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_guildhousecraftskillreverselinklist_bss(spec: Any, reverse_link_result: HandlerResult) -> None:
    reverse_link_result.check(spec)


def test_skill_numbers_are_unique(reverse_link_result: HandlerResult) -> None:
    skill_nos = [r["skill_no"] for r in reverse_link_result.records]
    assert len(skill_nos) == len(set(skill_nos)), "a skill number has two entries"


def test_links_invert_the_forward_table(reverse_link_result: HandlerResult) -> None:
    """Every filled `skill_nos[i]` of guildhousecraftskill.dbss is one link at slot i + 1, in row order."""
    expected: dict[int, list[dict]] = {}
    for row in parse_guildhousecraftskill_records(load_binary_fixture(FORWARD_FILE)):
        for index, skill_no in enumerate(row["skill_nos"]):
            if skill_no:
                expected.setdefault(skill_no, []).append(
                    {"receipe_key": row["receipe_key"], "slot": index + _FIRST_SLOT}
                )
    actual = {r["skill_no"]: r["links"] for r in reverse_link_result.records}
    assert actual == expected


def _file(skills: list[tuple[int, list[tuple[int, int]]]]) -> bytes:
    """A PABR file of `skills` and an empty string table."""
    body = b"".join(
        struct.pack("<HI", skill_no, len(links)) + b"".join(struct.pack("<iI", *link) for link in links)
        for skill_no, links in skills
    )
    rows_end = 8 + len(body)
    return b"PABR" + struct.pack("<I", len(skills)) + body + struct.pack("<III", 0, rows_end, 0)


def test_parser_reads_unpadded_skill_entries() -> None:
    data = _file([(_BUILDING_BOAT_1, [(_GUILD_SHIPYARD, 1)]), (65058, [(1609, 1), (1608, 1)])])
    records = parse_reverse_link_records(data)
    assert [(r["skill_no"], r["link_count"], r["links"]) for r in records] == [
        (_BUILDING_BOAT_1, 1, [{"receipe_key": _GUILD_SHIPYARD, "slot": 1}]),
        (65058, 2, [{"receipe_key": 1609, "slot": 1}, {"receipe_key": 1608, "slot": 1}]),
    ]


def test_parser_rejects_a_count_past_the_string_table() -> None:
    data = bytearray(_file([(_BUILDING_BOAT_1, [(_STORAGE, 1)])]))
    struct.pack_into("<I", data, 8 + 2, 2)
    with pytest.raises(ValueError):
        parse_reverse_link_records(bytes(data))
