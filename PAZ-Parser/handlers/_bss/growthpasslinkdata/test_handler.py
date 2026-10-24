from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    run_case,
)

from _bss.growthpasslinkdata.handler import SERVICE_RESOURCE_TYPE_NAMES
from _bss.growthpasslinkdata.parser import GuideLink, parse_growthpasslinkdata, quest_link_addresses
from _common.binary import u32

_FILE = "growthpasslinkdata.bss"
# `Button_GuideLink1` to `Button_GuideLink3` in panel_window_growthpass_1.luac.
_MAX_LINKS = 3

CASE = HandlerCase(
    handler_name=_FILE,
    data_file=_FILE,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title"],
    internal_path=f"gamecommondata/binary/{_FILE}",
    tests=[
        SchemaTest(required_keys=[
            "quest_chain_id", "quest_id", "entry_count", "title",
            "service_resource_type", "service_resource_type_name",
            "link_count", "link_index", "link", "author",
        ]),
        RangeTest(col="link_index", min_val=0, max_val=_MAX_LINKS - 1),
    ],
)


@pytest.fixture(scope="module")
def link_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_growthpasslinkdata_bss(spec: Any, link_result: HandlerResult) -> None:
    link_result.check(spec)


def test_one_record_per_declared_quest(link_result: HandlerResult) -> None:
    data = link_result.source.data
    records = parse_growthpasslinkdata(data)
    keys = {(r.quest_chain_id, r.quest_id) for r in records}
    assert len(records) == u32(data, 4) == len(keys)


def test_each_quest_lists_a_service_type_once(link_result: HandlerResult) -> None:
    for record in parse_growthpasslinkdata(link_result.source.data):
        types = [entry.service_resource_type for entry in record.entries]
        assert len(types) == len(set(types)), (record.quest_chain_id, record.quest_id)


def test_service_types_are_enum_members(link_result: HandlerResult) -> None:
    assert {r["service_resource_type"] for r in link_result.records} <= set(SERVICE_RESOURCE_TYPE_NAMES)


def test_every_link_is_a_web_address_with_an_author(link_result: HandlerResult) -> None:
    for r in link_result.records:
        assert r["link"].startswith("https://"), (r["quest_chain_id"], r["quest_id"])
        assert r["author"], (r["quest_chain_id"], r["quest_id"])
        assert 1 <= r["link_count"] <= _MAX_LINKS


def test_link_addresses_hold_every_quest(link_result: HandlerResult) -> None:
    addresses = quest_link_addresses(link_result.source.data)
    expected: dict[tuple[int, int], set[str]] = {}
    for r in link_result.records:
        expected.setdefault((r["quest_chain_id"], r["quest_id"]), set()).add(r["link"])
    assert {key: set(links) for key, links in addresses.items()} == expected


def _file(links: list[tuple[int, int]], strings: list[str], table_shift: int = 0) -> bytes:
    """PABR with quest 4470 / 1, one EN entry holding `links` (string refs), and `strings`."""
    entry = struct.pack("<BI", 2, len(links)) + b"".join(struct.pack("<II", *link) for link in links)
    record = struct.pack("<HHI", 4470, 1, 1) + entry
    table_start = 8 + len(record) + table_shift
    table = struct.pack("<I", len(strings)) + b"".join(
        struct.pack("<BI", 1, len(text.encode("utf-16-le"))) + text.encode("utf-16-le") for text in strings
    )
    return b"PABR" + struct.pack("<I", 1) + record + table + struct.pack("<II", table_start, 0)


def test_links_read_as_link_and_author_pairs() -> None:
    data = _file([(0, 1), (2, 3)], ["https://a", "A", "https://b", "B"])
    (record,) = parse_growthpasslinkdata(data)
    assert record.entries[0].links == (GuideLink("https://a", "A"), GuideLink("https://b", "B"))


def test_a_string_reference_outside_the_table_is_rejected() -> None:
    with pytest.raises(ValueError, match="outside"):
        parse_growthpasslinkdata(_file([(0, 2)], ["https://a", "A"]))


def test_records_that_miss_the_string_table_are_rejected() -> None:
    with pytest.raises(ValueError):
        parse_growthpasslinkdata(_file([(0, 1)], ["https://a", "A"], table_shift=4))
