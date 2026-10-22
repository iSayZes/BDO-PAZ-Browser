"""`pa_checksum`, the checksum of `pad00000.meta` and the PAZ headers (docs/paz-meta.md).

The client test skips without a client.
"""

from __future__ import annotations

import struct

import pytest

from paz.bdo_checksum import pa_checksum
from paz.bdo_paz_reader import parse_paz_file

from .fixtures import installed_paz_folder

# A path's checksum is its path_hash in the .meta; this row is on every client from 435 on.
_KNOWN_PATH = b"gamecommondata/binary/stringtable.bss"
_KNOWN_PATH_HASH = 3201528246


def test_empty_input_is_zero() -> None:
    assert pa_checksum(b"") == 0


def test_a_known_path_gives_its_meta_path_hash() -> None:
    assert pa_checksum(_KNOWN_PATH) == _KNOWN_PATH_HASH


def test_bytearray_and_memoryview_give_the_same_value_as_bytes() -> None:
    assert pa_checksum(bytearray(_KNOWN_PATH)) == pa_checksum(memoryview(_KNOWN_PATH)) == _KNOWN_PATH_HASH


def test_client_archive_header_holds_the_checksums_of_the_archive_and_its_paths() -> None:
    paz_folder = installed_paz_folder()
    if paz_folder is None:
        pytest.skip("no client installed")
    archive = min(paz_folder.glob("PAD*.PAZ"), key=lambda path: path.stat().st_size)
    data = archive.read_bytes()
    checksum, file_count, _path_length = struct.unpack_from("<III", data, 0)
    row_hashes = [row[0] for row in struct.iter_unpack("<6I", data[12 : 12 + file_count * 24])]
    paths = [entry.internal_path for entry in parse_paz_file(archive)]

    assert pa_checksum(data[4:]) == checksum
    ascii_rows = [(row_hash, path) for row_hash, path in zip(row_hashes, paths) if path.isascii()]
    assert ascii_rows
    assert all(pa_checksum(path.encode()) == row_hash for row_hash, path in ascii_rows)
