from __future__ import annotations

from pathlib import Path
import struct

from .bdo_payload_reader import ice_decrypt_bytes
from bdo_models import MetaFile, PazEntry, PazTable

# Layout: docs/file-formats/other/pad00000_meta.md.
_HEADER = struct.Struct("<II")
_PAZ_ROW = struct.Struct("<III")
_COUNT = struct.Struct("<I")
# path hash, folder index, name index, archive number, offset, compressed size, original size.
_FILE_ROW = struct.Struct("<7I")
# First name index and name count of the folder, then its NUL-terminated path.
_FOLDER_HEAD = struct.Struct("<II")


def read_bdo_meta(meta_path: Path) -> MetaFile:
    with meta_path.open("rb") as file:
        header: bytes = file.read(8)
        if len(header) != 8:
            raise ValueError(f"Invalid meta header: {meta_path}")

        version, paz_file_count = struct.unpack("<II", header)

        paz_files: list[PazTable] = []

        for _ in range(paz_file_count):
            entry_data: bytes = file.read(12)
            if len(entry_data) != 12:
                raise ValueError(f"Invalid PAZ table entry in: {meta_path}")

            paz_file_id, crc, size = struct.unpack("<III", entry_data)
            paz_files.append(
                PazTable(
                    paz_file_id=paz_file_id,
                    crc=crc,
                    size=size,
                )
            )

    return MetaFile(
        version=version,
        paz_file_count=paz_file_count,
        paz_files=paz_files,
    )


def read_meta_entries(meta_path: Path) -> list[PazEntry]:
    """Every file the `.meta` lists, whether or not its archive is on disk.

    The entries equal what `parse_paz_files` reads from the archive headers,
    so a client's file list is known from the `.meta` alone. Names are decoded
    as the archive headers are (UTF-8, invalid bytes replaced).
    """
    data = meta_path.read_bytes()
    _version, paz_count = _unpack(_HEADER, data, 0, meta_path)
    rows_start = _HEADER.size + paz_count * _PAZ_ROW.size + _COUNT.size
    (file_count,) = _unpack(_COUNT, data, rows_start - _COUNT.size, meta_path)
    rows_end = rows_start + file_count * _FILE_ROW.size
    if rows_end > len(data):
        raise ValueError(f"File table runs past the end of {meta_path}")

    folder_block, names_start = _encrypted_block(data, rows_end, meta_path)
    name_block, end = _encrypted_block(data, names_start, meta_path)
    if end != len(data):
        raise ValueError(f"{len(data) - end} bytes after the name block in {meta_path}")

    folders = _folder_paths(folder_block)
    names = [name.decode("utf-8", errors="replace") for name in name_block.split(b"\x00")]
    try:
        return [
            PazEntry(
                archive_name=f"pad{archive:05d}.paz",
                internal_path=folders[folder] + names[name],
                offset=offset,
                compressed_size=compressed_size,
                uncompressed_size=original_size,
                compression_type=0,
                encryption_type=0,
            )
            for _path_hash, folder, name, archive, offset, compressed_size, original_size
            in _FILE_ROW.iter_unpack(data[rows_start:rows_end])
        ]
    except IndexError as error:
        raise ValueError(f"A file row points past the folder or name block in {meta_path}") from error


def _unpack(layout: struct.Struct, data: bytes, offset: int, meta_path: Path) -> tuple[int, ...]:
    if offset + layout.size > len(data):
        raise ValueError(f"{meta_path} ends inside its header at {offset:#x}")
    return layout.unpack_from(data, offset)


def _encrypted_block(data: bytes, offset: int, meta_path: Path) -> tuple[bytes, int]:
    """The ICE-decrypted block at `offset` (a length, then that many bytes) and the offset after it."""
    (length,) = _unpack(_COUNT, data, offset, meta_path)
    start = offset + _COUNT.size
    if start + length > len(data):
        raise ValueError(f"Block at {offset:#x} runs past the end of {meta_path}")
    return ice_decrypt_bytes(data[start : start + length]), start + length


def _folder_paths(block: bytes) -> list[str]:
    """The folder paths in record order; the zero bytes that pad the block to 8 bytes end it."""
    paths: list[str] = []
    records_end = len(block.rstrip(b"\x00"))
    offset = 0
    while offset < records_end:
        end = block.index(b"\x00", offset + _FOLDER_HEAD.size)
        paths.append(block[offset + _FOLDER_HEAD.size : end].decode("utf-8", errors="replace"))
        offset = end + 1
    return paths
