"""`--coverage`: which files it checks, how a file passes or fails, and its JSON document."""
from __future__ import annotations

import argparse

import pytest

import bdo_app
from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from cli.coverage import ERROR_FIELD, FileResult, check_file, coverage_document, coverage_targets, describe_error

from _common import row_table


def _entry(path: str) -> PazEntry:
    return PazEntry(
        archive_name="pad00001.paz",
        internal_path=path,
        offset=0,
        compressed_size=1,
        uncompressed_size=1,
        compression_type=0,
        encryption_type=0,
    )


class _Handler(PreviewHandler):
    """Returns two records, or raises `error` when one is given, or returns `records` when given."""

    def __init__(self, error: Exception | None = None, records: list[dict] | None = None) -> None:
        self.error = error
        self.records = records
        self.released: list[bytes] = []

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        if self.error is not None:
            raise self.error
        return self.records if self.records is not None else [{"id": 1}, {"id": 2}]

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        return ""

    def release_data(self, data: bytes) -> None:
        self.released.append(data)
        super().release_data(data)


def _read(entry: PazEntry, handler: PreviewHandler) -> tuple[bytes, dict[str, bytes]]:
    return b"payload", {}


def _no_read(entry: PazEntry, handler: PreviewHandler) -> tuple[bytes, dict[str, bytes]]:
    raise ValueError("BDO decompression failed with error code -3.")


# ── Targets ──────────────────────────────────────────────────────────────────

def test_targets_are_the_parsed_view_files_in_path_order() -> None:
    handler = _Handler()
    entries = [_entry("b/table.bss"), _entry("a/image.dds"), _entry("a/table.dbss")]

    targets = coverage_targets(entries, None, lambda e: handler if "table" in e.internal_path else None)

    assert [entry.internal_path for entry, _ in targets] == ["a/table.dbss", "b/table.bss"]


def test_targets_keep_only_the_pattern_matches() -> None:
    handler = _Handler()
    entries = [_entry("gamecommondata/binary/quest.dbss"), _entry("gamecommondata/binary/skill.dbss")]

    targets = coverage_targets(entries, "quest*", lambda e: handler)

    assert [entry.internal_path for entry, _ in targets] == ["gamecommondata/binary/quest.dbss"]


# ── One file ─────────────────────────────────────────────────────────────────

def test_a_file_passes_with_its_record_count_and_drops_the_cached_parse() -> None:
    handler = _Handler()

    result = check_file(_read, _entry("gamecommondata/binary/table.bss"), handler)

    assert (result.ok, result.records, result.error) == (True, 2, None)
    assert handler.released == [b"payload"]


def test_a_parse_error_is_the_file_result() -> None:
    handler = _Handler(ValueError("row 0 runs past its record at 0x30"))

    result = check_file(_read, _entry("gamecommondata/binary/table.bss"), handler)

    assert (result.ok, result.records) == (False, None)
    assert result.error == "ValueError: row 0 runs past its record at 0x30"
    assert handler.released == [b"payload"]


def test_an_error_record_fails_the_file() -> None:
    handler = _Handler(records=[{ERROR_FIELD: "table.bss could not be parsed: rows end at 0x40\nbut strings start at 0x30"}])

    result = check_file(_read, _entry("gamecommondata/binary/table.bss"), handler)

    assert (result.ok, result.records) == (False, None)
    assert result.error == "table.bss could not be parsed: rows end at 0x40 but strings start at 0x30"
    assert handler.released == [b"payload"]


def test_the_error_field_is_the_one_handlers_write() -> None:
    assert ERROR_FIELD == row_table.ERROR_FIELD


def test_no_records_is_a_pass() -> None:
    result = check_file(_read, _entry("gamecommondata/binary/table.bss"), _Handler(records=[]))

    assert (result.ok, result.records) == (True, 0)


def test_a_read_error_is_the_file_result() -> None:
    result = check_file(_no_read, _entry("gamecommondata/binary/table.bss"), _Handler())

    assert not result.ok
    assert result.error == "ValueError: BDO decompression failed with error code -3."


def test_error_text_is_one_line_and_cut() -> None:
    text = describe_error(ValueError("first\nsecond " + "x" * 500))

    assert "\n" not in text
    assert text.startswith("ValueError: first second ")
    assert len(text) <= 300
    assert text.endswith("…")


# ── Document and options ─────────────────────────────────────────────────────

def test_json_document_counts_and_lists_every_file() -> None:
    results = [
        FileResult("a.bss", "a.bss", True, 3, None, 0.01),
        FileResult("b.dbss", ".dbss", False, None, "ValueError: x", 0.02),
    ]

    document = coverage_document(results, 1784)

    assert (document["client_version"], document["files"], document["passed"], document["failed"]) == (1784, 2, 1, 1)
    assert [row["file"] for row in document["results"]] == ["a.bss", "b.dbss"]
    assert document["results"][1]["error"] == "ValueError: x"


def _parse(*argv: str) -> argparse.Namespace:
    parser = bdo_app._build_parser()
    args = parser.parse_args(list(argv))
    bdo_app._check_options(parser, args)
    return args


def test_coverage_takes_an_optional_pattern_and_json_or_csv() -> None:
    assert _parse("--coverage").coverage == ""
    assert _parse("--coverage", "quest*", "--json").coverage == "quest*"
    assert _parse("--coverage", "--csv").csv


def test_coverage_rejects_the_records_only_options() -> None:
    with pytest.raises(SystemExit):
        _parse("--coverage", "--limit", "5")
