"""`content_key`: the meta version plus a digest of the `.meta` archive rows."""
from __future__ import annotations

from bdo_models import MetaFile, PazTable
from paz.bdo_content_key import content_key

_ROWS = [PazTable(paz_file_id=1, crc=0x1234ABCD, size=4_096), PazTable(paz_file_id=2, crc=0x0BADF00D, size=512)]


def _meta(version: int, rows: list[PazTable]) -> MetaFile:
    return MetaFile(version=version, paz_file_count=len(rows), paz_files=rows)


def test_the_same_archive_rows_give_the_same_key() -> None:
    assert content_key(_meta(3458, _ROWS)) == content_key(_meta(3458, list(_ROWS)))


def test_the_key_starts_with_the_version() -> None:
    assert content_key(_meta(3458, _ROWS)).startswith("3458-")


def test_a_repacked_archive_checksum_changes_the_key() -> None:
    repacked = [PazTable(paz_file_id=1, crc=0x1234ABCE, size=4_096), _ROWS[1]]

    assert content_key(_meta(3458, repacked)) != content_key(_meta(3458, _ROWS))


def test_a_new_archive_size_changes_the_key() -> None:
    grown = [_ROWS[0], PazTable(paz_file_id=2, crc=0x0BADF00D, size=513)]

    assert content_key(_meta(3458, grown)) != content_key(_meta(3458, _ROWS))


def test_a_patch_with_the_same_archives_changes_the_key() -> None:
    assert content_key(_meta(3459, _ROWS)) != content_key(_meta(3458, _ROWS))
