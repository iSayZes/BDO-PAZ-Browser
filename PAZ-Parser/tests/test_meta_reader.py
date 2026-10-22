"""`read_meta_entries`: the file table of `pad00000.meta` (docs/paz-meta.md).

The client test skips without a client.
"""

from __future__ import annotations

import struct
from pathlib import Path

import pytest

from bdo_models import PazEntry
from paz.bdo_ice import BDO_ICE_KEY, IceCipher
from paz.bdo_meta_reader import read_meta_entries
from paz.bdo_paz_extract import find_single_meta_file
from paz.bdo_paz_reader import parse_paz_files

from .fixtures import installed_paz_folder

# Archives compared on the installed client: enough to cover several folders, quick to read.
_CLIENT_ARCHIVES = 20

_FOLDERS = ["character/", "gamecommondata/binary/"]
# (folder index, name, archive, offset, compressed size, original size)
_FILES = [
    (0, "bonecontrol.xml", 1, 0, 120, 400),
    (1, "mainquest.bss", 2, 64, 900, 900),
    (1, "stringtable.bss", 1, 120, 50, 2000),
]


def _encrypted(block: bytes) -> bytes:
    padded = block + b"\x00" * (-len(block) % 8)
    return struct.pack("<I", len(padded)) + IceCipher(BDO_ICE_KEY).encrypt(padded)


def _meta_bytes(extra: bytes = b"", name_index_shift: int = 0) -> bytes:
    """A two-archive `.meta` holding `_FILES`, laid out as docs/paz-meta.md describes."""
    names = [name for _folder, name, *_ in _FILES]
    rows = b"".join(
        struct.pack("<7I", 0xC0FFEE, folder, index + name_index_shift, archive, offset, compressed, original)
        for index, (folder, _name, archive, offset, compressed, original) in enumerate(_FILES)
    )
    folder_block = b""
    first = 0
    for index, path in enumerate(_FOLDERS):
        count = sum(1 for folder, *_ in _FILES if folder == index)
        folder_block += struct.pack("<II", first, count) + path.encode() + b"\x00"
        first += count
    name_block = b"".join(name.encode() + b"\x00" for name in names)
    return (
        struct.pack("<II", 1234, 2)
        + struct.pack("<III", 1, 0xAAAA, 5000)
        + struct.pack("<III", 2, 0xBBBB, 6000)
        + struct.pack("<I", len(_FILES))
        + rows
        + _encrypted(folder_block)
        + _encrypted(name_block)
        + extra
    )


def _write(tmp_path: Path, data: bytes) -> Path:
    meta = tmp_path / "pad00000.meta"
    meta.write_bytes(data)
    return meta


def test_each_row_becomes_an_entry_named_from_its_folder_and_name(tmp_path: Path) -> None:
    entries = read_meta_entries(_write(tmp_path, _meta_bytes()))

    assert entries == [
        PazEntry(f"pad{archive:05d}.paz", _FOLDERS[folder] + name, offset, compressed, original, 0, 0)
        for folder, name, archive, offset, compressed, original in _FILES
    ]


def test_bytes_after_the_name_block_are_an_error(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="after the name block"):
        read_meta_entries(_write(tmp_path, _meta_bytes(extra=b"\x00\x00\x00\x00")))


def test_a_row_naming_a_missing_string_is_an_error(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="points past"):
        read_meta_entries(_write(tmp_path, _meta_bytes(name_index_shift=1000)))


def test_a_cut_file_is_an_error(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        read_meta_entries(_write(tmp_path, _meta_bytes()[:-9]))


def test_client_meta_lists_the_same_entries_as_the_archive_headers() -> None:
    paz_folder = installed_paz_folder()
    if paz_folder is None:
        pytest.skip("no client installed")
    archives = sorted(paz_folder.glob("PAD*.PAZ"))[:_CLIENT_ARCHIVES]
    names = {archive.name.lower() for archive in archives}

    from_meta = [entry for entry in read_meta_entries(find_single_meta_file(paz_folder)) if entry.archive_name in names]
    from_headers = [entry._replace(archive_name=entry.archive_name.lower()) for entry in parse_paz_files(archives)]

    assert from_headers
    assert sorted(from_meta) == sorted(from_headers)
