from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, case_id, run_case

from .parser import FILE_NAME, parse_weburl_records, url_template


_U32 = struct.Struct("<I")
_URLS_START = 4
_TRAILER_SIZE = 8
_INSERT_SIZE = 5
_URL_HEAD_SIZE = 8
# unknown_after_urls, between the last URL and the string table.
_AFTER_URLS_SIZE = 4
# Every URL opens with `https://`, and the first insert point follows it (weburl_bss.md, Insert Types).
_SCHEME = "https://"
_SCHEME_INSERT = {"insert_offset": len(_SCHEME), "insert_type": 4}


def _declared_urls(source: CaseInput) -> int:
    """The URLs between the magic and `unknown_after_urls`, walked by their insert counts."""
    data = source.data
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    pos, count = _URLS_START, 0
    while pos < table_start - _AFTER_URLS_SIZE:
        (insert_count,) = _U32.unpack_from(data, pos + _U32.size)
        pos += _URL_HEAD_SIZE + insert_count * _INSERT_SIZE
        count += 1
    return count


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "position", "url_ref", "url", "insert_count", "inserts", "url_template", "unknown_after_urls",
            ]
        ),
        DeclaredCountTest(declared=_declared_urls),
    ],
)


@pytest.fixture(scope="module")
def weburl_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_weburl_bss(spec: Any, weburl_result: HandlerResult) -> None:
    weburl_result.check(spec)


def test_positions_count_up_from_zero(weburl_result: HandlerResult) -> None:
    assert [r["position"] for r in weburl_result.records] == list(range(len(weburl_result.records)))


def test_every_url_takes_an_insert_after_its_scheme(weburl_result: HandlerResult) -> None:
    urls = [r for r in weburl_result.records if r["url"]]
    assert urls
    for r in urls:
        assert r["url"].startswith(_SCHEME), r
        assert r["inserts"][0] == _SCHEME_INSERT, r


def test_an_empty_url_has_no_insert(weburl_result: HandlerResult) -> None:
    assert all(not r["inserts"] for r in weburl_result.records if not r["url"])


def test_only_the_first_url_reads_string_zero(weburl_result: HandlerResult) -> None:
    assert [r["position"] for r in weburl_result.records if r["url_ref"] == 0] == [0]


def test_the_template_marks_each_insert_point() -> None:
    url = "https://a.com?userId="
    inserts = [{"insert_offset": 8, "insert_type": 4}, {"insert_offset": len(url), "insert_type": 0}]
    assert url_template(url, inserts) == "https://<4>a.com?userId=<0>"
    assert url_template("", []) == ""


def _pabr(values: bytes, strings: list[str]) -> bytes:
    """A PABR file: magic, `values`, the UTF-8 string table and the trailer."""
    table = _U32.pack(len(strings)) + b"".join(b"\0" + _U32.pack(len(s)) + s.encode() for s in strings)
    table_start = _URLS_START + len(values)
    return b"PABR" + values + table + _U32.pack(table_start) + _U32.pack(0)


def _url(url_ref: int, *inserts: tuple[int, int]) -> bytes:
    return _U32.pack(url_ref) + _U32.pack(len(inserts)) + b"".join(struct.pack("<IB", *insert) for insert in inserts)


def test_the_urls_end_at_the_value_after_them() -> None:
    values = _url(0, (8, 4)) + _url(1) + _url(1, (8, 4)) + _U32.pack(0)
    records = parse_weburl_records(_pabr(values, ["https://a.com", "https://b.com"]))
    assert [r["url_template"] for r in records] == ["https://<4>a.com", "https://b.com", "https://<4>b.com"]
    assert {r["unknown_after_urls"] for r in records} == {0}


def test_urls_that_stop_short_of_the_string_table_raise() -> None:
    values = _url(0) + _U32.pack(0) + _U32.pack(7)
    with pytest.raises(ValueError, match="string table starts"):
        parse_weburl_records(_pabr(values, ["https://a.com"]))


def test_an_insert_past_its_url_raises() -> None:
    values = _url(0, (99, 4)) + _U32.pack(0)
    with pytest.raises(ValueError, match="do not fit"):
        parse_weburl_records(_pabr(values, ["https://a.com"]))


def test_urls_with_no_end_value_raise() -> None:
    values = _url(0) + _url(1)
    with pytest.raises(ValueError, match="string table"):
        parse_weburl_records(_pabr(values, ["https://a.com", "https://b.com"]))
